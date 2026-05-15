# BRSR XBRL Outlier Verification
# Company: JSW Steel Limited
# Year: FY2023 (April 2022 - March 2023)
# PDF to upload: "JSW STEEL FY23.pdf"
# Also read: gemini_outlier_check_COMMON_INSTRUCTIONS.md (paste that first, then this)

---

## Company context

- **Reporting basis:** STANDALONE
- **Crude steel production this year:** 24,150,000 MT
- **Sector:** Integrated carbon steel (blast furnace - basic oxygen furnace)


---

## Checklist

Verify every item below. Do not skip any item. For each, find the value in the PDF and give a verdict.

### Section A - Peer outliers

Our value is compared to the median of the other 3 companies for the same metric and same year.

**ITEM_1**
- Tag: `BioMedicalWaste`
- Metric: Biomedical Waste Generated
- Our normalized value: **0.03 metric tonnes**
- Peer comparison: vs peer median of 141 metric tonnes (our value is near zero)
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_2**
- Tag: `Turnover`
- Metric: Company Annual Turnover
- Our normalized value: **1.30039e+11 INR Crore**
- Peer comparison: 8.3x lower than peer median of 1.044e+12 INR Crore
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_3**
- Tag: `EnergyIntensityPerRupeeOfTurnover`
- Metric: Energy Intensity per Rupee of Turnover
- Our normalized value: **0.0004 ?**
- Peer comparison: vs peer median of 437.4 ? (our value is near zero)
- Suspected cause: likely unit mismatch: extreme ratio suggests PJ vs GJ or TJ vs GJ reporting error
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_4**
- Tag: `TotalScope1AndScope2EmissionsIntensityPerRupeeOfTurnover`
- Metric: GHG Emissions Intensity Per Turnover
- Our normalized value: **0.038 ?**
- Peer comparison: vs peer median of 291.4 ? (our value is near zero)
- Suspected cause: likely unit mismatch: check if company reported in million tonnes vs tonnes
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_5**
- Tag: `PercentageOfSourcedDirectlyFromWithinTheDistrictAndNeighbouringDistricts`
- Metric: Local District Sourcing Percentage
- Our normalized value: **2.8 %**
- Peer comparison: 14.3x lower than peer median of 37.61 %
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_6**
- Tag: `TotalElectricityConsumptionFromNonRenewableSources`
- Metric: Non Renewable Electricity Consumption Volume
- Our normalized value: **1.12235e+07 GJ**
- Raw value in PDF/XBRL: 11223481 gigajoules (we converted to GJ)
- Peer comparison: 5.9x lower than peer median of 6.6e+07 GJ
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_7**
- Tag: `PercentageOfRAndD`
- Metric: Percentage Of R&D
- Our normalized value: **100 %**
- Peer comparison: 11.1x higher than peer median of 9.02 %
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_8**
- Tag: `PlasticWaste`
- Metric: Plastic Waste
- Our normalized value: **25.75 metric tonnes**
- Peer comparison: 100.0x lower than peer median of 2,260 metric tonnes
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_9**
- Tag: `RecyclingAndOrSafeDisposalAsAPercentageToTotalTurnover`
- Metric: Recycling Cost To Turnover
- Our normalized value: **100 %**
- Peer comparison: 5.3x higher than peer median of 19 %
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_10**
- Tag: `TotalElectricityConsumptionFromRenewableSources`
- Metric: Renewable Electricity Consumption Volume
- Our normalized value: **1.42716e+06 GJ**
- Raw value in PDF/XBRL: 1427160 gigajoules (we converted to GJ)
- Peer comparison: 11.2x higher than peer median of 1.272e+05 GJ
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_11**
- Tag: `TotalScope3EmissionsPerRupeeOfTurnover`
- Metric: Scope 3 Emissions Per Turnover
- Our normalized value: **0.00098 ?**
- Peer comparison: vs peer median of 27.1 ? (our value is near zero)
- Suspected cause: likely unit mismatch: check if company reported in million tonnes vs tonnes
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_12**
- Tag: `PercentageOfDirectlySourcedFromMSMEsOrSmallProducers`
- Metric: Sourcing From MSMEs
- Our normalized value: **5 %**
- Peer comparison: 6.2x lower than peer median of 32 %
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_13**
- Tag: `TotalElectricityConsumption`
- Metric: Total Electricity Consumption Volume
- Our normalized value: **1.26506e+07 GJ**
- Raw value in PDF/XBRL: 12650641 gigajoules (we converted to GJ)
- Peer comparison: 5.3x lower than peer median of 6.7e+07 GJ
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_14**
- Tag: `TotalEnergyConsumedFromRenewableSources`
- Metric: Total Renewable Energy Consumption
- Our normalized value: **1.42716e+06 GJ**
- Raw value in PDF/XBRL: 1427160 gigajoules (we converted to GJ)
- Peer comparison: 11.2x higher than peer median of 1.272e+05 GJ
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_15**
- Tag: `TotalScope3Emissions`
- Metric: Total Scope 3 GHG Emissions
- Our normalized value: **1.28055e+06 tCO2e**
- Raw value in PDF/XBRL: 1280553 Tonnes of CO2 (we converted to tCO2e)
- Peer comparison: 7.1x lower than peer median of 9.36e+06 tCO2e
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_16**
- Tag: `WasteDisposedByIncineration`
- Metric: Waste Disposed Incineration Volume
- Our normalized value: **2,916 metric tonnes**
- Peer comparison: 83.3x higher than peer median of 35 metric tonnes
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_17**
- Tag: `WaterWithdrawalByGroundwater`
- Metric: Water Withdrawal From Groundwater
- Our normalized value: **15,142 kL**
- Raw value in PDF/XBRL: 15142 kilolitres (we converted to kL)
- Peer comparison: vs peer median of 8.44e+06 kL (our value is near zero)
- Suspected cause: possible unit mismatch: check kL vs ML or mÂ³ vs kL
- Task: Find this metric in the PDF and confirm or correct the value.

### Section D - Training coverage

**ITEM_18**
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

Respond with exactly 18 lines. Use this format from COMMON_INSTRUCTIONS.md:

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
```

Verdicts: CONFIRMED / CORRECTED / UNIT_ERROR / EXPECTED / NOT_FOUND / ZERO_REPORTED
For CORRECTED and UNIT_ERROR: always write the correct value AND its unit in PDF_VALUE.
For the training item: use FOUND / NOT_FOUND / NOT_REPORTED, and list all values found in PDF_VALUE.