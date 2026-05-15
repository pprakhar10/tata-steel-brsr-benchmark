"""
generate_comparison_table.py — Cross-company comparison review table

Produces parser/review/comparison_table.html
Run: python parser/generate_comparison_table.py

Table layout:
  - 3 sections (FY2023 / FY2024 / FY2025)
  - Rows = categorized ESG/financial metrics (~130 indicators)
  - Columns = Tata Steel | JSW Steel | SAIL | Jindal Stainless | Notes (editable)
  - Color coding: gold=PDF-patched, red=null, orange-border=unit warning
  - Notes column is contenteditable — click to type in browser
"""

import json
from pathlib import Path
from datetime import date

BASE    = Path(__file__).parent.parent
DATA_DIR = BASE / "dashboard" / "src" / "data" / "companies"
OUT_HTML = BASE / "parser" / "review" / "comparison_table.html"

COMPANIES = [
    ("tata-steel",       "Tata Steel"),
    ("jsw-steel",        "JSW Steel"),
    ("sail",             "SAIL"),
    ("jindal-stainless", "Jindal Stainless"),
]
YEARS = ["FY2023", "FY2024", "FY2025"]

# v1/v2 alias → canonical name (older filings used different tag names)
TAG_ALIASES = {
    "Sox": "SOx",
    "Nox": "NOx",
    "TotalEnergyConsumption": "TotalEnergyConsumedFromRenewableAndNonRenewableSources",
    "TotalScope1AndScope2EmissionsPerRupeeOfTurnover": "TotalScope1AndScope2EmissionsIntensityPerRupeeOfTurnover",
    "TotalScope1AndScope2EmissionIntensity": "TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput",
}
# Reverse map: canonical → alias (for lookup fallback)
ALIAS_REVERSE = {v: k for k, v in TAG_ALIASES.items()}

# ---------------------------------------------------------------------------
# TAG_GROUPS — (category, tag, display_name, unit_hint)
# tag = canonical name; lookup will also try the alias if primary missing
# ---------------------------------------------------------------------------
TAG_GROUPS = [
    # ── Financial ──────────────────────────────────────────────────────────
    ("Financial",  "Turnover",                    "Turnover",                        "INR Crore"),
    ("Financial",  "NetWorth",                     "Net Worth",                       "INR Crore"),

    # ── GHG Emissions ──────────────────────────────────────────────────────
    ("GHG Emissions", "TotalScope1Emissions",      "Scope 1 GHG",                     "tCO2e"),
    ("GHG Emissions", "TotalScope2Emissions",      "Scope 2 GHG",                     "tCO2e"),
    ("GHG Emissions", "TotalScope3Emissions",      "Scope 3 GHG",                     "tCO2e"),
    ("GHG Emissions", "TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput",
                                                   "GHG Intensity (physical)",         "tCO2e/tcs"),
    ("GHG Emissions", "TotalScope1AndScope2EmissionsIntensityPerRupeeOfTurnover",
                                                   "GHG Intensity (per ₹ turnover)",  "tCO2e/₹"),
    ("GHG Emissions", "TotalScope3EmissionsPerRupeeOfTurnover",
                                                   "Scope 3 Intensity (per ₹)",       "tCO2e/₹"),

    # ── Energy ─────────────────────────────────────────────────────────────
    ("Energy", "TotalEnergyConsumedFromRenewableAndNonRenewableSources",
                                                   "Total Energy",                    "GJ"),
    ("Energy", "TotalEnergyConsumedFromRenewableSources",
                                                   "Total Energy — Renewable",        "GJ"),
    ("Energy", "TotalEnergyConsumedFromNonRenewableSources",
                                                   "Total Energy — Non-Renewable",    "GJ"),
    ("Energy", "TotalElectricityConsumptionFromRenewableSources",
                                                   "Electricity — Renewable",         "GJ"),
    ("Energy", "TotalElectricityConsumptionFromNonRenewableSources",
                                                   "Electricity — Non-Renewable",     "GJ"),
    ("Energy", "TotalFuelConsumptionFromRenewableSources",
                                                   "Fuel — Renewable",                "GJ"),
    ("Energy", "TotalFuelConsumptionFromNonRenewableSources",
                                                   "Fuel — Non-Renewable",            "GJ"),
    ("Energy", "EnergyConsumptionThroughOtherSourcesFromRenewableSources",
                                                   "Other Energy — Renewable",        "GJ"),
    ("Energy", "EnergyConsumptionThroughOtherSourcesFromNonRenewableSources",
                                                   "Other Energy — Non-Renewable",    "GJ"),
    ("Energy", "EnergyIntensityInTermOfPhysicalOutput",
                                                   "Energy Intensity (physical)",     "GJ/tcs"),
    ("Energy", "EnergyIntensityPerRupeeOfTurnover",
                                                   "Energy Intensity (per ₹ turnover)","GJ/₹"),

    # ── Air Emissions ──────────────────────────────────────────────────────
    ("Air Emissions", "SOx",                       "SOx",                             "kilotonnes"),
    ("Air Emissions", "NOx",                       "NOx",                             "kilotonnes"),
    ("Air Emissions", "ParticulateMatter",         "Particulate Matter (PM)",         "kilotonnes"),

    # ── Water — Withdrawal ─────────────────────────────────────────────────
    ("Water — Withdrawal", "TotalVolumeOfWaterWithdrawal",
                                                   "Total Water Withdrawal",          "kL"),
    ("Water — Withdrawal", "WaterWithdrawalByGroundwater",
                                                   "  Groundwater",                   "kL"),
    ("Water — Withdrawal", "WaterWithdrawalBySurfaceWater",
                                                   "  Surface Water",                 "kL"),
    ("Water — Withdrawal", "WaterWithdrawalBySeawaterOrDesalinatedWater",
                                                   "  Seawater / Desalinated",        "kL"),
    ("Water — Withdrawal", "WaterWithdrawalByThirdPartyWater",
                                                   "  Third-party Water",             "kL"),
    ("Water — Withdrawal", "WaterWithdrawalByOthers",
                                                   "  Other Sources",                 "kL"),

    # ── Water — Consumption & Discharge ───────────────────────────────────
    ("Water — Consumption & Discharge", "TotalVolumeOfWaterConsumption",
                                                   "Total Water Consumption",         "kL"),
    ("Water — Consumption & Discharge", "TotalWaterDischargedInKilolitres",
                                                   "Total Water Discharged",          "kL"),
    ("Water — Consumption & Discharge", "WaterDischargeToGroundwater",
                                                   "  Discharge → Groundwater",       "kL"),
    ("Water — Consumption & Discharge", "WaterDischargeToSurfaceWater",
                                                   "  Discharge → Surface Water",     "kL"),
    ("Water — Consumption & Discharge", "WaterDischargeToSeawater",
                                                   "  Discharge → Seawater",          "kL"),
    ("Water — Consumption & Discharge", "WaterDischargeBySentToThirdParties",
                                                   "  Discharge → Third Parties",     "kL"),
    ("Water — Consumption & Discharge", "WaterDischargeToOthers",
                                                   "  Discharge → Others",            "kL"),

    # ── Water — Intensity ──────────────────────────────────────────────────
    ("Water — Intensity", "WaterIntensityInTermOfPhysicalOutput",
                                                   "Water Intensity (physical)",      "kL/tcs"),
    ("Water — Intensity", "WaterIntensityPerRupeeOfTurnover",
                                                   "Water Intensity (per ₹ turnover)","L/₹"),

    # ── Waste — Totals ─────────────────────────────────────────────────────
    ("Waste — Totals", "TotalWasteGenerated",      "Total Waste Generated",           "metric tonnes"),
    ("Waste — Totals", "TotalWasteRecovered",      "Total Waste Recovered",           "metric tonnes"),
    ("Waste — Totals", "TotalWasteDisposed",       "Total Waste Disposed",            "metric tonnes"),

    # ── Waste — Recovery breakdown ─────────────────────────────────────────
    ("Waste — Recovery", "WasteRecoveredThroughRecycled",
                                                   "  Recycled",                      "metric tonnes"),
    ("Waste — Recovery", "WasteRecoveredThroughReUsed",
                                                   "  Re-used",                       "metric tonnes"),
    ("Waste — Recovery", "WasteRecoveredThroughOtherRecoveryOperations",
                                                   "  Other Recovery",                "metric tonnes"),

    # ── Waste — Disposal breakdown ─────────────────────────────────────────
    ("Waste — Disposal", "WasteDisposedByIncineration",
                                                   "  Incineration",                  "metric tonnes"),
    ("Waste — Disposal", "WasteDisposedByLandfilling",
                                                   "  Landfilling",                   "metric tonnes"),
    ("Waste — Disposal", "WasteDisposedByOtherDisposalOperations",
                                                   "  Other Disposal",                "metric tonnes"),

    # ── Waste — By Type ────────────────────────────────────────────────────
    ("Waste — By Type", "BatteryWaste",            "Battery Waste",                   "metric tonnes"),
    ("Waste — By Type", "EWaste",                  "E-Waste",                         "metric tonnes"),
    ("Waste — By Type", "BioMedicalWaste",         "Bio-Medical Waste",               "metric tonnes"),
    ("Waste — By Type", "ConstructionAndDemolitionWaste",
                                                   "Construction & Demolition Waste", "metric tonnes"),
    ("Waste — By Type", "OtherHazardousWaste",     "Other Hazardous Waste",           "metric tonnes"),
    ("Waste — By Type", "OtherNonHazardousWasteGenerated",
                                                   "Other Non-Hazardous Waste",       "metric tonnes"),
    ("Waste — By Type", "PlasticWaste",            "Plastic Waste",                   "metric tonnes"),
    ("Waste — By Type", "RadioactiveWaste",        "Radioactive Waste",               "metric tonnes"),

    # ── Waste — Intensity ──────────────────────────────────────────────────
    ("Waste — Intensity", "WasteIntensityInTermOfPhysicalOutput",
                                                   "Waste Intensity (physical)",      "MT/tcs"),
    ("Waste — Intensity", "WasteIntensityPerRupeeOfTurnover",
                                                   "Waste Intensity (per ₹ turnover)","MT/₹"),

    # ── Safety ─────────────────────────────────────────────────────────────
    ("Safety", "LTIFR_Employees",      "LTIFR (employees)",      "per million person-hours"),
    ("Safety", "LTIFR_Workers",        "LTIFR (workers)",        "per million person-hours"),
    ("Safety", "TRIFR_Employees",      "TRIFR (employees)",      ""),
    ("Safety", "TRIFR_Workers",        "TRIFR (workers)",        ""),
    ("Safety", "Fatalities_Employees", "Fatalities (employees)", ""),
    ("Safety", "Fatalities_Workers",   "Fatalities (workers)",   ""),
    ("Safety", "TotalNumberOfAffectedEmployees",   "Affected Employees (injury)",     ""),
    ("Safety", "TotalNumberOfAffectedWorkers",     "Affected Workers (injury)",       ""),
    ("Safety", "NumberOfEmployeesOrWhoseFamilyMembersRehabilitatedAndPlacedInSuitableEmployment",
                                                   "Employees Rehabilitated",         ""),
    ("Safety", "NumberOfWorkersOrWhoseFamilyMembersRehabilitatedAndPlacedInSuitableEmployment",
                                                   "Workers Rehabilitated",           ""),

    # ── Workforce ──────────────────────────────────────────────────────────
    ("Workforce", "TotalNumberOfEmployees",        "Total Employees",                 ""),
    ("Workforce", "PercentageOfFemaleEmployees",   "Female Employees (%)",            "%"),
    ("Workforce", "TotalNumberOfBoardOfDirectors", "Board of Directors (total)",      ""),
    ("Workforce", "NumberOfFemaleBoardOfDirectors","Board of Directors (female)",     ""),
    ("Workforce", "PercentageOfFemaleBoardOfDirectors",
                                                   "Board of Directors (female %)",   "%"),
    ("Workforce", "TotalNumberOfKeyManagementPersonnel",
                                                   "KMPs (total)",                    ""),
    ("Workforce", "NumberOfFemaleKeyManagementPersonnel",
                                                   "KMPs (female)",                   ""),
    ("Workforce", "PercentageOfFemaleKeyManagementPersonnel",
                                                   "KMPs (female %)",                 "%"),
    ("Workforce", "PercentageOfGrossWagesPaidToFemaleToTotalWagesPaid",
                                                   "Female Wage %",                   "%"),

    # ── Training ───────────────────────────────────────────────────────────
    ("Training", "TrainingCoverage_Employees_HealthSafety",
                                                   "Employee H&S Training Coverage",  "%"),
    ("Training", "TrainingCoverage_Employees_SkillUpgradation",
                                                   "Employee Skill Training Coverage","%"),
    ("Training", "TrainingCoverage_Workers_HealthSafety",
                                                   "Worker H&S Training Coverage",    "%"),
    ("Training", "TrainingCoverage_Workers_SkillUpgradation",
                                                   "Worker Skill Training Coverage",  "%"),


    # ── ESG Ratios & Governance ────────────────────────────────────────────
    ("ESG Ratios & Governance", "PercentageOfCapex",
                                                   "Capex on ESG/Sustainability",     "%"),
    ("ESG Ratios & Governance", "PercentageOfRAndD",
                                                   "R&D & Capex in Env/Social Technologies (% of total R&D & Capex)", "%"),
    ("ESG Ratios & Governance", "PercentageOfDirectlySourcedFromMSMEsOrSmallProducers",
                                                   "Sourced from MSMEs",              "%"),
    ("ESG Ratios & Governance", "PercentageOfCostIncurredOnWellBeingMeasuresWithRespectToTotalRevenueOfTheCompany",
                                                   "Wellbeing Cost (% revenue)",      "%"),
    ("ESG Ratios & Governance", "PercentageOfInputsWereSourcedSustainably",
                                                   "Inputs Sourced Sustainably",      "%"),
    ("ESG Ratios & Governance", "PercentageOfSourcedDirectlyFromWithinTheDistrictAndNeighbouringDistricts",
                                                   "Local Sourcing (%)",              "%"),
    ("ESG Ratios & Governance", "PercentageOfContributionOfExportsInTheTotalTurnoverOfTheEntity",
                                                   "Export Contribution (% turnover)","% "),
    ("ESG Ratios & Governance", "PercentageOfValueChainPartnersByValueOfBusinessDoneWithSuchPartnersThatWereAssessedForEnvironmentalImpacts",
                                                   "Value Chain Partners — Env Assessment","%"),
    ("ESG Ratios & Governance", "EnvironmentalAndSocialParametersRelevantToTheProductAsAPercentageToTotalTurnover",
                                                   "Products carrying info on env. & social parameters (% turnover)", "%"),
    ("ESG Ratios & Governance", "RecyclingAndOrSafeDisposalAsAPercentageToTotalTurnover",
                                                   "Products carrying info on Recycling/Safe Disposal (% turnover)","%"),
    ("ESG Ratios & Governance", "NumberOfDealersOrDistributorsToWhomSalesAreMade",
                                                   "Number of Dealers/Distributors",  ""),
    ("ESG Ratios & Governance", "NumberOfTradingHousesWherePurchasesAreMade",
                                                   "Number of Trading Houses",        ""),
    ("ESG Ratios & Governance", "NumberOfGreenCreditsHaveBeenGeneratedOrProcuredByTheListedEntity",
                                                   "Green Credits Generated/Procured",""),
    ("ESG Ratios & Governance", "TotalComplaintsReportedUnderSexualHarassmentOfWomenAtWorkplace",
                                                   "POSH Complaints (total)",         ""),
    ("ESG Ratios & Governance", "ComplaintsOnPOSHUpHeld",
                                                   "POSH Complaints (upheld)",        ""),

    # ── Related Party Transactions ─────────────────────────────────────────
    ("Related Party Transactions", "PercentageOfInvestmentsInRelatedPartiesInTotalInvestments",
                                                   "Related Party Investments (%)",   "%"),
    ("Related Party Transactions", "PercentageOfLoansAndAdvancesGivenToRelatedPartiesInTotalLoansAndAdvances",
                                                   "Related Party Loans & Advances (%)","% "),
    ("Related Party Transactions", "PercentageOfPurchasesFromRelatedPartiesInTotalPurchasesForShareOfRelatedPartyTransactions",
                                                   "Related Party Purchases (%)",     "%"),
    ("Related Party Transactions", "PercentageOfSalesToRelatedPartiesInTotalSalesForShareOfRelatedPartyTransactions",
                                                   "Related Party Sales (%)",         "%"),
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load(company_id: str) -> dict:
    with open(DATA_DIR / f"{company_id}.json", encoding="utf-8") as f:
        return json.load(f)


def get_val_obj(company_data: dict, year: str, tag: str):
    """Return the value object for a tag, checking alias fallback."""
    yr_data = company_data["years"].get(year, {})
    v = yr_data.get(tag)
    if v is None:
        # Try the reverse alias (canonical → old name)
        alt = ALIAS_REVERSE.get(tag)
        if alt:
            v = yr_data.get(alt)
    return v


def fmt_value(v_obj) -> str:
    """Format a value object to a display string."""
    if v_obj is None:
        return "—"
    val = v_obj.get("value")
    if val is None:
        return "—"
    if isinstance(val, bool):
        return "Yes" if val else "No"
    if isinstance(val, (int, float)):
        av = abs(val)
        if av == 0:
            return "0"
        elif av >= 1_000_000:
            s = f"{val:,.0f}"
        elif av >= 1_000:
            s = f"{val:,.1f}"
        elif av >= 1:
            s = f"{val:.4f}".rstrip("0").rstrip(".")
        else:
            # Small numbers (intensities, ratios) — avoid scientific notation
            s = f"{val:.6g}"
    else:
        s = str(val)
    if v_obj.get("patchSource") == "PDF":
        s += " \U0001f4c4"  # 📄
    return s


def cell_class(v_obj) -> str:
    """Return CSS class(es) for a value cell."""
    if v_obj is None:
        return "null-val"
    val = v_obj.get("value")
    if val is None:
        return "null-val"
    classes = []
    if v_obj.get("patchSource") == "PDF":
        classes.append("patched")
    if v_obj.get("unitWarning"):
        classes.append("unit-warn")
    if isinstance(val, (int, float)) and val == 0:
        classes.append("zero-val")
    return " ".join(classes) if classes else ""


def html_escape(s: str) -> str:
    return (s.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;")
             .replace('"', "&quot;"))


# ---------------------------------------------------------------------------
# HTML template pieces
# ---------------------------------------------------------------------------

CSS = """
<style>
* { box-sizing: border-box; }
body {
  font-family: "Segoe UI", Arial, sans-serif;
  font-size: 13px;
  color: #1a1a1a;
  margin: 0;
  padding: 0;
  background: #f0f2f5;
}
nav {
  position: sticky;
  top: 0;
  z-index: 100;
  background: #1c2a3a;
  padding: 10px 24px;
  display: flex;
  align-items: center;
  gap: 20px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.3);
}
nav a {
  color: #7eb8f7;
  text-decoration: none;
  font-weight: 600;
  font-size: 14px;
  padding: 4px 10px;
  border-radius: 4px;
  transition: background 0.15s;
}
nav a:hover { background: #2d4a6a; }
nav .title {
  color: #cdd8e3;
  font-size: 13px;
  margin-left: auto;
}
.legend {
  background: #fff;
  border: 1px solid #dde3ea;
  border-radius: 6px;
  padding: 8px 16px;
  margin: 16px 24px 0;
  font-size: 12px;
  color: #555;
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
  align-items: center;
}
.legend span { display: flex; align-items: center; gap: 5px; }
.swatch {
  display: inline-block; width: 14px; height: 14px;
  border-radius: 2px; border: 1px solid #bbb;
}
.swatch.patched  { background: #fff3b0; }
.swatch.null-val { background: #fde8e8; }
.swatch.zero-val { background: #f0f0f0; }
.swatch.unit-warn { background: #fff; border-left: 3px solid #f0a500; }
section {
  margin: 20px 24px 40px;
}
h2 {
  font-size: 18px;
  color: #1c2a3a;
  border-bottom: 3px solid #2c4a6e;
  padding-bottom: 6px;
  margin-bottom: 12px;
}
.table-wrapper {
  overflow-x: auto;
  border-radius: 6px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.12);
}
table {
  border-collapse: collapse;
  width: 100%;
  background: #fff;
  min-width: 900px;
}
thead tr {
  position: sticky;
  top: 41px;  /* nav height */
  z-index: 50;
}
thead th {
  background: #2c4a6e;
  color: #fff;
  padding: 9px 12px;
  text-align: left;
  font-size: 12.5px;
  font-weight: 600;
  white-space: nowrap;
  border-right: 1px solid #3d5f8a;
}
thead th.val-col { text-align: right; }
thead th.notes-col { text-align: left; min-width: 160px; }
tr.cat-row td {
  background: #e8eef5;
  color: #1c2a3a;
  font-weight: 700;
  font-size: 12px;
  padding: 6px 12px;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  border-top: 2px solid #b8c8da;
}
tbody tr:hover td:not(.cat-row td) {
  background-color: #f3f7fd !important;
}
td {
  border: 1px solid #e0e6ed;
  padding: 6px 10px;
  vertical-align: middle;
  font-size: 12.5px;
}
td.metric-name { color: #333; max-width: 260px; }
td.unit-cell   { color: #777; font-size: 11.5px; white-space: nowrap; }
td.val-cell    { text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; }
td.patched     { background: #fff3b0; }
td.null-val    { background: #fde8e8; color: #999; text-align: right; }
td.unit-warn   { border-left: 3px solid #f0a500; }
td.zero-val    { background: #f5f5f5; color: #aaa; }
td.notes-cell  {
  background: #fffef0;
  min-width: 160px;
  max-width: 250px;
  cursor: text;
  color: #888;
  font-style: italic;
  font-size: 12px;
}
td.notes-cell:focus {
  outline: 2px solid #4a90d9;
  background: #fff;
  color: #1a1a1a;
  font-style: normal;
}
td.notes-cell:not(:empty) {
  color: #1a1a1a;
  font-style: normal;
}
</style>
"""

JS = """
<script>
// Clear placeholder text when user starts typing in a notes cell
document.querySelectorAll('.notes-cell').forEach(function(cell) {
  cell.addEventListener('focus', function() {
    if (this.textContent.trim() === 'type here') {
      this.textContent = '';
    }
  });
  cell.addEventListener('blur', function() {
    if (this.textContent.trim() === '') {
      this.textContent = 'type here';
    }
  });
});
</script>
"""


# ---------------------------------------------------------------------------
# Table builder
# ---------------------------------------------------------------------------

def build_table(year: str, company_data_map: dict) -> str:
    rows = []
    rows.append("<div class='table-wrapper'>")
    rows.append("<table>")
    rows.append(
        "<thead><tr>"
        "<th style='min-width:200px'>Metric</th>"
        "<th class='unit-col' style='min-width:90px'>Unit</th>"
        "<th class='val-col' style='min-width:120px'>Tata Steel</th>"
        "<th class='val-col' style='min-width:120px'>JSW Steel</th>"
        "<th class='val-col' style='min-width:120px'>SAIL</th>"
        "<th class='val-col' style='min-width:130px'>Jindal Stainless</th>"
        "<th class='notes-col'>Notes (click to type)</th>"
        "</tr></thead>"
    )
    rows.append("<tbody>")

    current_cat = None
    for category, tag, display_name, unit_hint in TAG_GROUPS:
        if category != current_cat:
            current_cat = category
            rows.append(
                f"<tr class='cat-row'>"
                f"<td colspan='7'>{html_escape(category)}</td>"
                f"</tr>"
            )

        # Collect value objects for all companies
        val_objs = [
            get_val_obj(company_data_map[cid], year, tag)
            for cid, _ in COMPANIES
        ]

        # Build cells
        val_cells = []
        for v_obj in val_objs:
            text = fmt_value(v_obj)
            cls = cell_class(v_obj)
            # Compose class string (always include val-cell for alignment)
            full_cls = " ".join(filter(None, ["val-cell", cls]))
            # Add unit warning tooltip if present
            title_attr = ""
            if v_obj and v_obj.get("unitWarning"):
                title_attr = f' title="{html_escape(v_obj["unitWarning"][:120])}"'
            val_cells.append(f"<td class='{full_cls}'{title_attr}>{html_escape(text)}</td>")

        unit_display = html_escape(unit_hint) if unit_hint else "—"
        metric_display = html_escape(display_name)

        rows.append(
            f"<tr>"
            f"<td class='metric-name'>{metric_display}</td>"
            f"<td class='unit-cell'>{unit_display}</td>"
            + "".join(val_cells) +
            f"<td class='notes-cell' contenteditable='true'>type here</td>"
            f"</tr>"
        )

    rows.append("</tbody></table></div>")
    return "\n".join(rows)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("Loading company data...")
    company_data_map = {cid: load(cid) for cid, _ in COMPANIES}

    total_rows = len(TAG_GROUPS)
    print(f"  {total_rows} metric rows × 3 years = {total_rows * 3} data rows")

    parts = [
        "<!DOCTYPE html>",
        "<html lang='en'>",
        "<head>",
        "  <meta charset='utf-8'>",
        "  <meta name='viewport' content='width=device-width, initial-scale=1'>",
        f"  <title>BRSR Comparison Review — {date.today()}</title>",
        CSS,
        "</head>",
        "<body>",

        # ── Navigation ──
        "<nav>",
        "  <strong style='color:#fff;font-size:15px'>BRSR Review</strong>",
        "  <a href='#FY2023'>FY2023</a>",
        "  <a href='#FY2024'>FY2024</a>",
        "  <a href='#FY2025'>FY2025</a>",
        f"  <span class='title'>Generated {date.today()} &nbsp;|&nbsp; "
        f"{total_rows} metrics &nbsp;|&nbsp; 4 companies &nbsp;|&nbsp; 3 years</span>",
        "</nav>",

        # ── Legend ──
        "<div class='legend'>",
        "  <strong>Legend:</strong>",
        "  <span><span class='swatch patched'></span> PDF-patched value (📄)</span>",
        "  <span><span class='swatch null-val'></span> Null / not reported</span>",
        "  <span><span class='swatch unit-warn'></span> Unit warning (hover for detail)</span>",
        "  <span><span class='swatch zero-val'></span> Explicit zero</span>",
        "  <span style='color:#888;font-size:11px'>Ctrl+F to search &nbsp;|&nbsp; Click Notes cell to type</span>",
        "</div>",
    ]

    for year in YEARS:
        parts += [
            f"<section id='{year}'>",
            f"<h2>{year}</h2>",
            build_table(year, company_data_map),
            "</section>",
        ]

    parts += [JS, "</body>", "</html>"]

    html = "\n".join(parts)
    OUT_HTML.parent.mkdir(exist_ok=True)
    OUT_HTML.write_text(html, encoding="utf-8")
    print(f"\nWrote: {OUT_HTML}")
    print(f"       {total_rows} metric rows × 3 years")
    print("\nOpen comparison_table.html in your browser to review.")
    print("Ctrl+F to search  |  Click any Notes cell to type  |  Gold = PDF-patched  |  Red = null")


if __name__ == "__main__":
    main()
