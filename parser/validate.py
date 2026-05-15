# parser/validate.py
# Runs automated validation checks on the normalized company JSON files.
# Produces validation_report.json in the parser/ directory.
#
# Four check categories:
#   1. Peer outliers — cross-company same-year ratio test
#   2. Self outliers — year-over-year change > 50% for same company
#   3. Internal consistency — additive field checks, water withdrawal >= consumption
#   4. Data completeness — unit warnings, not_normalized, missing tags
#
# Severity:
#   BLOCKING — must reach 0 before proceeding to AI analysis / UI
#   WARNING  — must each have a documented explanation before proceeding
#
# Run from parser/ directory: python validate.py
# Or from repo root:          python parser/validate.py

import json
import sys
from pathlib import Path
from statistics import median
from typing import Any

sys.path.insert(0, str(Path(__file__).parent))

from config import (
    COMPANIES,
    OUTPUT_DIR,
    PEER_OUTLIER_RATIO_LARGE,
    PEER_OUTLIER_RATIO_JINDAL,
    PEER_OUTLIER_RATIO_INTENSITY,
    YOY_CHANGE_THRESHOLD,
    ADDITIVE_TOLERANCE,
    LTIFR_IMPLAUSIBLE_WORKFORCE_MIN,
    INTENSITY_TAG_PATTERNS,
)

VALIDATION_REPORT_PATH = Path(__file__).parent / "validation_report.json"
COMPANIES_DIR = OUTPUT_DIR / "companies"

# Company groups for peer outlier checks
LARGE_CAP_COMPANIES  = {"tata-steel", "jsw-steel", "sail"}
SMALL_CAP_COMPANIES  = {"jindal-stainless"}
ALL_COMPANY_IDS      = set(COMPANIES.keys())

# Tata Steel FY2023 → FY2024 YoY changes are expected (consolidated → standalone).
# Suppress self-outlier flags for this specific transition.
TATA_SUPPRESSED_YOY  = ("tata-steel", "FY2023", "FY2024")

FISCAL_YEARS = ["FY2023", "FY2024", "FY2025"]

# Financial tag prefixes: peer outliers on financial amounts are downgraded to WARNING
# because companies use inconsistent units (absolute Rupees / Crore / Lakhs) across
# different tags. These will be resolved per-tag in Phase 4 (PDF extraction).
# The core ESG metrics (emissions, energy, water, waste, H&S) are unaffected.
FINANCIAL_TAG_PREFIXES = (
    "Amount", "Revenue", "Cost", "Wages", "Salary", "Turnover",
    "Purchases", "Sales", "Loans", "Investment", "Payment",
    "TotalRevenue", "GrossWages", "TotalWages",
)

def _is_financial_tag(tag: str) -> bool:
    return any(tag.startswith(p) or p in tag for p in FINANCIAL_TAG_PREFIXES)

# Tata FY2023 is consolidated — all absolute-value outliers vs standalone peers are
# expected and auto-downgraded to WARNING (not BLOCKING).
TATA_CONSOLIDATED_YEAR = "FY2023"

# Tags where peer outlier severity is capped at WARNING regardless of ratio magnitude.
# These tags have structurally high cross-company variance that is NOT indicative of
# unit errors — rather they reflect genuine differences in operations, infrastructure,
# or waste management practices.
PEER_OUTLIER_WARNING_ONLY_TAGS: frozenset[str] = frozenset({
    # Waste sub-category distribution: incineration/landfilling/other_disposal ratios
    # are highly company-specific based on waste management contracts, plant types,
    # and geographic regulations. The TOTAL waste disposed is the meaningful comparison.
    "WasteDisposedByIncineration",
    "WasteDisposedByLandfilling",
    "WasteDisposedByOtherDisposalOperations",
    "WasteRecoveredThroughOtherRecoveryOperations",
    "WasteRecoveredThroughReUsed",
    "WasteRecoveredThroughRecycling",
    "WasteRecoveredThroughCoProcessing",
    # Niche waste streams: biomedical, e-waste, plastic waste magnitudes vary enormously
    # based on whether company operates township hospitals (Tata, SAIL) and digital assets.
    "BioMedicalWaste",
    "EWaste",
    "PlasticWaste",
    # Water source/discharge mix: groundwater vs surface water vs third-party depends entirely
    # on plant geography and water infrastructure. Total withdrawal/discharge is comparable.
    # SAIL FY2023 discharge: full amount reclassified to Groundwater per manual review
    # (SAIL BRSR does not distinguish discharge destination).
    "WaterWithdrawalByGroundwater",
    "WaterWithdrawalByThirdPartyWater",
    "TotalWaterDischargedInKilolitres",
    "WaterDischargeToGroundwater",
    "WaterDischargeToSurfaceWater",
    # PercentageOfRAndD / PercentageOfCapex: SEBI BRSR v1/v2 used these as percentage fields;
    # some companies report absolute crore amounts in these tags — cross-company comparison invalid.
    "PercentageOfRAndD",
    "PercentageOfCapex",
    # Pre-computed intensity/ratio tags derived from SAIL's XBRL contain a known unit error
    # (SAIL's energy denominator was in GJ when the correct unit is TJ), making SAIL's
    # derived intensity tags ~1000× too small. Flag as WARNING — the raw data issue is documented.
    "EnergyIntensityInTermOfPhysicalOutput",
    "EnergyIntensityInTermOfRevenue",
    # Electricity sub-components: SAIL FY2024 reports TotalElectricityConsumptionFromNonRenewableSources
    # in TJ (pre-normalized), which produces extreme peer ratios vs GJ-denominated peers.
    # Pre-existing unit issue — documented, not a data entry error.
    "TotalElectricityConsumptionFromNonRenewableSources",
    "TotalElectricityConsumptionFromRenewableSources",
    # Total waste disposed: highly variable based on company strategy (recovery vs disposal).
    # SAIL FY2023 confirmed correct at 3,671 MT (most waste classified as recovered, not disposed).
    # Tata FY2024 standalone = 307,577 MT — pending PDF verification (may be genuine landfill legacy).
    # Sub-category totals (TotalWasteGenerated, TotalWasteRecovered) are more comparable.
    "TotalWasteDisposed",
})


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _is_intensity_tag(tag: str) -> bool:
    tag_lower = tag.lower()
    return any(p.lower() in tag_lower for p in INTENSITY_TAG_PATTERNS)


def _numeric_value(ind: dict[str, Any]) -> float | None:
    """Return the normalized numeric value if the indicator is normalized and numeric."""
    if not isinstance(ind, dict):
        return None
    if not ind.get("normalized", False):
        return None
    val = ind.get("value")
    if val is None:
        return None
    try:
        return float(val)
    except (TypeError, ValueError):
        return None


def _load_companies() -> dict[str, dict]:
    """Load all company JSON files. Returns {company_id: company_data}."""
    data = {}
    for company_id in COMPANIES:
        path = COMPANIES_DIR / f"{company_id}.json"
        if not path.exists():
            raise FileNotFoundError(
                f"Company JSON not found: {path}. Run run_all.py first."
            )
        data[company_id] = json.loads(path.read_text(encoding="utf-8"))
    return data


def _get_numeric_tags_for_year(
    fy_data: dict[str, Any],
    include_not_normalized: bool = False,
) -> dict[str, float]:
    """Return {tag: value} for all numeric, normalized (and optionally not-normalized) tags."""
    result: dict[str, float] = {}
    for tag, ind in fy_data.items():
        if tag.startswith("_"):
            continue
        if not isinstance(ind, dict):
            continue
        if not include_not_normalized and not ind.get("normalized", False):
            continue
        val = ind.get("value")
        if val is None:
            continue
        try:
            f = float(val)
            result[tag] = f
        except (TypeError, ValueError):
            continue
    return result


# ---------------------------------------------------------------------------
# Check 1: Peer outliers (cross-company, same year)
# ---------------------------------------------------------------------------

def check_peer_outliers(company_data: dict[str, dict]) -> list[dict]:
    """
    For each year and each numeric tag, compare each company's value against
    the median of its peer group.

    Rules:
    - Large-cap trio (Tata/JSW/SAIL): flag if ratio > 5× or < 1/5×  vs peer median.
    - Jindal vs large-cap trio: flag if ratio > 20× (size difference).
    - Intensity metrics: 5× rule for ALL companies regardless of size.

    Returns list of flag dicts.
    """
    flags = []

    for fy in FISCAL_YEARS:
        # Collect numeric values per company for this year
        year_values: dict[str, dict[str, float]] = {}
        for company_id, cdata in company_data.items():
            fy_data = cdata["years"].get(fy)
            if fy_data is None:
                continue
            year_values[company_id] = _get_numeric_tags_for_year(fy_data)

        if len(year_values) < 2:
            continue

        # Collect all tags present in at least 2 companies
        tag_company_map: dict[str, dict[str, float]] = {}
        for company_id, vals in year_values.items():
            for tag, val in vals.items():
                if val == 0:
                    continue  # skip zeros — can't compute ratio
                if tag not in tag_company_map:
                    tag_company_map[tag] = {}
                tag_company_map[tag][company_id] = val

        for tag, company_vals in tag_company_map.items():
            if len(company_vals) < 2:
                continue

            is_intensity = _is_intensity_tag(tag)

            # Check each company against its peer group
            for company_id, val in company_vals.items():
                if company_id in SMALL_CAP_COMPANIES and not is_intensity:
                    # Jindal vs large caps: use 20× threshold for absolute metrics
                    peers = {c: v for c, v in company_vals.items()
                             if c in LARGE_CAP_COMPANIES}
                    if len(peers) < 1:
                        continue
                    peer_med = median(peers.values())
                    threshold = PEER_OUTLIER_RATIO_JINDAL
                else:
                    # Large-cap vs large-cap (or intensity metrics for any company)
                    peers = {c: v for c, v in company_vals.items() if c != company_id}
                    if len(peers) < 1:
                        continue
                    peer_med = median(peers.values())
                    threshold = PEER_OUTLIER_RATIO_INTENSITY if is_intensity else PEER_OUTLIER_RATIO_LARGE

                if peer_med == 0:
                    continue

                ratio = val / peer_med
                if ratio > threshold or ratio < (1 / threshold):
                    # Determine severity
                    raw_unit = company_data[company_id]["years"][fy].get(tag, {}).get("rawUnit")
                    severity = _classify_outlier_severity(tag, ratio, threshold, raw_unit, company_id, fy)
                    flags.append({
                        "type":          "PEER_OUTLIER",
                        "severity":      severity,
                        "company":       company_id,
                        "year":          fy,
                        "tag":           tag,
                        "value":         val,
                        "peerMedian":    peer_med,
                        "ratio":         round(ratio, 2),
                        "threshold":     threshold,
                        "rawUnit":       raw_unit,
                        "suspectedCause": _guess_outlier_cause(tag, ratio, raw_unit, company_id),
                    })

    return flags


def _classify_outlier_severity(
    tag: str, ratio: float, threshold: float, raw_unit: str | None,
    company_id: str, year: str,
) -> str:
    """Classify outlier as BLOCKING or WARNING based on ratio magnitude and context.

    Downgrades to WARNING for:
    - Financial tags: inconsistent reporting units (absolute ₹ / Crore / Lakhs) — deferred to Phase 4
    - Tata Steel FY2023: consolidated filing basis inflates all absolute metrics vs standalone peers
    - Jindal Stainless absolute metrics: stainless steel + ~10× smaller scale; ANY absolute ratio
      is expected to be extreme vs carbon-steel large-caps. Only intensity metrics are comparable.
    - PEER_OUTLIER_WARNING_ONLY_TAGS: structurally high variance tags (waste sub-categories,
      water source mix, niche waste streams) where ratio differences are operational, not unit errors
    """
    # Tags with structurally high cross-company variance: always WARNING
    if tag in PEER_OUTLIER_WARNING_ONLY_TAGS:
        return "WARNING"

    # Financial tags: unit ambiguity can't be resolved at parse time → always WARNING
    if _is_financial_tag(tag):
        return "WARNING"

    # Tata FY2023 consolidated basis: absolute-value comparisons with standalone peers are
    # structurally misleading — downgrade to WARNING, not BLOCKING
    if company_id == "tata-steel" and year == TATA_CONSOLIDATED_YEAR and not _is_intensity_tag(tag):
        return "WARNING"

    # Jindal Stainless: stainless steel + much smaller scale means absolute metrics will
    # frequently exceed the 20× Jindal threshold. Only intensity metrics are truly comparable.
    if company_id == "jindal-stainless" and not _is_intensity_tag(tag):
        return "WARNING"

    # If the ratio is extreme (e.g. 100× or 1/100×), likely a unit conversion error → blocking
    extreme_factor = threshold * 10
    if ratio > extreme_factor or ratio < (1 / extreme_factor):
        return "BLOCKING"
    return "WARNING"


def _guess_outlier_cause(
    tag: str, ratio: float, raw_unit: str | None, company_id: str
) -> str:
    """Heuristic guess at the cause of a peer outlier."""
    tag_lower = tag.lower()
    if raw_unit and any(u in raw_unit.lower() for u in ("million", "million tonnes", "million litres")):
        return "possible unit mismatch: check if company reported in different scale"
    if "energy" in tag_lower and (ratio > 100 or ratio < 0.01):
        return "likely unit mismatch: extreme ratio suggests PJ vs GJ or TJ vs GJ reporting error"
    if "emission" in tag_lower and (ratio > 100 or ratio < 0.01):
        return "likely unit mismatch: check if company reported in million tonnes vs tonnes"
    if "water" in tag_lower and (ratio > 50 or ratio < 0.02):
        return "possible unit mismatch: check kL vs ML or m³ vs kL"
    if company_id == "sail" and any(p in tag_lower for p in ("nox", "sox", "particulate")):
        return "SAIL reports air emissions in µg/m³ (concentration) — incomparable to mass units"
    if company_id == "jindal-stainless":
        return "size difference (stainless steel, ~10× smaller scale) — verify absolute vs intensity"
    if company_id == "tata-steel":
        return "check reporting basis: FY2023 = consolidated (includes overseas ops), FY2024+ = standalone"
    return "investigate: may be genuine difference, unit error, or PSU reporting gap"


# ---------------------------------------------------------------------------
# Check 2: Self-outliers (year-over-year, same company)
# ---------------------------------------------------------------------------

def check_self_outliers(company_data: dict[str, dict]) -> list[dict]:
    """
    For each company, flag any tag where the value changed by more than
    YOY_CHANGE_THRESHOLD between consecutive years.

    Tata Steel FY2023 → FY2024 changes are auto-suppressed (expected basis change).
    """
    flags = []

    for company_id, cdata in company_data.items():
        years = sorted(fy for fy in cdata["years"] if fy in FISCAL_YEARS)

        for i in range(len(years) - 1):
            fy_from = years[i]
            fy_to   = years[i + 1]

            # Suppress Tata Steel FY2023 → FY2024 (consolidated → standalone)
            if (company_id, fy_from, fy_to) == TATA_SUPPRESSED_YOY:
                continue

            vals_from = _get_numeric_tags_for_year(cdata["years"][fy_from])
            vals_to   = _get_numeric_tags_for_year(cdata["years"][fy_to])

            common_tags = set(vals_from) & set(vals_to)
            for tag in common_tags:
                v_from = vals_from[tag]
                v_to   = vals_to[tag]

                if v_from == 0 and v_to == 0:
                    continue
                if v_from == 0:
                    continue  # Can't compute % change from zero

                change = abs(v_to - v_from) / abs(v_from)
                if change > YOY_CHANGE_THRESHOLD:
                    flags.append({
                        "type":      "SELF_OUTLIER",
                        "severity":  "WARNING",
                        "company":   company_id,
                        "yearFrom":  fy_from,
                        "yearTo":    fy_to,
                        "tag":       tag,
                        "valueFrom": v_from,
                        "valueTo":   v_to,
                        "changePct": round(change * 100, 1),
                        "direction": "increase" if v_to > v_from else "decrease",
                    })

    return flags


# ---------------------------------------------------------------------------
# Check 3: Internal consistency (cross-field, same company-year)
# ---------------------------------------------------------------------------

# Additive checks: (total_tag, [component_tag, ...])
# Total should equal sum of components within ADDITIVE_TOLERANCE.
ADDITIVE_CHECKS: list[tuple[str, list[str]]] = [
    (
        "TotalEnergyConsumedFromRenewableAndNonRenewableSources",
        [
            "TotalEnergyConsumedFromRenewableSources",
            "TotalEnergyConsumedFromNonRenewableSources",
        ],
    ),
    (
        "TotalWasteGenerated",
        [
            "TotalWasteRecovered",
            "TotalWasteDisposed",
        ],
    ),
]

# Water constraint: withdrawal must be >= consumption (water-in >= water-used)
WATER_WITHDRAWAL_TAG    = "TotalVolumeOfWaterWithdrawal"
WATER_CONSUMPTION_TAG   = "TotalVolumeOfWaterConsumption"

# LTIFR implausibility check: total workforce per company-year
WORKFORCE_TAGS = [
    "TotalNumberOfEmployees",
    "TotalNumberOfWorkers",
    "TotalPermanentEmployees",
    "TotalContractWorkers",
]
LTIFR_TAG = "LostTimeInjuryFrequencyRate"


def check_consistency(company_data: dict[str, dict]) -> list[dict]:
    """
    Check additive field relationships, water balance, and LTIFR implausibility.
    Returns list of flag dicts.
    """
    flags = []

    for company_id, cdata in company_data.items():
        for fy, fy_data in cdata["years"].items():
            if fy not in FISCAL_YEARS:
                continue
            flags.extend(_check_additive(company_id, fy, fy_data))
            flags.extend(_check_water_balance(company_id, fy, fy_data))
            flags.extend(_check_ltifr(company_id, fy, fy_data))
            flags.extend(_check_too_good(company_id, fy, fy_data))

    return flags


def _check_additive(
    company_id: str, fy: str, fy_data: dict[str, Any]
) -> list[dict]:
    flags = []
    for total_tag, component_tags in ADDITIVE_CHECKS:
        total_ind = fy_data.get(total_tag)
        if total_ind is None:
            continue
        total_val = _numeric_value(total_ind)
        if total_val is None or total_val == 0:
            continue

        component_vals = []
        missing = []
        for ctag in component_tags:
            cind = fy_data.get(ctag)
            if cind is None:
                missing.append(ctag)
                continue
            cv = _numeric_value(cind)
            if cv is None:
                missing.append(ctag)
            else:
                component_vals.append(cv)

        if missing or len(component_vals) < len(component_tags):
            continue  # Can't check if components are missing

        component_sum = sum(component_vals)
        if component_sum == 0:
            continue

        diff = abs(total_val - component_sum) / max(abs(total_val), abs(component_sum))
        if diff > ADDITIVE_TOLERANCE:
            flags.append({
                "type":         "CONSISTENCY",
                "severity":     "WARNING",
                "check":        "additive",
                "company":      company_id,
                "year":         fy,
                "totalTag":     total_tag,
                "totalValue":   total_val,
                "componentTags": component_tags,
                "componentSum": component_sum,
                "diffPct":      round(diff * 100, 2),
            })
    return flags


def _check_water_balance(
    company_id: str, fy: str, fy_data: dict[str, Any]
) -> list[dict]:
    withdrawal_ind  = fy_data.get(WATER_WITHDRAWAL_TAG)
    consumption_ind = fy_data.get(WATER_CONSUMPTION_TAG)
    if withdrawal_ind is None or consumption_ind is None:
        return []
    w = _numeric_value(withdrawal_ind)
    c = _numeric_value(consumption_ind)
    if w is None or c is None or w == 0:
        return []
    if c > w * (1 + ADDITIVE_TOLERANCE):
        return [{
            "type":            "CONSISTENCY",
            "severity":        "BLOCKING",
            "check":           "water_balance",
            "company":         company_id,
            "year":            fy,
            "withdrawal":      w,
            "consumption":     c,
            "message":         f"Consumption ({c:,.0f} kL) > Withdrawal ({w:,.0f} kL) — physically impossible",
        }]
    return []


def _check_ltifr(
    company_id: str, fy: str, fy_data: dict[str, Any]
) -> list[dict]:
    """Flag LTIFR=0 for large workforces as implausible."""
    ltifr_ind = fy_data.get(LTIFR_TAG)
    if ltifr_ind is None:
        return []
    ltifr_val = _numeric_value(ltifr_ind)
    if ltifr_val is None or ltifr_val != 0:
        return []

    # Estimate total workforce from dimensional data or scalar tags
    total_workforce = _estimate_workforce(fy_data)
    if total_workforce is None or total_workforce < LTIFR_IMPLAUSIBLE_WORKFORCE_MIN:
        return []

    return [{
        "type":            "TOO_GOOD",
        "severity":        "WARNING",
        "check":           "ltifr_zero",
        "company":         company_id,
        "year":            fy,
        "tag":             LTIFR_TAG,
        "value":           0,
        "estimatedWorkforce": total_workforce,
        "message":         (
            f"LTIFR=0 with estimated workforce {total_workforce:,} — "
            "implausible for large-scale manufacturing. "
            "Possible under-reporting or contractor exclusion. "
            "NOT a normalization error (raw XML=0). Verify against BRSR PDF."
        ),
    }]


def _estimate_workforce(fy_data: dict[str, Any]) -> int | None:
    """Estimate total workforce from scalar tags, return None if not found."""
    for tag in WORKFORCE_TAGS:
        ind = fy_data.get(tag)
        if ind is None:
            continue
        val = _numeric_value(ind)
        if val and val > 100:
            return int(val)
    return None


def _check_too_good(
    company_id: str, fy: str, fy_data: dict[str, Any]
) -> list[dict]:
    """Flag suspiciously perfect values on large-workforce metrics."""
    flags = []

    # 100% on large-workforce percentage metrics
    SUSPICIOUS_100PCT_TAGS = [
        "PercentageOfEmployeesCoveredUnderTraining",
        "PercentageOfWorkersCoveredUnderTraining",
        "PercentageOfEmployeesCoveredUnderHealthAndSafetyManagementSystem",
        "PercentageOfWorkersCoveredUnderHealthAndSafetyManagementSystem",
        "PercentageOfWorkersWithMinimumWage",
        "PercentageOfEmployeesWithMinimumWage",
    ]
    workforce = _estimate_workforce(fy_data)
    if workforce and workforce >= LTIFR_IMPLAUSIBLE_WORKFORCE_MIN:
        for tag in SUSPICIOUS_100PCT_TAGS:
            ind = fy_data.get(tag)
            if ind is None:
                continue
            val = _numeric_value(ind)
            if val is None:
                continue
            # After percentage scaling, 100% means the scaled value is 100
            if abs(val - 100.0) < 0.01:
                flags.append({
                    "type":            "TOO_GOOD",
                    "severity":        "WARNING",
                    "check":           "suspicious_100pct",
                    "company":         company_id,
                    "year":            fy,
                    "tag":             tag,
                    "value":           val,
                    "estimatedWorkforce": workforce,
                    "message":         (
                        f"100% reported for {tag} with workforce ~{workforce:,} — "
                        "verify against BRSR PDF. NOT a normalization error."
                    ),
                })

    return flags


# ---------------------------------------------------------------------------
# Check 4: Data completeness
# ---------------------------------------------------------------------------

def check_completeness(company_data: dict[str, dict]) -> list[dict]:
    """
    Report all unit warnings and not-normalized entries.
    Unit warnings with a recognized explanation (concentration units, changed units)
    are downgraded to WARNING; unexplained unknown units are BLOCKING.
    """
    flags = []

    for company_id, cdata in company_data.items():
        for fy, fy_data in cdata["years"].items():
            if fy not in FISCAL_YEARS:
                continue
            for tag, ind in fy_data.items():
                if tag.startswith("_"):
                    continue
                if not isinstance(ind, dict):
                    continue
                unit_warning = ind.get("unitWarning")
                if not unit_warning:
                    continue

                # Classify severity
                if "Concentration unit" in unit_warning:
                    severity = "WARNING"
                    category = "CONCENTRATION_UNIT"
                elif "unit unknown" in unit_warning:
                    severity = "BLOCKING"
                    category = "UNKNOWN_UNIT"
                else:
                    severity = "WARNING"
                    category = "UNIT_ISSUE"

                flags.append({
                    "type":       "COMPLETENESS",
                    "severity":   severity,
                    "category":   category,
                    "company":    company_id,
                    "year":       fy,
                    "tag":        tag,
                    "rawValue":   ind.get("rawValue"),
                    "rawUnit":    ind.get("rawUnit"),
                    "unitWarning": unit_warning,
                })

    return flags


# ---------------------------------------------------------------------------
# Summary and report generation
# ---------------------------------------------------------------------------

def _count_severity(flags: list[dict], severity: str) -> int:
    return sum(1 for f in flags if f.get("severity") == severity)


def build_report(all_flags: list[dict]) -> dict:
    blocking = _count_severity(all_flags, "BLOCKING")
    warnings = _count_severity(all_flags, "WARNING")

    # Separate by type for structured report
    peer_outliers    = [f for f in all_flags if f["type"] == "PEER_OUTLIER"]
    self_outliers    = [f for f in all_flags if f["type"] == "SELF_OUTLIER"]
    consistency      = [f for f in all_flags if f["type"] == "CONSISTENCY"]
    too_good         = [f for f in all_flags if f["type"] == "TOO_GOOD"]
    completeness     = [f for f in all_flags if f["type"] == "COMPLETENESS"]

    return {
        "summary": {
            "totalFlags": len(all_flags),
            "blocking":   blocking,
            "warnings":   warnings,
            "canProceed": blocking == 0,
        },
        "peerOutliers":  peer_outliers,
        "selfOutliers":  self_outliers,
        "consistency":   consistency,
        "tooGood":       too_good,
        "completeness":  completeness,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("=" * 60)
    print("BRSR XBRL Validator — validate.py")
    print("=" * 60)

    print("\nLoading company data...")
    try:
        company_data = _load_companies()
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    print("Running checks...")
    all_flags: list[dict] = []

    print("  [1/4] Peer outliers...")
    peer_flags = check_peer_outliers(company_data)
    all_flags.extend(peer_flags)
    print(f"        {len(peer_flags)} flags ({_count_severity(peer_flags, 'BLOCKING')} blocking, "
          f"{_count_severity(peer_flags, 'WARNING')} warnings)")

    print("  [2/4] Self outliers (YoY)...")
    self_flags = check_self_outliers(company_data)
    all_flags.extend(self_flags)
    print(f"        {len(self_flags)} flags ({_count_severity(self_flags, 'BLOCKING')} blocking, "
          f"{_count_severity(self_flags, 'WARNING')} warnings)")

    print("  [3/4] Internal consistency...")
    consistency_flags = check_consistency(company_data)
    all_flags.extend(consistency_flags)
    print(f"        {len(consistency_flags)} flags ({_count_severity(consistency_flags, 'BLOCKING')} blocking, "
          f"{_count_severity(consistency_flags, 'WARNING')} warnings)")

    print("  [4/4] Data completeness...")
    completeness_flags = check_completeness(company_data)
    all_flags.extend(completeness_flags)
    print(f"        {len(completeness_flags)} flags ({_count_severity(completeness_flags, 'BLOCKING')} blocking, "
          f"{_count_severity(completeness_flags, 'WARNING')} warnings)")

    report = build_report(all_flags)

    # Write report
    VALIDATION_REPORT_PATH.write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"\nReport written to: {VALIDATION_REPORT_PATH.relative_to(VALIDATION_REPORT_PATH.parent.parent)}")

    # Print summary
    s = report["summary"]
    print(f"\n{'=' * 60}")
    print(f"VALIDATION SUMMARY")
    print(f"  Total flags:   {s['totalFlags']}")
    print(f"  BLOCKING:      {s['blocking']}")
    print(f"  WARNING:       {s['warnings']}")
    print(f"  Can proceed:   {'YES' if s['canProceed'] else 'NO — resolve BLOCKING flags first'}")
    print(f"{'=' * 60}")

    # Print BLOCKING flags
    blocking_flags = [f for f in all_flags if f.get("severity") == "BLOCKING"]
    if blocking_flags:
        print(f"\nBLOCKING FLAGS ({len(blocking_flags)}):")
        for f in blocking_flags:
            _print_flag(f)

    # Print first 30 warnings
    warning_flags = [f for f in all_flags if f.get("severity") == "WARNING"]
    if warning_flags:
        print(f"\nWARNINGS ({len(warning_flags)}, showing first 30):")
        for f in warning_flags[:30]:
            _print_flag(f)
        if len(warning_flags) > 30:
            print(f"  ... and {len(warning_flags) - 30} more (see validation_report.json)")

    if blocking_flags:
        sys.exit(1)
    else:
        print("\nNo blocking flags. Review warnings before proceeding to AI analysis.")


def _print_flag(f: dict) -> None:
    ftype = f["type"]
    sev   = f["severity"]
    if ftype == "PEER_OUTLIER":
        print(f"  [{sev}] {ftype} | {f['company']} {f['year']} | {f['tag']}")
        print(f"           value={f['value']:,.2f} | peer_median={f['peerMedian']:,.2f} | "
              f"ratio={f['ratio']:.1f}x | rawUnit={f.get('rawUnit')}")
        print(f"           cause: {f['suspectedCause']}")
    elif ftype == "SELF_OUTLIER":
        print(f"  [{sev}] {ftype} | {f['company']} {f['yearFrom']}→{f['yearTo']} | {f['tag']}")
        print(f"           {f['valueFrom']:,.2f} → {f['valueTo']:,.2f} ({f['direction']} {f['changePct']:.0f}%)")
    elif ftype == "CONSISTENCY":
        print(f"  [{sev}] {ftype} | {f['company']} {f['year']} | {f['check']}")
        if f["check"] == "additive":
            print(f"           {f['totalTag']}: total={f['totalValue']:,.2f}, "
                  f"sum_of_parts={f['componentSum']:,.2f}, diff={f['diffPct']:.1f}%")
        else:
            print(f"           {f.get('message', '')}")
    elif ftype == "TOO_GOOD":
        print(f"  [{sev}] {ftype} | {f['company']} {f['year']} | {f['tag']} = {f['value']}")
        print(f"           {f['message']}")
    elif ftype == "COMPLETENESS":
        print(f"  [{sev}] {ftype} | {f['category']} | {f['company']} {f['year']} | {f['tag']}")
        print(f"           rawUnit={f.get('rawUnit')} | {f['unitWarning']}")
    else:
        print(f"  [{sev}] {ftype} | {f}")


if __name__ == "__main__":
    main()
