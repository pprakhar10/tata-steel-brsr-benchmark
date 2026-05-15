# parser/parse_xbrl.py
# Parses a single BRSR XBRL XML file and returns a structured dict of raw values.
# Handles all 4 SEBI namespace versions (v1–v4).
# Does NOT normalize units — that is done in normalize.py.
# Does NOT write files — that is done in run_all.py.

import xml.etree.ElementTree as ET
import re
from pathlib import Path
from typing import Any

from config import (
    NAMESPACE_VERSIONS,
    XBRL_INSTANCE_NS,
    EXCLUDED_TAGS,
    TAG_ALIASES,
    entity_ns,
    capmkt_ns,
)


# ---------------------------------------------------------------------------
# Namespace detection
# ---------------------------------------------------------------------------

def detect_namespace_version(root: ET.Element) -> tuple[str, str]:
    """
    Detect the SEBI namespace version key and entity namespace URI.

    The root element is the standard XBRL instance tag
    ({http://www.xbrl.org/2003/instance}xbrl).  The SEBI namespace appears
    in the child data element tags.  We find it by scanning element tags for
    the known sebi.gov.in URI pattern.

    Returns:
        (version_key, entity_ns_uri)  e.g. ("2024-04-30", "https://www.sebi.gov.in/xbrl/BRSR/2024-04-30/...")
    Raises:
        ValueError if the namespace cannot be identified.
    """
    for el in root.iter():
        tag = el.tag
        if "sebi.gov.in" not in tag:
            continue
        # tag format: "{https://www.sebi.gov.in/xbrl/2024-04-30/in-capmkt}TagName"
        uri = tag[1: tag.index("}")]
        for version_key in NAMESPACE_VERSIONS:
            if version_key in uri:
                return version_key, entity_ns(version_key)

    raise ValueError(
        f"Cannot identify SEBI namespace version — no sebi.gov.in element "
        f"found in file. Known versions: {list(NAMESPACE_VERSIONS.keys())}"
    )


# ---------------------------------------------------------------------------
# Fiscal year detection
# ---------------------------------------------------------------------------

def detect_fiscal_year(root: ET.Element) -> str:
    """
    Derive the fiscal year label (e.g. 'FY2023') from the DCYMain context's endDate.
    Indian fiscal year ends 31 March — a file ending 2023-03-31 is FY2023.

    Raises:
        ValueError if DCYMain context or its endDate cannot be found.
    """
    xns = XBRL_INSTANCE_NS
    for ctx in root.findall(f"{{{xns}}}context"):
        if ctx.get("id") != "DCYMain":
            continue
        period = ctx.find(f"{{{xns}}}period")
        if period is None:
            continue
        end_el = period.find(f"{{{xns}}}endDate")
        if end_el is None or not end_el.text:
            continue
        # endDate format: YYYY-MM-DD; FY = calendar year of the end date (Apr–Mar)
        year = int(end_el.text.strip()[:4])
        return f"FY{year}"

    raise ValueError("DCYMain context with endDate not found in XBRL file.")


# ---------------------------------------------------------------------------
# Reporting basis detection
# ---------------------------------------------------------------------------

def detect_reporting_basis(root: ET.Element, ent_ns_uri: str) -> tuple[str, str | None]:
    """
    Read the ReportingBoundary tag (contextRef=DCYMain) to determine whether the
    filing is on a Standalone or Consolidated basis.

    Returns:
        ("standalone" | "consolidated", basis_warning_string | None)
    """
    consolidated_warning = (
        "This year's data is reported on a Consolidated basis (includes subsidiaries and "
        "international operations). All other years of this company and all other companies "
        "in this benchmark are Standalone. Cross-company and cross-year comparisons for "
        "this year-company are not directly comparable."
    )
    for el in root.iter():
        local = _local_name(el)
        if local == "ReportingBoundary" and el.get("contextRef") == "DCYMain":
            val = (el.text or "").strip().lower()
            if "consolidated" in val:
                return "consolidated", consolidated_warning
            return "standalone", None

    # Default to standalone if tag absent (unlikely but safe)
    return "standalone", None


# ---------------------------------------------------------------------------
# Unit tag extraction
# ---------------------------------------------------------------------------

def extract_unit_tags(root: ET.Element, ent_ns_uri: str) -> dict[str, str]:
    """
    Extract all UnitOf{TagName} companion tags from DCYMain context.
    Returns dict mapping canonical tag name → raw unit string (lowercased and stripped).

    In v1/v2 files, unit tags exist.  In v3/v4 files, this returns an empty dict
    (caller falls back to KNOWN_UNITS_FALLBACK from config.py).
    """
    units: dict[str, str] = {}
    for el in root.iter():
        local = _local_name(el)
        if not local.startswith("UnitOf"):
            continue
        if el.get("contextRef") != "DCYMain":
            continue
        raw_val = (el.text or "").strip()
        if not raw_val:
            continue
        # Strip the "UnitOf" prefix to get the associated tag name
        associated_tag = local[len("UnitOf"):]  # e.g. "UnitOfNox" → "Nox"
        # Apply alias resolution so unit is keyed under canonical name
        canonical = TAG_ALIASES.get(associated_tag, associated_tag)
        units[canonical] = raw_val.strip()
    return units


# ---------------------------------------------------------------------------
# Value extraction — DCYMain (primary) and DPYMain (fallback)
# ---------------------------------------------------------------------------

def _local_name(el: ET.Element) -> str:
    """Return the local part of an element's tag (strips namespace URI)."""
    tag = el.tag
    return tag[tag.index("}") + 1:] if "}" in tag else tag


def _is_numeric(s: str) -> bool:
    """True if s can be interpreted as a number (including scientific notation)."""
    try:
        float(s.replace(",", ""))
        return True
    except ValueError:
        return False


def _extract_values_for_context(
    root: ET.Element,
    context_id: str,
) -> dict[str, str]:
    """
    Extract all tag values for a given contextRef, keyed by canonical local tag name.
    Excluded tags and UnitOf* companion tags are skipped.
    Returns raw string values — normalization is not done here.
    """
    values: dict[str, str] = {}
    for el in root.iter():
        if el.get("contextRef") != context_id:
            continue
        local = _local_name(el)
        # Skip UnitOf* companion tags (handled separately)
        if local.startswith("UnitOf"):
            continue
        # Apply alias resolution
        canonical = TAG_ALIASES.get(local, local)
        # Skip excluded tags (check both original and canonical)
        if local in EXCLUDED_TAGS or canonical in EXCLUDED_TAGS:
            continue
        raw_val = (el.text or "").strip()
        values[canonical] = raw_val
    return values


def extract_dcymain_values(root: ET.Element) -> dict[str, str]:
    """
    Extract DCYMain values (current year primary context).
    For any tag missing from DCYMain, falls back to DPYMain.
    Returns dict: canonical_tag → raw_string_value.
    """
    primary = _extract_values_for_context(root, "DCYMain")
    fallback = _extract_values_for_context(root, "DPYMain")

    # Merge: primary takes precedence; add any DPYMain-only entries
    result = dict(fallback)  # start with DPYMain
    result.update(primary)   # overwrite with DCYMain where available
    return result


# ---------------------------------------------------------------------------
# Dimensional context extraction (table rows)
# ---------------------------------------------------------------------------

def extract_dimensional_values(root: ET.Element) -> list[dict[str, Any]]:
    """
    Extract values from multi-dimensional contexts (D_* contexts, excluding DCYMain/DPYMain/ICYMain).
    Each returned dict has:
        contextId:   original context ID string
        dimensions:  dict of dimension member labels extracted from xbrldi:explicitMember
        values:      dict of canonical_tag → raw_value
    """
    xns = XBRL_INSTANCE_NS
    xdi = "http://xbrl.org/2006/xbrldi"

    # Build map of contextId → dimension members for all D_* contexts
    dim_contexts: dict[str, dict[str, str]] = {}
    for ctx in root.findall(f"{{{xns}}}context"):
        cid = ctx.get("id", "")
        # Skip the three main non-dimensional contexts
        if cid in ("DCYMain", "DPYMain", "ICYMain"):
            continue
        # Only process current-year dimensional contexts (same period as DCYMain)
        period = ctx.find(f"{{{xns}}}period")
        if period is None:
            continue
        # Check this context covers the current year (has startDate, not instant)
        start_el = period.find(f"{{{xns}}}startDate")
        if start_el is None:
            continue  # skip instant contexts

        # Extract dimension labels from xbrldi:explicitMember elements
        dims: dict[str, str] = {}
        entity = ctx.find(f"{{{xns}}}entity")
        if entity is not None:
            segment = entity.find(f"{{{xns}}}segment")
            if segment is not None:
                for member in segment.findall(f"{{{xdi}}}explicitMember"):
                    dim_attr = member.get("dimension", "")
                    dim_label = _local_name_from_str(dim_attr)
                    member_label = _local_name_from_str(member.text or "")
                    dims[dim_label] = member_label

        dim_contexts[cid] = dims

    if not dim_contexts:
        return []

    # Now extract values for each dimensional context
    results: list[dict[str, Any]] = []
    context_values: dict[str, dict[str, str]] = {}
    for el in root.iter():
        cid = el.get("contextRef", "")
        if cid not in dim_contexts:
            continue
        local = _local_name(el)
        if local.startswith("UnitOf"):
            continue
        canonical = TAG_ALIASES.get(local, local)
        if local in EXCLUDED_TAGS or canonical in EXCLUDED_TAGS:
            continue
        raw_val = (el.text or "").strip()
        if cid not in context_values:
            context_values[cid] = {}
        context_values[cid][canonical] = raw_val

    for cid, dims in dim_contexts.items():
        if cid in context_values and context_values[cid]:
            results.append({
                "contextId": cid,
                "dimensions": dims,
                "values": context_values[cid],
            })

    return results


def _local_name_from_str(qname: str) -> str:
    """Extract local name from a QName string like 'prefix:LocalPart' or '{uri}LocalPart'."""
    if "}" in qname:
        return qname[qname.index("}") + 1:]
    if ":" in qname:
        return qname.split(":")[-1]
    return qname


# ---------------------------------------------------------------------------
# Main entry point: parse a single file
# ---------------------------------------------------------------------------

def parse_file(xml_path: Path) -> dict[str, Any]:
    """
    Parse a single BRSR XBRL XML file.

    Returns a dict with structure:
    {
        "filePath":         str,
        "fiscalYear":       "FY2023" | "FY2024" | "FY2025",
        "namespaceVersion": "v1" | "v2" | "v3" | "v4",
        "reportingBasis":   "standalone" | "consolidated",
        "basisWarning":     str | None,
        "unitTags":         { canonical_tag: raw_unit_string },  # may be empty for v3/v4
        "dcyValues":        { canonical_tag: raw_value_string },
        "dimensionalRows":  [ { contextId, dimensions, values } ],
    }

    Raises:
        ValueError / ET.ParseError on malformed or unrecognised files.
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()

    version_key, ent_ns_uri = detect_namespace_version(root)
    fiscal_year              = detect_fiscal_year(root)
    reporting_basis, basis_warning = detect_reporting_basis(root, ent_ns_uri)
    unit_tags                = extract_unit_tags(root, ent_ns_uri)
    dcy_values               = extract_dcymain_values(root)
    dimensional_rows         = extract_dimensional_values(root)

    return {
        "filePath":         str(xml_path),
        "fiscalYear":       fiscal_year,
        "namespaceVersion": NAMESPACE_VERSIONS[version_key],
        "reportingBasis":   reporting_basis,
        "basisWarning":     basis_warning,
        "unitTags":         unit_tags,
        "dcyValues":        dcy_values,
        "dimensionalRows":  dimensional_rows,
    }


# ---------------------------------------------------------------------------
# Parse all files for one company
# ---------------------------------------------------------------------------

def parse_company(company_id: str, xbrl_folder: Path) -> list[dict[str, Any]]:
    """
    Parse all XML files in xbrl_folder for a given company.
    Returns a list of parsed file dicts (one per file), sorted by fiscal year.

    Raises:
        FileNotFoundError if the folder doesn't exist.
        ValueError if duplicate fiscal years are found (would overwrite data).
    """
    if not xbrl_folder.exists():
        raise FileNotFoundError(f"XBRL folder not found: {xbrl_folder}")

    xml_files = sorted(xbrl_folder.glob("*.xml"))
    if not xml_files:
        raise FileNotFoundError(f"No XML files found in {xbrl_folder}")

    parsed: list[dict[str, Any]] = []
    seen_years: set[str] = set()

    for xml_path in xml_files:
        result = parse_file(xml_path)
        fy = result["fiscalYear"]
        if fy in seen_years:
            raise ValueError(
                f"Duplicate fiscal year {fy} found for company {company_id} "
                f"in {xbrl_folder}. Remove the duplicate file."
            )
        seen_years.add(fy)
        parsed.append(result)
        print(f"  Parsed {company_id} {fy} ({result['namespaceVersion']}, "
              f"{result['reportingBasis']}, "
              f"{len(result['dcyValues'])} DCYMain tags, "
              f"{len(result['dimensionalRows'])} dimensional rows)")

    # Sort by fiscal year for deterministic processing order (FY2023 → FY2024 → FY2025)
    parsed.sort(key=lambda r: r["fiscalYear"])
    return parsed
