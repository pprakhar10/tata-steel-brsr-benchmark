"""
apply_pdf_patches.py
Applies patches from Gemini PDF extraction to company JSON files and writes
pdf_enrichment JSON files.

Patches are derived from manual review of gemini_pdf_out_*.md files.
Every numeric change is documented with patchSource.

Run from the project root:
    cd "C:/Prakhar/claude code/Tata steel BRSR benchmark"
    python parser/apply_pdf_patches.py
"""

import json
import os
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "dashboard" / "src" / "data"
COMPANIES_DIR = DATA_DIR / "companies"
ENRICHMENT_DIR = DATA_DIR / "pdf_enrichment"
ENRICHMENT_DIR.mkdir(parents=True, exist_ok=True)

PRODUCTION = {
    "jsw-steel":  {"FY2023": 24_150_000, "FY2024": 26_430_000, "FY2025": 27_790_000},
    "sail":       {"FY2023": 18_290_000, "FY2024": 19_240_000, "FY2025": 19_170_000},
}


def load_company(company_id):
    path = COMPANIES_DIR / f"{company_id}.json"
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_company(company_id, data):
    path = COMPANIES_DIR / f"{company_id}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  Saved {path.name}")


def make_air_patch(raw_value, raw_unit, std_value, std_unit, patch_source, data_type="numeric"):
    return {
        "value": std_value,
        "rawValue": str(raw_value),
        "rawUnit": raw_unit,
        "standardUnit": std_unit,
        "normalized": True,
        "unitWarning": None,
        "dataType": data_type,
        "valueStatus": "reported",
        "patchSource": patch_source,
    }


def make_not_normalizable(raw_value, raw_unit, warning):
    return {
        "value": None,
        "rawValue": str(raw_value),
        "rawUnit": raw_unit,
        "standardUnit": None,
        "normalized": False,
        "unitWarning": warning,
        "dataType": "text",
        "valueStatus": "not_normalizable",
        "patchSource": "PDF verification: unit confirmed as concentration (mg/Nm³), cannot convert to mass",
    }


# ─────────────────────────────────────────────────────────────────────────────
# TATA STEEL
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== Patching tata-steel ===")
ts = load_company("tata-steel")

# FY2023: Scope1+2 intensity — XBRL 61 is an error
# Computed: (75,750,000 + 5,200,000) / 28,180,000 = 2.872 tCO2e/tonne
computed_intensity = (75_750_000 + 5_200_000) / 28_180_000
print(f"  FY2023 Scope1+2 intensity computed: {computed_intensity:.4f} tCO2e/tonne")
tag = "TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput"
ts["years"]["FY2023"][tag] = {
    "value": round(computed_intensity, 4),
    "rawValue": "61",
    "rawUnit": None,
    "standardUnit": "tCO2e/tonne of crude steel",
    "normalized": True,
    "unitWarning": "XBRL raw value was 61 — PDF could not locate value; computed from (Scope1+Scope2)/production = (75.75M+5.2M)/28.18M. XBRL value appears to be a filing error.",
    "dataType": "numeric",
    "valueStatus": "computed",
    "patchSource": "Computed: (TotalScope1Emissions+TotalScope2Emissions)/steel_production_FY2023_consolidated",
}
print(f"  FY2023: patched intensity 61 -> {round(computed_intensity, 4)}")

# FY2023: Water intensity — add unit annotation, keep value
wi_tag = "WaterIntensityPerRupeeOfTurnover"
if wi_tag in ts["years"]["FY2023"]:
    ts["years"]["FY2023"][wi_tag]["rawUnit"] = "litres per rupee of turnover"
    ts["years"]["FY2023"][wi_tag]["standardUnit"] = "L/rupee"
    ts["years"]["FY2023"][wi_tag]["unitWarning"] = (
        "PDF confirms unit is litres per rupee of turnover. PDF reports 0.07 (India entity only); "
        "XBRL shows 0.08 (consolidated). Minor difference due to entity breakdown. XBRL value retained."
    )
    print("  FY2023: annotated WaterIntensityPerRupeeOfTurnover unit")

# FY2024: add SOx and NOx from PDF
for yr, sox_kt, nox_kt in [("FY2024", 38.0, 20.0), ("FY2025", 46.0, 24.0)]:
    ts["years"][yr]["Sox"] = make_air_patch(
        raw_value=sox_kt, raw_unit="Kilotonnes/year",
        std_value=sox_kt, std_unit="kilotonnes",
        patch_source=f"PDF: Tata Steel {yr} BRSR — SOx not in XBRL",
    )
    ts["years"][yr]["Nox"] = make_air_patch(
        raw_value=nox_kt, raw_unit="Kilotonnes/year",
        std_value=nox_kt, std_unit="kilotonnes",
        patch_source=f"PDF: Tata Steel {yr} BRSR — NOx not in XBRL",
    )
    print(f"  {yr}: added Sox={sox_kt} kt, Nox={nox_kt} kt")

save_company("tata-steel", ts)


# ─────────────────────────────────────────────────────────────────────────────
# JSW STEEL
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== Patching jsw-steel ===")
jsw = load_company("jsw-steel")

# FY2024: SOx and NOx from PDF (kg/tcs), normalize using production
jsw_sox_nox = {
    "FY2024": {"Sox_kgtcs": 1.66, "Nox_kgtcs": 1.19},
    "FY2025": {"Sox_kgtcs": 1.66, "Nox_kgtcs": 1.15},
}
for yr, vals in jsw_sox_nox.items():
    prod = PRODUCTION["jsw-steel"][yr]
    sox_kt = vals["Sox_kgtcs"] * prod / 1_000_000
    nox_kt = vals["Nox_kgtcs"] * prod / 1_000_000
    jsw["years"][yr]["Sox"] = make_air_patch(
        raw_value=vals["Sox_kgtcs"], raw_unit="kg/tcs",
        std_value=round(sox_kt, 6), std_unit="kilotonnes",
        patch_source=f"PDF: JSW Steel {yr} BRSR; normalized: {vals['Sox_kgtcs']} kg/tcs × {prod:,} t / 1,000,000",
    )
    jsw["years"][yr]["Nox"] = make_air_patch(
        raw_value=vals["Nox_kgtcs"], raw_unit="kg/tcs",
        std_value=round(nox_kt, 6), std_unit="kilotonnes",
        patch_source=f"PDF: JSW Steel {yr} BRSR; normalized: {vals['Nox_kgtcs']} kg/tcs × {prod:,} t / 1,000,000",
    )
    print(f"  {yr}: Sox={round(sox_kt,4)} kt, Nox={round(nox_kt,4)} kt")

save_company("jsw-steel", jsw)


# ─────────────────────────────────────────────────────────────────────────────
# SAIL
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== Patching sail ===")
sail = load_company("sail")

# FY2023: SOx, NOx, PM — concentration ranges, permanently non-normalizable
SAIL_CONC_WARNING = (
    "SAIL FY2023 reports air emissions as concentration ranges in mg/Nm³ (stack concentration). "
    "Cannot convert to absolute mass (kilotonnes) without stack flow rate data, which is not publicly disclosed. "
    "These values are excluded from cross-company air emission comparisons."
)
sail["years"]["FY2023"]["Sox"] = make_not_normalizable("3 to 76", "mg/Nm³ (range)", SAIL_CONC_WARNING)
sail["years"]["FY2023"]["Nox"] = make_not_normalizable("3 to 87", "mg/Nm³ (range)", SAIL_CONC_WARNING)
sail["years"]["FY2023"]["ParticulateMatter"] = make_not_normalizable("31 to 99", "mg/Nm³ (range)", SAIL_CONC_WARNING)
print("  FY2023: SOx/NOx/PM marked non-normalizable (mg/Nm³ concentration ranges)")

# FY2024: emissions intensity 0.0 -> patch to 2.8 (PDF confirmed)
tag = "TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput"
sail["years"]["FY2024"][tag]["value"] = 2.8
sail["years"]["FY2024"][tag]["rawValue"] = "2.8"
sail["years"]["FY2024"][tag]["rawUnit"] = "tCO2e/tonne of crude steel"
sail["years"]["FY2024"][tag]["standardUnit"] = "tCO2e/tonne of crude steel"
sail["years"]["FY2024"][tag]["normalized"] = True
sail["years"]["FY2024"][tag]["unitWarning"] = None
sail["years"]["FY2024"][tag]["patchSource"] = "PDF: SAIL FY2024 BRSR — XBRL reported 0 (filing error)"
print("  FY2024: patched emissions intensity 0 -> 2.8")

# FY2024: water intensity 52.33 -> null (denominator error)
wi_tag = "WaterIntensityPerRupeeOfTurnover"
sail["years"]["FY2024"][wi_tag]["value"] = None
sail["years"]["FY2024"][wi_tag]["normalized"] = False
sail["years"]["FY2024"][wi_tag]["valueStatus"] = "erroneous"
sail["years"]["FY2024"][wi_tag]["unitWarning"] = (
    "XBRL FY2024 value (52.33) is erroneous — XBRL filer changed denominator unit between FY2023 and FY2024. "
    "PDF reports 5.49 KL/Crore but this does not reconcile with total water withdrawal and SAIL's turnover. "
    "Estimated correct value ~0.055 L/rupee (~550 KL/Crore) based on total water (57.4M kL) and turnover (~104,000 Cr). "
    "Value set to null pending manual verification."
)
sail["years"]["FY2024"][wi_tag]["patchSource"] = "PDF verification revealed XBRL denominator error; value nulled"
print("  FY2024: WaterIntensity 52.33 -> null (denominator error)")

# FY2024: PM — PDF says 0.58 kg/tcs (XBRL had 0.58 µg/m³ — unit was wrong)
prod_fy24 = PRODUCTION["sail"]["FY2024"]
pm_fy24_kt = 0.58 * prod_fy24 / 1_000_000
sail["years"]["FY2024"]["ParticulateMatter"] = make_air_patch(
    raw_value=0.58, raw_unit="kg/tcs (PDF corrects XBRL label of µg/m³)",
    std_value=round(pm_fy24_kt, 6), std_unit="kilotonnes",
    patch_source="PDF: SAIL FY2024 BRSR reports PM as 0.58 kg/tcs (mass intensity), correcting XBRL unit label of µg/m³",
)
print(f"  FY2024: PM unit corrected µg/m³->kg/tcs, value={round(pm_fy24_kt,4)} kt")

# FY2024: SOx and NOx from PDF
sail_sox_nox = {
    "FY2024": {"Sox_kgtcs": 0.53, "Nox_kgtcs": 0.55},
    "FY2025": {"Sox_kgtcs": 0.61, "Nox_kgtcs": 0.61},
}
for yr, vals in sail_sox_nox.items():
    prod = PRODUCTION["sail"][yr]
    sox_kt = vals["Sox_kgtcs"] * prod / 1_000_000
    nox_kt = vals["Nox_kgtcs"] * prod / 1_000_000
    sail["years"][yr]["Sox"] = make_air_patch(
        raw_value=vals["Sox_kgtcs"], raw_unit="kg/tcs",
        std_value=round(sox_kt, 6), std_unit="kilotonnes",
        patch_source=f"PDF: SAIL {yr} BRSR; normalized: {vals['Sox_kgtcs']} kg/tcs × {prod:,} t / 1,000,000",
    )
    sail["years"][yr]["Nox"] = make_air_patch(
        raw_value=vals["Nox_kgtcs"], raw_unit="kg/tcs",
        std_value=round(nox_kt, 6), std_unit="kilotonnes",
        patch_source=f"PDF: SAIL {yr} BRSR; normalized: {vals['Nox_kgtcs']} kg/tcs × {prod:,} t / 1,000,000",
    )
    print(f"  {yr}: Sox={round(sox_kt,4)} kt, Nox={round(nox_kt,4)} kt")

# FY2025: PM — 0.56 kg/tcs confirmed from FY2025 PDF target note
prod_fy25 = PRODUCTION["sail"]["FY2025"]
pm_fy25_kt = 0.56 * prod_fy25 / 1_000_000
sail["years"]["FY2025"]["ParticulateMatter"] = make_air_patch(
    raw_value=0.56, raw_unit="kg/tcs (XBRL label was µg/m³; PDF target note confirms kg/tcs)",
    std_value=round(pm_fy25_kt, 6), std_unit="kilotonnes",
    patch_source="FY2025 SAIL PDF target note: 'PM reduction from 0.58 kg/tcs (FY24) to 0.56 kg/tcs achieved (FY25)'",
)
print(f"  FY2025: PM unit corrected µg/m³->kg/tcs, value={round(pm_fy25_kt,4)} kt")

save_company("sail", sail)


# ─────────────────────────────────────────────────────────────────────────────
# JINDAL STAINLESS
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== Patching jindal-stainless ===")
jindal = load_company("jindal-stainless")

# Water intensity — all 3 years use KL/Crore INR; FY2025 XBRL was erroneously
# reported as kL/rupee (filer divided by 1e7). Normalise all to KL/Crore.
wi_tag = "WaterIntensityPerRupeeOfTurnover"
JINDAL_WI_WARNING = (
    "Jindal Stainless reports water intensity per Crore INR of turnover (not per single rupee as SEBI specifies). "
    "FY2023=335 KL/Cr, FY2024=333 KL/Cr, FY2025=358.67 KL/Cr. "
    "FY2025 XBRL filer erroneously normalised to kL/rupee (divided by 1e7); corrected here to KL/Crore for consistency. "
    "For comparison with Tata/JSW (L/rupee): 335 KL/Cr ≈ 0.0335 L/rupee."
)

# FY2023: value 335 KL/Crore, already correct
jindal["years"]["FY2023"][wi_tag]["rawUnit"] = "KL per Crore INR of turnover"
jindal["years"]["FY2023"][wi_tag]["standardUnit"] = "KL/Crore INR"
jindal["years"]["FY2023"][wi_tag]["unitWarning"] = JINDAL_WI_WARNING
print("  FY2023: WaterIntensity annotated as KL/Crore INR (value 335 correct)")

# FY2024: value 333 KL/Crore, already correct
if wi_tag in jindal["years"]["FY2024"]:
    jindal["years"]["FY2024"][wi_tag]["rawUnit"] = "KL per Crore INR of turnover"
    jindal["years"]["FY2024"][wi_tag]["standardUnit"] = "KL/Crore INR"
    jindal["years"]["FY2024"][wi_tag]["unitWarning"] = JINDAL_WI_WARNING
    print("  FY2024: WaterIntensity annotated as KL/Crore INR (value 333 correct)")

# FY2025: XBRL stored 0.0000359 kL/rupee -> correct to 358.67 KL/Crore
if wi_tag in jindal["years"]["FY2025"]:
    jindal["years"]["FY2025"][wi_tag]["value"] = 358.67
    jindal["years"]["FY2025"][wi_tag]["rawValue"] = "358.67"
    jindal["years"]["FY2025"][wi_tag]["rawUnit"] = "KL per Crore INR of turnover"
    jindal["years"]["FY2025"][wi_tag]["standardUnit"] = "KL/Crore INR"
    jindal["years"]["FY2025"][wi_tag]["unitWarning"] = JINDAL_WI_WARNING
    jindal["years"]["FY2025"][wi_tag]["patchSource"] = (
        "PDF: FY2025 value confirmed as 358.67 KL/Crore. "
        "XBRL filed as 0.0000359 kL/rupee (same metric, different denominator unit). Corrected for consistency."
    )
    print("  FY2025: WaterIntensity corrected 0.0000359 kL/rupee -> 358.67 KL/Crore")

# FY2024: SOx and NOx from PDF
jindal["years"]["FY2024"]["Sox"] = make_air_patch(
    raw_value="3072.064", raw_unit="MT",
    std_value=round(3072.064 / 1000, 6), std_unit="kilotonnes",
    patch_source="PDF: Jindal Stainless FY2024 BRSR — SOx not in XBRL",
)
jindal["years"]["FY2024"]["Nox"] = make_air_patch(
    raw_value="1782.58", raw_unit="MT",
    std_value=round(1782.58 / 1000, 6), std_unit="kilotonnes",
    patch_source="PDF: Jindal Stainless FY2024 BRSR — NOx not in XBRL",
)
print(f"  FY2024: Sox={round(3072.064/1000,4)} kt, Nox={round(1782.58/1000,4)} kt")

# FY2025: SOx and NOx from PDF
jindal["years"]["FY2025"]["Sox"] = make_air_patch(
    raw_value="4580.69", raw_unit="MT",
    std_value=round(4580.69 / 1000, 6), std_unit="kilotonnes",
    patch_source="PDF: Jindal Stainless FY2025 BRSR — SOx not in XBRL",
)
jindal["years"]["FY2025"]["Nox"] = make_air_patch(
    raw_value="2527.48", raw_unit="MT",
    std_value=round(2527.48 / 1000, 6), std_unit="kilotonnes",
    patch_source="PDF: Jindal Stainless FY2025 BRSR — NOx not in XBRL",
)
print(f"  FY2025: Sox={round(4580.69/1000,4)} kt, Nox={round(2527.48/1000,4)} kt")

save_company("jindal-stainless", jindal)


# ─────────────────────────────────────────────────────────────────────────────
# PDF ENRICHMENT FILES
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== Writing pdf_enrichment files ===")

ENRICHMENT_DATA = {
    "tata-steel": {
        "FY2023": {
            "targets": [
                {"description": "Net Zero emissions for the Tata Steel Group", "metric": "Scope 1 and 2 emissions", "baseline": None, "targetValue": "Net Zero", "timeline": "2045"},
                {"description": "Achieve specific dust emission intensity of 0.43 kg per tonne of crude steel in India", "metric": "Dust Emission Intensity", "baseline": None, "targetValue": "0.43 kg/tonne", "timeline": "2025"},
                {"description": "Achieve specific freshwater consumption of 2.0 m³ per tonne of crude steel across all steelmaking sites in India", "metric": "Freshwater consumption intensity", "baseline": None, "targetValue": "2.0 m3/tonne", "timeline": "2025"},
            ],
            "initiatives": [
                {"name": "Zero Carbon Logistics programme", "area": "emissions", "description": "Reduce CO2 footprint from product transport by 30% by 2030. Uses Optimum Voyage to optimise fuel efficiency.", "outcome": "Savings of ~5% CO2 emissions; replacing road with rail reduced >5,000 trucks/year."},
                {"name": "Benchmarking Energy Efficiency IMPACT Centre", "area": "energy", "description": "Drive energy efficiency campaigns across the Company.", "outcome": "Savings of more than Rs. 750 crore since 2015."},
                {"name": "Tata Power Renewable Energy Agreement", "area": "energy", "description": "Set up 950 MW solar & wind hybrid renewable power capacity under captive arrangement.", "outcome": "Will cater to 379 MW of power requirement and enable reduction of over 2 million tonnes CO2 per annum."},
            ],
            "scope3Breakdown": {"totalScope3": "13.1 million tCO2e", "categories": [], "note": "Tata Steel measures end-to-end Scope 3 emissions for all modes of transportation."},
            "managementCommentary": "In line with our vision of being the steel industry benchmark in Corporate Citizenship, Tata Steel has adopted ESG goals driving initiatives across the Company. We are committed to avoiding operational activities near sites containing globally or nationally important biodiversity. The Policy aspires to achieve no Net Loss of Biodiversity.",
            "awardsAndRatings": [
                {"name": "JRDQV award (Benchmark Leader under TBEM Assessment)", "score": None, "year": "2021"},
                {"name": "ResponsibleSteel™ Certification (Jamshedpur site)", "score": "Certified", "year": "2022"},
            ],
            "nonCompliance": [],
            "forwardLooking": [
                {"description": "Net Zero emissions for the Tata Steel Group", "timeline": "2045"},
                {"description": "Cover 100% sites under Biodiversity Management Plans across India, UK and the Netherlands", "timeline": "2025"},
            ],
            "qualitativePolicies": {
                "P1_ethics": "The Anti-Bribery and Anti-Corruption (ABAC) Policy ensures operations are conducted with highest ethical standards, preventing fraud, bribery and corruption, applicable to all employees, contractors, and partners.",
                "P3_ohs": "The Safety & Occupational Health Policy commits to 'Zero Harm' and becoming an industry leader in safety and health performance through robust management and reporting systems.",
                "P6_environment": "The Biodiversity and Environmental policies integrate biodiversity into the business ecosystem, aiming for no Net Loss of Biodiversity and ensuring habitat conservation and restoration.",
            },
            "steelProduction": {"value": 28_180_000, "unit": "metric tonnes", "note": "Consolidated basis (as per plan config). PDF states capacity of 35 MTPA but production volume not explicitly stated in BRSR."},
            "reportingBoundary": "Consolidated basis — Tata Steel Limited and 13 key subsidiary companies.",
        },
        "FY2024": {
            "targets": [
                {"description": "Net Zero emissions for the Tata Steel Group", "metric": "Scope 1 and 2 emissions", "baseline": None, "targetValue": "Net Zero", "timeline": "2045"},
                {"description": "Achieve specific freshwater consumption of <1.5 m³ per tonne of crude steel across all India sites", "metric": "Water intensity", "baseline": None, "targetValue": "<1.5 m3/tonne", "timeline": "2030"},
                {"description": "Achieve 20% diversity in workforce for Tata Steel Limited", "metric": "Workforce diversity", "baseline": None, "targetValue": "20%", "timeline": "2025"},
            ],
            "initiatives": [
                {"name": "Zero Carbon Logistics programme", "area": "emissions", "description": "Aim to reduce CO2 footprint from product transport by 30% by 2030.", "outcome": "Optimum Voyage resulted in savings of ~5% CO2 emissions."},
                {"name": "Captive Renewable Power Sourcing", "area": "energy", "description": "Definitive agreement with Tata Power to source 379 MW of captive renewable power.", "outcome": "Will reduce 50 million tonnes of carbon emissions over 25-year contract period."},
                {"name": "Floating Solar Power Project", "area": "energy", "description": "Commissioned 10.8 MWp floating solar project on upper cooling pond in Jamshedpur.", "outcome": "Brought total solar capacity to 20.34 MWp at Jamshedpur plant."},
            ],
            "scope3Breakdown": {"totalScope3": "15 million tCO2e (Standalone)", "categories": [], "note": "Measurement of end-to-end Scope 3 emissions for all modes of transportation is highly prioritized."},
            "managementCommentary": "We are proud to present the second edition of our BRSR, underscoring our unwavering commitment to ESG stewardship. As the global shift to a low-carbon economy gains momentum, Tata Steel has been at the forefront of advancing sustainable practices by reducing GHG emissions, increasing energy efficiency, improving water management, and promoting waste recycling initiatives through innovative R&D investments.",
            "awardsAndRatings": [{"name": "TAAP Assessment", "score": "700–725", "year": "2023"}],
            "nonCompliance": [],
            "forwardLooking": [
                {"description": "Net Zero emissions for the Tata Steel Group", "timeline": "2045"},
                {"description": "Achieve zero harm for Tata Steel Limited", "timeline": "2030"},
            ],
            "qualitativePolicies": {
                "P1_ethics": "Tata Code of Conduct (TCoC) and Anti-Bribery and Anti-Corruption Policy guide fair practices and ethics, establishing a framework against fraud, bribery, and corruption.",
                "P3_ohs": "The Safety Principles and Occupational Health Policy aim to secure zero harm, including continuous monitoring and hazard assessment through Safety Leadership Development Centres.",
                "P6_environment": "The Responsible Supply Chain Policy (RSCP) and Environmental Policy enforce tracking and mitigation of scope emissions, environmental restoration, and material efficiency goals.",
            },
            "steelProduction": {"value": 20_120_000, "unit": "metric tonnes", "note": "Standalone (India only). From plan config — not explicitly stated in BRSR text block."},
            "reportingBoundary": "Standalone basis (Tata Steel Limited India operations). FY2024 BRSR also discloses consolidated figures separately.",
        },
        "FY2025": {
            "targets": [
                {"description": "Net Zero emissions for the Tata Steel Group", "metric": "Scope 1 and 2 emissions", "baseline": None, "targetValue": "Net Zero", "timeline": "2045"},
            ],
            "initiatives": [
                {"name": "Green Mobility Fleet Expansion", "area": "emissions", "description": "Deployed 70% Electric Vehicles (EVs) in warehouse and delivery operations.", "outcome": "Reduction of ~200 tonnes CO2 annually."},
                {"name": "B24 Biofuel Shipments", "area": "emissions", "description": "First Indian steel company to conduct full laden leg shipments using B24 biofuel from Australia to India.", "outcome": "Executed 39 biofuel vessels and 5 LNG vessels — ~18% of imported shipments."},
                {"name": "Rooftop Solar Panel at Jamshedpur Warehouse", "area": "energy", "description": "Installation of 2.2 MW rooftop solar panel.", "outcome": "Facility became energy-positive, generating 2,303 MWh against consumption of 1,582 MWh."},
            ],
            "scope3Breakdown": {"totalScope3": "23 million tCO2e (Standalone)", "categories": [], "note": "Emphasis on Scope 3 logistics tracking including global frameworks for emissions reporting in subsidiary hubs."},
            "managementCommentary": "We have embraced decarbonisation not as a compulsion but as a deliberate choice with shared enthusiasm. The report highlights how we are moving decisively from intent to impact, re-engineering and future proofing operations across the full arc of our value chain. We realise technological innovation is our bridge to the future and have accelerated efforts towards digitalisation, automation, AI-enabled systems and climate smart solutions.",
            "awardsAndRatings": [{"name": "ResponsibleSteel™ Certification (Jamshedpur, Kalinganagar, Meramandali)", "score": "Certified", "year": "2024"}],
            "nonCompliance": [
                {"description": "Collector of Stamps, Enforcement I and II imposed penalties of Rs 1,46,14,380 and Rs 1,28,07,700 towards belated filing of stamp-duty application related to scheme of amalgamation.", "resolution": "Penalty paid; no appeal preferred."},
            ],
            "forwardLooking": [{"description": "Net Zero emissions", "timeline": "2045"}],
            "qualitativePolicies": {
                "P1_ethics": "The Tata Code of Conduct and related whistleblower/anti-bribery policies mandate transparent, accountable, and ethical behaviour from all stakeholders and employees.",
                "P3_ohs": "The occupational health and safety systems aim for zero harm, relying on continuous internal reviews, 6-strategic initiative frameworks, and robust grievance redressing systems.",
                "P6_environment": "Environmental and Biodiversity policies detail commitments toward habitat protection, nature-positive solutions, emission curbs, and integration of the 4R framework across plants.",
            },
            "steelProduction": {"value": 21_710_000, "unit": "metric tonnes", "note": "Standalone (India only). From plan config."},
            "reportingBoundary": "Standalone basis (Tata Steel Limited India operations).",
        },
    },
    "jsw-steel": {
        "FY2023": {
            "targets": [
                {"description": "Reduce specific CO2 emissions intensity", "metric": "tCO2e/tcs", "baseline": "2005", "targetValue": "1.95 tCO2/tcs (42% reduction)", "timeline": "2030"},
                {"description": "Achieve carbon neutrality", "metric": "Net Neutrality", "baseline": None, "targetValue": "Net Neutral", "timeline": "2050"},
            ],
            "initiatives": [
                {"name": "Energy Efficiency Interventions", "area": "energy", "description": "Implementation of environment sustainability interventions and optimisation of resource utilization.", "outcome": "Capex investment of 3.13% of total capex for environmental sustainability."},
            ],
            "scope3Breakdown": {"totalScope3": "5,595,113 tCO2e", "categories": [{"categoryNumber": 1, "name": "Purchased goods and services", "value": "Not explicitly itemized"}], "note": "Total Scope 3 emissions reported in BRSR."},
            "managementCommentary": "Today the variety of applications where steel is used necessitates producers to continuously improve quality and offer products with a lesser carbon footprint. JSW Steel is at the forefront of both these trends. We are doubling up on sustainability by controlling our emissions and ensuring multi-pronged digital focus.",
            "awardsAndRatings": [
                {"name": "CDP Score", "score": "A- (Climate Change)", "year": "2023"},
                {"name": "DJSI", "score": "S&P Global Sustainability Yearbook member", "year": "2023"},
            ],
            "nonCompliance": [],
            "forwardLooking": [{"description": "Achieve 'No Net Loss' of biodiversity at all operating sites", "timeline": "2030"}],
            "qualitativePolicies": {
                "P1_ethics": "Code of Conduct for Board & Senior Management and Policy on Business Conduct.",
                "P3_ohs": "People Policy and Health & Safety Policy ensuring a zero-harm vision.",
                "P6_environment": "Climate Change Policy, Energy Policy, and Water Resource Management Policy.",
            },
            "steelProduction": {"value": 24_150_000, "unit": "metric tonnes", "note": "From plan config (annual report). Gemini derived ~20.9M t from BRSR emissions/intensity — difference may be due to saleable vs crude steel denominator."},
            "reportingBoundary": "Standalone basis.",
        },
        "FY2024": {
            "targets": [{"description": "Carbon emissions intensity reduction", "metric": "tCO2e/tcs", "baseline": "2005", "targetValue": "1.95 tCO2/tcs", "timeline": "2030"}],
            "initiatives": [
                {"name": "Clean Technology Investment (Best Available Technologies)", "area": "energy", "description": "Investment in BATs contributing to environmental and social parameters.", "outcome": "Capex investment of 4.01% of total capex."},
            ],
            "scope3Breakdown": {"totalScope3": "5,842,454 tCO2e", "categories": [], "note": "Total Scope 3 emissions reported."},
            "managementCommentary": "We have set a target of achieving 1.95 tCO2/tcs by 2030 and committed to be Net Neutral by 2050. Steel is a hard-to-abate sector, and we are proactively working on achieving set targets through clear decarbonisation actions.",
            "awardsAndRatings": [
                {"name": "BSC 5 Star Rating", "score": "5 Star", "year": "2024"},
                {"name": "DJSI Score", "score": "High performer in steel industry", "year": "2024"},
            ],
            "nonCompliance": [],
            "forwardLooking": [{"description": "Continuous focus on product diversification and sustainable practices", "timeline": "1–3 years"}],
            "qualitativePolicies": {
                "P1_ethics": "Whistle blower policy in place for employees, vendors, and channel partners.",
                "P3_ohs": "Occupational health and safety management system (ISO 45001:2018) implemented across Integrated Steel Plants.",
                "P6_environment": "Climate action agenda driven by the Climate Action Group.",
            },
            "steelProduction": {"value": 26_430_000, "unit": "metric tonnes", "note": "From plan config (annual report)."},
            "reportingBoundary": "Standalone basis.",
        },
        "FY2025": {
            "targets": [{"description": "Climate change reduction target", "metric": "CO2 Intensity", "baseline": "2005", "targetValue": "1.95 tCO2/tcs", "timeline": "2030"}],
            "initiatives": [
                {"name": "ResponsibleSteel Certification", "area": "governance", "description": "Achieved certification for four manufacturing sites (Vijayanagar, Dolvi, Salem, Tarapur).", "outcome": "Over 80% of primary steel production from certified sites."},
                {"name": "Steel Scrap Recycling", "area": "waste", "description": "Recycled 2.30 million tonnes of scrap.", "outcome": "Circularity enhancement in production."},
            ],
            "scope3Breakdown": {"totalScope3": "6,120,450 tCO2e", "categories": [], "note": "Total Scope 3 included in emission summary."},
            "managementCommentary": "We are committed to preventing, abating and mitigating our emissions to air. We have developed clear targets for decarbonisation and committed to be Net Neutral by 2050.",
            "awardsAndRatings": [{"name": "ResponsibleSteel Certification", "score": "Certified", "year": "2025"}],
            "nonCompliance": [
                {"description": "Penalty from Chhattisgarh Environment Conservation Board for emission of smoke and improper tarpaulin covering.", "resolution": "Fines of INR 360,000 and INR 570,000 remitted."},
                {"description": "Penalty for belated remittance of Provident Fund (2016–2019).", "resolution": "Damages and interest of INR 18,314,378 remitted."},
            ],
            "forwardLooking": [{"description": "Strive to achieve 'No Net Loss' of biodiversity", "timeline": "2030"}],
            "qualitativePolicies": {
                "P1_ethics": "Policy covers ethics, anti-corruption, and eliminating all forms of bribery.",
                "P3_ohs": "Strict safety systems leveraging real-time data and sensors in men-machine interfaces.",
                "P6_environment": "Dedicated policies for air emissions, biodiversity, and resource conservation.",
            },
            "steelProduction": {"value": 27_790_000, "unit": "metric tonnes", "note": "From plan config (annual report)."},
            "reportingBoundary": "Standalone basis.",
        },
    },
    "sail": {
        "FY2023": {
            "targets": [
                {"description": "Eco-restoration of mined-out areas and waste dumps at Meghahatuburu Iron Ore Mines", "metric": "Area restored / seedlings", "baseline": None, "targetValue": "30,000 seedlings raised", "timeline": "2025–26"},
            ],
            "initiatives": [
                {"name": "SAIL Sarathi (AI Chatbot)", "area": "governance", "description": "AI-based Chatbot launched on website to enhance customer engagement.", "outcome": "One of the most advanced customer-facing bots in the steel industry."},
                {"name": "Zero Liquid Discharge (ZLD)", "area": "water", "description": "Implementation of ZLD projects across Integrated Steel Plants including ISP, DSP, and RSP.", "outcome": "Pioneering projects towards 100% water recycling."},
                {"name": "CO2 Capture & Mineralisation (IIT Bombay)", "area": "emissions", "description": "R&D project with IIT Bombay for sustainable, low-energy consuming carbon capture technology.", "outcome": "Part of decarbonization effort."},
            ],
            "scope3Breakdown": {"totalScope3": None, "categories": [], "note": "SAIL started a study to prepare a comprehensive GHG inventory including Scope 3. No Scope 3 figure disclosed."},
            "managementCommentary": "We made a decision to work on focus areas: maximise capacity utilisation and provide best value to customers. Strategic interventions were made in ramping up production and focusing on Decarbonisation and Sustainability. We achieved record Crude Steel capacity utilisation of about 94%.",
            "awardsAndRatings": [
                {"name": "Greentech Environment Award", "score": "Winner", "year": "2022"},
                {"name": "National Energy Conservation Award", "score": "1st Prize (RSP)", "year": "2022"},
            ],
            "nonCompliance": [
                {"description": "Non-compliance of environmental standards at IISCO Steel Plant (ISP).", "resolution": "Direction issued by WBPCB; corrective measures implemented with a time-bound action plan."},
            ],
            "forwardLooking": [
                {"description": "Expansion of Capacity and Intensifying Digitisation", "timeline": "Next decade"},
                {"description": "Green fuel adoption and decarbonisation efforts", "timeline": "Upcoming years"},
            ],
            "qualitativePolicies": {
                "P1_ethics": "Upholds highest ethical standards in business conduct through transparency and accountability.",
                "P3_ohs": "ISO 45001 certified; Hazard Identification and Risk Assessment (HIRA) conducted for most activities.",
                "P6_environment": "Corporate Environmental Policy emphasises going beyond compliance to preserve ecological balance.",
            },
            "steelProduction": {"value": 18_289_000, "unit": "metric tonnes", "note": "Reported as 18.289 MT crude steel production in BRSR PDF."},
            "reportingBoundary": "Standalone.",
        },
        "FY2024": {
            "targets": [{"description": "Achieve Zero Liquid Discharge across all SAIL plants", "metric": "Water Recycling %", "baseline": None, "targetValue": "100%", "timeline": "Continuous"}],
            "initiatives": [
                {"name": "SAIL Green Tiles Plant", "area": "waste", "description": "Utilisation of slag for manufacturing green tiles at Bhilai.", "outcome": "Utilised 5.3 MT of slag."},
            ],
            "scope3Breakdown": {"totalScope3": None, "categories": [], "note": "Scope 3 emission identification is ongoing; partially covered."},
            "managementCommentary": "Focused on smart steel and sustainable growth. The reporting boundary excludes subsidiaries and focuses on integrated and special steel plants on a standalone basis.",
            "awardsAndRatings": [{"name": "Productivity Excellence Award", "score": "5 Star Rating", "year": "2023"}],
            "nonCompliance": [{"description": "Specific environmental non-compliances mentioned for integrated plants.", "resolution": "Corrective actions underway via revamped pollution control equipment."}],
            "forwardLooking": [{"description": "Expansion of renewable energy footprint and decarbonization", "timeline": "Next 3 years"}],
            "qualitativePolicies": {
                "P1_ethics": "Policies cover NGRBC principles; ethics monitored by Board.",
                "P3_ohs": "100% of plants and offices assessed for health and safety practices.",
                "P6_environment": "Dedicated environmental management division oversees restoration and treatment.",
            },
            "steelProduction": {"value": 19_240_000, "unit": "metric tonnes", "note": "From plan config. Gemini derived ~19.67M t from emissions/intensity."},
            "reportingBoundary": "Standalone.",
        },
        "FY2025": {
            "targets": [{"description": "Reduction of Specific PM Emission Load", "metric": "kg/tcs", "baseline": "0.58 kg/tcs (FY2024)", "targetValue": "0.56 kg/tcs", "timeline": "FY2024–25 (achieved)"}],
            "initiatives": [
                {"name": "Green Power Import from DVC", "area": "energy", "description": "Arrangement for green power import from DVC at Durgapur (DSP) and IISCO (ISP) plants.", "outcome": "Significant increase in renewable energy from 266 TJ to 1,400 TJ."},
            ],
            "scope3Breakdown": {"totalScope3": None, "categories": [], "note": "Entity is in the process of identifying all relevant Scope 3 categories."},
            "managementCommentary": "Reduced emissions align with global climate goals and enhance SAIL's competitiveness in green steel markets. Sustainability leads to carbon credits and green bond opportunities.",
            "awardsAndRatings": [],
            "nonCompliance": [{"description": "Bhilai Steel Plant: Inefficient operation of Sewage Treatment Plant (STP) in violation of Water Act 1974.", "resolution": "Direction issued by CECB; corrective actions being taken."}],
            "forwardLooking": [{"description": "Implementation of Solid State Interlocking (SSI) and automation up-gradation", "timeline": "2025–26"}],
            "qualitativePolicies": {
                "P1_ethics": "Anti-corruption and ethics policies covered under NGRBC framework.",
                "P3_ohs": "Occupational Health & Safety is critical for maintaining uninterrupted operations.",
                "P6_environment": "Action plan in place for PM reduction and ZLD implementation.",
            },
            "steelProduction": {"value": 19_170_000, "unit": "metric tonnes", "note": "From plan config. Gemini derived ~18.93M t from emissions/intensity."},
            "reportingBoundary": "Standalone. FY2025 water withdrawal doubling (57M->129M kL) confirmed genuine — expanded operations and inclusion of new reporting units.",
        },
    },
    "jindal-stainless": {
        "FY2023": {
            "targets": [
                {"description": "Net Zero carbon emission target", "metric": "GHG Emissions", "baseline": None, "targetValue": "Net Zero", "timeline": "2050"},
                {"description": "Reduce carbon emission intensity by 50%", "metric": "tCO2e/tcs", "baseline": "FY2022 (1.91 tCO2e/tcs)", "targetValue": "50% reduction", "timeline": "2035"},
            ],
            "initiatives": [
                {"name": "Oxygen Enrichment in Walking Beam Furnace", "area": "energy", "description": "Enrichment of oxygen to reduce Propane/LSHS consumption.", "outcome": "Fuel saving of 3%."},
                {"name": "Water Fixture Replacement", "area": "water", "description": "Replaced 25 taps with efficient dual mist foam water nozzles.", "outcome": "2 m³/day fresh water saved."},
                {"name": "Floor Cleaning with Waste Water", "area": "water", "description": "Cleaning of floors done using waste water and water tankers instead of soft water.", "outcome": "50 m³/day fresh water saved."},
            ],
            "scope3Breakdown": {"totalScope3": "2,781,561 tCO2e", "categories": [], "note": "FY2023 value from comparative column in FY2024 PDF."},
            "managementCommentary": "The Company is unwavering in its dedication to creating a greener, more sustainable future, driven by a strong sense of environmental responsibility. As part of its commitment, the company has adopted an eco-conscious approach in manufacturing stainless steel. This involves utilizing scrap in an electric arc furnace, which stands as the most eco-friendly method with minimal greenhouse gas emissions, fostering a circular economy.",
            "awardsAndRatings": [{"name": "ISO 9001, ISO 14001, ISO 45001, ISO 50001 Certified", "score": None, "year": "2023"}],
            "nonCompliance": [{"description": "No instances of regulatory penalties, environmental non-compliance, or fines reported.", "resolution": "Nil"}],
            "forwardLooking": [
                {"description": "Achieve Net Zero carbon emissions", "timeline": "2050"},
                {"description": "Evaluate realistic targets for reducing waste landfilled", "timeline": "Next 1–3 years"},
            ],
            "qualitativePolicies": {
                "P1_ethics": "Anti-corruption and Anti-bribery policy demonstrates zero tolerance towards bribery and corrupt practices. Manages conflict of interest through annual declarations from the Board and employees.",
                "P3_ohs": "Implements ISO 45001:2018 and adopts a 4-E principle (Engineering Control, Education, Encouragement, Enforcement) to promote an ACCIDENT-FREE STEEL culture.",
                "P6_environment": "Focuses on utilizing scrap in EAF to minimize GHG emissions. Evaluating biodiversity risk, planting native species, and ensuring Zero Liquid Discharge across facilities.",
            },
            "steelProduction": {"value": 1_710_000, "unit": "metric tonnes", "note": "From plan config. Gemini derived ~1.58M t from emissions/intensity — difference may reflect saleable vs crude denominator."},
            "reportingBoundary": "Standalone.",
        },
        "FY2024": {
            "targets": [
                {"description": "Achieve Net Zero emissions", "metric": "GHG Emissions", "baseline": None, "targetValue": "Net Zero", "timeline": "2050"},
                {"description": "Reduce emission intensity by 50%", "metric": "Emission Intensity (tCO2e/tcs)", "baseline": "FY2022", "targetValue": "50% reduction", "timeline": "Medium-term (implied ~2035)"},
            ],
            "initiatives": [
                {"name": "Floating & Rooftop Solar", "area": "energy", "description": "7.3 MWp floating solar installed and 23 MWp rooftop solar under commission in Jajpur.", "outcome": "Generated 6,155,850 kWh from onsite solar generation."},
                {"name": "Chrome Palletisation Plant", "area": "emissions", "description": "Installed chrome palletization plant instead of traditional briquetting — lower specific energy consumption.", "outcome": "Reduction in overall emissions."},
                {"name": "Waste Heat Recovery Boiler (WHRB)", "area": "energy", "description": "Captures and utilizes waste heat during steelmaking to generate steam.", "outcome": "Abated 298.8 tonnes of propane equivalent."},
            ],
            "scope3Breakdown": {"totalScope3": "3,345,443 tCO2e", "categories": [], "note": "Scope 3 emission intensity is 1.90 tCO2e/tcs."},
            "managementCommentary": "The Company is unwavering in its dedication to creating a sustainable future, driven by ESG responsibility. Utilizing scrap in an electric arc furnace — the most eco-friendly steelmaking method — ensures 100% recyclability. Management is evaluating realistic targets for reducing waste landfilled.",
            "awardsAndRatings": [{"name": "Responsible Steel certification (In Progress)", "score": None, "year": "2024"}],
            "nonCompliance": [{"description": "No fines, penalties, or non-compliances reported for the year.", "resolution": "Nil"}],
            "forwardLooking": [{"description": "Develop science-based targets for near-term and Net Zero GHG emissions through SBTi", "timeline": "Long-term (2050)"}],
            "qualitativePolicies": {
                "P1_ethics": "The ABAC Policy ensures operations align with highest ethical standards to prevent fraud, bribery, and corruption.",
                "P3_ohs": "Driven by a 'No Harm' philosophy. Implemented ISO 45001:2018. Safety culture relies on Engineering Control, Education, Encouragement, and Enforcement.",
                "P6_environment": "Operations centred around Reduce, Reuse, Recycle, Recover, and Repurpose. ~72% of input material consists of recycled scrap and revert.",
            },
            "steelProduction": {"value": 2_080_000, "unit": "metric tonnes", "note": "From plan config. Gemini derived ~1.76M t from BRSR — difference may reflect saleable vs crude denominator."},
            "reportingBoundary": "Standalone.",
        },
        "FY2025": {
            "targets": [
                {"description": "Carbon emission intensity reduction by 50%", "metric": "tCO2e/tcs", "baseline": "FY2022", "targetValue": "50% reduction", "timeline": "2035"},
                {"description": "Zero-Waste-to-Landfill certification", "metric": "Waste to landfill", "baseline": None, "targetValue": "Zero", "timeline": "2030"},
                {"description": "Diversity and inclusion — female workforce representation", "metric": "% female workforce", "baseline": None, "targetValue": "8%", "timeline": "2030"},
            ],
            "initiatives": [
                {"name": "Smart cooling control (electrode temperature)", "area": "energy", "description": "Reduced blower runtime by 4.28 hours/day by modifying control logic.", "outcome": "Saved 1.66 lakh units electricity annually (INR 10.8 lakhs)."},
                {"name": "CPP-DM Plant optimisation", "area": "water", "description": "Replaced faulty ejectors/valves, optimised downflow rates and degasser levels.", "outcome": "12% reduction in HCl, 15% reduction in NaOH; raw water dropped by 420 m³/year."},
                {"name": "Boiler waste water reuse", "area": "water", "description": "Created settling tank and pipeline to cooling tower basin to reuse DM water from boiler hydro-tests.", "outcome": "Saved 2,532 m³ of water annually."},
            ],
            "scope3Breakdown": {"totalScope3": "3,216,693 tCO2e", "categories": [], "note": "Intensity is 1.64 tCO2e/tcs — reduction from FY2024."},
            "managementCommentary": "JSL remains steadfast in its commitment to building a greener and more sustainable future, guided by a deep sense of environmental responsibility. Embracing scrap-based production through electric arc furnaces — one of the most environment-friendly methods — the company promotes waste-to-value creation and a closed-loop recycling system.",
            "awardsAndRatings": [{"name": "LEED v4.1 O+M: Platinum (Stainless Centre Gurgaon) & Gold (JSL Jajpur clubhouse)", "score": "Platinum / Gold", "year": "2025"}],
            "nonCompliance": [{"description": "Zero human rights violations and zero cybersecurity breaches reported.", "resolution": "Nil"}],
            "forwardLooking": [
                {"description": "Develop science-based targets for Nature (SBTn)", "timeline": "Not explicitly stated"},
                {"description": "Assess 100% of suppliers on ESG criteria", "timeline": "Ongoing"},
            ],
            "qualitativePolicies": {
                "P1_ethics": "Implements Anti-Bribery & Anti-Corruption Policy and rigorous Supplier Code of Conduct, evaluating partners across all 9 BRSR principles.",
                "P3_ohs": "Occupational Health and Safety Policy under ISO 45001:2018. Achieved LTIFR of 0 for employees and contractors in FY2025.",
                "P6_environment": "Supported by Climate Change, Water Management, and Biodiversity policies. Implements ZLD and sources 72.11% recycled scrap for production.",
            },
            "steelProduction": {"value": 2_430_000, "unit": "metric tonnes", "note": "From plan config."},
            "reportingBoundary": "Standalone.",
        },
    },
}

for company_id, years_data in ENRICHMENT_DATA.items():
    for year, enrichment in years_data.items():
        out = {
            "companyId": company_id,
            "year": year,
            "source": "PDF",
            "enrichment": enrichment,
        }
        path = ENRICHMENT_DIR / f"{company_id}-{year}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(out, f, indent=2, ensure_ascii=False)
        print(f"  Written {path.name}")

print("\n=== Done ===")
print("Next step: re-run validate.py and review updated counts.")
