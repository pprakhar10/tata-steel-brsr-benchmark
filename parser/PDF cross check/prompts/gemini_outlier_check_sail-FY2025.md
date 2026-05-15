# BRSR XBRL Outlier Verification
# Company: SAIL - Steel Authority of India Limited
# Year: FY2025 (April 2024 - March 2025)
# PDF to upload: "SAIL FY25.pdf"
# Also read: gemini_outlier_check_COMMON_INSTRUCTIONS.md (paste that first, then this)

---

## Company context

- **Reporting basis:** STANDALONE
- **Crude steel production this year:** 19,170,000 MT
- **Sector:** Integrated carbon steel (blast furnace - basic oxygen furnace), PSU

> **Note:** SAIL is a PSU. Air emissions FY2023 were in mg/Nm3 concentration units (non-comparable with peers). FY2024/FY2025 switched to kg/tcs mass intensity. Wages may be reported in absolute INR rather than INR Crore - check units carefully.

---

## Checklist

Verify every item below. Do not skip any item. For each, find the value in the PDF and give a verdict.

### Section A - Peer outliers

Our value is compared to the median of the other 3 companies for the same metric and same year.

**ITEM_1**
- Tag: `AmountOfAccountsPayableDuringTheYear`
- Metric: Amount of Accounts Payable During the Year
- Our normalized value: **4.71415e+13 INR Crore**
- Peer comparison: 5534742.0x higher than peer median of 8.517e+06 INR Crore
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_2**
- Tag: `AmountOfCostIncurredOnWellBeingMeasures`
- Metric: Amount of Cost Incurred on Wellbeing Measures
- Our normalized value: **1.47553e+10 INR Crore**
- Peer comparison: 46.4x higher than peer median of 3.18e+08 INR Crore
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_3**
- Tag: `AmountOfInvestmentsInRelatedParties`
- Metric: Amount of Investments in Related Parties
- Our normalized value: **1.38643e+10 INR Crore**
- Peer comparison: 195432.6x higher than peer median of 7.094e+04 INR Crore
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_4**
- Tag: `AmountOfLoansAndAdvancesGivenToRelatedParties`
- Metric: Amount of Loans and Advances Given to Related Parties
- Our normalized value: **4.48e+08 INR Crore**
- Peer comparison: 91151.9x higher than peer median of 4,915 INR Crore
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_5**
- Tag: `AmountOfPurchasesFromRelatedParties`
- Metric: Amount of Purchases from Related Parties
- Our normalized value: **4.33192e+10 INR Crore**
- Peer comparison: 1098417.4x higher than peer median of 3.944e+04 INR Crore
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_6**
- Tag: `AmountOfSalesToRelatedParties`
- Metric: Amount of Sales to Related Parties
- Our normalized value: **8.553e+08 INR Crore**
- Peer comparison: 49489.9x higher than peer median of 1.728e+04 INR Crore
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_7**
- Tag: `AmountOfTotalInvestments`
- Metric: Amount of Total Investments
- Our normalized value: **1.75893e+10 INR Crore**
- Peer comparison: 241946.5x higher than peer median of 7.27e+04 INR Crore
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_8**
- Tag: `AmountOfTotalLoansAndAdvances`
- Metric: Amount of Total Loans and Advances
- Our normalized value: **5.58378e+10 INR Crore**
- Peer comparison: 4955123.5x higher than peer median of 1.127e+04 INR Crore
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_9**
- Tag: `AmountOfTotalPurchasesForShareOfRelatedPartyTransactions`
- Metric: Amount of Total Purchases for Share of Related Party Transactions
- Our normalized value: **5.03949e+11 INR Crore**
- Peer comparison: 4827692.8x higher than peer median of 1.044e+05 INR Crore
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_10**
- Tag: `AmountOfTotalSalesForShareOfRelatedPartyTransactions`
- Metric: Amount of Total Sales for Share of Related Party Transactions
- Our normalized value: **1.01716e+12 INR Crore**
- Peer comparison: 7675693.9x higher than peer median of 1.325e+05 INR Crore
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_11**
- Tag: `CostOfGoodsOrServicesProcuredDuringTheYear`
- Metric: Cost of Goods or Services Procured
- Our normalized value: **5.03949e+11 INR Crore**
- Peer comparison: 4827693.3x higher than peer median of 1.044e+05 INR Crore
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_12**
- Tag: `PercentageOfComplaintsInRespectOfNumberOfEmployeesOrWorker`
- Metric: Employee Complaints Percentage
- Our normalized value: **0.09 %**
- Peer comparison: 5.9x lower than peer median of 0.53 %
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_13**
- Tag: `NumberOfEmployeesOrWhoseFamilyMembersRehabilitatedAndPlacedInSuitableEmployment`
- Metric: Employees Rehabilitated And Placed
- Our normalized value: **1 ?**
- Peer comparison: 5.9x lower than peer median of 6 ?
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_14**
- Tag: `EnergyIntensityInTermOfPhysicalOutput`
- Metric: Energy Intensity by Physical Output
- Our normalized value: **0.027 ?**
- Peer comparison: vs peer median of 23.55 ? (our value is near zero)
- Suspected cause: likely unit mismatch: extreme ratio suggests PJ vs GJ or TJ vs GJ reporting error
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_15**
- Tag: `PercentageOfContributionOfExportsInTheTotalTurnoverOfTheEntity`
- Metric: Export Contribution To Turnover
- Our normalized value: **0.48 %**
- Peer comparison: 12.5x lower than peer median of 6 %
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_16**
- Tag: `TotalScope1AndScope2EmissionsIntensityPerRupeeOfTurnover`
- Metric: GHG Emissions Intensity Per Turnover
- Our normalized value: **0.0578014 ?**
- Peer comparison: 2199.0x higher than peer median of 2.629e-05 ?
- Suspected cause: likely unit mismatch: check if company reported in million tonnes vs tonnes
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_17**
- Tag: `NumberOfCountriesWhereMarketServedByTheEntity`
- Metric: Number Of Countries Served
- Our normalized value: **3 ?**
- Peer comparison: 25.0x lower than peer median of 77 ?
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_18**
- Tag: `PercentageOfCapex`
- Metric: Percentage Of Capex
- Our normalized value: **1.84 %**
- Peer comparison: 6.2x lower than peer median of 11.33 %
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_19**
- Tag: `PercentageOfRAndD`
- Metric: Percentage Of R&D
- Our normalized value: **10.48 %**
- Peer comparison: 10.0x lower than peer median of 100 %
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_20**
- Tag: `PlasticWaste`
- Metric: Plastic Waste
- Our normalized value: **0.97 metric tonnes**
- Peer comparison: vs peer median of 1,486 metric tonnes (our value is near zero)
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_21**
- Tag: `PercentageOfLoansAndAdvancesGivenToRelatedPartiesInTotalLoansAndAdvances`
- Metric: Related Party Loans Percentage
- Our normalized value: **0.8 %**
- Peer comparison: 100.0x lower than peer median of 100 %
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_22**
- Tag: `PercentageOfSalesToRelatedPartiesInTotalSalesForShareOfRelatedPartyTransactions`
- Metric: Related Party Sales Percentage
- Our normalized value: **0.08 %**
- Peer comparison: 100.0x lower than peer median of 15.91 %
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_23**
- Tag: `RevenueFromOperations`
- Metric: Revenue From Operations
- Our normalized value: **9.85697e+08 INR Crore**
- Peer comparison: vs peer median of 1.257e+12 INR Crore (our value is near zero)
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_24**
- Tag: `TotalScope3EmissionsPerRupeeOfTurnover`
- Metric: Scope 3 Emissions Per Turnover
- Our normalized value: **49 ?**
- Peer comparison: 6121097.8x higher than peer median of 8.005e-06 ?
- Suspected cause: likely unit mismatch: check if company reported in million tonnes vs tonnes
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_25**
- Tag: `TotalWasteDisposed`
- Metric: Total Waste Disposed Volume
- Our normalized value: **969,314 metric tonnes**
- Peer comparison: 48.2x higher than peer median of 2.01e+04 metric tonnes
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_26**
- Tag: `WasteDisposedByLandfilling`
- Metric: Waste Disposed Landfilling Volume
- Our normalized value: **969,314 metric tonnes**
- Peer comparison: 60.6x higher than peer median of 1.599e+04 metric tonnes
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_27**
- Tag: `WasteIntensityPerRupeeOfTurnover`
- Metric: Waste Intensity Per Turnover
- Our normalized value: **0.0143497 ?**
- Peer comparison: 1095.8x higher than peer median of 1.309e-05 ?
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_28**
- Tag: `WasteRecoveredThroughOtherRecoveryOperations`
- Metric: Waste Recovered Other Operations
- Our normalized value: **1.12491e+07 metric tonnes**
- Peer comparison: 146874.6x higher than peer median of 76.59 metric tonnes
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_29**
- Tag: `WasteRecoveredThroughRecycled`
- Metric: Waste Recovered Through Recycling
- Our normalized value: **1.87059e+06 metric tonnes**
- Peer comparison: 9.1x lower than peer median of 1.648e+07 metric tonnes
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_30**
- Tag: `WaterIntensityPerRupeeOfTurnoverAdjustingForPurchasingPowerParity`
- Metric: Water Intensity Adjusted PPP
- Our normalized value: **1.84 ?**
- Peer comparison: 2102.1x higher than peer median of 0.0008753 ?
- Suspected cause: possible unit mismatch: check kL vs ML or mÂ³ vs kL
- Task: Find this metric in the PDF and confirm or correct the value.

**ITEM_31**
- Tag: `PercentageOfCostIncurredOnWellBeingMeasuresWithRespectToTotalRevenueOfTheCompany`
- Metric: Wellbeing Cost To Revenue
- Our normalized value: **1.44 %**
- Peer comparison: 28.8x higher than peer median of 0.05 %
- Suspected cause: investigate: may be genuine difference, unit error, or PSU reporting gap
- Task: Find this metric in the PDF and confirm or correct the value.

### Section B - Year-over-year outliers

These values changed dramatically from the prior year. Verify the current year value is correct.

**ITEM_32**
- Tag: `AmountOfSalesToDealersOrDistributors`
- Metric: Amount of Sales to Dealers or Distributors
- Change: 229 INR Crore (FY2024) -> 1.61085e+11 INR Crore (FY2025), change = +70342691046%
- Task: Verify the FY2025 value (1.61085e+11 INR Crore) in the PDF. Is this correct?

**ITEM_33**
- Tag: `AmountOfSalesToTopTenDealersOrDistributors`
- Metric: Amount of Sales to Top Ten Dealers or Distributors
- Change: 656.5 INR Crore (FY2024) -> 4.28472e+10 INR Crore (FY2025), change = +6526616724%
- Task: Verify the FY2025 value (4.28472e+10 INR Crore) in the PDF. Is this correct?

**ITEM_34**
- Tag: `AmountOfTotalSales`
- Metric: Amount of Total Sales
- Change: 1,725 INR Crore (FY2024) -> 1.01223e+12 INR Crore (FY2025), change = +58679999900%
- Task: Verify the FY2025 value (1.01223e+12 INR Crore) in the PDF. Is this correct?

**ITEM_35**
- Tag: `AmountOfTotalSalesToDealersOrDistributors`
- Metric: Amount of Total Sales to Dealers or Distributors
- Change: 2,290 INR Crore (FY2024) -> 1.61085e+11 INR Crore (FY2025), change = +7034269015%
- Task: Verify the FY2025 value (1.61085e+11 INR Crore) in the PDF. Is this correct?

**ITEM_36**
- Tag: `BatteryWaste`
- Metric: Battery Waste Generated
- Change: 228 metric tonnes (FY2024) -> 512 metric tonnes (FY2025), change = +125%
- Task: Verify the FY2025 value (512 metric tonnes) in the PDF. Is this correct?

**ITEM_37**
- Tag: `ConstructionAndDemolitionWaste`
- Metric: Construction and Demolition Waste Generated
- Change: 9,063 metric tonnes (FY2024) -> 0 metric tonnes (FY2025), change = +100%
- Task: Verify the FY2025 value (0 metric tonnes) in the PDF. Is this correct?

**ITEM_38**
- Tag: `EnergyIntensityPerRupeeOfTurnoverAdjustingForPurchasingPowerParity`
- Metric: Energy Intensity Adjusted for PPP
- Change: 11.323 ? (FY2024) -> 0.0109 ? (FY2025), change = +100%
- Task: Verify the FY2025 value (0.0109 ?) in the PDF. Is this correct?

**ITEM_39**
- Tag: `EnergyIntensityPerRupeeOfTurnover`
- Metric: Energy Intensity per Rupee of Turnover
- Change: 0.560003 ? (FY2024) -> 0.000526968 ? (FY2025), change = +100%
- Task: Verify the FY2025 value (0.000526968 ?) in the PDF. Is this correct?

**ITEM_40**
- Tag: `GrossWagesPaidToFemale`
- Metric: Gross Wages Paid to Female Employees
- Change: 338.16 INR Crore (FY2024) -> 5.59368e+09 INR Crore (FY2025), change = +1654152754%
- Task: Verify the FY2025 value (5.59368e+09 INR Crore) in the PDF. Is this correct?

**ITEM_41**
- Tag: `TotalElectricityConsumptionFromNonRenewableSources`
- Metric: Non Renewable Electricity Consumption Volume
- Change: 1.43445e+08 GJ (FY2024) -> 3.0472e+07 GJ (FY2025), change = +79%
- Raw value in PDF/XBRL for FY2025: 30472 terajoules (we converted to GJ)
- Task: Verify the FY2025 value (3.0472e+07 GJ) in the PDF. Is this correct?

**ITEM_42**
- Tag: `EnergyConsumptionThroughOtherSourcesFromNonRenewableSources`
- Metric: Non-Renewable Energy Consumption from Other Sources
- Change: 678,500 GJ (FY2024) -> 2.757e+06 GJ (FY2025), change = +306%
- Raw value in PDF/XBRL for FY2025: 2757 terajoules (we converted to GJ)
- Task: Verify the FY2025 value (2.757e+06 GJ) in the PDF. Is this correct?

**ITEM_43**
- Tag: `NumberOfFemaleBoardOfDirectors`
- Metric: Number Of Female Directors
- Change: 2 ? (FY2024) -> 0 ? (FY2025), change = +100%
- Task: Verify the FY2025 value (0 ?) in the PDF. Is this correct?

**ITEM_44**
- Tag: `OtherHazardousWaste`
- Metric: Other Hazardous Waste
- Change: 162,006 metric tonnes (FY2024) -> 302,410 metric tonnes (FY2025), change = +87%
- Task: Verify the FY2025 value (302,410 metric tonnes) in the PDF. Is this correct?

**ITEM_45**
- Tag: `PercentageOfFemaleBoardOfDirectors`
- Metric: Percentage Female Board Directors
- Change: 12.5 % (FY2024) -> 0 % (FY2025), change = +100%
- Task: Verify the FY2025 value (0 %) in the PDF. Is this correct?

**ITEM_46**
- Tag: `EnvironmentalAndSocialParametersRelevantToTheProductAsAPercentageToTotalTurnover`
- Metric: Product Sustainability Parameters as Percentage of Turnover
- Change: 100 % (FY2024) -> 0 % (FY2025), change = +100%
- Task: Verify the FY2025 value (0 %) in the PDF. Is this correct?

**ITEM_47**
- Tag: `RecyclingAndOrSafeDisposalAsAPercentageToTotalTurnover`
- Metric: Recycling Cost To Turnover
- Change: 100 % (FY2024) -> 0 % (FY2025), change = +100%
- Task: Verify the FY2025 value (0 %) in the PDF. Is this correct?

**ITEM_48**
- Tag: `TotalElectricityConsumptionFromRenewableSources`
- Metric: Renewable Electricity Consumption Volume
- Change: 266,000 GJ (FY2024) -> 1.4e+06 GJ (FY2025), change = +426%
- Raw value in PDF/XBRL for FY2025: 1400 terajoules (we converted to GJ)
- Task: Verify the FY2025 value (1.4e+06 GJ) in the PDF. Is this correct?

**ITEM_49**
- Tag: `SafeAndResponsibleUsageAsAPercentageToTotalTurnover`
- Metric: Safe Usage Information Turnover Percentage
- Change: 100 % (FY2024) -> 0 % (FY2025), change = +100%
- Task: Verify the FY2025 value (0 %) in the PDF. Is this correct?

**ITEM_50**
- Tag: `PercentageOfDirectlySourcedFromMSMEsOrSmallProducers`
- Metric: Sourcing From MSMEs
- Change: 29.28 % (FY2024) -> 5.13 % (FY2025), change = +82%
- Task: Verify the FY2025 value (5.13 %) in the PDF. Is this correct?

**ITEM_51**
- Tag: `PercentageOfInputsWereSourcedSustainably`
- Metric: Sustainably Sourced Inputs Percentage
- Change: 100 % (FY2024) -> 0 % (FY2025), change = +100%
- Task: Verify the FY2025 value (0 %) in the PDF. Is this correct?

**ITEM_52**
- Tag: `TotalRevenueOfTheCompany`
- Metric: Total Annual Company Revenue
- Change: 105,375 INR Crore (FY2024) -> 1.02478e+12 INR Crore (FY2025), change = +972513198%
- Task: Verify the FY2025 value (1.02478e+12 INR Crore) in the PDF. Is this correct?

**ITEM_53**
- Tag: `TotalWagesPaid`
- Metric: Total Employee Wages Paid
- Change: 5,308.85 INR Crore (FY2024) -> 9.03997e+10 INR Crore (FY2025), change = +1702810305%
- Task: Verify the FY2025 value (9.03997e+10 INR Crore) in the PDF. Is this correct?

**ITEM_54**
- Tag: `TotalEnergyConsumedFromRenewableSources`
- Metric: Total Renewable Energy Consumption
- Change: 266,000 GJ (FY2024) -> 1.4e+06 GJ (FY2025), change = +426%
- Raw value in PDF/XBRL for FY2025: 1400 terajoules (we converted to GJ)
- Task: Verify the FY2025 value (1.4e+06 GJ) in the PDF. Is this correct?

**ITEM_55**
- Tag: `TotalScope2Emissions`
- Metric: Total Scope 2 GHG Emissions
- Change: 2.44663e+06 tCO2e (FY2024) -> 4.79607e+06 tCO2e (FY2025), change = +96%
- Raw value in PDF/XBRL for FY2025: 4796073 Tonnes of CO2 (we converted to tCO2e)
- Task: Verify the FY2025 value (4.79607e+06 tCO2e) in the PDF. Is this correct?

**ITEM_56**
- Tag: `TotalVolumeOfWaterConsumption`
- Metric: Total Water Consumption Volume
- Change: 5.73965e+07 kL (FY2024) -> 8.77681e+07 kL (FY2025), change = +53%
- Raw value in PDF/XBRL for FY2025: 87768084 kilolitres (we converted to kL)
- Task: Verify the FY2025 value (8.77681e+07 kL) in the PDF. Is this correct?

**ITEM_57**
- Tag: `TotalWaterDischargedInKilolitres`
- Metric: Total Water Discharged Volume
- Change: 2.29856e+07 kL (FY2024) -> 4.18091e+07 kL (FY2025), change = +82%
- Raw value in PDF/XBRL for FY2025: 41809132 kilolitres (we converted to kL)
- Task: Verify the FY2025 value (4.18091e+07 kL) in the PDF. Is this correct?

**ITEM_58**
- Tag: `TotalVolumeOfWaterWithdrawal`
- Metric: Total Water Withdrawal Volume
- Change: 5.73965e+07 kL (FY2024) -> 1.29577e+08 kL (FY2025), change = +126%
- Raw value in PDF/XBRL for FY2025: 129577216 kilolitres (we converted to kL)
- Task: Verify the FY2025 value (1.29577e+08 kL) in the PDF. Is this correct?

**ITEM_59**
- Tag: `WasteRecoveredThroughReUsed`
- Metric: Waste Recovered Through Reuse
- Change: 8,673 metric tonnes (FY2024) -> 2.24565e+06 metric tonnes (FY2025), change = +25792%
- Task: Verify the FY2025 value (2.24565e+06 metric tonnes) in the PDF. Is this correct?

**ITEM_60**
- Tag: `WaterDischargeToSurfaceWater`
- Metric: Water Discharge To Surface Water
- Change: 2.29856e+07 kL (FY2024) -> 4.18091e+07 kL (FY2025), change = +82%
- Raw value in PDF/XBRL for FY2025: 41809132 kilolitres (we converted to kL)
- Task: Verify the FY2025 value (4.18091e+07 kL) in the PDF. Is this correct?

**ITEM_61**
- Tag: `WaterDischargeToSurfaceWaterWithTreatment`
- Metric: Water Discharge Treated Surface
- Change: 2.29856e+07 kL (FY2024) -> 4.18091e+07 kL (FY2025), change = +82%
- Raw value in PDF/XBRL for FY2025: 41809132 kilolitres (we converted to kL)
- Task: Verify the FY2025 value (4.18091e+07 kL) in the PDF. Is this correct?

**ITEM_62**
- Tag: `WaterWithdrawalBySurfaceWater`
- Metric: Water Withdrawal Surface Water
- Change: 5.73965e+07 kL (FY2024) -> 1.29577e+08 kL (FY2025), change = +126%
- Raw value in PDF/XBRL for FY2025: 129577216 kilolitres (we converted to kL)
- Task: Verify the FY2025 value (1.29577e+08 kL) in the PDF. Is this correct?

### Section C - External assurance

**ITEM_63**
- Issue: XBRL data shows a change in external assurance coverage in FY2025
- Task: Find the external assurance statement in the PDF (usually at the start or end of the BRSR).
  - Was this BRSR externally assured for FY2025?
  - If yes: who was the assurer, what level (reasonable / limited), and what scope?
  - If no: confirm the BRSR was not externally assured.

### Section D - Training coverage

**ITEM_64**
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

Respond with exactly 64 lines. Use this format from COMMON_INSTRUCTIONS.md:

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
ITEM_53 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_54 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_55 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_56 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_57 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_58 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_59 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_60 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_61 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_62 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_63 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_64 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
```

Verdicts: CONFIRMED / CORRECTED / UNIT_ERROR / EXPECTED / NOT_FOUND / ZERO_REPORTED
For CORRECTED and UNIT_ERROR: always write the correct value AND its unit in PDF_VALUE.
For the training item: use FOUND / NOT_FOUND / NOT_REPORTED, and list all values found in PDF_VALUE.