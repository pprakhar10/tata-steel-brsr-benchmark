"""
generate_analysis_prompts.py — Generate Gemini Gem prompt files for AI analysis

Produces 13 topic-specific prompt .md files in parser/gem_analysis_prompts/,
ready to paste directly into the Gemini Gem.

Run: python parser/generate_analysis_prompts.py

Workflow:
  1. Run this script → 13 prompt files generated
  2. Paste gem_analysis_prompts/ghg-scope3.md into Gem first (validation)
  3. Share Gem output → review quality → adjust prompt if needed
  4. Run remaining 12 sessions → save outputs to parser/gem_analysis_outputs/
"""

import json
import re
from pathlib import Path
from datetime import date

BASE     = Path(__file__).parent.parent
DATA_DIR = BASE / "dashboard" / "src" / "data" / "companies"
OUT_DIR  = BASE / "parser" / "gem_analysis_prompts"

COMPANIES = [
    ("tata-steel",        "Tata Steel"),
    ("jsw-steel",         "JSW Steel"),
    ("sail",              "SAIL"),
    ("jindal-stainless",  "Jindal Stainless"),
]
YEARS = ["FY2023", "FY2024", "FY2025"]

# TAG_ALIASES — v1/v2 tag name → canonical (matches generate_comparison_table.py)
TAG_ALIASES = {
    "Sox": "SOx",
    "Nox": "NOx",
    "TotalEnergyConsumption": "TotalEnergyConsumedFromRenewableAndNonRenewableSources",
    "TotalScope1AndScope2EmissionsPerRupeeOfTurnover":
        "TotalScope1AndScope2EmissionsIntensityPerRupeeOfTurnover",
    "TotalScope1AndScope2EmissionIntensity":
        "TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput",
}
ALIAS_REVERSE = {v: k for k, v in TAG_ALIASES.items()}

# ---------------------------------------------------------------------------
# TOPIC_TAGS — maps each of the 13 topic keys to their metrics
# Each entry: (canonical_tag, display_label, unit_hint)
# Derived from TAG_GROUPS in generate_comparison_table.py
# ---------------------------------------------------------------------------
TOPIC_TAGS = {
    "ghg-scope3": [
        ("TotalScope1Emissions",
         "Scope 1 GHG Emissions", "tCO2e"),
        ("TotalScope2Emissions",
         "Scope 2 GHG Emissions", "tCO2e"),
        ("TotalScope3Emissions",
         "Scope 3 GHG Emissions", "tCO2e"),
        ("TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput",
         "GHG Intensity (physical output)", "tCO2e/tcs"),
        ("TotalScope1AndScope2EmissionsIntensityPerRupeeOfTurnover",
         "GHG Intensity (per ₹ turnover)", "tCO2e/₹"),
        ("TotalScope3EmissionsPerRupeeOfTurnover",
         "Scope 3 Intensity (per ₹ turnover)", "tCO2e/₹"),
    ],
    "energy": [
        ("TotalEnergyConsumedFromRenewableAndNonRenewableSources",
         "Total Energy Consumed", "GJ"),
        ("TotalEnergyConsumedFromRenewableSources",
         "Total Energy — Renewable", "GJ"),
        ("TotalEnergyConsumedFromNonRenewableSources",
         "Total Energy — Non-Renewable", "GJ"),
        ("TotalElectricityConsumptionFromRenewableSources",
         "Electricity — Renewable", "GJ"),
        ("TotalElectricityConsumptionFromNonRenewableSources",
         "Electricity — Non-Renewable", "GJ"),
        ("TotalFuelConsumptionFromRenewableSources",
         "Fuel — Renewable", "GJ"),
        ("TotalFuelConsumptionFromNonRenewableSources",
         "Fuel — Non-Renewable", "GJ"),
        ("EnergyConsumptionThroughOtherSourcesFromRenewableSources",
         "Other Energy — Renewable", "GJ"),
        ("EnergyConsumptionThroughOtherSourcesFromNonRenewableSources",
         "Other Energy — Non-Renewable", "GJ"),
        ("EnergyIntensityInTermOfPhysicalOutput",
         "Energy Intensity (physical output)", "GJ/tcs"),
        ("EnergyIntensityPerRupeeOfTurnover",
         "Energy Intensity (per ₹ turnover)", "GJ/₹"),
    ],
    "water": [
        ("TotalVolumeOfWaterWithdrawal",
         "Total Water Withdrawal", "kL"),
        ("WaterWithdrawalByGroundwater",
         "Water Withdrawal — Groundwater", "kL"),
        ("WaterWithdrawalBySurfaceWater",
         "Water Withdrawal — Surface Water", "kL"),
        ("WaterWithdrawalBySeawaterOrDesalinatedWater",
         "Water Withdrawal — Seawater/Desalinated", "kL"),
        ("WaterWithdrawalByThirdPartyWater",
         "Water Withdrawal — Third Party", "kL"),
        ("WaterWithdrawalByOthers",
         "Water Withdrawal — Other Sources", "kL"),
        ("TotalVolumeOfWaterConsumption",
         "Total Water Consumption", "kL"),
        ("TotalWaterDischargedInKilolitres",
         "Total Water Discharged", "kL"),
        ("WaterDischargeToGroundwater",
         "Water Discharge — To Groundwater", "kL"),
        ("WaterDischargeToSurfaceWater",
         "Water Discharge — To Surface Water", "kL"),
        ("WaterDischargeToSeawater",
         "Water Discharge — To Seawater", "kL"),
        ("WaterDischargeBySentToThirdParties",
         "Water Discharge — To Third Parties", "kL"),
        ("WaterDischargeToOthers",
         "Water Discharge — Others", "kL"),
        ("WaterIntensityInTermOfPhysicalOutput",
         "Water Intensity (physical output)", "kL/tcs"),
        ("WaterIntensityPerRupeeOfTurnover",
         "Water Intensity (per ₹ turnover)", "L/₹"),
    ],
    "waste": [
        ("TotalWasteGenerated",
         "Total Waste Generated", "metric tonnes"),
        ("TotalWasteRecovered",
         "Total Waste Recovered", "metric tonnes"),
        ("TotalWasteDisposed",
         "Total Waste Disposed", "metric tonnes"),
        ("WasteRecoveredThroughRecycled",
         "Waste Recovered — Recycled", "metric tonnes"),
        ("WasteRecoveredThroughReUsed",
         "Waste Recovered — Re-used", "metric tonnes"),
        ("WasteRecoveredThroughOtherRecoveryOperations",
         "Waste Recovered — Other Recovery", "metric tonnes"),
        ("WasteDisposedByIncineration",
         "Waste Disposed — Incineration", "metric tonnes"),
        ("WasteDisposedByLandfilling",
         "Waste Disposed — Landfilling", "metric tonnes"),
        ("WasteDisposedByOtherDisposalOperations",
         "Waste Disposed — Other Disposal", "metric tonnes"),
        ("BatteryWaste",
         "Battery Waste", "metric tonnes"),
        ("EWaste",
         "E-Waste", "metric tonnes"),
        ("BioMedicalWaste",
         "Bio-Medical Waste", "metric tonnes"),
        ("ConstructionAndDemolitionWaste",
         "Construction & Demolition Waste", "metric tonnes"),
        ("OtherHazardousWaste",
         "Other Hazardous Waste", "metric tonnes"),
        ("OtherNonHazardousWasteGenerated",
         "Other Non-Hazardous Waste", "metric tonnes"),
        ("PlasticWaste",
         "Plastic Waste", "metric tonnes"),
        ("RadioactiveWaste",
         "Radioactive Waste", "metric tonnes"),
        ("WasteIntensityInTermOfPhysicalOutput",
         "Waste Intensity (physical output)", "MT/tcs"),
        ("WasteIntensityPerRupeeOfTurnover",
         "Waste Intensity (per ₹ turnover)", "MT/₹"),
    ],
    "air-emissions": [
        ("SOx",              "SOx Emissions", "kilotonnes"),
        ("NOx",              "NOx Emissions", "kilotonnes"),
        ("ParticulateMatter","Particulate Matter (PM)", "kilotonnes"),
    ],
    "health-safety": [
        ("LTIFR_Employees",  "LTIFR — Employees", "per million person-hours"),
        ("LTIFR_Workers",    "LTIFR — Workers",   "per million person-hours"),
        ("TRIFR_Employees",  "TRIFR — Employees", ""),
        ("TRIFR_Workers",    "TRIFR — Workers",   ""),
        ("Fatalities_Employees", "Fatalities — Employees", "count"),
        ("Fatalities_Workers",   "Fatalities — Workers",   "count"),
        ("TotalNumberOfAffectedEmployees", "Affected Employees (injury)", ""),
        ("TotalNumberOfAffectedWorkers",   "Affected Workers (injury)",   ""),
        ("NumberOfEmployeesOrWhoseFamilyMembersRehabilitatedAndPlacedInSuitableEmployment",
         "Employees Rehabilitated", ""),
        ("NumberOfWorkersOrWhoseFamilyMembersRehabilitatedAndPlacedInSuitableEmployment",
         "Workers Rehabilitated", ""),
    ],
    "workforce-diversity": [
        ("TotalNumberOfEmployees",
         "Total Employees", ""),
        ("PercentageOfFemaleEmployees",
         "Female Employees (%)", "%"),
        ("TotalNumberOfBoardOfDirectors",
         "Board of Directors (total)", ""),
        ("NumberOfFemaleBoardOfDirectors",
         "Board of Directors (female)", ""),
        ("PercentageOfFemaleBoardOfDirectors",
         "Board of Directors (female %)", "%"),
        ("TotalNumberOfKeyManagementPersonnel",
         "Key Management Personnel (total)", ""),
        ("NumberOfFemaleKeyManagementPersonnel",
         "Key Management Personnel (female)", ""),
        ("PercentageOfFemaleKeyManagementPersonnel",
         "Key Management Personnel (female %)", "%"),
        ("PercentageOfGrossWagesPaidToFemaleToTotalWagesPaid",
         "Female Wage Share (%)", "%"),
        ("PercentageOfCostIncurredOnWellBeingMeasuresWithRespectToTotalRevenueOfTheCompany",
         "Wellbeing Cost (% of revenue)", "%"),
    ],
    "training-development": [
        ("TrainingCoverage_Employees_HealthSafety",
         "Employee H&S Training Coverage (%)", "%"),
        ("TrainingCoverage_Employees_SkillUpgradation",
         "Employee Skill Training Coverage (%)", "%"),
        ("TrainingCoverage_Workers_HealthSafety",
         "Worker H&S Training Coverage (%)", "%"),
        ("TrainingCoverage_Workers_SkillUpgradation",
         "Worker Skill Training Coverage (%)", "%"),
    ],
    "ethics-compliance": [
        ("TotalComplaintsReportedUnderSexualHarassmentOfWomenAtWorkplace",
         "POSH Complaints — Total Reported", "count"),
        ("ComplaintsOnPOSHUpHeld",
         "POSH Complaints — Upheld", "count"),
    ],
    "governance-related-party": [
        ("PercentageOfInvestmentsInRelatedPartiesInTotalInvestments",
         "Related Party — Investments (%)", "%"),
        ("PercentageOfLoansAndAdvancesGivenToRelatedPartiesInTotalLoansAndAdvances",
         "Related Party — Loans & Advances (%)", "%"),
        ("PercentageOfPurchasesFromRelatedPartiesInTotalPurchasesForShareOfRelatedPartyTransactions",
         "Related Party — Purchases (%)", "%"),
        ("PercentageOfSalesToRelatedPartiesInTotalSalesForShareOfRelatedPartyTransactions",
         "Related Party — Sales (%)", "%"),
        ("PercentageOfCapex",
         "Capex on ESG/Sustainability (%)", "%"),
        ("PercentageOfRAndD",
         "R&D & Capex in Env/Social Technologies (% of total)", "%"),
        ("NumberOfGreenCreditsHaveBeenGeneratedOrProcuredByTheListedEntity",
         "Green Credits Generated/Procured", ""),
    ],
    "financial-profile": [
        ("Turnover",
         "Turnover", "INR Crore"),
        ("NetWorth",
         "Net Worth", "INR Crore"),
        ("PercentageOfContributionOfExportsInTheTotalTurnoverOfTheEntity",
         "Export Contribution (% of turnover)", "%"),
    ],
    "stakeholder-human-rights": [
        ("PercentageOfDirectlySourcedFromMSMEsOrSmallProducers",
         "Sourced from MSMEs / Small Producers (%)", "%"),
        ("PercentageOfValueChainPartnersByValueOfBusinessDoneWithSuchPartnersThatWereAssessedForEnvironmentalImpacts",
         "Value Chain Partners Assessed for Env. Impact (%)", "%"),
        ("PercentageOfInputsWereSourcedSustainably",
         "Inputs Sourced Sustainably (%)", "%"),
        ("PercentageOfSourcedDirectlyFromWithinTheDistrictAndNeighbouringDistricts",
         "Local Sourcing — Within District & Neighbours (%)", "%"),
    ],
    "csr-products-consumer": [
        ("EnvironmentalAndSocialParametersRelevantToTheProductAsAPercentageToTotalTurnover",
         "Products with Env/Social Info (% of turnover)", "%"),
        ("RecyclingAndOrSafeDisposalAsAPercentageToTotalTurnover",
         "Products with Recycling/Safe Disposal Info (% of turnover)", "%"),
        ("NumberOfDealersOrDistributorsToWhomSalesAreMade",
         "Number of Dealers / Distributors", ""),
        ("NumberOfTradingHousesWherePurchasesAreMade",
         "Number of Trading Houses (purchases)", ""),
    ],
}

# Topic display names (for prompt headers)
TOPIC_NAMES = {
    "ghg-scope3":             "GHG Emissions & Scope 3",
    "energy":                 "Energy Consumption",
    "water":                  "Water Management",
    "waste":                  "Waste Management",
    "air-emissions":          "Air Emissions",
    "health-safety":          "Health & Safety",
    "workforce-diversity":    "Workforce & Diversity",
    "training-development":   "Training & Development",
    "ethics-compliance":      "Ethics & Compliance",
    "governance-related-party": "Governance & Related Party Transactions",
    "financial-profile":      "Financial Profile",
    "stakeholder-human-rights": "Stakeholder Engagement & Human Rights",
    "csr-products-consumer":  "CSR, Products & Consumer Responsibility",
}

# BRSR principle context per topic (for prompt instructions)
TOPIC_PRINCIPLES = {
    "ghg-scope3":             "BRSR Principle 6 — Environment (Essential & Leadership indicators)",
    "energy":                 "BRSR Principle 6 — Environment (Essential & Leadership indicators)",
    "water":                  "BRSR Principle 6 — Environment (Essential & Leadership indicators)",
    "waste":                  "BRSR Principle 6 — Environment (Essential & Leadership indicators)",
    "air-emissions":          "BRSR Principle 6 — Environment (Essential indicators)",
    "health-safety":          "BRSR Principle 3 — Employee Wellbeing (Essential indicators)",
    "workforce-diversity":    "BRSR Principle 3 — Employee Wellbeing + Section A General Disclosures",
    "training-development":   "BRSR Principle 3 — Employee Wellbeing (Essential indicators)",
    "ethics-compliance":      "BRSR Principle 1 — Ethics & Transparency (Essential indicators)",
    "governance-related-party": "BRSR Principle 7 — Public Policy + Section A General Disclosures",
    "financial-profile":      "BRSR Section A — General Disclosures",
    "stakeholder-human-rights": "BRSR Principle 4 — Stakeholder Engagement + Principle 5 — Human Rights",
    "csr-products-consumer":  "BRSR Principle 2 — Sustainable Products + Principle 8 — Inclusive Growth + Principle 9 — Consumer Responsibility",
}


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_company_data(company_id: str) -> dict:
    with open(DATA_DIR / f"{company_id}.json", encoding="utf-8") as f:
        return json.load(f)


def _get_val_obj(company_data: dict, year: str, tag: str):
    """Return value object for tag, with alias fallback."""
    yr_data = company_data["years"].get(year, {})
    v = yr_data.get(tag)
    if v is None:
        alt = ALIAS_REVERSE.get(tag)
        if alt:
            v = yr_data.get(alt)
    return v


def _is_consolidated(company_id: str, year: str, company_data: dict) -> bool:
    """True if this company-year is on consolidated reporting basis."""
    meta = company_data["years"].get(year, {}).get("_meta", {})
    return meta.get("reportingBasis") == "consolidated"


def get_value_str(company_data: dict, year: str, tag: str, company_id: str) -> str:
    """
    Format a value for the data table in the Gemini prompt.
    Returns a string like: "75,750,000 tCO2e (P)" or "—" or
    "56,000,000 tCO2e (consolidated)" for Tata FY2023.
    """
    v_obj = _get_val_obj(company_data, year, tag)

    if v_obj is None:
        base = "—"
    else:
        val = v_obj.get("value")
        if val is None:
            base = "—"
        elif isinstance(val, bool):
            base = "Yes" if val else "No"
        elif isinstance(val, (int, float)):
            av = abs(val)
            if av == 0:
                base = "0"
            elif av >= 1_000_000:
                base = f"{val:,.0f}"
            elif av >= 1_000:
                base = f"{val:,.1f}"
            elif av >= 1:
                base = f"{val:.4f}".rstrip("0").rstrip(".")
            else:
                base = f"{val:.6g}"
        else:
            base = str(val)

        # Mark patched values
        if v_obj.get("patchSource") in ("PDF", "Excel"):
            base += " (P)"

        # Standalone note in unitWarning (set during patch for Tata FY2023 standalone cross-refs)
        unit_warn = v_obj.get("unitWarning") or ""
        if "standalone" in unit_warn.lower() and _is_consolidated(company_id, year, company_data):
            m = re.search(r"standalone[:\s]+([0-9,\.]+)", unit_warn, re.IGNORECASE)
            if m:
                base += f" (standalone: {m.group(1)})"

    # Flag consolidated basis for Tata FY2023
    if _is_consolidated(company_id, year, company_data) and base != "—":
        base += " ⚠consolidated"

    return base


# ---------------------------------------------------------------------------
# Prompt building blocks
# ---------------------------------------------------------------------------

def build_data_table(topic_key: str, all_company_data: dict) -> str:
    """Build the markdown data table for a topic (rows=metrics, cols=company×year)."""
    tags = TOPIC_TAGS[topic_key]

    # Header row: Metric | Unit | Tata FY23 | Tata FY24 | Tata FY25 | JSW FY23 | ...
    col_headers = ["Metric", "Unit"]
    for cid, cname in COMPANIES:
        for yr in YEARS:
            yr_short = yr.replace("FY20", "FY")
            col_headers.append(f"{cname} {yr_short}")

    # Separator
    sep = "| " + " | ".join(["---"] * len(col_headers)) + " |"
    header = "| " + " | ".join(col_headers) + " |"

    rows = [header, sep]
    for tag, label, unit_hint in tags:
        cells = [label, unit_hint or "—"]
        for cid, _ in COMPANIES:
            for yr in YEARS:
                cells.append(get_value_str(all_company_data[cid], yr, tag, cid))
        rows.append("| " + " | ".join(cells) + " |")

    return "\n".join(rows)


def build_rules_block() -> str:
    """Static rules block included in every prompt."""
    return """## Rules for your analysis

1. **Audience:** Internal senior management at Tata Steel. Technical steel industry terminology is appropriate (blast furnace, EAF, BF-BOF, tcs, tonne of crude steel, etc.).

2. **Ranking:**
   - Rank 1 = best performer, Rank 4 = worst performer.
   - Tied ranks are allowed — if two companies perform equally, both receive the same rank and the next rank is skipped (e.g., two at rank 1 → next is rank 3).
   - A null/missing value (—) is treated as the worst possible performance and ranked last.

3. **Metric direction:** For each metric, determine whether a higher value or lower value indicates better performance. State this clearly in the ABOUT section. If genuinely ambiguous, output `DIRECTION_UNCLEAR: [reason]`.

4. **Sources:**
   - Use the BRSR PDF disclosures in your knowledge base as the primary source.
   - If a target or context is not available in the BRSR but you can source it reliably elsewhere, include it and note: `(Source: [source name] — not from BRSR disclosure)`.
   - If no meaningful analysis is possible for a metric, output `CONTEXT_INSUFFICIENT: [reason]` rather than producing thin or speculative analysis.

5. **Data flags in the table:**
   - `(P)` = value was standardised or corrected for comparability. Company annual reports may show a different unit or value.
   - `—` = not reported / data not available.
   - `⚠consolidated` = Tata Steel FY2022-23 is on a Consolidated basis (includes Indian and international operations). Standalone values are noted where available. All other company-years are Standalone (Indian operations only).

6. **Trend direction:** Use `Improved`, `Worsened`, or `Stable`. If the trend is genuinely ambiguous (e.g., due to a reporting methodology change between years), output `AMBIGUOUS: [reason]`.

7. **Tata Steel positioning:** Write a combined narrative story anchored on FY2024-25 as the primary reference. Cover Tata's rank and gap from the best performer in the latest year (or, if Tata leads, who is closest and why). Then cover trajectory: has Tata's ranking changed across the 3 years — improved, declined, or held steady — and what drove that change?

8. **Targets:** Cite targets stated in BRSR first. External sources allowed with attribution. If nothing found: `"No targets identified for this metric."`

9. **Comparability notes:** Only include if the reader needs this to correctly interpret the numbers (unit conversions, scope boundary differences, methodology changes). Omit if not applicable.

10. **Technical depth:** Explanations may include steel process chemistry, production route differences, regulatory context, and industry benchmarks — users are technical professionals from the steel industry."""


def build_output_format_block() -> str:
    """The required output format instructions for the Gemini Gem."""
    return """## Required output format

Follow this structure EXACTLY for every metric. Do not add or remove sections. Use the exact header names shown.

```
#### INDICATOR: {exact_tag_name_from_table}

**DIRECTION:** lower_is_better | higher_is_better | DIRECTION_UNCLEAR: [reason]

**PEER_RANK:**
FY2023: Tata={1-4}, JSW={1-4}, SAIL={1-4}, Jindal={1-4}
FY2024: Tata={1-4}, JSW={1-4}, SAIL={1-4}, Jindal={1-4}
FY2025: Tata={1-4}, JSW={1-4}, SAIL={1-4}, Jindal={1-4}

**TREND_DIRECTION:**
Tata:   FY2023-24=Improved|Worsened|Stable|AMBIGUOUS: [reason], FY2024-25=Improved|Worsened|Stable|AMBIGUOUS: [reason]
JSW:    FY2023-24=..., FY2024-25=...
SAIL:   FY2023-24=..., FY2024-25=...
Jindal: FY2023-24=..., FY2024-25=...

**ABOUT:**
[2-3 sentences: what the metric measures, which BRSR principle and Essential/Leadership classification it falls under. Final sentence: "A lower/higher value indicates better performance" or "Direction is unclear: [reason]".]

**PERFORMANCE_AND_DRIVERS:**
[Integrated narrative covering all 4 companies across all 3 years with the WHY woven in. Cite specific numbers. Cover structural drivers — process type (BF-BOF vs EAF), captive power, technology investments, scale, reporting methodology. If any value was sourced outside BRSR, note: "(Source: [source name])".]

**TATA_POSITIONING:**
[Combined narrative story anchored on FY2024-25. State Tata's rank and the percentage gap from the best performer in the latest year (or, if Tata leads, who is closest and what % behind). Then cover trajectory across all 3 years: has Tata's ranking changed and why?]

**TARGETS:**
[Targets from BRSR first. External sources with attribution if BRSR has nothing. If none found: "No targets identified for this metric."]

**COMPARABILITY_NOTES:**
[Only include if reader needs this to interpret the numbers correctly. Omit section entirely if not applicable.]

**FLAGS:**
DIRECTION_UNCLEAR: yes|no
CONTEXT_INSUFFICIENT: yes|no
EXTERNAL_SOURCE_USED: yes|no
TREND_AMBIGUITY: yes|no
FLAG_NOTE: [explanation if any flag is yes — omit this line if all flags are no]
```

After all INDICATOR blocks, write one BENCHMARK block:

```
#### BENCHMARK: {topic_key}

**FY2022-23:**
[150-200 words. Overall leader and laggard for this theme in FY2022-23 with reasoning. Structural factors explaining genuine differences. Note Tata consolidated basis.]

**FY2023-24:**
[150-200 words. Same structure.]

**FY2024-25:**
[150-200 words. Most detailed — this is the primary year.]
```"""


def build_prompt(topic_key: str, all_company_data: dict) -> str:
    """Assemble the complete prompt .md for one Gemini session."""
    topic_name = TOPIC_NAMES[topic_key]
    principle   = TOPIC_PRINCIPLES[topic_key]
    tags        = TOPIC_TAGS[topic_key]
    tag_list    = ", ".join(t[0] for t in tags)

    sections = []

    # ── Header ──────────────────────────────────────────────────────────────
    sections.append(f"# BRSR Analysis: {topic_name}")
    sections.append(f"*Generated: {date.today()} | Metrics: {len(tags)} | Companies: 4 | Years: FY2022-23, FY2023-24, FY2024-25*\n")

    # ── Session context ──────────────────────────────────────────────────────
    sections.append("## Session context\n")
    sections.append(
        f"You are analysing **{topic_name}** disclosures from BRSR filings for 4 Indian steel companies "
        f"across FY2022-23, FY2023-24, and FY2024-25. "
        f"Coverage: {principle}.\n\n"
        f"You have access to all 12 company BRSR PDFs and SEBI/ICAI BRSR guidance in your knowledge base. "
        f"Use PDF content to enrich your analysis — cite specific targets, commitments, methodology changes, "
        f"and initiatives from the PDFs wherever relevant. "
        f"The quantitative data table below has been standardised for cross-company comparability.\n\n"
        f"**Metrics covered in this session ({len(tags)}):** {tag_list}"
    )

    # ── Rules ────────────────────────────────────────────────────────────────
    sections.append(build_rules_block())

    # ── Data table ───────────────────────────────────────────────────────────
    sections.append("## Standardised data\n")
    sections.append(
        "> **(P)** = value standardised or corrected for comparability — company annual reports may show "
        "a different unit or number. **⚠consolidated** = Tata Steel FY2022-23 on Consolidated basis "
        "(includes international operations). **—** = not reported.\n"
    )
    sections.append(build_data_table(topic_key, all_company_data))

    # ── Output format ────────────────────────────────────────────────────────
    sections.append(build_output_format_block())

    # ── Closing instruction ──────────────────────────────────────────────────
    sections.append(
        f"\n---\n\n"
        f"Now produce the analysis for all {len(tags)} metrics listed above, "
        f"followed by the BENCHMARK block for topic key `{topic_key}`."
    )

    return "\n\n".join(sections)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Loading company data...")
    all_company_data = {cid: load_company_data(cid) for cid, _ in COMPANIES}

    topics = list(TOPIC_TAGS.keys())
    print(f"Generating {len(topics)} prompt files...\n")

    for topic_key in topics:
        content  = build_prompt(topic_key, all_company_data)
        out_path = OUT_DIR / f"{topic_key}.md"
        out_path.write_text(content, encoding="utf-8")
        n_tags   = len(TOPIC_TAGS[topic_key])
        print(f"  OK {topic_key}.md  ({n_tags} metrics, {len(content):,} chars)")

    total_metrics = sum(len(v) for v in TOPIC_TAGS.values())
    print(f"\nDone. {len(topics)} prompt files in: {OUT_DIR}")
    print(f"Total metrics covered: {total_metrics}")
    print(f"\nStart with: {OUT_DIR / 'ghg-scope3.md'}")
    print("  Paste into Gemini Gem, share output for quality review before running remaining 12.")


if __name__ == "__main__":
    main()
