# BRSR XBRL Outlier Verification
# Company: Jindal Stainless Limited
# Year: FY2023 (April 2022 - March 2023)
# PDF to upload: "JINDAL STAINLESS FY23.pdf"
# Also read: gemini_outlier_check_COMMON_INSTRUCTIONS.md (paste that first, then this)

---

## Company context

- **Reporting basis:** STANDALONE
- **Crude steel production this year:** 1,710,000 MT
- **Sector:** Stainless steel (electric arc furnace), mid-cap (~10x smaller than Tata/JSW/SAIL)

> **Note:** Jindal Stainless is ~10x smaller than Tata/JSW/SAIL and uses electric arc furnace (not blast furnace). Lower absolute volumes for water, energy, and waste are expected. Intensity metrics (per tonne, per rupee) should still be broadly comparable.

---

## Checklist

Verify every item below. Do not skip any item. For each, find the value in the PDF and give a verdict.

### Section A - Peer outliers

Our value is compared to the median of the other 3 companies for the same metric and same year.

**ITEM_1**
- Tag: `BioMedicalWaste`
- Metric: Biomedical Waste Generated
- Our normalized value: **0.74 metric tonnes**
- Peer comparison: 100.0x lower than peer median of 141 metric tonnes
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_2**
- Tag: `EnergyIntensityPerRupeeOfTurnover`
- Metric: Energy Intensity per Rupee of Turnover
- Our normalized value: **869 ?**
- Peer comparison: 304.9x higher than peer median of 2.85 ?
- Suspected cause: likely unit mismatch: extreme ratio suggests PJ vs GJ or TJ vs GJ reporting error
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_3**
- Tag: `PercentageOfCapex`
- Metric: Percentage Of Capex
- Our normalized value: **0.02 %**
- Peer comparison: vs peer median of 13.06 % (our value is near zero)
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_4**
- Tag: `PercentageOfRAndD`
- Metric: Percentage Of R&D
- Our normalized value: **0.02 %**
- Peer comparison: vs peer median of 100 % (our value is near zero)
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_5**
- Tag: `RecyclingAndOrSafeDisposalAsAPercentageToTotalTurnover`
- Metric: Recycling Cost To Turnover
- Our normalized value: **4.1 %**
- Peer comparison: 25.0x lower than peer median of 100 %
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_6**
- Tag: `TotalElectricityConsumptionFromRenewableSources`
- Metric: Renewable Electricity Consumption Volume
- Our normalized value: **12,743 GJ**
- Raw value in PDF/XBRL: 12743 gigajoules (we converted to GJ)
- Peer comparison: 100.0x lower than peer median of 1e+06 GJ
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_7**
- Tag: `Sox`
- Metric: Sulphur Oxides Air Emissions
- Our normalized value: **0.85189 kilotonnes**
- Raw value in PDF/XBRL: 851.89 MT (we converted to kilotonnes)
- Peer comparison: 50.0x lower than peer median of 45.91 kilotonnes
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_8**
- Tag: `TotalEnergyConsumedFromRenewableSources`
- Metric: Total Renewable Energy Consumption
- Our normalized value: **12,743 GJ**
- Raw value in PDF/XBRL: 12743 gigajoules (we converted to GJ)
- Peer comparison: 100.0x lower than peer median of 1e+06 GJ
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_9**
- Tag: `TotalWaterDischargedInKilolitres`
- Metric: Total Water Discharged Volume
- Our normalized value: **5,400 kL**
- Raw value in PDF/XBRL: 5400 kilolitres (we converted to kL)
- Peer comparison: vs peer median of 1.392e+08 kL (our value is near zero)
- Suspected cause: possible unit mismatch: check kL vs ML or mÂ³ vs kL
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_10**
- Tag: `WasteDisposedByIncineration`
- Metric: Waste Disposed Incineration Volume
- Our normalized value: **1.4 metric tonnes**
- Peer comparison: vs peer median of 2,916 metric tonnes (our value is near zero)
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_11**
- Tag: `WasteDisposedByOtherDisposalOperations`
- Metric: Waste Other Disposal Volume
- Our normalized value: **766,298 metric tonnes**
- Peer comparison: 1213.5x higher than peer median of 631.5 metric tonnes
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_12**
- Tag: `WasteRecoveredThroughOtherRecoveryOperations`
- Metric: Waste Recovered Other Operations
- Our normalized value: **489.94 metric tonnes**
- Peer comparison: vs peer median of 5.497e+06 metric tonnes (our value is near zero)
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_13**
- Tag: `WasteRecoveredThroughReUsed`
- Metric: Waste Recovered Through Reuse
- Our normalized value: **88,751 metric tonnes**
- Peer comparison: 100.0x lower than peer median of 8.535e+06 metric tonnes
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_14**
- Tag: `WaterWithdrawalByGroundwater`
- Metric: Water Withdrawal From Groundwater
- Our normalized value: **10,413 kL**
- Raw value in PDF/XBRL: 10413 kilolitres (we converted to kL)
- Peer comparison: vs peer median of 8.443e+06 kL (our value is near zero)
- Suspected cause: possible unit mismatch: check kL vs ML or mÂ³ vs kL
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_15**
- Tag: `WaterWithdrawalByThirdPartyWater`
- Metric: Water Withdrawal Third Party
- Our normalized value: **54,000 kL**
- Raw value in PDF/XBRL: 54000 kilolitres (we converted to kL)
- Peer comparison: vs peer median of 1.936e+07 kL (our value is near zero)
- Suspected cause: possible unit mismatch: check kL vs ML or mÂ³ vs kL
- Task: Find this metric in the PDF and confirm or correct the value.

### Section D - Training coverage

**ITEM_16**
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

Respond with exactly 16 lines. Use this format from COMMON_INSTRUCTIONS.md:

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
```

Verdicts: CONFIRMED / CORRECTED / UNIT_ERROR / EXPECTED / NOT_FOUND / ZERO_REPORTED
For CORRECTED and UNIT_ERROR: always write the correct value AND its unit in PDF_VALUE.
For the training item: use FOUND / NOT_FOUND / NOT_REPORTED, and list all values found in PDF_VALUE.