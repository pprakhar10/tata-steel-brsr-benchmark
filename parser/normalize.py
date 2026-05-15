# parser/normalize.py
# Takes raw parsed output from parse_xbrl.py and produces normalized IndicatorValue dicts.
# Unit normalization rules: SEBI guidance first, Tata Steel reference where SEBI is silent.
# If normalization is ambiguous, sets normalized=False and unitWarning rather than guessing.

import re
from typing import Any

from config import (
    UNIT_CONVERSIONS,
    UNIT_CORRECTIONS,
    UNIT_REQUIRES_PRODUCTION_VOLUME,
    UNIT_IS_CONCENTRATION,
    NIL_TEXT_VALUES,
    KNOWN_UNITS_FALLBACK,
    KNOWN_UNITS_V3V4_OVERRIDE,
    SEBI_MANDATED_UNIT_PATTERNS,
    BOOLEAN_TAG_PATTERNS,
    PERCENTAGE_TAG_PATTERNS,
    INTENSITY_TAG_PATTERNS,
    STEEL_PRODUCTION_TONNES,
    STANDARD_UNITS,
    UNIT_CHANGED_IN_V3V4,
    V3V4_VERSIONS,
    XBRL_VALUE_PATCHES,
)


# ---------------------------------------------------------------------------
# Data type inference
# ---------------------------------------------------------------------------

# "1" and "0" intentionally excluded — they are ambiguous with numeric values (e.g. 1 PJ energy).
# Boolean-by-value detection uses only unambiguous text strings.
# Numeric zero and one fall through to the numeric path and are handled correctly there.
_BOOL_TRUE  = {"yes", "y", "true", "applicable", "implemented", "conducted"}
_BOOL_FALSE = {"no", "n", "false", "not applicable", "not implemented", "not conducted"}


def infer_data_type(tag: str, raw_value: str) -> str:
    """
    Infer the display data type for an indicator.
    Returns one of: 'numeric' | 'boolean' | 'text' | 'percentage' | 'intensity'

    Classification priority:
    1. If tag name matches intensity patterns → 'intensity'
    2. If tag name matches percentage patterns → 'percentage'
    3. If raw value is a bool-like string → 'boolean'
    4. If tag name matches boolean patterns → 'boolean'
    5. If raw value is numeric → 'numeric'
    6. Otherwise → 'text'
    """
    tag_lower = tag.lower()
    val_lower = raw_value.strip().lower()

    # Intensity metrics (subset of numeric, but displayed differently)
    if any(p.lower() in tag_lower for p in INTENSITY_TAG_PATTERNS):
        if _is_numeric_str(raw_value):
            return "intensity"

    # Percentage / rate metrics
    if any(p.lower() in tag_lower for p in PERCENTAGE_TAG_PATTERNS):
        if _is_numeric_str(raw_value):
            return "percentage"

    # Boolean by value
    if val_lower in _BOOL_TRUE or val_lower in _BOOL_FALSE:
        return "boolean"

    # Boolean by tag name pattern
    if any(p.lower() in tag_lower for p in BOOLEAN_TAG_PATTERNS):
        if val_lower not in _BOOL_TRUE and val_lower not in _BOOL_FALSE:
            # Tag looks boolean but value isn't — treat as text
            return "text"
        return "boolean"

    # Numeric
    if _is_numeric_str(raw_value):
        return "numeric"

    return "text"


def _is_numeric_str(s: str) -> bool:
    if not s:
        return False
    try:
        float(s.replace(",", "").strip())
        return True
    except ValueError:
        return False


# ---------------------------------------------------------------------------
# Unit resolution: find the right unit string for a tag
# ---------------------------------------------------------------------------

def resolve_unit(
    tag: str,
    unit_tags_from_file: dict[str, str],
    company_id: str,
    company_unit_cache: dict[str, str],
    namespace_version: str = "",
) -> str | None:
    """
    Determine the raw unit string for a given tag, in priority order:
    1. Unit tag present in this file (unit_tags_from_file)
    2. Unit cached from an earlier year of the same company (company_unit_cache)
    3. Pre-seeded fallback from KNOWN_UNITS_FALLBACK (config.py)
    4. None (unknown — caller sets unitWarning)
    """
    # 0. Hard correction — the XBRL file's own unit tag is known to be wrong.
    #    Takes priority over everything including the file's own UnitOf* tag.
    #    Only entries confirmed by user via PDF. See UNIT_CORRECTIONS in config.py.
    correction = UNIT_CORRECTIONS.get(company_id, {}).get(tag)
    if correction:
        return correction

    # Check if this tag's unit is known to have CHANGED in v3/v4 schema.
    # If so, the FY23 cache is stale and must not be used.
    # KNOWN_UNITS_FALLBACK is still consulted — it may have been updated to reflect
    # the new v3/v4 unit (e.g. Tata energy: PJ in FY23 → GJ in FY24+).
    # If KNOWN_UNITS_FALLBACK is intentionally absent (e.g. JSW NOx: new unit unknown),
    # the tag correctly falls through to "unit unknown".
    cache_blocked = (
        namespace_version in V3V4_VERSIONS
        and tag in UNIT_CHANGED_IN_V3V4.get(company_id, set())
    )

    # 1. Unit tag in this file (always authoritative unless overridden at step 0)
    if tag in unit_tags_from_file:
        raw = unit_tags_from_file[tag].strip()
        if raw:
            return raw

    # 2. Cached from earlier year — skip if unit changed in v3/v4
    if not cache_blocked and tag in company_unit_cache:
        return company_unit_cache[tag]

    # 3a. v3/v4-specific override — the correct new unit when the cache is blocked
    #     (e.g. Tata energy: PJ in FY23 → GJ in FY24+).
    #     Only consulted when cache was blocked; otherwise the cache (step 2) is authoritative.
    if cache_blocked:
        v3v4_override = KNOWN_UNITS_V3V4_OVERRIDE.get(company_id, {})
        if tag in v3v4_override:
            return v3v4_override[tag]

    # 3b. Pre-seeded fallback (v1/v2 unit, or universal default)
    fallback = KNOWN_UNITS_FALLBACK.get(company_id, {})
    if tag in fallback:
        return fallback[tag]

    # 4. SEBI-mandated category override (water → kL, waste → metric tonnes)
    tag_lower = tag.lower()
    for pattern, unit in SEBI_MANDATED_UNIT_PATTERNS:
        if pattern in tag_lower:
            return unit

    return None


# ---------------------------------------------------------------------------
# Unit conversion: raw unit string → multiplier
# ---------------------------------------------------------------------------

def _normalise_unit_key(raw_unit: str) -> str:
    """Normalise a raw unit string for lookup in UNIT_CONVERSIONS."""
    s = raw_unit.lower().strip()
    # collapse whitespace and remove trailing punctuation
    s = re.sub(r"\s+", " ", s)
    s = s.rstrip(".")
    return s


def get_conversion_factor(raw_unit: str) -> float | None:
    """
    Return the multiplier to convert raw_unit to the standard unit.
    Returns None if the unit is unknown.
    """
    key = _normalise_unit_key(raw_unit)
    if key in UNIT_CONVERSIONS:
        return UNIT_CONVERSIONS[key]
    # Try stripping trailing year qualifiers (e.g. "kilotonnes/year" → "kilotonnes")
    stripped = re.split(r"[/\s]", key)[0]
    if stripped in UNIT_CONVERSIONS:
        return UNIT_CONVERSIONS[stripped]
    return None


# ---------------------------------------------------------------------------
# Air emission normalization via production volume
# ---------------------------------------------------------------------------

def convert_kg_per_tcs_to_kilotonnes(
    raw_value: float,
    company_id: str,
    fiscal_year: str,
) -> tuple[float | None, str | None]:
    """
    Convert a kg/tcs (kg per tonne of crude steel) value to absolute kilotonnes
    using the production volume from STEEL_PRODUCTION_TONNES.

    Returns (converted_value_in_kilotonnes, None) on success.
    Returns (None, warning_string) if production volume is missing.
    """
    prod = STEEL_PRODUCTION_TONNES.get(company_id, {}).get(fiscal_year)
    if not prod:
        return None, (
            f"Cannot convert kg/tcs to kilotonnes: production volume for "
            f"{company_id} {fiscal_year} not configured in STEEL_PRODUCTION_TONNES"
        )
    # raw_value (kg/tonne) × production (tonnes) = kg → ÷ 1,000,000 = kilotonnes
    kt = raw_value * prod / 1_000_000
    return kt, None


# ---------------------------------------------------------------------------
# Core normalization: produce an IndicatorValue dict for one tag
# ---------------------------------------------------------------------------

def normalize_value(
    tag: str,
    raw_value: str,
    unit_tags_from_file: dict[str, str],
    company_id: str,
    fiscal_year: str,
    company_unit_cache: dict[str, str],
    namespace_version: str = "",
) -> dict[str, Any]:
    """
    Produce a normalized IndicatorValue dict for a single tag/value pair.

    Output schema:
    {
        "value":        number | bool | str | null,
        "rawValue":     str,
        "rawUnit":      str | null,
        "standardUnit": str | null,
        "normalized":   bool,
        "unitWarning":  str | null,
        "dataType":     str,
        "patchSource":  str | null,   # set if value was overridden from PDF
    }

    Rules:
    - Text / boolean values: returned as-is, normalized=True, no unit processing.
    - Nil/zero text values: returned as value=0 (numeric zero), normalized=True.
    - Numeric values without a resolvable unit: normalized=False + unitWarning.
    - Numeric values with a concentration unit (µg/m³): normalized=False + specific warning.
    - Numeric values with kg/tcs unit: converted via production volume; warning if production missing.
    - Numeric values with known unit: multiplied by conversion factor; normalized=True.
    - Numeric values with unknown unit string: normalized=False + unitWarning.
    """
    # --- PDF value patch (highest priority — overrides XBRL raw value) ---
    patch = XBRL_VALUE_PATCHES.get(company_id, {}).get(fiscal_year, {}).get(tag)
    patch_source: str | None = patch["source"] if patch else None
    if patch:
        raw_value = patch["rawValue"]
        # Inject patched unit into unit_tags_from_file so resolve_unit picks it up
        unit_tags_from_file = {**unit_tags_from_file, tag: patch["rawUnit"]}

    result = _normalize_value_inner(
        tag, raw_value, unit_tags_from_file, company_id, fiscal_year,
        company_unit_cache, namespace_version,
    )
    result["patchSource"] = patch_source
    return result


def _normalize_value_inner(
    tag: str,
    raw_value: str,
    unit_tags_from_file: dict[str, str],
    company_id: str,
    fiscal_year: str,
    company_unit_cache: dict[str, str],
    namespace_version: str = "",
) -> dict[str, Any]:
    """Core normalization logic — called by normalize_value after patch application."""

    data_type = infer_data_type(tag, raw_value)
    stripped  = raw_value.strip()

    # --- Null/empty ---
    if not stripped:
        return _indicator(
            value=None, raw_value=raw_value, raw_unit=None,
            standard_unit=None, normalized=True, unit_warning=None,
            data_type=data_type, value_status="blank",
        )

    # --- Boolean ---
    if data_type == "boolean":
        bool_val = stripped.lower() in _BOOL_TRUE
        return _indicator(
            value=bool_val, raw_value=raw_value, raw_unit=None,
            standard_unit=None, normalized=True, unit_warning=None,
            data_type="boolean", value_status="value",
        )

    # --- Text ---
    if data_type == "text":
        # Nil strings in a text field → null with explicit status
        # "0" is NOT treated as nil — a company writing "0" means zero, not not-applicable
        if stripped.lower() in NIL_TEXT_VALUES:
            return _indicator(
                value=None, raw_value=raw_value, raw_unit=None,
                standard_unit=None, normalized=True, unit_warning=None,
                data_type="text", value_status="nil_reported",
            )
        return _indicator(
            value=stripped, raw_value=raw_value, raw_unit=None,
            standard_unit=None, normalized=True, unit_warning=None,
            data_type="text", value_status="value",
        )

    # --- Numeric (includes intensity and percentage) ---
    try:
        numeric_val = float(stripped.replace(",", ""))
    except ValueError:
        # Could not parse as float despite infer_data_type saying numeric — treat as text
        return _indicator(
            value=stripped, raw_value=raw_value, raw_unit=None,
            standard_unit=None, normalized=True, unit_warning="value could not be parsed as number",
            data_type="text",
        )

    # Percentage tags: SEBI XBRL stores all Percentage* values as 0-1 fractions.
    # Multiply by 100 to get the standard display range of 0-100.
    # Only applies to tags with the word "Percentage" in the name — rate/ratio/coverage
    # tags use their own natural scale and must not be adjusted.
    # Guard: only scale values in [0, 1.001] to avoid double-scaling any that are already 0-100.
    if "Percentage" in tag and 0 <= numeric_val <= 1.001:
        scaled = round(numeric_val * 100, 6)
        return _indicator(
            value=scaled, raw_value=raw_value, raw_unit=None,
            standard_unit="%", normalized=True, unit_warning=None,
            data_type="percentage",
        )

    # Financial tags: units are inconsistent at the tag level across all 4 companies
    # (some in absolute Rupees, some in Crore, SAIL uses Lakhs for some tags).
    # A blanket correction is not safe. These tags are flagged as WARNING in validate.py
    # and will be resolved per-tag in Phase 4 (PDF extraction + unit verification).
    # For now, pass financial values through as-is — no conversion.

    # If this tag doesn't carry a physical unit (it's a dimensionless count/ratio/index),
    # pass the value through directly without unit resolution.
    if not _tag_needs_unit_conversion(tag):
        return _indicator(
            value=numeric_val, raw_value=raw_value, raw_unit=None,
            standard_unit=None, normalized=True, unit_warning=None,
            data_type=data_type,
        )

    # Resolve unit
    raw_unit = resolve_unit(tag, unit_tags_from_file, company_id, company_unit_cache, namespace_version)

    # No unit at all
    if raw_unit is None:
        # Zero of any physical unit is still zero — no conversion needed, no warning.
        # This silences spurious warnings on tags like EnergyConsumptionThroughOtherSourcesFromRenewableSources=0
        # where the company genuinely has nothing to report but no unit tag exists.
        if numeric_val == 0:
            return _indicator(
                value=0.0, raw_value=raw_value, raw_unit=None,
                standard_unit=None, normalized=True, unit_warning=None,
                data_type=data_type, value_status="zero",
            )
        return _indicator(
            value=numeric_val, raw_value=raw_value, raw_unit=None,
            standard_unit=None, normalized=False,
            unit_warning="unit unknown: no unit tag found and no fallback configured",
            data_type=data_type,
        )

    unit_key = _normalise_unit_key(raw_unit)

    # Unit string is "0", "-", or empty — company wrote a placeholder as the unit.
    # The value is zero or not reported; treat as zero with no warning.
    if unit_key in ("0", "-", "na", "n/a", "n.a.", "nil", "none", ""):
        return _indicator(
            value=0.0, raw_value=raw_value, raw_unit=raw_unit,
            standard_unit=None, normalized=True, unit_warning=None,
            data_type=data_type, value_status="zero",
        )

    # Disambiguate mass units for air emission tags.
    # Air emission standard unit is kilotonnes; waste standard unit is metric tonnes.
    # Same unit string means different things in each context — remap via "(air)" suffix.
    if _is_air_emission_tag(tag):
        if unit_key == "kg":
            unit_key = "kg (air)"           # kg → kilotonnes (÷ 1,000,000)
        elif unit_key in ("mt", "tonnes", "metric tonnes", "metric ton"):
            unit_key = "mt (air)"           # metric tonnes → kilotonnes (÷ 1,000)

    # Concentration unit — permanently non-normalizable
    if unit_key in {_normalise_unit_key(u) for u in UNIT_IS_CONCENTRATION}:
        return _indicator(
            value=numeric_val, raw_value=raw_value, raw_unit=raw_unit,
            standard_unit=None, normalized=False,
            unit_warning=(
                f"Concentration unit ({raw_unit}) cannot be converted to mass. "
                "Excluded from cross-company air emission comparisons."
            ),
            data_type=data_type,
        )

    # kg/tcs — needs production volume for conversion
    if unit_key in {_normalise_unit_key(u) for u in UNIT_REQUIRES_PRODUCTION_VOLUME}:
        converted, warning = convert_kg_per_tcs_to_kilotonnes(numeric_val, company_id, fiscal_year)
        if converted is None:
            return _indicator(
                value=numeric_val, raw_value=raw_value, raw_unit=raw_unit,
                standard_unit=STANDARD_UNITS["air"], normalized=False,
                unit_warning=warning, data_type=data_type,
            )
        return _indicator(
            value=converted, raw_value=raw_value, raw_unit=raw_unit,
            standard_unit=STANDARD_UNITS["air"], normalized=True,
            unit_warning=None, data_type=data_type,
        )

    # Standard conversion — unit_key may have been remapped (e.g. "kg"→"kg (air)"),
    # so look up by unit_key which is already normalised.
    factor = UNIT_CONVERSIONS.get(unit_key)
    if factor is None:
        return _indicator(
            value=numeric_val, raw_value=raw_value, raw_unit=raw_unit,
            standard_unit=None, normalized=False,
            unit_warning=f"Unknown unit '{raw_unit}': no conversion factor defined. Value preserved as-is.",
            data_type=data_type,
        )

    converted_val = numeric_val * factor
    # Determine the standard unit for this tag (best-effort from tag name pattern)
    standard_unit = _infer_standard_unit(tag, raw_unit)

    return _indicator(
        value=converted_val, raw_value=raw_value, raw_unit=raw_unit,
        standard_unit=standard_unit, normalized=True,
        unit_warning=None, data_type=data_type,
    )


def _indicator(
    value: Any,
    raw_value: str,
    raw_unit: str | None,
    standard_unit: str | None,
    normalized: bool,
    unit_warning: str | None,
    data_type: str,
    value_status: str = "value",
) -> dict[str, Any]:
    """
    Construct a normalized IndicatorValue dict.

    valueStatus semantics:
      "value"        — a real reported value (number, bool, or text)
      "zero"         — company explicitly reported zero (numeric 0, rawValue="0")
      "nil_reported" — company wrote nil/NA/not-applicable (rawValue preserved)
      "blank"        — field was empty in the XBRL file (not reported at all)
    """
    # Distinguish genuine zero from a value
    if value_status == "value" and isinstance(value, (int, float)) and value == 0:
        value_status = "zero"
    return {
        "value":       value,
        "rawValue":    raw_value,
        "rawUnit":     raw_unit,
        "standardUnit":standard_unit,
        "normalized":  normalized,
        "unitWarning": unit_warning,
        "dataType":    data_type,
        "valueStatus": value_status,
    }


# Tags whose name contains any of these substrings carry a physical unit that must be converted.
_UNIT_BEARING_PATTERNS = (
    # GHG
    "scope1", "scope2", "scope3", "emission", "co2", "ghg",
    # Energy
    "energy", "fuel", "electricity", "calorific",
    # Water
    "water", "withdrawal", "discharge",
    # Waste
    "waste", "generated", "recovered", "disposed", "recycled", "reused",
    # Air
    "nox", "sox", "particulatematter", "volatileorganic", "persistentorganic",
    "hazardousair", "airpollut",
)


_AIR_EMISSION_PATTERNS = ("nox", "sox", "particulatematter", "particulate", "voc",
                          "volatileorganic", "persistentorganic", "hazardousair", "pop", "hap")


def _is_air_emission_tag(tag: str) -> bool:
    """Return True if this tag represents an air emission metric."""
    tag_lower = tag.lower()
    return any(p in tag_lower for p in _AIR_EMISSION_PATTERNS)


def _tag_needs_unit_conversion(tag: str) -> bool:
    """
    Return True if this tag carries a physical unit that requires normalization.
    Returns False for dimensionless values (counts, percentages, booleans, text).
    """
    tag_lower = tag.lower()
    # Percentage/rate tags are dimensionless
    if any(p.lower() in tag_lower for p in PERCENTAGE_TAG_PATTERNS):
        return False
    # Intensity tags are dimensionless ratios (already divided by a denominator)
    if any(p.lower() in tag_lower for p in INTENSITY_TAG_PATTERNS):
        return False
    # Count tags are dimensionless
    count_prefixes = ("numberof", "totalnumber", "countof", "totalcount",
                      "numberand", "totaland")
    if any(tag_lower.startswith(p) for p in count_prefixes):
        return False
    # Boolean-pattern tags are dimensionless
    if any(p.lower() in tag_lower for p in BOOLEAN_TAG_PATTERNS):
        return False
    # Check if tag matches any unit-bearing pattern
    return any(p in tag_lower for p in _UNIT_BEARING_PATTERNS)


def _infer_standard_unit(tag: str, raw_unit: str) -> str | None:
    """Best-effort mapping from tag + raw unit to standard unit label."""
    tag_lower  = tag.lower()
    unit_lower = _normalise_unit_key(raw_unit)

    if "scope" in tag_lower and ("emission" in tag_lower or "co2" in unit_lower or "tco2" in unit_lower):
        return STANDARD_UNITS["ghg"]
    if "energy" in tag_lower or unit_lower in ("pj", "petajoules", "gj", "gigajoules", "tj", "terajoules", "mwh", "kwh"):
        return STANDARD_UNITS["energy"]
    if "water" in tag_lower or unit_lower in ("kl", "kilolitres", "kiloliters", "m3", "cubic metres"):
        return STANDARD_UNITS["water"]
    if "waste" in tag_lower:
        return STANDARD_UNITS["waste"]
    if "nox" in tag_lower or "sox" in tag_lower or "particulate" in tag_lower or "voc" in tag_lower:
        return STANDARD_UNITS["air"]
    return None


# ---------------------------------------------------------------------------
# Build per-company JSON structure from parsed file results
# ---------------------------------------------------------------------------

def build_company_json(
    company_id: str,
    parsed_years: list[dict[str, Any]],
) -> dict[str, Any]:
    """
    Convert a list of parsed file dicts (from parse_xbrl.py) into the final
    company JSON structure written to dashboard/src/data/companies/{id}.json.

    Also builds and returns a unit cache so FY23 units can be used as fallback
    for FY24/FY25 (files are expected sorted FY2023 → FY2024 → FY2025).

    Returns: CompanyData dict ready for JSON serialisation.
    """
    from datetime import date

    years_data: dict[str, Any] = {}
    company_unit_cache: dict[str, str] = {}

    for parsed in parsed_years:
        fy       = parsed["fiscalYear"]
        ns_ver   = parsed["namespaceVersion"]   # "v1" | "v2" | "v3" | "v4"
        unit_tags = parsed["unitTags"]
        dcy_values = parsed["dcyValues"]
        dim_rows  = parsed["dimensionalRows"]

        # Update the unit cache with whatever unit tags this file provided
        for tag, unit in unit_tags.items():
            if unit:
                company_unit_cache[tag] = unit

        # Normalise all DCYMain scalar values
        normalised: dict[str, Any] = {}
        for tag, raw_val in dcy_values.items():
            ind_val = normalize_value(
                tag=tag,
                raw_value=raw_val,
                unit_tags_from_file=unit_tags,
                company_id=company_id,
                fiscal_year=fy,
                company_unit_cache=company_unit_cache,
                namespace_version=ns_ver,
            )
            normalised[tag] = ind_val

        # Normalise dimensional rows (units inherited from scalar unit cache for same tags)
        normalised_dims: list[dict[str, Any]] = []
        for row in dim_rows:
            norm_row_values: dict[str, Any] = {}
            for tag, raw_val in row["values"].items():
                ind_val = normalize_value(
                    tag=tag,
                    raw_value=raw_val,
                    unit_tags_from_file=unit_tags,
                    company_id=company_id,
                    fiscal_year=fy,
                    company_unit_cache=company_unit_cache,
                    namespace_version=ns_ver,
                )
                norm_row_values[tag] = ind_val
            if norm_row_values:
                normalised_dims.append({
                    "contextId":  row["contextId"],
                    "dimensions": row["dimensions"],
                    "values":     norm_row_values,
                })

        years_data[fy] = {
            "_meta": {
                "reportingBasis": parsed["reportingBasis"],
                "basisWarning":   parsed["basisWarning"],
            },
            **normalised,
            "_dimensionalData": normalised_dims,
        }

    return {
        "companyId":   company_id,
        "lastUpdated": date.today().isoformat(),
        "years":       years_data,
    }
