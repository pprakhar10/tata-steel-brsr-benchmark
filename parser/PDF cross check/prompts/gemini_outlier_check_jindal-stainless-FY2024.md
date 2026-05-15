# BRSR XBRL Outlier Verification
# Company: Jindal Stainless Limited
# Year: FY2024 (April 2023 - March 2024)
# PDF to upload: "JINDAL STAINLESS FY24.pdf"
# Also read: gemini_outlier_check_COMMON_INSTRUCTIONS.md (paste that first, then this)

---

## Company context

- **Reporting basis:** STANDALONE
- **Crude steel production this year:** 2,080,000 MT
- **Sector:** Stainless steel (electric arc furnace), mid-cap (~10x smaller than Tata/JSW/SAIL)

> **Note:** Jindal Stainless is ~10x smaller than Tata/JSW/SAIL and uses electric arc furnace (not blast furnace). Lower absolute volumes for water, energy, and waste are expected. Intensity metrics (per tonne, per rupee) should still be broadly comparable.

---

## Checklist

Verify every item below. Do not skip any item. For each, find the value in the PDF and give a verdict.

### Section A - Peer outliers

Our value is compared to the median of the other 3 companies for the same metric and same year.

**ITEM_1**
- Tag: `AmountOfAccountsPayableDuringTheYear`
- Metric: Amount of Accounts Payable During the Year
- Our normalized value: **2.67786e+06 INR Crore**
- Peer comparison: vs peer median of 7.763e+13 INR Crore (our value is near zero)
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_2**
- Tag: `AmountOfCostIncurredOnWellBeingMeasures`
- Metric: Amount of Cost Incurred on Wellbeing Measures
- Our normalized value: **3 INR Crore**
- Peer comparison: vs peer median of 4.766e+08 INR Crore (our value is near zero)
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_3**
- Tag: `AmountOfInvestmentsInRelatedParties`
- Metric: Amount of Investments in Related Parties
- Our normalized value: **2.49406e+10 INR Crore**
- Peer comparison: 391937.8x higher than peer median of 6.363e+04 INR Crore
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_4**
- Tag: `AmountOfLoansAndAdvancesGivenToRelatedParties`
- Metric: Amount of Loans and Advances Given to Related Parties
- Our normalized value: **7.2263e+09 INR Crore**
- Peer comparison: 792281.9x higher than peer median of 9,121 INR Crore
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_5**
- Tag: `AmountOfPurchasesFromRelatedParties`
- Metric: Amount of Purchases from Related Parties
- Our normalized value: **1.78334e+10 INR Crore**
- Peer comparison: 394016.1x higher than peer median of 4.526e+04 INR Crore
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_6**
- Tag: `AmountOfPurchasesFromTopTenTradingHouses`
- Metric: Amount of Purchases from Top Ten Trading Houses
- Our normalized value: **67 INR Crore**
- Peer comparison: vs peer median of 3.531e+11 INR Crore (our value is near zero)
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_7**
- Tag: `AmountOfPurchasesFromTradingHouses`
- Metric: Amount of Purchases from Trading Houses
- Our normalized value: **78 INR Crore**
- Peer comparison: vs peer median of 3.564e+11 INR Crore (our value is near zero)
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_8**
- Tag: `AmountOfSalesToDealersOrDistributors`
- Metric: Amount of Sales to Dealers or Distributors
- Our normalized value: **27 INR Crore**
- Peer comparison: vs peer median of 2.351e+11 INR Crore (our value is near zero)
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_9**
- Tag: `AmountOfSalesToRelatedParties`
- Metric: Amount of Sales to Related Parties
- Our normalized value: **6.55953e+10 INR Crore**
- Peer comparison: 3759534.6x higher than peer median of 1.745e+04 INR Crore
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_10**
- Tag: `AmountOfSalesToTopTenDealersOrDistributors`
- Metric: Amount of Sales to Top Ten Dealers or Distributors
- Our normalized value: **40 INR Crore**
- Peer comparison: vs peer median of 6.913e+10 INR Crore (our value is near zero)
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_11**
- Tag: `AmountOfTotalInvestments`
- Metric: Amount of Total Investments
- Our normalized value: **2.8043e+10 INR Crore**
- Peer comparison: 424902.8x higher than peer median of 6.6e+04 INR Crore
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_12**
- Tag: `AmountOfTotalLoansAndAdvances`
- Metric: Amount of Total Loans and Advances
- Our normalized value: **7.2263e+09 INR Crore**
- Peer comparison: 488201.5x higher than peer median of 1.48e+04 INR Crore
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_13**
- Tag: `AmountOfTotalPurchases`
- Metric: Amount of Total Purchases
- Our normalized value: **100 INR Crore**
- Peer comparison: vs peer median of 1.124e+12 INR Crore (our value is near zero)
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_14**
- Tag: `AmountOfTotalPurchasesForShareOfRelatedPartyTransactions`
- Metric: Amount of Total Purchases for Share of Related Party Transactions
- Our normalized value: **2.65984e+11 INR Crore**
- Peer comparison: 2332124.1x higher than peer median of 1.141e+05 INR Crore
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_15**
- Tag: `AmountOfTotalPurchasesFromTradingHouses`
- Metric: Amount of Total Purchases from Trading Houses
- Our normalized value: **100 INR Crore**
- Peer comparison: vs peer median of 3.564e+11 INR Crore (our value is near zero)
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_16**
- Tag: `AmountOfTotalSales`
- Metric: Amount of Total Sales
- Our normalized value: **100 INR Crore**
- Peer comparison: vs peer median of 1.336e+12 INR Crore (our value is near zero)
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_17**
- Tag: `AmountOfTotalSalesForShareOfRelatedPartyTransactions`
- Metric: Amount of Total Sales for Share of Related Party Transactions
- Our normalized value: **3.80814e+11 INR Crore**
- Peer comparison: 2701048.5x higher than peer median of 1.41e+05 INR Crore
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_18**
- Tag: `AmountOfTotalSalesToDealersOrDistributors`
- Metric: Amount of Total Sales to Dealers or Distributors
- Our normalized value: **100 INR Crore**
- Peer comparison: vs peer median of 2.351e+11 INR Crore (our value is near zero)
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_19**
- Tag: `BioMedicalWaste`
- Metric: Biomedical Waste Generated
- Our normalized value: **0.35 metric tonnes**
- Peer comparison: 33.3x lower than peer median of 11.52 metric tonnes
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_20**
- Tag: `CostOfGoodsOrServicesProcuredDuringTheYear`
- Metric: Cost of Goods or Services Procured
- Our normalized value: **30,121.3 INR Crore**
- Peer comparison: vs peer median of 7.096e+11 INR Crore (our value is near zero)
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_21**
- Tag: `EnergyIntensityPerRupeeOfTurnoverAdjustingForPurchasingPowerParity`
- Metric: Energy Intensity Adjusted for PPP
- Our normalized value: **20,524 ?**
- Peer comparison: 1812.6x higher than peer median of 11.32 ?
- Suspected cause: likely unit mismatch: extreme ratio suggests PJ vs GJ or TJ vs GJ reporting error
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_22**
- Tag: `EnergyIntensityPerRupeeOfTurnover`
- Metric: Energy Intensity per Rupee of Turnover
- Our normalized value: **916.251 ?**
- Peer comparison: 2364719.1x higher than peer median of 0.0003875 ?
- Suspected cause: likely unit mismatch: extreme ratio suggests PJ vs GJ or TJ vs GJ reporting error
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_23**
- Tag: `TotalScope1AndScope2EmissionsIntensityPerRupeeOfTurnoverAdjustedForPurchasingPowerParity`
- Metric: GHG Emissions Intensity Adjusted PPP
- Our normalized value: **2,207.22 ?**
- Peer comparison: 2207222.6x higher than peer median of 0.001 ?
- Suspected cause: likely unit mismatch: check if company reported in million tonnes vs tonnes
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_24**
- Tag: `RevenueFromOperations`
- Metric: Revenue From Operations
- Our normalized value: **38,356 INR Crore**
- Peer comparison: vs peer median of 1.336e+12 INR Crore (our value is near zero)
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_25**
- Tag: `TotalScope3EmissionsPerRupeeOfTurnover`
- Metric: Scope 3 Emissions Per Turnover
- Our normalized value: **87.22 ?**
- Peer comparison: 8722000.0x higher than peer median of 1e-05 ?
- Suspected cause: likely unit mismatch: check if company reported in million tonnes vs tonnes
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_26**
- Tag: `TotalRevenueOfTheCompany`
- Metric: Total Annual Company Revenue
- Our normalized value: **1,000 INR Crore**
- Peer comparison: vs peer median of 1.336e+12 INR Crore (our value is near zero)
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_27**
- Tag: `WasteDisposedByIncineration`
- Metric: Waste Disposed Incineration Volume
- Our normalized value: **1.04 metric tonnes**
- Peer comparison: vs peer median of 960.3 metric tonnes (our value is near zero)
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_28**
- Tag: `WasteIntensityPerRupeeOfTurnoverAdjustingForPurchasingPowerParity`
- Metric: Waste Intensity Adjusted PPP
- Our normalized value: **925.422 ?**
- Peer comparison: 3701687.2x higher than peer median of 0.00025 ?
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_29**
- Tag: `WasteIntensityPerRupeeOfTurnover`
- Metric: Waste Intensity Per Turnover
- Our normalized value: **41.3135 ?**
- Peer comparison: 3460176.2x higher than peer median of 1.194e-05 ?
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_30**
- Tag: `WasteRecoveredThroughOtherRecoveryOperations`
- Metric: Waste Recovered Other Operations
- Our normalized value: **19,418.5 metric tonnes**
- Peer comparison: vs peer median of 1.122e+07 metric tonnes (our value is near zero)
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_31**
- Tag: `WasteRecoveredThroughReUsed`
- Metric: Waste Recovered Through Reuse
- Our normalized value: **84,173.9 metric tonnes**
- Peer comparison: 50.0x lower than peer median of 3.726e+06 metric tonnes
- Suspected cause: size difference (stainless steel, ~10Ã— smaller scale) â€” verify absolute vs intensity
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_32**
- Tag: `WaterIntensityPerRupeeOfTurnoverAdjustingForPurchasingPowerParity`
- Metric: Water Intensity Adjusted PPP
- Our normalized value: **7,459.39 ?**
- Peer comparison: 8540.6x higher than peer median of 0.8734 ?
- Suspected cause: possible unit mismatch: check kL vs ML or mÂ³ vs kL
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_33**
- Tag: `WaterWithdrawalByGroundwater`
- Metric: Water Withdrawal From Groundwater
- Our normalized value: **19,102 kL**
- Raw value in PDF/XBRL: 19102 kilolitres (we converted to kL)
- Peer comparison: vs peer median of 6.663e+06 kL (our value is near zero)
- Suspected cause: possible unit mismatch: check kL vs ML or mÂ³ vs kL
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_34**
- Tag: `WaterWithdrawalByThirdPartyWater`
- Metric: Water Withdrawal Third Party
- Our normalized value: **31,700 kL**
- Raw value in PDF/XBRL: 31700 kilolitres (we converted to kL)
- Peer comparison: 100.0x lower than peer median of 3.971e+06 kL
- Suspected cause: possible unit mismatch: check kL vs ML or mÂ³ vs kL
- Task: Find this metric in the PDF and confirm or correct the value.

### Section B - Year-over-year outliers

These values changed dramatically from the prior year. Verify the current year value is correct.

**ITEM_35**
- Tag: `PercentageOfCapex`
- Metric: Percentage Of Capex
- Change: 0.02 % (FY2023) -> 23.42 % (FY2024), change = +117000%
- Task: Verify the FY2024 value (23.42 %) in the PDF. Is this correct?

**ITEM_36**
- Tag: `PercentageOfRAndD`
- Metric: Percentage Of R&D
- Change: 0.02 % (FY2023) -> 34.8 % (FY2024), change = +173900%
- Task: Verify the FY2024 value (34.8 %) in the PDF. Is this correct?

**ITEM_37**
- Tag: `PlasticWaste`
- Metric: Plastic Waste
- Change: 804 metric tonnes (FY2023) -> 1,600.14 metric tonnes (FY2024), change = +99%
- Task: Verify the FY2024 value (1,600.14 metric tonnes) in the PDF. Is this correct?

**ITEM_38**
- Tag: `RecyclingAndOrSafeDisposalAsAPercentageToTotalTurnover`
- Metric: Recycling Cost To Turnover
- Change: 4.1 % (FY2023) -> 100 % (FY2024), change = +2339%
- Task: Verify the FY2024 value (100 %) in the PDF. Is this correct?

**ITEM_39**
- Tag: `TotalElectricityConsumptionFromRenewableSources`
- Metric: Renewable Electricity Consumption Volume
- Change: 12,743 GJ (FY2023) -> 107,386 GJ (FY2024), change = +743%
- Raw value in PDF/XBRL for FY2024: 107386 gigajoules (we converted to GJ)
- Task: Verify the FY2024 value (107,386 GJ) in the PDF. Is this correct?

**ITEM_40**
- Tag: `Sox`
- Metric: Sulphur Oxides Air Emissions
- Change: 0.85189 kilotonnes (FY2023) -> 3.07206 kilotonnes (FY2024), change = +261%
- Raw value in PDF/XBRL for FY2024: 3072.064 MT (we converted to kilotonnes)
- Task: Verify the FY2024 value (3.07206 kilotonnes) in the PDF. Is this correct?

**ITEM_41**
- Tag: `TotalNumberOfAffectedWorkers`
- Metric: Total Number Affected Workers
- Change: 3 ? (FY2023) -> 0 ? (FY2024), change = +100%
- Task: Verify the FY2024 value (0 ?) in the PDF. Is this correct?

**ITEM_42**
- Tag: `TotalEnergyConsumedFromRenewableSources`
- Metric: Total Renewable Energy Consumption
- Change: 12,743 GJ (FY2023) -> 200,194 GJ (FY2024), change = +1471%
- Raw value in PDF/XBRL for FY2024: 200194 gigajoules (we converted to GJ)
- Task: Verify the FY2024 value (200,194 GJ) in the PDF. Is this correct?

**ITEM_43**
- Tag: `TotalWasteDisposed`
- Metric: Total Waste Disposed Volume
- Change: 766,300 metric tonnes (FY2023) -> 42,808.4 metric tonnes (FY2024), change = +94%
- Task: Verify the FY2024 value (42,808.4 metric tonnes) in the PDF. Is this correct?

**ITEM_44**
- Tag: `TotalWasteRecovered`
- Metric: Total Waste Recovered Volume
- Change: 862,284 metric tonnes (FY2023) -> 1.7777e+06 metric tonnes (FY2024), change = +106%
- Task: Verify the FY2024 value (1.7777e+06 metric tonnes) in the PDF. Is this correct?

**ITEM_45**
- Tag: `TotalWaterDischargedInKilolitres`
- Metric: Total Water Discharged Volume
- Change: 5,400 kL (FY2023) -> 0 kL (FY2024), change = +100%
- Raw value in PDF/XBRL for FY2024: 0 kilolitres (we converted to kL)
- Task: Verify the FY2024 value (0 kL) in the PDF. Is this correct?

**ITEM_46**
- Tag: `WasteDisposedByOtherDisposalOperations`
- Metric: Waste Other Disposal Volume
- Change: 766,298 metric tonnes (FY2023) -> 0 metric tonnes (FY2024), change = +100%
- Task: Verify the FY2024 value (0 metric tonnes) in the PDF. Is this correct?

**ITEM_47**
- Tag: `WasteRecoveredThroughRecycled`
- Metric: Waste Recovered Through Recycling
- Change: 773,043 metric tonnes (FY2023) -> 1.67411e+06 metric tonnes (FY2024), change = +117%
- Task: Verify the FY2024 value (1.67411e+06 metric tonnes) in the PDF. Is this correct?

**ITEM_48**
- Tag: `WaterDischargeToOthers`
- Metric: Water Discharge Other Sources
- Change: 5,400 kL (FY2023) -> 0 kL (FY2024), change = +100%
- Raw value in PDF/XBRL for FY2024: 0 kilolitres (we converted to kL)
- Task: Verify the FY2024 value (0 kL) in the PDF. Is this correct?

**ITEM_49**
- Tag: `WaterDischargeToOthersWithTreatment`
- Metric: Water Discharge Treated Others
- Change: 1,800 kL (FY2023) -> 0 kL (FY2024), change = +100%
- Raw value in PDF/XBRL for FY2024: 0 kilolitres (we converted to kL)
- Task: Verify the FY2024 value (0 kL) in the PDF. Is this correct?

**ITEM_50**
- Tag: `WaterDischargeToOthersWithoutTreatment`
- Metric: Water Discharge Untreated Others
- Change: 3,600 kL (FY2023) -> 0 kL (FY2024), change = +100%
- Raw value in PDF/XBRL for FY2024: 0 kilolitres (we converted to kL)
- Task: Verify the FY2024 value (0 kL) in the PDF. Is this correct?

**ITEM_51**
- Tag: `NumberOfWorkersOrWhoseFamilyMembersRehabilitatedAndPlacedInSuitableEmployment`
- Metric: Workers Rehabilitated And Placed
- Change: 3 ? (FY2023) -> 0 ? (FY2024), change = +100%
- Task: Verify the FY2024 value (0 ?) in the PDF. Is this correct?

### Section D - Training coverage

**ITEM_52**
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

Respond with exactly 52 lines. Use this format from COMMON_INSTRUCTIONS.md:

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
ITEM_24 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_25 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_26 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_27 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_28 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_29 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_30 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_31 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_32 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_33 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_34 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_35 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_36 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_37 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_38 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_39 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_40 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_41 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_42 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_43 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_44 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_45 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_46 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_47 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_48 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_49 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_50 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_51 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_52 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
```

Verdicts: CONFIRMED / CORRECTED / UNIT_ERROR / EXPECTED / NOT_FOUND / ZERO_REPORTED
For CORRECTED and UNIT_ERROR: always write the correct value AND its unit in PDF_VALUE.
For the training item: use FOUND / NOT_FOUND / NOT_REPORTED, and list all values found in PDF_VALUE.