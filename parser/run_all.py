# parser/run_all.py
# Entry point: parse all 4 companies, normalize, write output JSON to dashboard/src/data/.
# Run from the parser/ directory: python run_all.py
# Or from repo root: python parser/run_all.py

import json
import sys
from pathlib import Path

# Allow running from repo root or from parser/
sys.path.insert(0, str(Path(__file__).parent))

from config import COMPANIES, XBRL_DIR, OUTPUT_DIR
from parse_xbrl import parse_company
from normalize import build_company_json


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  Wrote {path.relative_to(path.parent.parent.parent.parent)}")


def _build_companies_registry(results: dict[str, dict]) -> dict:
    """Build companies.json from parsed company data."""
    registry = {}
    for company_id, company_data in results.items():
        company_meta = COMPANIES[company_id]
        available_years = sorted(company_data["years"].keys())
        registry[company_id] = {
            "id":             company_id,
            "name":           company_meta["name"],
            "sector":         company_meta["sector"],
            "availableYears": available_years,
        }
    return registry


def _build_indicators_stub(results: dict[str, dict]) -> dict:
    """
    Build a stub indicators.json from all canonical tags found across all companies.
    Labels, BRSR mappings, and categories will be enriched by Gemini Pro in Phase 2.
    The stub ensures every tag has an entry with at least its canonical name.
    """
    all_tags: set[str] = set()
    for company_data in results.values():
        for fy_data in company_data["years"].values():
            for key, val in fy_data.items():
                if key.startswith("_"):
                    continue
                all_tags.add(key)

    indicators: dict[str, dict] = {}
    for tag in sorted(all_tags):
        indicators[tag] = {
            "canonicalTag":              tag,
            "label":                     "",        # to be filled by Gemini Pro
            "brsr":                      {"principle": "", "section": ""},
            "dataType":                  "",        # to be inferred from data
            "standardUnit":              None,
            "category":                  "",        # to be filled by Gemini Pro
            "subcategory":               "",
            "comparableAcrossCompanies": True,      # default; Gemini / Claude to flag exceptions
        }

    return indicators


# ---------------------------------------------------------------------------
# Spot-check validation: verify known values match expectations
# ---------------------------------------------------------------------------

SPOT_CHECKS = [
    # (company_id, fiscal_year, tag, expected_value_approx, tolerance_fraction)
    # Tata Steel FY2023: Scope 1 = 75.75 Million tCO2e → normalized 75,750,000 tCO2e
    ("tata-steel", "FY2023", "TotalScope1Emissions", 75_750_000, 0.01),
    # Tata Steel FY2024: Scope 1 = 56 (same unit assumed PJ... wait, that's energy)
    # Scope 1 FY2024 = 56 Million tCO2e → 56,000,000
    ("tata-steel", "FY2024", "TotalScope1Emissions", 56_000_000, 0.01),
    # Tata Steel FY2025: Scope 1 = 61 Million tCO2e → 61,000,000
    ("tata-steel", "FY2025", "TotalScope1Emissions", 61_000_000, 0.01),
]


def run_spot_checks(results: dict[str, dict]) -> list[str]:
    """
    Run spot-checks against known expected values.
    Returns a list of failure messages (empty list = all passed).
    """
    failures = []
    for company_id, fy, tag, expected, tol in SPOT_CHECKS:
        company_data = results.get(company_id, {})
        fy_data = company_data.get("years", {}).get(fy, {})
        ind = fy_data.get(tag)
        if ind is None:
            failures.append(f"MISSING  {company_id} {fy} {tag}")
            continue
        if not ind.get("normalized"):
            failures.append(
                f"NOT NORMALIZED  {company_id} {fy} {tag} "
                f"(warning: {ind.get('unitWarning')})"
            )
            continue
        actual = ind.get("value")
        if actual is None:
            failures.append(f"NULL VALUE  {company_id} {fy} {tag}")
            continue
        try:
            actual_f = float(actual)
        except (TypeError, ValueError):
            failures.append(f"NON-NUMERIC  {company_id} {fy} {tag}: {actual!r}")
            continue
        if expected == 0:
            if actual_f != 0:
                failures.append(f"MISMATCH  {company_id} {fy} {tag}: got {actual_f}, expected 0")
        else:
            ratio = abs(actual_f - expected) / abs(expected)
            if ratio > tol:
                failures.append(
                    f"MISMATCH  {company_id} {fy} {tag}: "
                    f"got {actual_f:,.0f}, expected ~{expected:,.0f} "
                    f"(diff {ratio:.1%})"
                )
    return failures


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("=" * 60)
    print("BRSR XBRL Parser — run_all.py")
    print("=" * 60)

    results: dict[str, dict] = {}
    errors: list[str] = []

    for company_id, meta in COMPANIES.items():
        folder = XBRL_DIR / meta["folder"]
        print(f"\n[{company_id}] Parsing {folder.name}...")
        try:
            parsed_years = parse_company(company_id, folder)
            company_json = build_company_json(company_id, parsed_years)
            results[company_id] = company_json
        except Exception as e:
            errors.append(f"{company_id}: {e}")
            print(f"  ERROR: {e}")

    if errors:
        print(f"\n{'='*60}")
        print("PARSE ERRORS (fix before proceeding):")
        for err in errors:
            print(f"  {err}")
        sys.exit(1)

    # Write per-company JSON files
    print(f"\n[Output] Writing to {OUTPUT_DIR}...")
    companies_dir = OUTPUT_DIR / "companies"
    for company_id, company_data in results.items():
        _write_json(companies_dir / f"{company_id}.json", company_data)

    # Write companies.json registry
    registry = _build_companies_registry(results)
    _write_json(OUTPUT_DIR / "companies.json", registry)

    # Write indicators.json stub (to be enriched by Gemini Pro)
    indicators_path = OUTPUT_DIR / "indicators.json"
    if indicators_path.exists():
        print(f"  indicators.json already exists — not overwriting "
              f"(delete manually to regenerate stub)")
    else:
        indicators = _build_indicators_stub(results)
        _write_json(indicators_path, indicators)
        print(f"  indicators.json stub created with {len(indicators)} tags "
              f"(enrich labels/categories with Gemini Pro)")

    # Spot-checks
    print(f"\n[Spot-checks]")
    failures = run_spot_checks(results)
    if failures:
        print("  FAILED:")
        for f in failures:
            print(f"    {f}")
    else:
        print("  All spot-checks passed.")

    # Summary
    print(f"\n{'='*60}")
    print("Summary:")
    unit_warnings: list[tuple[str, str, str, str]] = []
    not_normalized: list[tuple[str, str, str, str]] = []

    for company_id, company_data in results.items():
        for fy, fy_data in company_data["years"].items():
            for tag, ind in fy_data.items():
                if tag.startswith("_") or not isinstance(ind, dict):
                    continue
                if ind.get("unitWarning"):
                    unit_warnings.append((company_id, fy, tag, ind["unitWarning"]))
                if not ind.get("normalized", True):
                    not_normalized.append((company_id, fy, tag, str(ind.get("unitWarning", ""))))

    for company_id, company_data in results.items():
        fy_keys = sorted(company_data["years"].keys())
        tag_counts = {fy: sum(1 for k in company_data["years"][fy] if not k.startswith("_"))
                      for fy in fy_keys}
        bases = {fy: company_data["years"][fy]["_meta"]["reportingBasis"] for fy in fy_keys}
        print(f"  {company_id}: {' | '.join(f'{fy} ({bases[fy][:2].upper()}) {tag_counts[fy]} tags' for fy in fy_keys)}")

    print(f"\n  unit_warnings: {len(unit_warnings)}")
    print(f"  not_normalized: {len(not_normalized)}")

    if unit_warnings:
        print("\n  Unit warnings (first 20):")
        for company_id, fy, tag, warn in unit_warnings[:20]:
            print(f"    {company_id} {fy} {tag}: {warn}")
        if len(unit_warnings) > 20:
            print(f"    ... and {len(unit_warnings) - 20} more")

    if failures:
        print("\nSpot-check failures found — review before proceeding.")
        sys.exit(1)
    else:
        print("\nParser complete. Review unit_warnings before running validate.py.")


if __name__ == "__main__":
    main()
