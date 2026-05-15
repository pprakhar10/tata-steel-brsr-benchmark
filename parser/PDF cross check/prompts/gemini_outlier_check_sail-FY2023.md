# BRSR XBRL Outlier Verification
# Company: SAIL - Steel Authority of India Limited
# Year: FY2023 (April 2022 - March 2023)
# PDF to upload: "SAIL FY23.pdf"
# Also read: gemini_outlier_check_COMMON_INSTRUCTIONS.md (paste that first, then this)

---

## Company context

- **Reporting basis:** STANDALONE
- **Crude steel production this year:** 18,290,000 MT
- **Sector:** Integrated carbon steel (blast furnace - basic oxygen furnace), PSU

> **Note:** SAIL is a PSU. Air emissions FY2023 were in mg/Nm3 concentration units (non-comparable with peers). FY2024/FY2025 switched to kg/tcs mass intensity. Wages may be reported in absolute INR rather than INR Crore - check units carefully.

---

## Checklist

Verify every item below. Do not skip any item. For each, find the value in the PDF and give a verdict.

### Section A - Peer outliers

Our value is compared to the median of the other 3 companies for the same metric and same year.

**ITEM_1**
- Tag: `BioMedicalWaste`
- Metric: Biomedical Waste Generated
- Our normalized value: **141 metric tonnes**
- Peer comparison: 190.5x higher than peer median of 0.74 metric tonnes
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_2**
- Tag: `EnergyConsumptionThroughOtherSources`
- Metric: Energy Consumption Through Other Sources
- Our normalized value: **916,000 GJ**
- Raw value in PDF/XBRL: 916 terajoules (we converted to GJ)
- Peer comparison: 33.3x lower than peer median of 2.8e+07 GJ
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_3**
- Tag: `EnergyIntensityPerRupeeOfTurnover`
- Metric: Energy Intensity per Rupee of Turnover
- Our normalized value: **5.7 ?**
- Peer comparison: 100.0x lower than peer median of 434.5 ?
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_4**
- Tag: `PercentageOfContributionOfExportsInTheTotalTurnoverOfTheEntity`
- Metric: Export Contribution To Turnover
- Our normalized value: **2.56 %**
- Peer comparison: 5.0x lower than peer median of 13 %
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_5**
- Tag: `TotalScope1AndScope2EmissionsIntensityPerRupeeOfTurnover`
- Metric: GHG Emissions Intensity Per Turnover
- Our normalized value: **487.9 ?**
- Peer comparison: 10.3x higher than peer median of 47.52 ?
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_6**
- Tag: `TotalElectricityConsumptionFromNonRenewableSources`
- Metric: Non Renewable Electricity Consumption Volume
- Our normalized value: **1.40245e+08 GJ**
- Raw value in PDF/XBRL: 140245 terajoules (we converted to GJ)
- Peer comparison: 12.5x higher than peer median of 1.122e+07 GJ
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_7**
- Tag: `NumberOfCountriesWhereMarketServedByTheEntity`
- Metric: Number Of Countries Served
- Our normalized value: **8 ?**
- Peer comparison: 5.3x lower than peer median of 42 ?
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_8**
- Tag: `PercentageOfRAndD`
- Metric: Percentage Of R&D
- Our normalized value: **9.02 %**
- Peer comparison: 11.1x lower than peer median of 100 %
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_9**
- Tag: `WhatPercentageOfTotalProcurementByValueDoesItConstitute`
- Metric: Procurement Value Percentage Share
- Our normalized value: **33 %**
- Peer comparison: 47.1x higher than peer median of 0.7 %
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_10**
- Tag: `RecyclingAndOrSafeDisposalAsAPercentageToTotalTurnover`
- Metric: Recycling Cost To Turnover
- Our normalized value: **100 %**
- Peer comparison: 5.3x higher than peer median of 19 %
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_11**
- Tag: `TotalElectricityConsumptionFromRenewableSources`
- Metric: Renewable Electricity Consumption Volume
- Our normalized value: **127,200 GJ**
- Raw value in PDF/XBRL: 127.2 terajoules (we converted to GJ)
- Peer comparison: 7.7x lower than peer median of 1e+06 GJ
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_12**
- Tag: `TotalScope3EmissionsPerRupeeOfTurnover`
- Metric: Scope 3 Emissions Per Turnover
- Our normalized value: **54.2 ?**
- Peer comparison: 110006.1x higher than peer median of 0.0004927 ?
- Suspected cause: likely unit mismatch: check if company reported in million tonnes vs tonnes
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_13**
- Tag: `PercentageOfDirectlySourcedFromMSMEsOrSmallProducers`
- Metric: Sourcing From MSMEs
- Our normalized value: **32.71 %**
- Peer comparison: 6.5x higher than peer median of 5 %
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_14**
- Tag: `TotalElectricityConsumption`
- Metric: Total Electricity Consumption Volume
- Our normalized value: **1.40372e+08 GJ**
- Raw value in PDF/XBRL: 140372.3 terajoules (we converted to GJ)
- Peer comparison: 11.1x higher than peer median of 1.265e+07 GJ
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_15**
- Tag: `TotalEnergyConsumedFromRenewableSources`
- Metric: Total Renewable Energy Consumption
- Our normalized value: **127,200 GJ**
- Raw value in PDF/XBRL: 127.2 terajoules (we converted to GJ)
- Peer comparison: 7.7x lower than peer median of 1e+06 GJ
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_16**
- Tag: `TotalWasteDisposed`
- Metric: Total Waste Disposed Volume
- Our normalized value: **3,671 metric tonnes**
- Peer comparison: 50.0x lower than peer median of 1.868e+05 metric tonnes
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_17**
- Tag: `TotalWaterDischargedInKilolitres`
- Metric: Total Water Discharged Volume
- Our normalized value: **2.23638e+07 kL**
- Raw value in PDF/XBRL: 22363784 kilolitres (we converted to kL)
- Peer comparison: 5.9x lower than peer median of 1.28e+08 kL
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_18**
- Tag: `WasteDisposedByIncineration`
- Metric: Waste Disposed Incineration Volume
- Our normalized value: **35 metric tonnes**
- Peer comparison: 100.0x lower than peer median of 2,916 metric tonnes
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_19**
- Tag: `WasteDisposedByLandfilling`
- Metric: Waste Disposed Landfilling Volume
- Our normalized value: **3,529 metric tonnes**
- Peer comparison: 33.3x lower than peer median of 1.31e+05 metric tonnes
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_20**
- Tag: `WasteDisposedByOtherDisposalOperations`
- Metric: Waste Other Disposal Volume
- Our normalized value: **107 metric tonnes**
- Peer comparison: vs peer median of 3.837e+05 metric tonnes (our value is near zero)
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_21**
- Tag: `WasteRecoveredThroughOtherRecoveryOperations`
- Metric: Waste Recovered Other Operations
- Our normalized value: **9.76589e+06 metric tonnes**
- Peer comparison: 15.9x higher than peer median of 6.141e+05 metric tonnes
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

### Section D - Training coverage

**ITEM_22**
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

Respond with exactly 22 lines. Use this format from COMMON_INSTRUCTIONS.md:

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
```

Verdicts: CONFIRMED / CORRECTED / UNIT_ERROR / EXPECTED / NOT_FOUND / ZERO_REPORTED
For CORRECTED and UNIT_ERROR: always write the correct value AND its unit in PDF_VALUE.
For the training item: use FOUND / NOT_FOUND / NOT_REPORTED, and list all values found in PDF_VALUE.