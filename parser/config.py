# parser/config.py
# Central configuration for the BRSR benchmark parser.
# All constants referenced by parse_xbrl.py, normalize.py, and run_all.py live here.
# Do NOT edit generated output files (dashboard/src/data/) by hand — re-run the parser.

from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

ROOT_DIR = Path(__file__).parent.parent          # repo root
XBRL_DIR = ROOT_DIR / "XBRL"
OUTPUT_DIR = ROOT_DIR / "dashboard" / "src" / "data"

# ---------------------------------------------------------------------------
# Company registry
# To add a new company: add an entry here, drop XMLs in XBRL/{folder}/, run run_all.py
# ---------------------------------------------------------------------------

COMPANIES = {
    "tata-steel":       {"name": "Tata Steel Limited",      "folder": "TATA STEEL",       "sector": "Integrated Steel"},
    "jsw-steel":        {"name": "JSW Steel Limited",        "folder": "JSW STEEL",        "sector": "Integrated Steel"},
    "sail":             {"name": "SAIL",                     "folder": "SAIL",             "sector": "Integrated Steel"},
    "jindal-stainless": {"name": "Jindal Stainless Limited", "folder": "JINDAL STAINLESS", "sector": "Stainless Steel"},
}

# ---------------------------------------------------------------------------
# Crude steel production volumes (metric tonnes)
# Used as physical output denominator for intensity metrics and to normalise
# JSW air emissions which are reported per tonne of crude steel (kg/tcs).
# Source: Integrated/Annual Reports as noted next to each value.
# Tata Steel FY2023: Consolidated basis — matches the XBRL filing basis.
# ---------------------------------------------------------------------------

STEEL_PRODUCTION_TONNES = {
    "tata-steel": {
        "FY2023": 28_180_000,   # Consolidated (matches XBRL consolidated filing)
        "FY2024": 20_120_000,   # Standalone (India only)
        "FY2025": 21_710_000,   # Standalone (India only)
    },
    "jsw-steel": {
        "FY2023": 24_150_000,   # Source: Integrated Report 2022-23
        "FY2024": 26_430_000,   # Source: Integrated Annual Report 2023-24
        "FY2025": 27_790_000,   # Source: Integrated Annual Report 2024-25
    },
    "sail": {
        "FY2023": 18_290_000,   # Source: Annual Report 2022-23
        "FY2024": 19_240_000,   # Source: Annual Report 2023-24
        "FY2025": 19_170_000,   # Source: PIB/FY25 Financial Performance Release
    },
    "jindal-stainless": {
        "FY2023":  1_710_000,   # Stainless steel; Source: Annual Report 2022-23
        "FY2024":  2_080_000,   # Source: Integrated Annual Report 2023-24
        "FY2025":  2_430_000,   # Source: Integrated Report 2024-25 / Env. Statement
    },
}

# ---------------------------------------------------------------------------
# XBRL namespace versions
# Key = URI segment that appears in xmlns:in-capmkt attribute on the root element
# ---------------------------------------------------------------------------

NAMESPACE_VERSIONS = {
    "2021-09-30": "v1",   # FY22-23 early filers (Tata, JSW)
    "2023-06-30": "v2",   # FY22-23 late filers (SAIL, Jindal)
    "2024-04-30": "v3",   # FY23-24 all companies
    "2025-05-31": "v4",   # FY24-25 all companies
}

XBRL_INSTANCE_NS = "http://www.xbrl.org/2003/instance"
XBRL_DI_NS       = "http://xbrl.org/2006/xbrldi"

def entity_ns(version_key: str) -> str:
    """Return the entity namespace URI for a given namespace version key."""
    return f"https://www.sebi.gov.in/xbrl/BRSR/{version_key}/in-capmkt/in-capmkt-ent"

def capmkt_ns(version_key: str) -> str:
    """Return the capmkt namespace URI for a given namespace version key."""
    return f"https://www.sebi.gov.in/xbrl/{version_key}/in-capmkt"

# ---------------------------------------------------------------------------
# Excluded tags (67 confirmed by user — do not re-derive)
# Group A: Company identity  |  Group B: Period metadata
# Group C: Web links         |  Group D: XBRL domain/scaffolding labels
# Group E: Calculation inputs (Amount* ratio denominators/numerators — not standalone metrics)
# ---------------------------------------------------------------------------

EXCLUDED_TAGS = {
    # Group A — Company Identity (12)
    "AddressOfCorporateOfficeOfCompany",
    "AddressOfRegisteredOfficeOfCompany",
    "ContactNumberOfContactPerson",
    "CorporateIdentityNumber",
    "EMailOfContactPerson",
    "EMailOfTheCompany",
    "NameOfContactPerson",
    "NameOfStockExchangeWhereTheCompanyIsListed",
    "NameOfTheCompany",
    "TelephoneOfCompany",
    "WebsiteOfCompany",
    "YearOfIncorporation",
    # Group B — Period Metadata (6)
    "DateOfEndOfFinancialYear",
    "DateOfEndOfPreviousYear",
    "DateOfEndOfPriorToPreviousYear",
    "DateOfStartOfFinancialYear",
    "DateOfStartOfPreviousYear",
    "DateOfStartOfPriorToPreviousYear",
    # Group C — Web Links only (boolean policy-existence tags ARE retained) (11)
    "DisclosureWebLinkOfEntityAtWhichBusinessContinuityAndDisasterManagementPlanIsPlaced",
    "WebLinkAtAntiCorruptionOrAntiBriberyPolicyIsPlace",
    "WebLinkForDetailsOfIntiativeTakenByEntity",
    "WebLinkForGrievanceRedressPolicy",
    "WebLinkOfEqualOppertunityPolicyTextBlock",
    "WebLinkOfResultsOfLifeCycleAssessments",
    "WebLinkOfResultsOfLifeCycleAssessmentsP6",
    "WebLinkOfThePoliciesExplanatoryTextBlock",
    "WebLinkOfThePolicyOnCyberSecurityAndRisksRelatedToDataPrivacy",
    "WebLinkPublicPolicyPositionAdvocated",
    "WeblinkWhereInformationOnProductsAndServicesOfTheEntityCanBeAccessedExplanatoryTextBlock",
    # Group D — XBRL Domain Labels / Schema Scaffolding (19)
    "AwarenessProgrammesConductedForValueChainPartnersDomain",
    "CSRProjectsDomain",
    "CSRProjectsUndertakenDomain",
    "DetailsOfBusinessActivitiesAccountingForNinetyPercentOfTheTurnoverDomain",
    "EnergyConsumptionThroughOtherSourceFromNonRenewableSourcesDomain",
    "EntitysMaterialResponsibleBusinessConductIssuesDomain",
    "EnvironmentalImpactAssessmentsOfProjectDomain",
    "FacilityOrPlantLocatedInAreasOfWaterStressDomain",
    "HoldingSubsidiaryAssociateCompaniesAndJointVenturesDomain",
    "OperationsOrOfficesWhereEnvironmentalApprovalsOrClearancesRequiredDomain",
    "OtherAssessmentsDomain",
    "ProductsOrServicesSoldByTheEntityAccountingForNinetyPercentOfTheTurnoverDomain",
    "ProjectsForRehabilitationAndResettlementDomain",
    "PublicPolicyDomain",
    "ReclaimedProductsAndTheirPackagingDomain",
    "RecycledOrReusedInputMaterialUsedInProductionOrProvidingServicesDomain",
    "SpecificInitiativesDomain",
    "StakeHolderGroupsDomain",
    "TheEntityConductedLifeCyclePerspectiveOrAssessmentsDomain",
    # Group E — Calculation Inputs (19)
    # These are ratio numerators/denominators used to compute % or days metrics.
    # The derived metric (%, days) is displayed — not the absolute amount input.
    # Exception: TotalRevenueOfTheCompany / RevenueFromOperations / Turnover are kept (standalone size metrics).
    "AmountOfAccountsPayableDuringTheYear",
    "AmountOfCostIncurredOnWellBeingMeasures",
    "AmountOfInvestmentsInRelatedParties",
    "AmountOfLoansAndAdvancesGivenToRelatedParties",
    "AmountOfPurchasesFromRelatedParties",
    "AmountOfPurchasesFromTopTenTradingHouses",
    "AmountOfPurchasesFromTradingHouses",
    "AmountOfSalesToDealersOrDistributors",
    "AmountOfSalesToRelatedParties",
    "AmountOfSalesToTopTenDealersOrDistributors",
    "AmountOfTotalInvestments",
    "AmountOfTotalLoansAndAdvances",
    "AmountOfTotalPurchases",
    "AmountOfTotalPurchasesForShareOfRelatedPartyTransactions",
    "AmountOfTotalPurchasesFromTradingHouses",
    "AmountOfTotalSales",
    "AmountOfTotalSalesForShareOfRelatedPartyTransactions",
    "AmountOfTotalSalesToDealersOrDistributors",
    "CostOfGoodsOrServicesProcuredDuringTheYear",
}

# ---------------------------------------------------------------------------
# Tag aliases: maps old v1/v2 tag names to canonical v3/v4 names.
# When a v1/v2 tag is encountered, it is stored under the canonical name.
# NOTE: This is a partial list — Gemini Pro will generate the complete alias
#       map by diffing all 4 namespace schema tag lists. Claude must review
#       that output before committing additional entries here.
# ---------------------------------------------------------------------------

TAG_ALIASES = {
    # v1/v2 → canonical (v3/v4)
    "TotalEnergyConsumption":                           "TotalEnergyConsumedFromRenewableAndNonRenewableSources",
    "TotalScope1AndScope2EmissionsPerRupeeOfTurnover":  "TotalScope1AndScope2EmissionsIntensityPerRupeeOfTurnover",
    "TotalScope1AndScope2EmissionIntensity":            "TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput",
}

# ---------------------------------------------------------------------------
# Unit normalization: standard target units per metric category
# ---------------------------------------------------------------------------

STANDARD_UNITS = {
    "ghg":    "tCO2e",          # GHG emissions — SEBI BRSR Template P6-E4
    "energy": "GJ",             # Energy — SEBI: "Joules or multiples"; Tata Steel reference = PJ, GJ used for granularity
    "water":  "kL",             # Water — SEBI BRSR Template P6-E2
    "waste":  "metric tonnes",  # Waste — SEBI BRSR Template P6-E5
    "air":    "kilotonnes",     # Air emissions — SEBI silent; Tata Steel reference
    "currency": "INR Crore",    # Financial — SEBI convention
}

# Unit conversion table: normalised lower-case key → multiplier to reach standard unit
# GHG → tCO2e | Energy → GJ | Water → kL | Waste → metric tonnes | Air → kilotonnes
UNIT_CONVERSIONS: dict[str, float] = {
    # ---------- GHG emissions → tCO2e ----------
    "million tonnes of co2 equivalent":      1_000_000.0,
    "million tonnes co2 equivalent":         1_000_000.0,
    "million tco2e":                         1_000_000.0,
    "million tonnes":                        1_000_000.0,   # contextual — only used for GHG tags
    "metric tonnes of co2 equivalent":       1.0,
    "metric tonnes":                         1.0,           # contextual — only for GHG tags
    "tonnes of co2":                         1.0,
    "tonnes of co2 equivalent":              1.0,
    "tco2e":                                 1.0,
    "tco2":                                  1.0,
    "t co2e":                                1.0,
    "kg co2e":                               0.001,
    "kg co2 equivalent":                     0.001,
    # ---------- Energy → GJ ----------
    "petajoules":                            1_000_000.0,
    "pj":                                    1_000_000.0,
    "terajoules":                            1_000.0,
    "tj":                                    1_000.0,
    "gigajoules":                            1.0,
    "gj":                                    1.0,
    "mwh":                                   3.6,
    "kwh":                                   0.0036,
    "gkcal":                                 4.1868,        # gigakilocalories → GJ
    "mkwh":                                  3_600.0,       # megawatt-hours → GJ  (1 MWh = 3.6 GJ; 1000 MWh → 3600 GJ)
    # ---------- Water → kL ----------
    "kilolitres":                            1.0,
    "kl":                                    1.0,
    "kiloliters":                            1.0,
    "cubic metres":                          1.0,           # 1 m³ = 1 kL
    "cubic meter":                           1.0,
    "m3":                                    1.0,
    "million litres":                        1_000.0,
    "million liters":                        1_000.0,
    "ml":                                    0.001,         # millilitres → kL  (rare; context check needed)
    # ---------- Waste → metric tonnes ----------
    "metric tonnes":                         1.0,
    "mt":                                    1.0,
    "tonnes":                                1.0,
    "metric ton":                            1.0,
    "kg":                                    0.001,
    # ---------- Air emissions → kilotonnes ----------
    "kilotonnes/year":                       1.0,
    "kilotonnes":                            1.0,
    "kt":                                    1.0,
    # kg for air emissions → kilotonnes (÷ 1,000,000).
    # Used for JSW NOx/SOx/PM FY2024/FY2025 which store absolute kg in XBRL.
    # Key is disambiguated from waste "kg" (→ metric tonnes) by using "kg (air)".
    # normalize.py uses this key specifically for air emission tags.
    "kg (air)":                              0.000001,
    # Metric tonnes / tonnes for air emissions → kilotonnes (÷ 1,000).
    # Used for Jindal Stainless NOx/SOx/PM which report in metric tonnes ("MT").
    # Disambiguated from waste "metric tonnes" (→ 1.0) by using "(air)" suffix.
    # normalize.py remaps "mt"/"tonnes"/"metric tonnes" to these keys for air emission tags.
    "mt (air)":                              0.001,
    "tonnes (air)":                          0.001,
    "metric tonnes (air)":                   0.001,
}

# ---------------------------------------------------------------------------
# PDF-sourced value patches
# Applied BEFORE normalization. Override the raw XBRL value where the XBRL filing
# contains a confirmed error, cross-checked against the company's BRSR PDF.
#
# Structure: { company_id: { fiscal_year: { tag: { "rawValue", "rawUnit", "source" } } } }
# "rawValue" and "rawUnit" are the corrected values in original reporting units.
# normalize.py applies unit conversion as normal after the patch.
# ---------------------------------------------------------------------------

XBRL_VALUE_PATCHES: dict[str, dict[str, dict[str, dict]]] = {
    "jsw-steel": {
        "FY2025": {
            # XBRL FY2025 SOx = 3,730,667 kg (3.73 kt) — confirmed filing error.
            # PDF (JSW BRSR FY2024-25, P6 table) shows SOx = 1.66 Kg/tcs, same as FY2024.
            # FY2024 XBRL raw = 36,211,092 kg (36.2 kt); PDF FY2024 = 1.66 kg/tcs × 26.43M t = 43.9 kt.
            # FY2025 PDF-derived absolute: 1.66 kg/tcs × 27,790,000 t = 46,131,400 kg.
            # Pattern check: NOx and PM FY2025 XBRL are ~81% of PDF estimate (consistent with FY2024 ~83%).
            # SOx FY2025 XBRL is ~8% of expected — clear magnitude error in JSW's XBRL submission.
            "SOx": {
                "rawValue": "46131400",
                "rawUnit":  "kg",
                "source":   "JSW BRSR FY2024-25 PDF: SOx = 1.66 Kg/tcs × 27,790,000 t production",
            },
        },
    },
}

# Tags where the unit is kg/tcs (per tonne crude steel) — needs production volume to convert to absolute kt
# These are set to normalized=False with a specific unitWarning until production volume allows conversion.
UNIT_REQUIRES_PRODUCTION_VOLUME = {
    "kg/tcs",
    "kg/tcs/year",
    "kg per tonne of crude steel",
    "kg per tcs",
}

# Tags where the unit is a concentration (µg/m³) — PERMANENTLY non-normalizable to mass.
# These will always be normalized=False with unitWarning="concentration unit; incomparable to mass"
UNIT_IS_CONCENTRATION = {
    "µg/m3",
    "ug/m3",
    "µg/m³",
    "micrograms per cubic metre",
    "micrograms per cubic meter",
}

# Tags that are known to report nil/zero values as text (e.g. "Nil", "-", "0")
# These are treated as numeric zero, not as text values.
# Text strings that indicate "not applicable" / "none" (but NOT "0" — zero is a real value).
# When a company writes any of these in a field, value → null and valueStatus → "nil_reported".
# This is distinct from:
#   - value=0 (company wrote "0" or a numeric zero — genuine zero)
#   - value=null + valueStatus="blank" (field was empty — not reported at all)
NIL_TEXT_VALUES = {"nil", "n.a.", "na", "n/a", "-", "not applicable", "not applicable.", "none"}

# ---------------------------------------------------------------------------
# SEBI-mandated units: applied universally to all companies/years when no
# explicit unit tag is present, based on tag name patterns.
# These override KNOWN_UNITS_FALLBACK when the tag matches.
# Reference: SEBI BRSR Core Template (P6 tables).
# ---------------------------------------------------------------------------

# Pattern → standard unit string (lowercase, for UNIT_CONVERSIONS lookup)
# Applied when tag_lower contains the key pattern
SEBI_MANDATED_UNIT_PATTERNS: list[tuple[str, str]] = [
    # Water → kilolitres (SEBI BRSR P6-E2)
    ("water",           "kilolitres"),
    ("withdrawal",      "kilolitres"),
    ("waterconsumption","kilolitres"),
    ("waterdischarge",  "kilolitres"),
    # Waste → metric tonnes (SEBI BRSR P6-E5)
    ("waste",           "metric tonnes"),
    ("biomedical",      "metric tonnes"),
    ("ewaste",          "metric tonnes"),
    ("plasticwaste",    "metric tonnes"),
    ("batterywaste",    "metric tonnes"),
    ("constructionanddemo", "metric tonnes"),
    ("hazardouswaste",  "metric tonnes"),
    ("nonhazardous",    "metric tonnes"),
]

# ---------------------------------------------------------------------------
# Data type inference: tag name patterns → DataType
# Used in normalize.py to classify each indicator for display type selection.
# ---------------------------------------------------------------------------

# Tags whose local name contains any of these substrings → boolean
BOOLEAN_TAG_PATTERNS = (
    "DoesTheEntity", "IsThe", "HasThe", "WhetherThe",
    "Policy", "Mechanism", "System", "Programme",
    "Implemented", "Conducted", "Established",
)

# Tags whose local name contains any of these substrings → percentage
PERCENTAGE_TAG_PATTERNS = (
    "Percentage", "Percent", "Rate", "Ratio", "Coverage",
    "LostTimeInjuryFrequencyRate", "Frequency",
)

# Tags whose local name contains any of these substrings → intensity metric
INTENSITY_TAG_PATTERNS = (
    "PerRupee", "PerTonne", "Intensity", "PerUnit",
    "PerKilowatt", "PerEmployee",
)

# ---------------------------------------------------------------------------
# Known units per company for FY24/FY25 fallback
# v3/v4 XBRL files have no UnitOf* tags at all. The parser builds this map
# dynamically from FY23 unit tags (v1/v2 files). The entries below are
# pre-seeded from manual inspection as a safety net if FY23 parsing fails.
# Assumption: companies did not change reporting units in FY24/FY25.
# Verify against BRSR PDFs during Phase 4.
# ---------------------------------------------------------------------------

KNOWN_UNITS_FALLBACK: dict[str, dict[str, str]] = {
    "tata-steel": {
        # Air emissions (v1/v2 tag names: Nox/Sox; v3/v4: NOx/SOx)
        "Nox":                    "kilotonnes/year",
        "NOx":                    "kilotonnes/year",
        "Sox":                    "kilotonnes/year",
        "SOx":                    "kilotonnes/year",
        "ParticulateMatter":      "kilotonnes/year",
        "TotalScope1Emissions":   "million tonnes of co2 equivalent",
        "TotalScope2Emissions":   "million tonnes co2 equivalent",
        "TotalScope3Emissions":   "million tonnes of co2 equivalent",
        # Energy: FY2023 (v1, consolidated) reported in PJ — raw 857 PJ.
        # Cross-check: 857 PJ / 28.18 MnT ≈ 30.4 GJ/t (plausible for consolidated ops).
        # FY2024/FY2025 switched to GJ (see KNOWN_UNITS_V3V4_OVERRIDE below).
        # This fallback applies to v1/v2 files (FY2023) only; v3/v4 uses the override.
        "TotalEnergyConsumedFromRenewableAndNonRenewableSources":      "petajoules",
        "TotalEnergyConsumedFromRenewableSources":                     "petajoules",
        "TotalEnergyConsumedFromNonRenewableSources":                  "petajoules",
        "TotalElectricityConsumption":                                 "petajoules",
        "TotalElectricityConsumptionFromRenewableSources":             "petajoules",
        "TotalElectricityConsumptionFromNonRenewableSources":          "petajoules",
        "TotalFuelConsumption":                                        "petajoules",
        "TotalFuelConsumptionFromNonRenewableSources":                 "petajoules",
        "EnergyConsumptionThroughOtherSources":                        "petajoules",
        "EnergyConsumptionThroughOtherSourcesFromNonRenewableSources": "petajoules",
        # Renewable subcomponents confirmed from user (PDF cross-check):
        # FY23=1 PJ, FY24=0.12 PJ, FY25=0.38 PJ for TotalFuelConsumptionFromRenewableSources
        "TotalFuelConsumptionFromRenewableSources":                    "petajoules",
        "EnergyConsumptionThroughOtherSourcesFromRenewableSources":    "petajoules",
    },
    "jsw-steel": {
        # NOTE on air emissions: JSW FY2023 (v1 schema) reported Nox/Sox/PM as intensity
        # metrics in kg/tcs. In FY2024/2025 (v3/v4 schema), tag was renamed NOx/SOx and
        # value scale changed dramatically (FY23: 1.19 → FY24: 25,797,403), indicating a
        # switch to absolute mass reporting. FY24/FY25 unit is UNKNOWN.
        # No fallback for Nox/Sox/ParticulateMatter (v1 names): v1 files have explicit
        # unit tags so fallback is never reached; v3/v4 files are cache-blocked and must
        # flag "unit unknown" until PDF verification (see UNIT_CHANGED_IN_V3V4 below).
        # NOx/SOx/ParticulateMatter (v3/v4 names) intentionally NOT in fallback:
        "TotalScope1Emissions":   "metric tonnes",
        "TotalScope2Emissions":   "metric tonnes",
        "TotalScope3Emissions":   "tonnes of co2",
        "TotalEnergyConsumedFromRenewableAndNonRenewableSources":      "gigajoules",
        "TotalEnergyConsumedFromRenewableSources":                     "gigajoules",
        "TotalEnergyConsumedFromNonRenewableSources":                  "gigajoules",
        "TotalElectricityConsumption":                                 "gigajoules",
        "TotalElectricityConsumptionFromRenewableSources":             "gigajoules",
        "TotalElectricityConsumptionFromNonRenewableSources":          "gigajoules",
        "TotalFuelConsumption":                                        "gigajoules",
        "TotalFuelConsumptionFromNonRenewableSources":                 "gigajoules",
        "EnergyConsumptionThroughOtherSources":                        "gigajoules",
        "EnergyConsumptionThroughOtherSourcesFromNonRenewableSources": "gigajoules",
        "TotalFuelConsumptionFromRenewableSources":                    "gigajoules",
        "EnergyConsumptionThroughOtherSourcesFromRenewableSources":    "gigajoules",
    },
    "sail": {
        "Nox":                    "µg/m3",           # concentration — permanently non-normalizable
        "NOx":                    "µg/m3",
        "Sox":                    "µg/m3",
        "SOx":                    "µg/m3",
        "ParticulateMatter":      "µg/m3",
        "TotalScope1Emissions":   "tonnes of co2",
        "TotalScope2Emissions":   "tonnes of co2",
        "TotalScope3Emissions":   "tonnes of co2",   # no unit tag in FY23; inferred from Scope1/2 unit
        # SAIL reports energy in Terajoules (TJ), NOT gigajoules.
        # Confirmed by user from SAIL FY2023 BRSR PDF: total energy = 5,91,044 TJ (Indian lakh notation).
        # 591,044 TJ × 1,000 = 591,044,000 GJ → ~32.3 GJ/tonne for 18.29M tonne output (plausible for old BF ops).
        # The XBRL unit tag (v2) said "gigajoules" — incorrect. Overriding with terajoules here.
        "TotalEnergyConsumedFromRenewableAndNonRenewableSources":      "terajoules",
        "TotalEnergyConsumedFromRenewableSources":                     "terajoules",
        "TotalEnergyConsumedFromNonRenewableSources":                  "terajoules",
        "TotalElectricityConsumption":                                 "terajoules",
        "TotalElectricityConsumptionFromRenewableSources":             "terajoules",
        "TotalElectricityConsumptionFromNonRenewableSources":          "terajoules",
        "TotalFuelConsumption":                                        "terajoules",
        "TotalFuelConsumptionFromNonRenewableSources":                 "terajoules",
        "EnergyConsumptionThroughOtherSources":                        "terajoules",
        "EnergyConsumptionThroughOtherSourcesFromNonRenewableSources": "terajoules",
        "TotalFuelConsumptionFromRenewableSources":                    "terajoules",
        "EnergyConsumptionThroughOtherSourcesFromRenewableSources":    "terajoules",
    },
    "jindal-stainless": {
        "Nox":                    "mt",              # metric tonnes → converted to kilotonnes
        "NOx":                    "mt",
        "Sox":                    "mt",
        "SOx":                    "mt",
        "ParticulateMatter":      "mt",
        "TotalScope1Emissions":   "tco2e",
        "TotalScope2Emissions":   "tco2e",
        "TotalScope3Emissions":   "tco2e",          # inferred from Scope1/2 unit (UnitOfScope3 absent)
        "TotalEnergyConsumedFromRenewableAndNonRenewableSources":      "gigajoules",
        "TotalEnergyConsumedFromRenewableSources":                     "gigajoules",
        "TotalEnergyConsumedFromNonRenewableSources":                  "gigajoules",
        "TotalElectricityConsumption":                                 "gigajoules",
        "TotalElectricityConsumptionFromRenewableSources":             "gigajoules",
        "TotalElectricityConsumptionFromNonRenewableSources":          "gigajoules",
        "TotalFuelConsumption":                                        "gigajoules",
        "TotalFuelConsumptionFromNonRenewableSources":                 "gigajoules",
        "EnergyConsumptionThroughOtherSources":                        "gigajoules",
        "EnergyConsumptionThroughOtherSourcesFromNonRenewableSources": "gigajoules",
        "TotalFuelConsumptionFromRenewableSources":                    "gigajoules",
        "EnergyConsumptionThroughOtherSourcesFromRenewableSources":    "gigajoules",
    },
}

# ---------------------------------------------------------------------------
# Unit change registry: company+tag combinations where the reporting unit
# CHANGED between v1/v2 (FY2023) and v3/v4 (FY2024+).
# For these tags, the FY2023 unit cache MUST NOT be applied to FY2024/2025.
# They will be flagged as normalized=False + unitWarning for PDF verification.
# ---------------------------------------------------------------------------

_TATA_ENERGY_TAGS = {
    # Tata Steel FY2023 (v1, consolidated) reported energy in PJ.
    # FY2024/FY2025 (v3/v4) report in GJ — the FY23 cache (PJ) must not carry forward.
    # KNOWN_UNITS_FALLBACK above has been updated to "gigajoules" for these tags,
    # which resolve_unit will use after the cache is blocked.
    "TotalEnergyConsumedFromRenewableAndNonRenewableSources",
    "TotalEnergyConsumedFromRenewableSources",
    "TotalEnergyConsumedFromNonRenewableSources",
    "TotalElectricityConsumption",
    "TotalElectricityConsumptionFromRenewableSources",
    "TotalElectricityConsumptionFromNonRenewableSources",
    "TotalFuelConsumption",
    "TotalFuelConsumptionFromNonRenewableSources",
    "EnergyConsumptionThroughOtherSources",
    "EnergyConsumptionThroughOtherSourcesFromNonRenewableSources",
}

UNIT_CHANGED_IN_V3V4: dict[str, set[str]] = {
    # Tata Steel: energy unit changed from PJ (v1/FY2023) to GJ (v3/v4 FY2024+).
    # Cache is blocked; KNOWN_UNITS_FALLBACK provides the correct "gigajoules" unit.
    "tata-steel": _TATA_ENERGY_TAGS,
    # JSW FY2023 reported Nox/Sox/ParticulateMatter as intensity (kg/tcs).
    # FY2024/2025 value scale (~25M vs ~1.19) confirms switch to absolute mass (likely kg).
    # Until PDF confirms the FY2024+ unit, these cannot be normalized.
    # (NOx/SOx intentionally absent from KNOWN_UNITS_FALLBACK for jsw-steel.)
    "jsw-steel": {"NOx", "SOx", "ParticulateMatter"},
}

# Versions considered v3/v4 (where unit reset applies)
V3V4_VERSIONS = {"v3", "v4"}

# ---------------------------------------------------------------------------
# Hard unit corrections: overrides the unit tag in the XBRL file itself.
# Use ONLY when the XBRL unit tag is confirmed wrong (e.g. file says "gigajoules"
# but the PDF and scale analysis confirm the values are actually in terajoules).
# These take priority over everything — file unit tag, cache, and fallback.
# Must have a PDF source or explicit user confirmation before adding entries here.
# ---------------------------------------------------------------------------

UNIT_CORRECTIONS: dict[str, dict[str, str]] = {
    "sail": {
        # SAIL FY2023 XBRL unit tag says "gigajoules" but values are in terajoules.
        # Confirmed by user from SAIL FY2023 BRSR PDF: total energy = 5,91,044 TJ.
        # 591,044 TJ × 1,000 = 591,044,000 GJ → 32.3 GJ/t (18.29M t output) — plausible.
        # If the PDF for FY2024/FY2025 also shows TJ, this applies to all years.
        # PDF verification required for FY2024/FY2025 (flagged in validate.py).
        "TotalEnergyConsumedFromRenewableAndNonRenewableSources":      "terajoules",
        "TotalEnergyConsumedFromRenewableSources":                     "terajoules",
        "TotalEnergyConsumedFromNonRenewableSources":                  "terajoules",
        "TotalElectricityConsumption":                                 "terajoules",
        "TotalElectricityConsumptionFromRenewableSources":             "terajoules",
        "TotalElectricityConsumptionFromNonRenewableSources":          "terajoules",
        "TotalFuelConsumption":                                        "terajoules",
        "TotalFuelConsumptionFromNonRenewableSources":                 "terajoules",
        "EnergyConsumptionThroughOtherSources":                        "terajoules",
        "EnergyConsumptionThroughOtherSourcesFromNonRenewableSources": "terajoules",
        "TotalFuelConsumptionFromRenewableSources":                    "terajoules",
        "EnergyConsumptionThroughOtherSourcesFromRenewableSources":    "terajoules",
    },
}

# ---------------------------------------------------------------------------
# Financial unit corrections: companies reporting financial values in absolute Rupees
# instead of SEBI convention (INR Crore). 1 Crore = 10,000,000 Rupees.
# Confirmed from PDFs: Tata Steel FY2024 BRSR shows revenue "Amount in ₹ crore" = 1,40,987
# but XBRL value = 1,409,874,287,726 (absolute Rupees). JSW has same pattern.
# SAIL and Jindal report in Crore natively (no correction needed).
# ---------------------------------------------------------------------------

FINANCIAL_UNIT_CORRECTION_FACTOR = 1 / 10_000_000  # absolute Rupees → INR Crore

# Tags that carry financial values (match if tag starts with "Amount" or contains these keywords)
FINANCIAL_TAG_PREFIXES = (
    "Amount", "Revenue", "Cost", "Wages", "Turnover", "Investment",
    "Purchases", "Sales", "Loans",
)

# Companies reporting financials in absolute Rupees (need ÷10^7 correction to get Crore)
FINANCIAL_RUPEE_COMPANIES = {"tata-steel", "jsw-steel"}

# ---------------------------------------------------------------------------
# v3/v4-specific unit overrides: the correct unit for a tag in v3/v4 schema
# when the v1/v2 fallback is wrong (unit changed between schema versions).
# Checked after cache is blocked; takes precedence over KNOWN_UNITS_FALLBACK
# for cache-blocked tags in v3/v4 files.
# ---------------------------------------------------------------------------

KNOWN_UNITS_V3V4_OVERRIDE: dict[str, dict[str, str]] = {
    "tata-steel": {
        # FY2024/FY2025 (v3/v4) switched from PJ to GJ for all energy reporting.
        # Cross-check: 545,962,401 GJ / 20.12 MnT = 27.1 GJ/t (FY2024) ✓
        #              587,567,890 GJ / 21.71 MnT = 27.1 GJ/t (FY2025) ✓
        "TotalEnergyConsumedFromRenewableAndNonRenewableSources":      "gigajoules",
        "TotalEnergyConsumedFromRenewableSources":                     "gigajoules",
        "TotalEnergyConsumedFromNonRenewableSources":                  "gigajoules",
        "TotalElectricityConsumption":                                 "gigajoules",
        "TotalElectricityConsumptionFromRenewableSources":             "gigajoules",
        "TotalElectricityConsumptionFromNonRenewableSources":          "gigajoules",
        "TotalFuelConsumption":                                        "gigajoules",
        "TotalFuelConsumptionFromNonRenewableSources":                 "gigajoules",
        "EnergyConsumptionThroughOtherSources":                        "gigajoules",
        "EnergyConsumptionThroughOtherSourcesFromNonRenewableSources": "gigajoules",
    },
    "jsw-steel": {
        # JSW FY2024/FY2025 XBRL raw values: NOx=25,797,403 / SOx=36,211,092 / PM=8,308,562
        # These are in kg (absolute mass). Converting to kilotonnes: 25,797,403 kg / 1,000,000 = 25.8 kt.
        # Cross-check: 25.8 kt NOx / 26.43 Mt production = 0.98 kg/tcs — consistent with PDF value 1.19 kg/tcs
        # (minor year-to-year variation acceptable).
        # The PDF shows 1.19 kg/tcs for DISPLAY but the XBRL stores the absolute kg value.
        # Standard conversion: kg → kilotonnes (÷ 1,000,000).
        "NOx":               "kg",
        "SOx":               "kg",
        "ParticulateMatter": "kg",
    },
}

# ---------------------------------------------------------------------------
# Validation thresholds (used by validate.py)
# ---------------------------------------------------------------------------

# Peer outlier: ratio threshold between companies of similar scale
PEER_OUTLIER_RATIO_LARGE = 5.0        # Tata / JSW / SAIL vs each other
PEER_OUTLIER_RATIO_JINDAL = 20.0      # Jindal vs large-cap trio (absolute metrics)
PEER_OUTLIER_RATIO_INTENSITY = 5.0    # Intensity metrics — same threshold regardless of company

# Self-outlier: YoY change threshold
YOY_CHANGE_THRESHOLD = 0.50           # flag if change > 50% year-over-year

# Consistency tolerance
ADDITIVE_TOLERANCE = 0.02             # ±2% for sum-of-parts checks

# Too-good-to-be-true thresholds
LTIFR_IMPLAUSIBLE_WORKFORCE_MIN = 5_000   # LTIFR=0 with workforce above this → flag
