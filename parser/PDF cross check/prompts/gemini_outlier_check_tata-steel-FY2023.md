# BRSR XBRL Outlier Verification
# Company: Tata Steel Limited
# Year: FY2023 (April 2022 - March 2023)
# PDF to upload: "TATA STEEL FY23.pdf"
# Also read: gemini_outlier_check_COMMON_INSTRUCTIONS.md (paste that first, then this)

---

## Company context

- **Reporting basis:** CONSOLIDATED (includes Tata Steel Netherlands, Tata Steel UK, and all Indian subsidiaries)
- **Crude steel production this year:** 28,180,000 MT
- **Sector:** Integrated carbon steel (blast furnace - basic oxygen furnace)

> **Important:** FY2023 is Consolidated. Tata Steel absolute volumes (water, waste, energy) are legitimately larger than standalone peers because they include European plants. Flag only if values seem wrong even after accounting for consolidated scope.

---

## Checklist

Verify every item below. Do not skip any item. For each, find the value in the PDF and give a verdict.

### Section A - Peer outliers

Our value is compared to the median of the other 3 companies for the same metric and same year.

**ITEM_1**
- Tag: `BioMedicalWaste`
- Metric: Biomedical Waste Generated
- Our normalized value: **180 metric tonnes**
- Peer comparison: 243.2x higher than peer median of 0.74 metric tonnes
- Suspected cause: check reporting basis: FY2023 = consolidated (includes overseas ops), FY2024+ = standalone
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_2**
- Tag: `EWaste`
- Metric: E-Waste Generated
- Our normalized value: **765 metric tonnes**
- Peer comparison: 18.4x higher than peer median of 41.5 metric tonnes
- Suspected cause: check reporting basis: FY2023 = consolidated (includes overseas ops), FY2024+ = standalone
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_3**
- Tag: `EnergyConsumptionThroughOtherSources`
- Metric: Energy Consumption Through Other Sources
- Our normalized value: **2.8e+07 GJ**
- Raw value in PDF/XBRL: 28 petajoules (we converted to GJ)
- Peer comparison: 30.6x higher than peer median of 9.16e+05 GJ
- Suspected cause: check reporting basis: FY2023 = consolidated (includes overseas ops), FY2024+ = standalone
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_4**
- Tag: `TotalElectricityConsumptionFromNonRenewableSources`
- Metric: Non Renewable Electricity Consumption Volume
- Our normalized value: **6.6e+07 GJ**
- Raw value in PDF/XBRL: 66 petajoules (we converted to GJ)
- Peer comparison: 5.9x higher than peer median of 1.122e+07 GJ
- Suspected cause: check reporting basis: FY2023 = consolidated (includes overseas ops), FY2024+ = standalone
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_5**
- Tag: `OtherHazardousWaste`
- Metric: Other Hazardous Waste
- Our normalized value: **1.20016e+06 metric tonnes**
- Peer comparison: 8.8x higher than peer median of 1.36e+05 metric tonnes
- Suspected cause: check reporting basis: FY2023 = consolidated (includes overseas ops), FY2024+ = standalone
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_6**
- Tag: `PercentageOfCapex`
- Metric: Percentage Of Capex
- Our normalized value: **23 %**
- Peer comparison: 14.6x higher than peer median of 1.575 %
- Suspected cause: check reporting basis: FY2023 = consolidated (includes overseas ops), FY2024+ = standalone
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_7**
- Tag: `PercentageOfRAndD`
- Metric: Percentage Of R&D
- Our normalized value: **100 %**
- Peer comparison: 11.1x higher than peer median of 9.02 %
- Suspected cause: check reporting basis: FY2023 = consolidated (includes overseas ops), FY2024+ = standalone
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_8**
- Tag: `PlasticWaste`
- Metric: Plastic Waste
- Our normalized value: **19,398 metric tonnes**
- Peer comparison: 24.1x higher than peer median of 804 metric tonnes
- Suspected cause: check reporting basis: FY2023 = consolidated (includes overseas ops), FY2024+ = standalone
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_9**
- Tag: `WhatPercentageOfTotalProcurementByValueDoesItConstitute`
- Metric: Procurement Value Percentage Share
- Our normalized value: **0.7 %**
- Peer comparison: 50.0x lower than peer median of 33 %
- Suspected cause: check reporting basis: FY2023 = consolidated (includes overseas ops), FY2024+ = standalone
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_10**
- Tag: `RecyclingAndOrSafeDisposalAsAPercentageToTotalTurnover`
- Metric: Recycling Cost To Turnover
- Our normalized value: **19 %**
- Peer comparison: 5.3x lower than peer median of 100 %
- Suspected cause: check reporting basis: FY2023 = consolidated (includes overseas ops), FY2024+ = standalone
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_11**
- Tag: `TotalElectricityConsumptionFromRenewableSources`
- Metric: Renewable Electricity Consumption Volume
- Our normalized value: **1e+06 GJ**
- Raw value in PDF/XBRL: 1 petajoules (we converted to GJ)
- Peer comparison: 7.9x higher than peer median of 1.272e+05 GJ
- Suspected cause: check reporting basis: FY2023 = consolidated (includes overseas ops), FY2024+ = standalone
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_12**
- Tag: `SafeAndResponsibleUsageAsAPercentageToTotalTurnover`
- Metric: Safe Usage Information Turnover Percentage
- Our normalized value: **13 %**
- Peer comparison: 7.7x lower than peer median of 100 %
- Suspected cause: check reporting basis: FY2023 = consolidated (includes overseas ops), FY2024+ = standalone
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_13**
- Tag: `TotalScope3EmissionsPerRupeeOfTurnover`
- Metric: Scope 3 Emissions Per Turnover
- Our normalized value: **5.4e-06 ?**
- Peer comparison: vs peer median of 27.1 ? (our value is near zero)
- Suspected cause: likely unit mismatch: check if company reported in million tonnes vs tonnes
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_14**
- Tag: `PercentageOfDirectlySourcedFromMSMEsOrSmallProducers`
- Metric: Sourcing From MSMEs
- Our normalized value: **32 %**
- Peer comparison: 6.4x higher than peer median of 5 %
- Suspected cause: check reporting basis: FY2023 = consolidated (includes overseas ops), FY2024+ = standalone
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_15**
- Tag: `TotalElectricityConsumption`
- Metric: Total Electricity Consumption Volume
- Our normalized value: **6.7e+07 GJ**
- Raw value in PDF/XBRL: 67 petajoules (we converted to GJ)
- Peer comparison: 5.3x higher than peer median of 1.265e+07 GJ
- Suspected cause: check reporting basis: FY2023 = consolidated (includes overseas ops), FY2024+ = standalone
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_16**
- Tag: `TotalEnergyConsumedFromRenewableSources`
- Metric: Total Renewable Energy Consumption
- Our normalized value: **1e+06 GJ**
- Raw value in PDF/XBRL: 1 petajoules (we converted to GJ)
- Peer comparison: 7.9x higher than peer median of 1.272e+05 GJ
- Suspected cause: check reporting basis: FY2023 = consolidated (includes overseas ops), FY2024+ = standalone
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_17**
- Tag: `TotalWaterDischargedInKilolitres`
- Metric: Total Water Discharged Volume
- Our normalized value: **2.55997e+08 kL**
- Raw value in PDF/XBRL: 255997345 kilolitres (we converted to kL)
- Peer comparison: 22.9x higher than peer median of 1.118e+07 kL
- Suspected cause: check reporting basis: FY2023 = consolidated (includes overseas ops), FY2024+ = standalone
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_18**
- Tag: `WasteDisposedByIncineration`
- Metric: Waste Disposed Incineration Volume
- Our normalized value: **11,682 metric tonnes**
- Peer comparison: 333.8x higher than peer median of 35 metric tonnes
- Suspected cause: check reporting basis: FY2023 = consolidated (includes overseas ops), FY2024+ = standalone
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_19**
- Tag: `WasteDisposedByOtherDisposalOperations`
- Metric: Waste Other Disposal Volume
- Our normalized value: **1,156 metric tonnes**
- Peer comparison: vs peer median of 3.832e+05 metric tonnes (our value is near zero)
- Suspected cause: check reporting basis: FY2023 = consolidated (includes overseas ops), FY2024+ = standalone
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_20**
- Tag: `WasteRecoveredThroughReUsed`
- Metric: Waste Recovered Through Reuse
- Our normalized value: **8.53485e+06 metric tonnes**
- Peer comparison: 96.2x higher than peer median of 8.875e+04 metric tonnes
- Suspected cause: check reporting basis: FY2023 = consolidated (includes overseas ops), FY2024+ = standalone
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_21**
- Tag: `WaterWithdrawalByGroundwater`
- Metric: Water Withdrawal From Groundwater
- Our normalized value: **1.68701e+07 kL**
- Raw value in PDF/XBRL: 16870056 kilolitres (we converted to kL)
- Peer comparison: 1320.3x higher than peer median of 1.278e+04 kL
- Suspected cause: possible unit mismatch: check kL vs ML or mÂ³ vs kL
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_22**
- Tag: `WaterWithdrawalByThirdPartyWater`
- Metric: Water Withdrawal Third Party
- Our normalized value: **1.93591e+07 kL**
- Raw value in PDF/XBRL: 19359133 kilolitres (we converted to kL)
- Peer comparison: 358.5x higher than peer median of 5.4e+04 kL
- Suspected cause: possible unit mismatch: check kL vs ML or mÂ³ vs kL
- Task: Find this metric in the PDF and confirm or correct the value.

### Section D - Training coverage

**ITEM_23**
- Issue: Training coverage % is absent from XBRL for ALL companies in ALL years. Must be extracted from PDF.
- Look in: Principle 3 training tables, HR metrics, workforce development section, "Training and Awareness Programs"
- Extract all of the following that are present:
  - % permanent employees trained on health and safety
  - % permanent employees trained on skill upgradation
  - % permanent workers trained on health and safety
  - % permanent workers trained on skill upgradation
  - Average training hours per employee
  - Total training person-hours
- If the training table reports number trained rather than %, also provide the denominator (total headcount) so % can be calculated.

---

## Required output

Respond with exactly 23 lines. Use this format from COMMON_INSTRUCTIONS.md:

```
ITEM_1 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_2 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_3 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_4 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_5 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_6 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_7 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_8 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_9 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_10 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_11 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_12 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_13 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_14 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_15 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_16 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_17 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_18 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_19 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_20 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_21 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_22 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_23 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
```

Verdicts: CONFIRMED / CORRECTED / UNIT_ERROR / EXPECTED / NOT_FOUND / ZERO_REPORTED
For CORRECTED and UNIT_ERROR: always write the correct value AND its unit in PDF_VALUE.
For the training item: use FOUND / NOT_FOUND / NOT_REPORTED, and list all values found in PDF_VALUE.