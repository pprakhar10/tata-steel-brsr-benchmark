# BRSR Data Review — 2026-04-14

**Instructions:** Read each section. Where you see `YOUR COMMENT`, type your note on that line.
Leave blank if the data looks correct. Save the file when done, then tell Claude to read it.

**Legend:** ⚠️ = value null or not normalized &nbsp;|&nbsp; 📄 = overridden by PDF patch

---

## 1. Reporting Basis

| Company | FY2023 | FY2024 | FY2025 |
|:--------|:------:|:------:|:------:|
| Tata Steel | ⚠️ Consolidated | ✓ Standalone | ✓ Standalone |
| JSW Steel | ✓ Standalone | ✓ Standalone | ✓ Standalone |
| SAIL | ✓ Standalone | ✓ Standalone | ✓ Standalone |
| Jindal Stainless | ✓ Standalone | ✓ Standalone | ✓ Standalone |

- **Tata Steel FY2023:** This year's data is reported on a Consolidated basis (includes subsidiaries and international operations). All other years of this company and all other companies in this benchmark are Standalone. Cross-company and cross-year comparisons for this year-company are not directly comparable.

> **YOUR COMMENT:** *(type here — leave blank if no issues)*

---

## 2. Validation Summary

| | Count |
|:--|:--|
| Blocking flags | **0** (must be 0) |
| Warning flags  | 712 |

### Peer outliers with ratio > 50× &nbsp; (98 of 346 total)

| Company | Year | Metric | Value | Peer Median | Ratio | Likely cause |
|:--------|:-----|:-------|------:|------------:|------:|:-------------|
| tata-steel | FY2023 | WaterWithdrawalByGroundwater | 16,870,056 | 12,778 | 1320x | possible unit mismatch: check kL vs ML or m³ vs kL |
| tata-steel | FY2023 | WaterWithdrawalByThirdPartyWater | 19,359,133 | 54,000 | 358x | possible unit mismatch: check kL vs ML or m³ vs kL |
| tata-steel | FY2023 | BioMedicalWaste | 180 | 0.7400 | 243x | check reporting basis: FY2023 = consolidated (includes overseas ops),  |
| sail | FY2023 | BioMedicalWaste | 141 | 0.7400 | 191x | investigate: may be genuine difference, unit error, or PSU reporting g |
| tata-steel | FY2023 | WasteRecoveredThroughReUsed | 8,534,853 | 88,751 | 96x | check reporting basis: FY2023 = consolidated (includes overseas ops),  |
| tata-steel | FY2023 | WasteDisposedByIncineration | 11,682 | 35 | 334x | check reporting basis: FY2023 = consolidated (includes overseas ops),  |
| jsw-steel | FY2023 | WasteDisposedByIncineration | 2,916 | 35 | 83x | investigate: may be genuine difference, unit error, or PSU reporting g |
| jindal-stainless | FY2023 | WasteDisposedByOtherDisposalOperations | 766,298 | 632 | 1213x | size difference (stainless steel, ~10× smaller scale) — verify absolut |
| sail | FY2023 | TotalScope3EmissionsPerRupeeOfTurnover | 54 | 0.0005 | 110006x | likely unit mismatch: check if company reported in million tonnes vs t |
| jindal-stainless | FY2023 | EnergyIntensityPerRupeeOfTurnover | 869 | 3 | 305x | likely unit mismatch: extreme ratio suggests PJ vs GJ or TJ vs GJ repo |
| tata-steel | FY2024 | AmountOfAccountsPayableDuringTheYear | 77,625,344,509,898 | 5,429,841 | 14296063x | check reporting basis: FY2023 = consolidated (includes overseas ops),  |
| jsw-steel | FY2024 | AmountOfAccountsPayableDuringTheYear | 105,680,275,000,000 | 5,429,841 | 19462869x | investigate: may be genuine difference, unit error, or PSU reporting g |
| tata-steel | FY2024 | CostOfGoodsOrServicesProcuredDuringTheYear | 1,023,407,934,241 | 67,601 | 15138983x | check reporting basis: FY2023 = consolidated (includes overseas ops),  |
| jsw-steel | FY2024 | CostOfGoodsOrServicesProcuredDuringTheYear | 709,640,000,000 | 67,601 | 10497503x | investigate: may be genuine difference, unit error, or PSU reporting g |
| tata-steel | FY2024 | AmountOfSalesToDealersOrDistributors | 606,252,378,253 | 229 | 2647390298x | check reporting basis: FY2023 = consolidated (includes overseas ops),  |
| jsw-steel | FY2024 | AmountOfSalesToDealersOrDistributors | 235,095,000,000 | 229 | 1026615721x | investigate: may be genuine difference, unit error, or PSU reporting g |
| tata-steel | FY2024 | AmountOfTotalSales | 1,372,843,287,397 | 1,725 | 795851181x | check reporting basis: FY2023 = consolidated (includes overseas ops),  |
| jsw-steel | FY2024 | AmountOfTotalSales | 1,336,090,000,000 | 1,725 | 774544928x | investigate: may be genuine difference, unit error, or PSU reporting g |
| tata-steel | FY2024 | AmountOfSalesToTopTenDealersOrDistributors | 154,058,979,570 | 656 | 234667143x | check reporting basis: FY2023 = consolidated (includes overseas ops),  |
| jsw-steel | FY2024 | AmountOfSalesToTopTenDealersOrDistributors | 69,127,800,000 | 656 | 105297487x | investigate: may be genuine difference, unit error, or PSU reporting g |
| tata-steel | FY2024 | AmountOfTotalSalesToDealersOrDistributors | 606,252,378,253 | 2,290 | 264739030x | check reporting basis: FY2023 = consolidated (includes overseas ops),  |
| jsw-steel | FY2024 | AmountOfTotalSalesToDealersOrDistributors | 235,095,000,000 | 2,290 | 102661572x | investigate: may be genuine difference, unit error, or PSU reporting g |
| jsw-steel | FY2024 | AmountOfPurchasesFromRelatedParties | 376,914,000,000 | 45,261 | 8327624x | investigate: may be genuine difference, unit error, or PSU reporting g |
| jindal-stainless | FY2024 | AmountOfPurchasesFromRelatedParties | 17,833,442,081 | 45,261 | 394016x | size difference (stainless steel, ~10× smaller scale) — verify absolut |
| jsw-steel | FY2024 | AmountOfTotalPurchasesForShareOfRelatedPartyTransactions | 1,108,430,000,000 | 114,052 | 9718605x | investigate: may be genuine difference, unit error, or PSU reporting g |
| jindal-stainless | FY2024 | AmountOfTotalPurchasesForShareOfRelatedPartyTransactions | 265,984,300,000 | 114,052 | 2332124x | size difference (stainless steel, ~10× smaller scale) — verify absolut |
| jsw-steel | FY2024 | AmountOfSalesToRelatedParties | 410,246,400,000 | 17,448 | 23512881x | investigate: may be genuine difference, unit error, or PSU reporting g |
| jindal-stainless | FY2024 | AmountOfSalesToRelatedParties | 65,595,344,600 | 17,448 | 3759535x | size difference (stainless steel, ~10× smaller scale) — verify absolut |
| jsw-steel | FY2024 | AmountOfTotalSalesForShareOfRelatedPartyTransactions | 1,336,090,000,000 | 140,987 | 9476660x | investigate: may be genuine difference, unit error, or PSU reporting g |
| jindal-stainless | FY2024 | AmountOfTotalSalesForShareOfRelatedPartyTransactions | 380,813,879,210 | 140,987 | 2701048x | size difference (stainless steel, ~10× smaller scale) — verify absolut |
| jsw-steel | FY2024 | AmountOfLoansAndAdvancesGivenToRelatedParties | 142,578,500,000 | 9,121 | 15632116x | investigate: may be genuine difference, unit error, or PSU reporting g |
| jindal-stainless | FY2024 | AmountOfLoansAndAdvancesGivenToRelatedParties | 7,226,300,000 | 9,121 | 792282x | size difference (stainless steel, ~10× smaller scale) — verify absolut |
| jsw-steel | FY2024 | AmountOfTotalLoansAndAdvances | 142,669,400,000 | 14,802 | 9638600x | investigate: may be genuine difference, unit error, or PSU reporting g |
| jindal-stainless | FY2024 | AmountOfTotalLoansAndAdvances | 7,226,300,000 | 14,802 | 488202x | size difference (stainless steel, ~10× smaller scale) — verify absolut |
| jsw-steel | FY2024 | AmountOfInvestmentsInRelatedParties | 306,979,800,000 | 63,634 | 4824134x | investigate: may be genuine difference, unit error, or PSU reporting g |
| jindal-stainless | FY2024 | AmountOfInvestmentsInRelatedParties | 24,940,638,686 | 63,634 | 391938x | size difference (stainless steel, ~10× smaller scale) — verify absolut |
| jsw-steel | FY2024 | AmountOfTotalInvestments | 307,138,400,000 | 65,999 | 4653709x | investigate: may be genuine difference, unit error, or PSU reporting g |
| jindal-stainless | FY2024 | AmountOfTotalInvestments | 28,043,000,000 | 65,999 | 424903x | size difference (stainless steel, ~10× smaller scale) — verify absolut |
| tata-steel | FY2024 | AmountOfCostIncurredOnWellBeingMeasures | 1,648,410,373 | 1,534 | 1074254x | check reporting basis: FY2023 = consolidated (includes overseas ops),  |
| jsw-steel | FY2024 | AmountOfCostIncurredOnWellBeingMeasures | 476,589,851 | 1,534 | 310589x | investigate: may be genuine difference, unit error, or PSU reporting g |
| tata-steel | FY2024 | TotalRevenueOfTheCompany | 1,409,874,287,724 | 105,375 | 13379642x | check reporting basis: FY2023 = consolidated (includes overseas ops),  |
| jsw-steel | FY2024 | TotalRevenueOfTheCompany | 1,336,090,000,000 | 105,375 | 12679432x | investigate: may be genuine difference, unit error, or PSU reporting g |
| tata-steel | FY2024 | RevenueFromOperations | 1,409,874,287,726 | 1,096,720 | 1285537x | check reporting basis: FY2023 = consolidated (includes overseas ops),  |
| jsw-steel | FY2024 | RevenueFromOperations | 1,336,090,000,000 | 1,096,720 | 1218260x | investigate: may be genuine difference, unit error, or PSU reporting g |
| sail | FY2024 | EnergyIntensityPerRupeeOfTurnover | 0.5600 | 0.0004 | 1445x | likely unit mismatch: extreme ratio suggests PJ vs GJ or TJ vs GJ repo |
| jindal-stainless | FY2024 | EnergyIntensityPerRupeeOfTurnover | 916 | 0.0004 | 2364719x | likely unit mismatch: extreme ratio suggests PJ vs GJ or TJ vs GJ repo |
| tata-steel | FY2024 | EnergyIntensityPerRupeeOfTurnoverAdjustingForPurchasingPowerParity | 8,861 | 11 | 783x | likely unit mismatch: extreme ratio suggests PJ vs GJ or TJ vs GJ repo |
| jindal-stainless | FY2024 | EnergyIntensityPerRupeeOfTurnoverAdjustingForPurchasingPowerParity | 20,524 | 11 | 1813x | likely unit mismatch: extreme ratio suggests PJ vs GJ or TJ vs GJ repo |
| tata-steel | FY2024 | WaterWithdrawalByGroundwater | 13,302,945 | 20,710 | 642x | possible unit mismatch: check kL vs ML or m³ vs kL |
| tata-steel | FY2024 | WaterWithdrawalByThirdPartyWater | 3,970,520 | 31,700 | 125x | possible unit mismatch: check kL vs ML or m³ vs kL |
| jindal-stainless | FY2024 | WaterIntensityPerRupeeOfTurnoverAdjustingForPurchasingPowerParity | 7,459 | 0.8734 | 8541x | possible unit mismatch: check kL vs ML or m³ vs kL |
| jindal-stainless | FY2024 | TotalScope1AndScope2EmissionsIntensityPerRupeeOfTurnoverAdjustedForPurchasingPowerParity | 2,207 | 0.0010 | 2207223x | likely unit mismatch: check if company reported in million tonnes vs t |
| tata-steel | FY2024 | BioMedicalWaste | 23 | 0.1900 | 121x | check reporting basis: FY2023 = consolidated (includes overseas ops),  |
| sail | FY2024 | WasteIntensityPerRupeeOfTurnover | 13 | 0.0000 | 1069535x | investigate: may be genuine difference, unit error, or PSU reporting g |
| jindal-stainless | FY2024 | WasteIntensityPerRupeeOfTurnover | 41 | 0.0000 | 3460176x | size difference (stainless steel, ~10× smaller scale) — verify absolut |
| jindal-stainless | FY2024 | WasteIntensityPerRupeeOfTurnoverAdjustingForPurchasingPowerParity | 925 | 0.0003 | 3701687x | size difference (stainless steel, ~10× smaller scale) — verify absolut |
| tata-steel | FY2024 | WasteRecoveredThroughReUsed | 7,444,172 | 46,423 | 160x | check reporting basis: FY2023 = consolidated (includes overseas ops),  |
| tata-steel | FY2024 | WasteDisposedByLandfilling | 303,496 | 2,965 | 102x | check reporting basis: FY2023 = consolidated (includes overseas ops),  |
| tata-steel | FY2024 | TotalWasteDisposed | 307,577 | 3,109 | 99x | check reporting basis: FY2023 = consolidated (includes overseas ops),  |
| sail | FY2024 | TotalScope3EmissionsPerRupeeOfTurnover | 48 | 0.0000 | 4830000x | likely unit mismatch: check if company reported in million tonnes vs t |
*... 38 more in validation_report.json*

> **YOUR COMMENT:** *(type here — leave blank if no issues)*

### Year-over-year outliers &nbsp; (321 shown — 0 Tata FY23 suppressed as expected basis change)

| Company | Metric | Period | Change | Direction |
|:--------|:-------|:-------|-------:|:----------|
| tata-steel | WasteIntensityPerRupeeOfTurnoverAdjustingForPurchasingPowerParity | FY2024→FY2025 | 893% | increase |
| tata-steel | TotalScope3EmissionsPerRupeeOfTurnover | FY2024→FY2025 | 1900% | increase |
| tata-steel | BatteryWaste | FY2024→FY2025 | 160% | increase |
| tata-steel | CostOfGoodsOrServicesProcuredDuringTheYear | FY2024→FY2025 | 100% | decrease |
| tata-steel | PercentageOfCapex | FY2024→FY2025 | 106% | increase |
| tata-steel | AmountOfAccountsPayableDuringTheYear | FY2024→FY2025 | 100% | decrease |
| tata-steel | TotalElectricityConsumptionFromRenewableSources | FY2024→FY2025 | 231% | increase |
| tata-steel | WasteDisposedByOtherDisposalOperations | FY2024→FY2025 | 100% | decrease |
| tata-steel | PercentageOfComplaintsInRespectOfNumberOfEmployeesOrWorker | FY2024→FY2025 | 100% | increase |
| tata-steel | WhatPercentageOfTotalProcurementByValueDoesItConstitute | FY2024→FY2025 | 1167% | increase |
| tata-steel | NumberOfEmployeesOrWhoseFamilyMembersRehabilitatedAndPlacedInSuitableEmployment | FY2024→FY2025 | 200% | increase |
| tata-steel | BioMedicalWaste | FY2024→FY2025 | 1013% | increase |
| tata-steel | TotalNumberOfAffectedEmployees | FY2024→FY2025 | 100% | increase |
| tata-steel | TotalScope3Emissions | FY2024→FY2025 | 53% | increase |
| tata-steel | WasteRecoveredThroughReUsed | FY2024→FY2025 | 60% | decrease |
| tata-steel | WaterDischargeToGroundwaterWithTreatment | FY2024→FY2025 | 100% | decrease |
| tata-steel | WaterDischargeToGroundwater | FY2024→FY2025 | 100% | decrease |
| tata-steel | WaterWithdrawalByThirdPartyWater | FY2024→FY2025 | 160% | increase |
| tata-steel | TotalWasteDisposed | FY2024→FY2025 | 94% | decrease |
| tata-steel | TotalEnergyConsumedFromRenewableSources | FY2024→FY2025 | 231% | increase |
| tata-steel | AmountOfTotalPurchases | FY2024→FY2025 | 100% | decrease |
| tata-steel | NumberOfWorkersOrWhoseFamilyMembersRehabilitatedAndPlacedInSuitableEmployment | FY2024→FY2025 | 111% | increase |
| tata-steel | TotalComplaintsReportedUnderSexualHarassmentOfWomenAtWorkplace | FY2024→FY2025 | 115% | increase |
| tata-steel | WasteDisposedByLandfilling | FY2024→FY2025 | 95% | decrease |
| tata-steel | WasteDisposedByIncineration | FY2024→FY2025 | 132% | increase |
| tata-steel | NetWorth | FY2024→FY2025 | 840% | increase |
| tata-steel | ComplaintsOnPOSHUpHeld | FY2024→FY2025 | 125% | increase |
| tata-steel | TotalWagesPaid | FY2024→FY2025 | 60% | increase |
| jsw-steel | TotalScope3EmissionsPerRupeeOfTurnover | FY2023→FY2024 | 100% | decrease |
| jsw-steel | BatteryWaste | FY2023→FY2024 | 136% | increase |
| jsw-steel | EWaste | FY2023→FY2024 | 481% | increase |
| jsw-steel | WasteDisposedByLandfilling | FY2023→FY2024 | 98% | decrease |
| jsw-steel | WasteDisposedByIncineration | FY2023→FY2024 | 95% | decrease |
| jsw-steel | IsThereAMechanismAvailableToReceiveAndRedressGrievancesForPermanentWorkers | FY2023→FY2024 | 100% | decrease |
| jsw-steel | PlasticWaste | FY2023→FY2024 | 674% | increase |
| jsw-steel | Turnover | FY2023→FY2024 | 928% | increase |
| jsw-steel | TotalWasteDisposed | FY2023→FY2024 | 98% | decrease |
| jsw-steel | IsThereAMechanismAvailableToReceiveAndRedressGrievancesForOtherThanPermanentEmployees | FY2023→FY2024 | 100% | decrease |
| jsw-steel | TotalScope2Emissions | FY2023→FY2024 | 56% | decrease |
| jsw-steel | TotalNumberOfAffectedWorkers | FY2023→FY2024 | 67% | decrease |
| jsw-steel | NumberOfCountriesWhereMarketServedByTheEntity | FY2023→FY2024 | 88% | increase |
| jsw-steel | WaterIntensityPerRupeeOfTurnover | FY2023→FY2024 | 100% | decrease |
| jsw-steel | TotalScope3Emissions | FY2023→FY2024 | 444% | increase |
| jsw-steel | PercentageOfSourcedDirectlyFromWithinTheDistrictAndNeighbouringDistricts | FY2023→FY2024 | 2221% | increase |
| jsw-steel | TotalScope1AndScope2EmissionsIntensityPerRupeeOfTurnover | FY2023→FY2024 | 100% | decrease |
| jsw-steel | PercentageOfChildLabourOfValueChainPartnersP5 | FY2024→FY2025 | 65% | decrease |
| jsw-steel | PlasticWaste | FY2024→FY2025 | 196% | increase |
| jsw-steel | TotalElectricityConsumptionFromRenewableSources | FY2024→FY2025 | 66% | increase |
| jsw-steel | PercentageOfComplaintsInRespectOfNumberOfEmployeesOrWorker | FY2024→FY2025 | 342% | increase |
| jsw-steel | WaterWithdrawalByGroundwater | FY2024→FY2025 | 429% | increase |
*... 271 more*

> **YOUR COMMENT:** *(type here — leave blank if no issues)*

---

## 3. PDF Patches Applied

Values the parser stored from XBRL that were overridden by PDF-confirmed data.

### Tata Steel

| Year | Metric | Patched value | Raw PDF value | Unit | Note |
|:----|:-------|:-------------|:-------------|:-----|:-----|
| FY2023 | TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput | 2.21 | 2.21 | tCO2e/tcs | XBRL value of 61 was a filing error. PDF-confirmed: 2.21 tCO2e/tcs fro |
| FY2023 | TrainingCoverage_Employees_HealthSafety | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% permanent employees trained on health |
| FY2023 | TrainingCoverage_Employees_SkillUpgradation | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% permanent employees trained on skill  |
| FY2023 | TrainingCoverage_Workers_HealthSafety | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% permanent workers trained on health & |
| FY2023 | TrainingCoverage_Workers_SkillUpgradation | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% permanent workers trained on skill up |
| FY2024 | AmountOfTotalSales | 137284.33 | 1372843287397.3 | INR (absolute rupees in XBRL) | XBRL filed in absolute rupees. Converted: raw / 1e7 = 1,37,284 Crore. |
| FY2024 | TotalRevenueOfTheCompany | 140987.43 | 1409874287723.51 | INR (absolute rupees in XBRL) | XBRL filed in absolute rupees. PDF confirms 1,40,987.43 Crore (Page 4) |
| FY2024 | RevenueFromOperations | 140987.43 | 1409874287725.64 | INR (absolute rupees in XBRL) | XBRL filed in absolute rupees. PDF confirms 1,40,987.43 Crore (Page 4) |
| FY2024 | EnergyIntensityPerRupeeOfTurnover | None | 0.0003872419 | GJ/Rs (inferred) | PDF reports 0.0043 PJ/Rs Crore; our 0.000387 GJ/Rs = 0.00387 PJ/Crore  |
| FY2024 | EnergyIntensityPerRupeeOfTurnoverAdjustingForPurchasingPowerParity | None | 8860.87 | GJ/Million USD (inferred) | PDF reports 0.0098 PJ/Million USD; our 8,860 GJ/Million USD = 0.00886  |
| FY2024 | WasteIntensityPerRupeeOfTurnoverAdjustingForPurchasingPowerParity | 0.000273 | 0.000273 |  | XBRL stored 2.73e-5; PDF confirms 0.000273 (Page 65). 10x correction a |
| FY2024 | TotalScope3EmissionsPerRupeeOfTurnover | 0.0001 | 0.0001 |  | XBRL stored 1e-5; PDF confirms 0.0001 MnT/Cr (Page 69). 10x correction |
| FY2024 | Sox | 38.0 | 38 | Kilotonnes/year | Not in FY2024 XBRL; extracted from PDF (standalone) |
| FY2024 | Nox | 20.0 | 20 | Kilotonnes/year | Not in FY2024 XBRL; extracted from PDF (standalone) |
| FY2024 | TrainingCoverage_Employees_HealthSafety | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% permanent employees trained on health |
| FY2024 | TrainingCoverage_Employees_SkillUpgradation | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% permanent employees trained on skill  |
| FY2024 | TrainingCoverage_Workers_HealthSafety | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% permanent workers trained on health & |
| FY2024 | TrainingCoverage_Workers_SkillUpgradation | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% permanent workers trained on skill up |
| FY2025 | NumberOfWorkersOrWhoseFamilyMembersRehabilitatedAndPlacedInSuitableEmployment | 24.0 | 24 |  | XBRL had 19 (consolidated figure). PDF standalone FY2024-25 = 24 (Prin |
| FY2025 | EnergyIntensityPerRupeeOfTurnoverAdjustingForPurchasingPowerParity | None | 9160.39 | GJ/Million USD (inferred) | PDF reports 0.0092 PJ/Million USD; our 9,160 GJ/Million USD = 0.00916  |
| FY2025 | WaterDischargeToGroundwater | 3000.0 | 3 | Million Litres | XBRL filed as 0; PDF reports 3 Million Litres = 3,000 kL (Principle 6, |
| FY2025 | WaterDischargeToGroundwaterWithTreatment | 3000.0 | 3 | Million Litres | XBRL filed as 0; PDF reports 3 Million Litres = 3,000 kL (Principle 6, |
| FY2025 | NetWorth | None | 1380415390970.18 |  | XBRL FY2025 tag contains FY2024 comparative value (1,38,041.53 Crore). |
| FY2025 | Sox | 46.0 | 46 | Kilotonnes/year | Not in FY2025 XBRL; extracted from PDF (standalone) |
| FY2025 | Nox | 24.0 | 24 | Kilotonnes/year | Not in FY2025 XBRL; extracted from PDF (standalone) |
| FY2025 | TrainingCoverage_Employees_HealthSafety | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% permanent employees trained on health |
| FY2025 | TrainingCoverage_Employees_SkillUpgradation | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% permanent employees trained on skill  |
| FY2025 | TrainingCoverage_Workers_HealthSafety | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% permanent workers trained on health & |
| FY2025 | TrainingCoverage_Workers_SkillUpgradation | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% permanent workers trained on skill up |

> **YOUR COMMENT:** *(type here — leave blank if no issues)*

### JSW Steel

| Year | Metric | Patched value | Raw PDF value | Unit | Note |
|:----|:-------|:-------------|:-------------|:-----|:-----|
| FY2023 | Turnover | 130039.0 | 130039000000 | INR (absolute rupees in XBRL, 10x u | XBRL filed raw 130039000000 — 10x lower than expected absolute INR. PD |
| FY2023 | TrainingCoverage_Employees_HealthSafety | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% permanent employees trained on H&S (P |
| FY2023 | TrainingCoverage_Employees_SkillUpgradation | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% permanent employees trained on skill  |
| FY2023 | TrainingCoverage_Workers_HealthSafety | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% permanent workers trained on H&S (Pri |
| FY2023 | TrainingCoverage_Workers_SkillUpgradation | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% permanent workers trained on skill up |
| FY2024 | TotalRevenueOfTheCompany | 133609.0 | 1336090000000 | INR (absolute rupees in XBRL) | XBRL filed in absolute rupees. PDF Page 4 confirms 1,33,609 Crore. Con |
| FY2024 | PercentageOfCostIncurredOnWellBeingMeasuresWithRespectToTotalRevenueOfTheCompany | 0.035 | 0.00035 |  | XBRL rounded to 0.04%; PDF Page 14 explicitly states 0.035%. Corrected |
| FY2024 | RevenueFromOperations | 133609.0 | 1336090000000 | INR (absolute rupees in XBRL) | XBRL filed in absolute rupees. PDF Page 4 confirms 1,33,609 Crore. Con |
| FY2024 | WaterIntensityPerRupeeOfTurnover | 0.0389 | 0.0389 | litres per rupee of turnover | PDF Page 24 confirms 0.0389 L/₹. XBRL stored as kL/₹ (3.89951e-05); re |
| FY2024 | TotalScope3EmissionsPerRupeeOfTurnover | 5.21e-06 | 0.00000521 | kgCO2/₹ (from PDF), stored as tCO2/ | PDF Page 28 reports 0.00521 kgCO2/₹ = 5.21e-06 tCO2/₹. Our stored valu |
| FY2024 | PercentageOfSourcedDirectlyFromWithinTheDistrictAndNeighbouringDistricts | 65.0 | 0.65 |  | PDF Page 31 confirms 65% but labels it as sourcing 'directly from with |
| FY2024 | Turnover | 133609.0 | 1336090000000 | INR (absolute rupees in XBRL) | XBRL filed in absolute rupees. PDF Page 4 confirms 1,33,609 Crore. Con |
| FY2024 | IsThereAMechanismAvailableToReceiveAndRedressGrievancesForPermanentWorkers | True | true |  | XBRL filed as 0/false (error). PDF Page 15 explicitly states 'Yes'. Co |
| FY2024 | IsThereAMechanismAvailableToReceiveAndRedressGrievancesForOtherThanPermanentEmployees | True | true |  | XBRL filed as 0/false (error). PDF Page 15 explicitly states 'Yes'. Co |
| FY2024 | Sox | 43.8738 | 1.66 | kg/tcs | Not in FY2024 XBRL; PDF: 1.66 kg/tcs × 26,430,000 t production = 43.87 |
| FY2024 | Nox | 31.4517 | 1.19 | kg/tcs | Not in FY2024 XBRL; PDF: 1.19 kg/tcs × 26,430,000 t production = 31.45 |
| FY2024 | TrainingCoverage_Employees_HealthSafety | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% permanent employees trained on H&S (P |
| FY2024 | TrainingCoverage_Employees_SkillUpgradation | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% permanent employees trained on skill  |
| FY2024 | TrainingCoverage_Workers_HealthSafety | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% permanent workers trained on H&S (Pri |
| FY2024 | TrainingCoverage_Workers_SkillUpgradation | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% permanent workers trained on skill up |
| FY2025 | TotalRevenueOfTheCompany | 125678.0 | 1256780000000 | INR (absolute rupees in XBRL) | XBRL filed in absolute rupees (same pattern as FY2024). raw / 1e7 = 12 |
| FY2025 | PercentageOfCostIncurredOnWellBeingMeasuresWithRespectToTotalRevenueOfTheCompany | 0.0253 | 0.000253 |  | XBRL rounded to 0.03%; PDF Page 9 explicitly states 0.0253%. Corrected |
| FY2025 | RevenueFromOperations | 125678.0 | 1256780000000 | INR (absolute rupees in XBRL) | XBRL filed in absolute rupees (same pattern as FY2024). raw / 1e7 = 12 |
| FY2025 | WaterIntensityPerRupeeOfTurnover | 0.0424 | 0.0423703 | litres per rupee of turnover | XBRL stored as kL/₹ (4.23703e-05); converted to L/₹ = 0.0424 for consi |
| FY2025 | Turnover | 125678.0 | 1256780000000 | INR (absolute rupees in XBRL) | XBRL filed in absolute rupees (same pattern as FY2024). raw / 1e7 = 12 |
| FY2025 | WhetherTheWasteCollectionPlanIsInLineWithTheExtendedProducerResponsibilityPlanSubmittedToPollutionControlBoards | True | true |  | XBRL filed as 0/false (error). PDF Page 8 confirms 'Yes' — waste colle |
| FY2025 | Sox | 46.1314 | 1.66 | kg/tcs | Not in FY2025 XBRL; PDF: 1.66 kg/tcs × 27,790,000 t production = 46.13 |
| FY2025 | Nox | 31.9585 | 1.15 | kg/tcs | Not in FY2025 XBRL; PDF: 1.15 kg/tcs × 27,790,000 t production = 31.95 |
| FY2025 | TrainingCoverage_Employees_HealthSafety | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% permanent employees trained on H&S (P |
| FY2025 | TrainingCoverage_Employees_SkillUpgradation | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% permanent employees trained on skill  |
| FY2025 | TrainingCoverage_Workers_HealthSafety | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% permanent workers trained on H&S (Pri |
| FY2025 | TrainingCoverage_Workers_SkillUpgradation | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% permanent workers trained on skill up |

> **YOUR COMMENT:** *(type here — leave blank if no issues)*

### SAIL

| Year | Metric | Patched value | Raw PDF value | Unit | Note |
|:----|:-------|:-------------|:-------------|:-----|:-----|
| FY2023 | WaterIntensityPerRupeeOfTurnover | 0.053 | 0.053 | L/Rs | PDF confirms 0.053 L/₹ (litres per rupee of turnover). XBRL stored 0.0 |
| FY2023 | ParticulateMatter | 10.4253 | 0.57 | kg/tcs | FY2023 XBRL reported as concentration range (31–99 mg/Nm³). FY2024 BRS |
| FY2023 | TrainingCoverage_Employees_HealthSafety | 30.4 | 30.4 | % | Not in XBRL. PDF-confirmed: 30.4% permanent employees trained on H&S ( |
| FY2023 | TrainingCoverage_Employees_SkillUpgradation | 32.6 | 32.6 | % | Not in XBRL. PDF-confirmed: 32.6% permanent employees trained on skill |
| FY2023 | TrainingCoverage_Workers_HealthSafety | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% permanent workers trained on H&S (Pri |
| FY2023 | AverageTrainingHours_Employees | 4.88 | 4.88 | hours | Not in XBRL. PDF: avg training hours per employee = 4.88 (Principle 3, |
| FY2023 | AverageTrainingHours_Workers | 9.18 | 9.18 | hours | Not in XBRL. PDF: avg training hours per worker = 9.18 (Principle 3, P |
| FY2023 | TotalTrainingPersonHours | 894411 | 894411 | person-hours | Not in XBRL. PDF: 2,88,881 (employees) + 6,05,530 (workers) = 8,94,411 |
| FY2024 | AmountOfAccountsPayableDuringTheYear | None | 5429840.58 |  | XBRL value 5.43e+06 INR Crore is a filing error (wrong unit). PDF only |
| FY2024 | AmountOfTotalSales | 104545.09 | 104545.09 | INR Crore | XBRL stored 1,725 Crore (partial/wrong). PDF Section A Q24 confirms 1, |
| FY2024 | TotalRevenueOfTheCompany | 104545.09 | 104545.09 | INR Crore | XBRL stored 1,05,375 Crore; PDF Section A Q24 confirms 1,04,545.09 Cro |
| FY2024 | RevenueFromOperations | 109672.5 | 109672.5 | INR Crore | XBRL stored 10x too high (1,096,725 vs 109,672.5 Crore). PDF Principle |
| FY2024 | TotalElectricityConsumptionFromNonRenewableSources | 613900000.0 | 613900 | TJ | XBRL stored 143,445 TJ (143,445,000 GJ). PDF Principle 6 Q1 Page 23 sh |
| FY2024 | WaterIntensityPerRupeeOfTurnover | None | 52.33 | L/Rs (assumed) | XBRL value 52.33 L/₹ is a filing error (1000× FY2023 value of 0.053).  |
| FY2024 | ParticulateMatter | 11.1592 | 0.58 | kg/tcs | XBRL unit tag showed µg/m³ (incorrect); PDF confirms 0.58 kg/tcs. SAIL |
| FY2024 | TotalScope1AndScope2EmissionsIntensityPerRupeeOfTurnover | 502.0 | 502 | tCO2e/INR Crore | XBRL stored 50.21 (10x low). PDF Principle 6 Q7 confirms 502 tCO2e/INR |
| FY2024 | TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput | 2.8 | 2.8 | tCO2e/tonne of crude steel | XBRL filed as 0 (error); PDF confirms 2.8 tCO2e/tcs |
| FY2024 | WasteIntensityPerRupeeOfTurnover | 128.0 | 128 | Tonnes/INR Crore | XBRL stored 12.77 (10x low). PDF Principle 6 Q9 confirms 128 Tonnes/IN |
| FY2024 | Sox | 21.164 | 1.10 | kg/tcs | Not in FY2024 XBRL; PDF: 1.10 kg/tcs × 19,240,000 t = 21.164 kt. SAIL  |
| FY2024 | Nox | 14.6224 | 0.76 | kg/tcs | Not in FY2024 XBRL; PDF: 0.76 kg/tcs × 19,240,000 t = 14.6224 kt |
| FY2024 | TrainingCoverage_Employees_HealthSafety | 40.6 | 40.6 | % | Not in XBRL. PDF: 40.6% permanent employees trained on H&S (Principle  |
| FY2024 | TrainingCoverage_Employees_SkillUpgradation | 34.7 | 34.7 | % | Not in XBRL. PDF: 34.7% permanent employees trained on skill upgradati |
| FY2024 | TrainingCoverage_Workers_HealthSafety | 100.0 | 100 | % | Not in XBRL. PDF: 100% permanent workers trained on H&S (Principle 3,  |
| FY2025 | AmountOfAccountsPayableDuringTheYear | None | 47141465500000 |  | XBRL value 4.71e+13 INR Crore is a filing error (wrong unit). PDF only |
| FY2025 | CostOfGoodsOrServicesProcuredDuringTheYear | 50394.9 | 50394.9 | INR Crore | XBRL filed in absolute INR (not Crore). PDF confirms: 50,394.9 Crore ( |
| FY2025 | AmountOfSalesToDealersOrDistributors | 16183.0 | 16183.0 | INR Crore | XBRL filed in absolute INR (not Crore). PDF confirms: 16,183 Crore (Pr |
| FY2025 | AmountOfTotalSales | 101716.0 | 101716.0 | INR Crore | XBRL filed in absolute INR (not Crore). PDF confirms: 1,01,716 Crore ( |
| FY2025 | AmountOfSalesToTopTenDealersOrDistributors | 4284.7 | 4284.7 | INR Crore | XBRL filed in absolute INR (not Crore). PDF confirms: 4,284.7 Crore (P |
| FY2025 | AmountOfTotalSalesToDealersOrDistributors | 16183.0 | 16183.0 | INR Crore | XBRL filed in absolute INR (not Crore). PDF confirms: 16,183 Crore (Pr |
| FY2025 | AmountOfPurchasesFromRelatedParties | 4333.9 | 4333.9 | INR Crore | XBRL filed in absolute INR (not Crore). PDF confirms: 4,333.9 Crore (P |
| FY2025 | AmountOfTotalPurchasesForShareOfRelatedPartyTransactions | 50394.9 | 50394.9 | INR Crore | XBRL filed in absolute INR (not Crore). PDF confirms: 50,394.9 Crore ( |
| FY2025 | AmountOfSalesToRelatedParties | 85.53 | 85.53 | INR Crore | XBRL filed in absolute INR (not Crore). PDF confirms: 85.53 Crore (Pri |
| FY2025 | AmountOfTotalSalesForShareOfRelatedPartyTransactions | 101716.0 | 101716.0 | INR Crore | XBRL filed in absolute INR (not Crore). PDF confirms: 1,01,716 Crore ( |
| FY2025 | AmountOfLoansAndAdvancesGivenToRelatedParties | 44.8 | 44.8 | INR Crore | XBRL filed in absolute INR (not Crore). PDF confirms: 44.8 Crore (Prin |
| FY2025 | AmountOfTotalLoansAndAdvances | 5583.78 | 5583.78 | INR Crore | XBRL filed in absolute INR (not Crore). PDF confirms: 5,583.78 Crore ( |
| FY2025 | AmountOfInvestmentsInRelatedParties | 1386.43 | 1386.43 | INR Crore | XBRL filed in absolute INR (not Crore). PDF confirms: 1,386.43 Crore ( |
| FY2025 | AmountOfTotalInvestments | 1758.93 | 1758.93 | INR Crore | XBRL filed in absolute INR (not Crore). PDF confirms: 1,758.93 Crore ( |
| FY2025 | AmountOfCostIncurredOnWellBeingMeasures | 1464.71 | 1464.71 | INR Crore | XBRL filed in absolute INR (not Crore). PDF confirms: 1,464.71 Crore ( |
| FY2025 | TotalRevenueOfTheCompany | 101716.0 | 101716.0 | INR Crore | XBRL filed in absolute INR (not Crore). PDF confirms: 1,01,716 Crore ( |
| FY2025 | GrossWagesPaidToFemale | 559.368 | 559.368 | INR Crore | XBRL filed in absolute INR (not Crore). PDF confirms: 559.368 Crore (P |
| FY2025 | TotalWagesPaid | 9039.97 | 9039.97 | INR Crore | XBRL filed in absolute INR (not Crore). PDF confirms: 9,039.97 Crore ( |
| FY2025 | RevenueFromOperations | 101716.0 | 101716 | INR Crore | XBRL stored in absolute INR (filing error). PDF Section A Q24 confirms |
| FY2025 | ParticulateMatter | 10.7352 | 0.56 | kg/tcs | XBRL unit tag showed µg/m³ (incorrect); PDF confirms kg/tcs. |
| FY2025 | TotalScope1AndScope2EmissionsIntensityPerRupeeOfTurnover | 578.014 | 578.014 | tCO2e/INR Crore | XBRL stored as kg/Rs (0.0578014). Converted: 0.0578014 kg/Rs ÷ 1000 ×  |
| FY2025 | WasteIntensityPerRupeeOfTurnover | 143.5 | 143.5 | Tonnes/INR Crore | XBRL stored as kg/Rs (0.0143497). Converted: 0.0143497 kg/Rs ÷ 1000 ×  |
| FY2025 | Sox | 18.2115 | 0.95 | kg/tcs | Not in FY2025 XBRL; PDF: 0.95 kg/tcs × 19,170,000 t = 18.2115 kt |
| FY2025 | Nox | 15.336 | 0.80 | kg/tcs | Not in FY2025 XBRL; PDF: 0.80 kg/tcs × 19,170,000 t = 15.336 kt |
| FY2025 | TrainingCoverage_Employees_HealthSafety | 15.0 | 15 | % | Not in XBRL. PDF: 15% permanent employees trained on H&S (Principle 3, |
| FY2025 | TrainingCoverage_Employees_SkillUpgradation | 34.0 | 34 | % | Not in XBRL. PDF: 34% permanent employees trained on skill upgradation |
| FY2025 | TrainingCoverage_Workers_HealthSafety | 100.0 | 100 | % | Not in XBRL. PDF: 100% permanent workers trained on H&S (Principle 3,  |

> **YOUR COMMENT:** *(type here — leave blank if no issues)*

### Jindal Stainless

| Year | Metric | Patched value | Raw PDF value | Unit | Note |
|:----|:-------|:-------------|:-------------|:-----|:-----|
| FY2023 | WaterIntensityPerRupeeOfTurnover | 335.0 | 335 | KL/Rs.Crore | Unit is kL/Rs.Crore (PDF confirmed). L/₹ equivalent: 0.0335000 L/₹ (=  |
| FY2023 | WasteRecoveredThroughOtherRecoveryOperations | 201.0 | 201 | MT | XBRL stored 489.94 MT. PDF Page 29 sum of 'Other recovery operations'  |
| FY2023 | TrainingCoverage_Employees_HealthSafety | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% trained on H&S (Pages 11, 18; combine |
| FY2023 | TrainingCoverage_Employees_SkillUpgradation | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% trained on skill upgradation (Pages 1 |
| FY2023 | TrainingCoverage_Workers_HealthSafety | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% trained on H&S (Pages 11, 18) |
| FY2023 | TrainingCoverage_Workers_SkillUpgradation | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% trained on skill upgradation (Pages 1 |
| FY2023 | TotalTrainingPersonHours | 150000 | 150000 | person-hours | Not in XBRL. PDF: >1,50,000 total training hours (Pages 11, 18). Store |
| FY2024 | TotalRevenueOfTheCompany | 38356.0 | 38356 | INR Crore | XBRL stored 1,000 Crore (filing error). PDF Section A Q24 confirms 38, |
| FY2024 | EnergyIntensityPerRupeeOfTurnover | 916.2506288456 | 916.2506288456 | GJ/Crore INR | PDF Principle 6, El-1 confirms 916.25 GJ/Crore INR. Jindal files inten |
| FY2024 | EnergyIntensityPerRupeeOfTurnoverAdjustingForPurchasingPowerParity | 20524.02 | 20524.02 | GJ/Crore USD | PDF Principle 6, El-1 confirms 20,524.02 GJ/Crore USD. (Phase 3c ITEM_ |
| FY2024 | WaterIntensityPerRupeeOfTurnover | 333.0084732506 | 333.0084732506 | KL/Rs.Crore | Unit is kL/Rs.Crore (PDF confirmed). L/₹ equivalent: 0.0333000 L/₹ (=  |
| FY2024 | WaterIntensityPerRupeeOfTurnoverAdjustingForPurchasingPowerParity | 7459.3908 | 7459.3908 | kL/Crore USD | PDF Principle 6, El-3 confirms 7,459.39 kL/Crore USD. Consistent with  |
| FY2024 | TotalScope1AndScope2EmissionsIntensityPerRupeeOfTurnoverAdjustedForPurchasingPowerParity | 2207.2226 | 2207.2226 | tCO2e/Crore USD | PDF Principle 6, El-7 confirms 2,207.22 tCO2e/Crore USD. (Phase 3c ITE |
| FY2024 | WasteIntensityPerRupeeOfTurnover | 41.3134662113 | 41.3134662113 | MT/Crore INR | PDF Principle 6, El-9 confirms 41.31 MT/Crore INR. (Phase 3c ITEM_29) |
| FY2024 | WasteIntensityPerRupeeOfTurnoverAdjustingForPurchasingPowerParity | 925.4218 | 925.4218 | MT/Crore USD | PDF Principle 6, El-9 confirms 925.42 MT/Crore USD. (Phase 3c ITEM_28) |
| FY2024 | TotalScope3EmissionsPerRupeeOfTurnover | 87.22 | 87.22 | tCO2e/Crore INR | PDF Principle 6, LI-2 confirms 87.22 tCO2e/Crore INR. (Phase 3c ITEM_2 |
| FY2024 | Sox | 3.072064 | 3072.064 | MT | Not in FY2024 XBRL; extracted from PDF: 3072.064 MT / 1000 = 3.072 kt |
| FY2024 | Nox | 1.78258 | 1782.58 | MT | Not in FY2024 XBRL; extracted from PDF: 1782.58 MT / 1000 = 1.783 kt |
| FY2024 | TrainingCoverage_Employees_HealthSafety | 50.04 | 50.04 | % | Not in XBRL. PDF Principle 3, El-8: 50.04% trained on H&S (total headc |
| FY2024 | TrainingCoverage_Employees_SkillUpgradation | 32.21 | 32.21 | % | Not in XBRL. PDF Principle 3, El-8: 32.21% trained on skill upgradatio |
| FY2024 | TrainingCoverage_Workers_HealthSafety | 19.27 | 19.27 | % | Not in XBRL. PDF Principle 3, El-8: 19.27% workers trained on H&S |
| FY2024 | TrainingCoverage_Workers_SkillUpgradation | 3.73 | 3.73 | % | Not in XBRL. PDF Principle 3, El-8: 3.73% workers trained on skill upg |
| FY2024 | TotalTrainingPersonHours | 166000 | 166000 | person-hours | Not in XBRL. PDF Performance Section: >1,66,000 total training hours.  |
| FY2025 | NumberOfDealersOrDistributorsToWhomSalesAreMade | 367.0 | 367 |  | XBRL stored 478 (which is the trading houses count). PDF Page 16 repor |
| FY2025 | TotalRevenueOfTheCompany | 40181.68 | 40181.68 | INR Crore | XBRL stored Net Worth (16,197 Crore) instead of Turnover. PDF Page 4 c |
| FY2025 | RevenueFromOperations | 40181.68 | 401820000000 | INR (absolute rupees in XBRL) | XBRL filed in absolute rupees. PDF Page 4 confirms 401,81,68,00,000 IN |
| FY2025 | EnergyIntensityPerRupeeOfTurnover | 7.97546e-05 | 0.0000797546 | GJ/Rs (stored); 797.55 GJ/Crore INR | PDF Page 33 confirms 797.55 GJ/Crore INR. Our 7.97546e-05 GJ/Rs × 1e7  |
| FY2025 | EnergyIntensityPerRupeeOfTurnoverAdjustingForPurchasingPowerParity | 0.001647742 | 0.001647742 | GJ/Rs (stored); 16,477.42 GJ/Crore  | PDF Page 33 confirms 16,477.42 GJ/Crore INR. Our 0.00164774 × 1e7 = 16 |
| FY2025 | WaterWithdrawalByGroundwater | 19102.0 | 19102 | kL | XBRL reversed FY2024 and FY2025 values. PDF Page 34 confirms 19,102 kL |
| FY2025 | WaterIntensityPerRupeeOfTurnover | 358.67 | 358.67 | KL/Rs.Crore | Unit is kL/Rs.Crore (PDF confirmed). L/₹ equivalent: 0.0358670 L/₹ (=  |
| FY2025 | WaterIntensityPerRupeeOfTurnoverAdjustingForPurchasingPowerParity | 0.000741006 | 0.000741006 | kL/Rs (stored); 7,410.06 kL/Crore U | PDF Page 34 confirms 7,410.06 kL/Crore USD. Our 0.000741006 × 1e7 = 7, |
| FY2025 | TotalScope1AndScope2EmissionsIntensityPerRupeeOfTurnover | 9.0048e-06 | 0.0000090048 | tCO2e/Rs (stored); 90.05 tCO2e/Cror | PDF Page 36 confirms 90.05 tCO2e/Crore INR. Our 9.0048e-06 × 1e7 = 90. |
| FY2025 | TotalScope1AndScope2EmissionsIntensityPerRupeeOfTurnoverAdjustedForPurchasingPowerParity | 0.000186041 | 0.000186041 | tCO2e/Rs (stored); 1,860.41 tCO2e/C | PDF Page 36 confirms 1,860.41 tCO2e/Crore USD. Our 0.000186041 × 1e7 = |
| FY2025 | WasteIntensityPerRupeeOfTurnover | 4.8416e-06 | 0.0000048416 | MT/Rs (stored); 48.42 MT/Crore INR | PDF Page 37 confirms 48.42 MT/Crore INR. Our 4.8416e-06 × 1e7 = 48.42  |
| FY2025 | WasteIntensityPerRupeeOfTurnoverAdjustingForPurchasingPowerParity | 960.87 | 960.87 | MT/Crore USD | PDF Page 37 confirms 960.87 MT/Crore USD. Value matches directly. (Pha |
| FY2025 | TotalScope3EmissionsPerRupeeOfTurnover | 8.0051e-06 | 0.0000080051 | tCO2e/Rs (stored); 80.05 tCO2e/Cror | PDF Page 41 confirms 80.05 tCO2e/Crore INR. Our 8.0051e-06 × 1e7 = 80. |
| FY2025 | Sox | 4.58069 | 4580.69 | MT | Not in FY2025 XBRL; extracted from PDF: 4580.69 MT / 1000 = 4.581 kt |
| FY2025 | Nox | 2.52748 | 2527.48 | MT | Not in FY2025 XBRL; extracted from PDF: 2527.48 MT / 1000 = 2.527 kt |
| FY2025 | TrainingCoverage_Employees_HealthSafety | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% employees trained on H&S (Pages 12, 2 |
| FY2025 | TrainingCoverage_Employees_SkillUpgradation | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% employees trained on skill upgradatio |
| FY2025 | TrainingCoverage_Workers_HealthSafety | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% workers trained on H&S (Pages 12, 22) |
| FY2025 | TrainingCoverage_Workers_SkillUpgradation | 100.0 | 100 | % | Not in XBRL. PDF-confirmed: 100% workers trained on skill upgradation  |
| FY2025 | TotalTrainingPersonHours | 166000 | 166000 | person-hours | Not in XBRL. PDF: 1,66,000 total training person-hours (Pages 12, 22). |

> **YOUR COMMENT:** *(type here — leave blank if no issues)*

---

## 4. Key Metrics by Financial Year

One table per year. Each row = one metric. Last column lists concerns for specific companies.
Add your comment in the `> YOUR COMMENT` block after each table.

### FY2023

| Metric | Unit | Tata Steel | JSW Steel | SAIL | Jindal Stainless | Concerns |
|:-------|:-----|----------:|----------:|-----:|-----------------:|:---------|
| Scope 1 GHG | tCO2e | 75,750,000 | 46,941,683 | 47,603,938 | 2,584,460 |  |
| Scope 2 GHG | tCO2e | 5,200,000 | 2,417,702 | 3,020,822 | 735,913.0 |  |
| GHG Intensity | tCO2e/tcs | 2.210 📄 | 2.360 | 2.800 | 2.100 | **Tata Steel:** PDF-patched; XBRL value of 61 was a filing error. PDF-confirmed: 2.21 tCO2e/tcs from ESG factsheet in FY2022-23 Integrated Report (co |
| Total Energy | GJ | 857,000,000 | 494,384,430 | 591,044,300 | 30,275,547 |  |
| Renewable Energy | GJ | 1,000,000 | 1,427,160 | 127,200.0 | 12,743.0 |  |
| SOx | kilotonnes | 51.000 | 40.813 | null ⚠️ | 0.851890 | **SAIL:** value nulled; not normalized; SAIL FY2023 reports SOx and NOx as concentration ranges (mg/Nm³), not mass intensity. Cannot convert to kilotonnes witho |
| NOx | kilotonnes | 30.000 | 28.738 | null ⚠️ | 1.981 | **SAIL:** value nulled; not normalized; SAIL FY2023 reports SOx and NOx as concentration ranges (mg/Nm³), not mass intensity. Cannot convert to kilotonnes witho |
| Particulate Matter | kilotonnes | 11.000 | 10.143 | 10.425 📄 | 2.084 | **SAIL:** PDF-patched; FY2023 XBRL reported as concentration range (31–99 mg/Nm³). FY2024 BRSR comparative column shows 0.57 kg/tcs — used as c |
| Water Withdrawal | kL | 201,372,353 | 86,267,847 | 55,285,451 | 11,681,607 |  |
| Water Consumption | kL | 201,372,353 | 51,053,889 | 55,285,451 | 11,681,607 |  |
| Water Intensity | L/₹ or kL/Cr — NOT uniform | 0.080000 | 0.039300 | 0.053000 📄 | 335.000 ⚠️ 📄 | **Tata Steel:** Unit confirmed by PDF as litres/rupee. Not directly comparable to SAIL/Jindal which report kL/Crore.<br>**SAIL:** PDF-patched; PDF confirms 0.053 L/₹ (litres per rupee of turnover). XBRL stored 0.05 — same unit, minor rounding. Consistent with Tat<br>**Jindal Stainless:** not normalized; PDF-patched; Unit is kL/Rs.Crore (PDF confirmed). L/₹ equivalent: 0.0335000 L/₹ (= 335.0 ÷ 10,000,000). For reference: Tata Steel={'F |
| Total Waste | metric tonnes | 20,226,592 | 14,414,261 | 12,724,292 | 1,628,584 |  |
| Waste Recovered | metric tonnes | 20,198,507 | 14,381,621 | 12,906,681 | 862,283.9 |  |
| Waste Disposed | metric tonnes | 90,945.0 | 186,788.0 | 3,671.0 | 766,299.7 |  |
| LTIFR | — | 1.000 | 0.000000 | 0.000000 | 0.000000 | **Tata Steel:** Extracted from dimensional XBRL context D_Employees.<br>**JSW Steel:** LTIFR=0 is implausible given 6 fatalities reported in same year. Likely a filing error or definitional exclusion.<br>**SAIL:** LTIFR=0 is implausible given 11 fatalities. Likely a filing error or different denominator.<br>**Jindal Stainless:** LTIFR=0 with 3 fatalities — likely filing error or definitional difference. |
| Fatalities | — | 7 | 6 | 11 | 3 | **Tata Steel:** Sum of NumberOfFatalities [D_Employees] + [D_Workers] from dimensional XBRL contexts.<br>**JSW Steel:** Sum of NumberOfFatalities [D_Employees] + [D_Workers] from dimensional XBRL contexts.<br>**SAIL:** Sum of NumberOfFatalities [D_Employees] + [D_Workers] from dimensional XBRL contexts.<br>**Jindal Stainless:** Sum of NumberOfFatalities [D_Employees] + [D_Workers] from dimensional XBRL contexts. |
| Total Employees | — | 67,784 | 12,856 | 59,186 | 4,363 | **Tata Steel:** Extracted from multi-dimensional XBRL context D_Gender_Employees_TableA (permanent employees). Parser DCYMain-only extra<br>**JSW Steel:** Extracted from multi-dimensional XBRL context D_Gender_Employees_TableA (permanent employees). Parser DCYMain-only extra<br>**SAIL:** Extracted from multi-dimensional XBRL context D_Gender_Employees_TableA (permanent employees). Parser DCYMain-only extra<br>**Jindal Stainless:** Extracted from multi-dimensional XBRL context D_Gender_Employees_TableA (permanent employees). Parser DCYMain-only extra |
| Female Employees | % | 8.430 | 5.780 | 6.110 | 2.890 | **Tata Steel:** Calculated from female/total employee counts in dimensional XBRL contexts.<br>**JSW Steel:** Calculated from female/total employee counts in dimensional XBRL contexts.<br>**SAIL:** Calculated from female/total employee counts in dimensional XBRL contexts.<br>**Jindal Stainless:** Calculated from female/total employee counts in dimensional XBRL contexts. |
| Training Coverage | % | null ⚠️ | null ⚠️ | null ⚠️ | null ⚠️ | **Tata Steel:** value nulled; not normalized; Training coverage % not found in XBRL for this company-year. To be extracted from PDF.<br>**JSW Steel:** value nulled; not normalized; Training coverage % not found in XBRL for this company-year. To be extracted from PDF.<br>**SAIL:** value nulled; not normalized; Training coverage % not found in XBRL for this company-year. To be extracted from PDF.<br>**Jindal Stainless:** value nulled; not normalized; Training coverage % not found in XBRL for this company-year. To be extracted from PDF. |

> **YOUR COMMENT:** *(type here — leave blank if no issues)*

---

### FY2024

| Metric | Unit | Tata Steel | JSW Steel | SAIL | Jindal Stainless | Concerns |
|:-------|:-----|----------:|----------:|-----:|-----------------:|:---------|
| Scope 1 GHG | tCO2e | 56,000,000 | 52,106,566 | 52,622,079 | 2,992,334 |  |
| Scope 2 GHG | tCO2e | 7,000,000 | 1,061,079 | 2,446,630 | 787,140.2 |  |
| GHG Intensity | tCO2e/tcs | 3.100 | 2.440 | 2.800 📄 | 2.150 | **SAIL:** PDF-patched; XBRL filed as 0 (error); PDF confirms 2.8 tCO2e/tcs |
| Total Energy | GJ | 545,962,401 | 517,690,735 | 614,166,500 | 35,143,709 |  |
| Renewable Energy | GJ | 116,199.0 | 1,981,229 | 266,000.0 | 200,194.0 |  |
| SOx | kilotonnes | 38.000 📄 | 43.874 📄 | 21.164 📄 | 3.072 📄 | **Tata Steel:** PDF-patched; Not in FY2024 XBRL; extracted from PDF (standalone)<br>**JSW Steel:** PDF-patched; Not in FY2024 XBRL; PDF: 1.66 kg/tcs × 26,430,000 t production = 43.8738 kt<br>**SAIL:** PDF-patched; Not in FY2024 XBRL; PDF: 1.10 kg/tcs × 19,240,000 t = 21.164 kt. SAIL switched to mass intensity reporting in FY2024.<br>**Jindal Stainless:** PDF-patched; Not in FY2024 XBRL; extracted from PDF: 3072.064 MT / 1000 = 3.072 kt |
| NOx | kilotonnes | 20.000 📄 | 31.452 📄 | 14.622 📄 | 1.783 📄 | **Tata Steel:** PDF-patched; Not in FY2024 XBRL; extracted from PDF (standalone)<br>**JSW Steel:** PDF-patched; Not in FY2024 XBRL; PDF: 1.19 kg/tcs × 26,430,000 t production = 31.4517 kt<br>**SAIL:** PDF-patched; Not in FY2024 XBRL; PDF: 0.76 kg/tcs × 19,240,000 t = 14.6224 kt<br>**Jindal Stainless:** PDF-patched; Not in FY2024 XBRL; extracted from PDF: 1782.58 MT / 1000 = 1.783 kt |
| Particulate Matter | kilotonnes | 9.000 | 8.309 | 11.159 📄 | 1.313 | **SAIL:** PDF-patched; XBRL unit tag showed µg/m³ (incorrect); PDF confirms 0.58 kg/tcs. SAIL switched from concentration (mg/Nm³) in FY2023 to |
| Water Withdrawal | kL | 102,359,060 | 89,191,228 | 57,396,487 | 13,320,439 |  |
| Water Consumption | kL | 88,350,241 | 52,100,921 | 57,396,487 | 12,772,873 |  |
| Water Intensity | L/₹ or kL/Cr — NOT uniform | 0.000063 | 0.038900 📄 | null ⚠️ | 333.008 ⚠️ 📄 | **Tata Steel:** Unit confirmed by PDF as litres/rupee. Not directly comparable to SAIL/Jindal which report kL/Crore.<br>**JSW Steel:** PDF-patched; PDF Page 24 confirms 0.0389 L/₹. XBRL stored as kL/₹ (3.89951e-05); reverted to L/₹ for consistency with Tata Steel and <br>**SAIL:** value nulled; not normalized; PDF-patched; XBRL value 52.33 L/₹ is a filing error (1000× FY2023 value of 0.053). PDF cross-check did not confirm correct value. Nul<br>**Jindal Stainless:** not normalized; PDF-patched; Unit is kL/Rs.Crore (PDF confirmed). L/₹ equivalent: 0.0333000 L/₹ (= 333.0 ÷ 10,000,000). For reference: Tata Steel={'F |
| Total Waste | metric tonnes | 16,833,524 | 15,211,308 | 14,005,029 | 1,584,619 |  |
| Waste Recovered | metric tonnes | 18,884,589 | 15,076,412 | 14,370,239 | 1,777,700 |  |
| Waste Disposed | metric tonnes | 307,577.0 | 3,108.7 | 2,358.0 | 42,808.4 |  |
| LTIFR | — | 0.490000 | 0.110000 | 0.000000 | 0.040000 | **Tata Steel:** Extracted from dimensional XBRL context D_Employees.<br>**JSW Steel:** Extracted from dimensional XBRL context D_Employees.<br>**SAIL:** SAIL FY2024 employee counts identical to FY2023 — XBRL likely used prior-year context. Verify against PDF. LTIFR=0 also <br>**Jindal Stainless:** Extracted from dimensional XBRL context D_Employees. |
| Fatalities | — | 5 | 2 | 11 | 1 | **Tata Steel:** Sum of NumberOfFatalities [D_Employees] + [D_Workers] from dimensional XBRL contexts.<br>**JSW Steel:** Sum of NumberOfFatalities [D_Employees] + [D_Workers] from dimensional XBRL contexts.<br>**SAIL:** Sum of NumberOfFatalities [D_Employees] + [D_Workers] from dimensional XBRL contexts.<br>**Jindal Stainless:** Sum of NumberOfFatalities [D_Employees] + [D_Workers] from dimensional XBRL contexts. |
| Total Employees | — | 44,476 | 13,301 | 59,186 | 5,737 | **Tata Steel:** Extracted from multi-dimensional XBRL context D_Gender_Employees_TableA (permanent employees). Parser DCYMain-only extra<br>**JSW Steel:** Extracted from multi-dimensional XBRL context D_Gender_Employees_TableA (permanent employees). Parser DCYMain-only extra<br>**SAIL:** Extracted from multi-dimensional XBRL context D_Gender_Employees_TableA (permanent employees). Parser DCYMain-only extra<br>**Jindal Stainless:** Extracted from multi-dimensional XBRL context D_Gender_Employees_TableA (permanent employees). Parser DCYMain-only extra |
| Female Employees | % | 8.360 | 6.450 | 6.110 | 3.540 | **Tata Steel:** Calculated from female/total employee counts in dimensional XBRL contexts.<br>**JSW Steel:** Calculated from female/total employee counts in dimensional XBRL contexts.<br>**SAIL:** Calculated from female/total employee counts in dimensional XBRL contexts.<br>**Jindal Stainless:** Calculated from female/total employee counts in dimensional XBRL contexts. |
| Training Coverage | % | null ⚠️ | null ⚠️ | null ⚠️ | null ⚠️ | **Tata Steel:** value nulled; not normalized; Training coverage % not found in XBRL for this company-year. To be extracted from PDF.<br>**JSW Steel:** value nulled; not normalized; Training coverage % not found in XBRL for this company-year. To be extracted from PDF.<br>**SAIL:** value nulled; not normalized; Training coverage % not found in XBRL for this company-year. To be extracted from PDF.<br>**Jindal Stainless:** value nulled; not normalized; Training coverage % not found in XBRL for this company-year. To be extracted from PDF. |

> **YOUR COMMENT:** *(type here — leave blank if no issues)*

---

### FY2025

| Metric | Unit | Tata Steel | JSW Steel | SAIL | Jindal Stainless | Concerns |
|:-------|:-----|----------:|----------:|-----:|-----------------:|:---------|
| Scope 1 GHG | tCO2e | 61,000,000 | 53,100,752 | 52,178,648 | 2,995,798 |  |
| Scope 2 GHG | tCO2e | 5,000,000 | 1,653,057 | 4,796,073 | 622,511.0 |  |
| GHG Intensity | tCO2e/tcs | 3.200 | 2.436 | 3.010 | 1.850 |  |
| Total Energy | GJ | 587,567,890 | 529,209,357 | 519,431,000 | 32,046,976 |  |
| Renewable Energy | GJ | 384,862.0 | 3,227,578 | 1,400,000 | 1,307,231 |  |
| SOx | kilotonnes | 46.000 📄 | 46.131 📄 | 18.212 📄 | 4.581 📄 | **Tata Steel:** PDF-patched; Not in FY2025 XBRL; extracted from PDF (standalone)<br>**JSW Steel:** PDF-patched; Not in FY2025 XBRL; PDF: 1.66 kg/tcs × 27,790,000 t production = 46.1314 kt<br>**SAIL:** PDF-patched; Not in FY2025 XBRL; PDF: 0.95 kg/tcs × 19,170,000 t = 18.2115 kt<br>**Jindal Stainless:** PDF-patched; Not in FY2025 XBRL; extracted from PDF: 4580.69 MT / 1000 = 4.581 kt |
| NOx | kilotonnes | 24.000 📄 | 31.959 📄 | 15.336 📄 | 2.527 📄 | **Tata Steel:** PDF-patched; Not in FY2025 XBRL; extracted from PDF (standalone)<br>**JSW Steel:** PDF-patched; Not in FY2025 XBRL; PDF: 1.15 kg/tcs × 27,790,000 t production = 31.9585 kt<br>**SAIL:** PDF-patched; Not in FY2025 XBRL; PDF: 0.80 kg/tcs × 19,170,000 t = 15.336 kt<br>**Jindal Stainless:** PDF-patched; Not in FY2025 XBRL; extracted from PDF: 2527.48 MT / 1000 = 2.527 kt |
| Particulate Matter | kilotonnes | 8.000 | 8.765 | 10.735 📄 | 1.601 | **SAIL:** PDF-patched; XBRL unit tag showed µg/m³ (incorrect); PDF confirms kg/tcs. |
| Water Withdrawal | kL | 110,829,245 | 95,735,451 | 129,577,216 | 15,077,894 |  |
| Water Consumption | kL | 98,609,097 | 53,250,097 | 87,768,084 | 14,411,834 |  |
| Water Intensity | L/₹ or kL/Cr — NOT uniform | 0.000074 | 0.042400 📄 | 0.089042 ⚠️ | 358.670 ⚠️ 📄 | **Tata Steel:** Unit confirmed by PDF as litres/rupee. Not directly comparable to SAIL/Jindal which report kL/Crore.<br>**JSW Steel:** PDF-patched; XBRL stored as kL/₹ (4.23703e-05); converted to L/₹ = 0.0424 for consistency with Tata Steel and SAIL. Not independently<br>**SAIL:** not normalized; Unit assumed L/₹ based on FY2023 PDF-confirmed value of 0.053 L/₹. FY2025 PDF not independently verified.<br>**Jindal Stainless:** not normalized; PDF-patched; Unit is kL/Rs.Crore (PDF confirmed). L/₹ equivalent: 0.0358670 L/₹ (= 358.67 ÷ 10,000,000). For reference: Tata Steel={' |
| Total Waste | metric tonnes | 17,352,473 | 19,109,339 | 14,144,422 | 1,945,438 |  |
| Waste Recovered | metric tonnes | 19,438,386 | 16,546,750 | 15,365,364 | 2,018,038 |  |
| Waste Disposed | metric tonnes | 20,100.0 | 3,375.9 | 969,314.0 | 42,852.3 |  |
| LTIFR | — | 0.390000 | 0.250000 | 0.230000 | 0.000000 | **Tata Steel:** Extracted from dimensional XBRL context D_Employees.<br>**JSW Steel:** Extracted from dimensional XBRL context D_Employees.<br>**SAIL:** Extracted from dimensional XBRL context D_Employees.<br>**Jindal Stainless:** Extracted from dimensional XBRL context D_Employees. |
| Fatalities | — | 5 | 5 | 6 | 0 | **Tata Steel:** Sum of NumberOfFatalities [D_Employees] + [D_Workers] from dimensional XBRL contexts.<br>**JSW Steel:** Sum of NumberOfFatalities [D_Employees] + [D_Workers] from dimensional XBRL contexts.<br>**SAIL:** Sum of NumberOfFatalities [D_Employees] + [D_Workers] from dimensional XBRL contexts.<br>**Jindal Stainless:** Sum of NumberOfFatalities [D_Employees] + [D_Workers] from dimensional XBRL contexts. |
| Total Employees | — | 43,467 | 14,353 | 53,159 | 5,898 | **Tata Steel:** Extracted from multi-dimensional XBRL context D_Gender_Employees_TableA (permanent employees). Parser DCYMain-only extra<br>**JSW Steel:** Extracted from multi-dimensional XBRL context D_Gender_Employees_TableA (permanent employees). Parser DCYMain-only extra<br>**SAIL:** Extracted from multi-dimensional XBRL context D_Gender_Employees_TableA (permanent employees). Parser DCYMain-only extra<br>**Jindal Stainless:** Extracted from multi-dimensional XBRL context D_Gender_Employees_TableA (permanent employees). Parser DCYMain-only extra |
| Female Employees | % | 9.120 | 6.710 | 6.280 | 4.410 | **Tata Steel:** Calculated from female/total employee counts in dimensional XBRL contexts.<br>**JSW Steel:** Calculated from female/total employee counts in dimensional XBRL contexts.<br>**SAIL:** Calculated from female/total employee counts in dimensional XBRL contexts.<br>**Jindal Stainless:** Calculated from female/total employee counts in dimensional XBRL contexts. |
| Training Coverage | % | null ⚠️ | null ⚠️ | null ⚠️ | null ⚠️ | **Tata Steel:** value nulled; not normalized; Training coverage % not found in XBRL for this company-year. To be extracted from PDF.<br>**JSW Steel:** value nulled; not normalized; Training coverage % not found in XBRL for this company-year. To be extracted from PDF.<br>**SAIL:** value nulled; not normalized; Training coverage % not found in XBRL for this company-year. To be extracted from PDF.<br>**Jindal Stainless:** value nulled; not normalized; Training coverage % not found in XBRL for this company-year. To be extracted from PDF. |

> **YOUR COMMENT:** *(type here — leave blank if no issues)*

---

## 5. PDF Enrichment Summaries

Targets, initiatives, and non-compliance extracted from company BRSR PDFs.

### Tata Steel

#### FY2023

**Targets (3)**
- Net Zero emissions for the Tata Steel Group  _2045_
- Achieve specific dust emission intensity of 0.43 kg per tonne of crude steel in India  _2025_
- Achieve specific freshwater consumption of 2.0 m³ per tonne of crude steel across all steelmaking sites in India  _2025_

**Initiatives (3)**
- [emissions] **Zero Carbon Logistics programme**: Savings of ~5% CO2 emissions; replacing road with rail reduced >5,000 trucks/year.
- [energy] **Benchmarking Energy Efficiency IMPACT Centre**: Savings of more than Rs. 750 crore since 2015.
- [energy] **Tata Power Renewable Energy Agreement**: Will cater to 379 MW of power requirement and enable reduction of over 2 million tonnes CO2 per annu

**Scope 3 total:** 13.1 million tCO2e

**Steel production:** 28,180,000 metric tonnes  _Consolidated basis (as per plan config). PDF states capacity of 35 MTPA but production volume not explicitly stated in BRSR._

> **YOUR COMMENT:** *(type here — leave blank if no issues)*

#### FY2024

**Targets (3)**
- Net Zero emissions for the Tata Steel Group  _2045_
- Achieve specific freshwater consumption of <1.5 m³ per tonne of crude steel across all India sites  _2030_
- Achieve 20% diversity in workforce for Tata Steel Limited  _2025_

**Initiatives (3)**
- [emissions] **Zero Carbon Logistics programme**: Optimum Voyage resulted in savings of ~5% CO2 emissions.
- [energy] **Captive Renewable Power Sourcing**: Will reduce 50 million tonnes of carbon emissions over 25-year contract period.
- [energy] **Floating Solar Power Project**: Brought total solar capacity to 20.34 MWp at Jamshedpur plant.

**Scope 3 total:** 15 million tCO2e (Standalone)

**Steel production:** 20,120,000 metric tonnes  _Standalone (India only). From plan config — not explicitly stated in BRSR text block._

> **YOUR COMMENT:** *(type here — leave blank if no issues)*

#### FY2025

**Targets (1)**
- Net Zero emissions for the Tata Steel Group  _2045_

**Initiatives (3)**
- [emissions] **Green Mobility Fleet Expansion**: Reduction of ~200 tonnes CO2 annually.
- [emissions] **B24 Biofuel Shipments**: Executed 39 biofuel vessels and 5 LNG vessels — ~18% of imported shipments.
- [energy] **Rooftop Solar Panel at Jamshedpur Warehouse**: Facility became energy-positive, generating 2,303 MWh against consumption of 1,582 MWh.

**Scope 3 total:** 23 million tCO2e (Standalone)

**Non-compliance (1)**
- Collector of Stamps, Enforcement I and II imposed penalties of Rs 1,46,14,380 and Rs 1,28,07,700 towards belated filing 

**Steel production:** 21,710,000 metric tonnes  _Standalone (India only). From plan config._

> **YOUR COMMENT:** *(type here — leave blank if no issues)*

### JSW Steel

#### FY2023

**Targets (2)**
- Reduce specific CO2 emissions intensity  _2030_
- Achieve carbon neutrality  _2050_

**Initiatives (1)**
- [energy] **Energy Efficiency Interventions**: Capex investment of 3.13% of total capex for environmental sustainability.

**Scope 3 total:** 5,595,113 tCO2e

**Steel production:** 24,150,000 metric tonnes  _From plan config (annual report). Gemini derived ~20.9M t from BRSR emissions/intensity — difference may be due to saleable vs crude steel denominator._

> **YOUR COMMENT:** *(type here — leave blank if no issues)*

#### FY2024

**Targets (1)**
- Carbon emissions intensity reduction  _2030_

**Initiatives (1)**
- [energy] **Clean Technology Investment (Best Available Technologies)**: Capex investment of 4.01% of total capex.

**Scope 3 total:** 5,842,454 tCO2e

**Steel production:** 26,430,000 metric tonnes  _From plan config (annual report)._

> **YOUR COMMENT:** *(type here — leave blank if no issues)*

#### FY2025

**Targets (1)**
- Climate change reduction target  _2030_

**Initiatives (2)**
- [governance] **ResponsibleSteel Certification**: Over 80% of primary steel production from certified sites.
- [waste] **Steel Scrap Recycling**: Circularity enhancement in production.

**Scope 3 total:** 6,120,450 tCO2e

**Non-compliance (2)**
- Penalty from Chhattisgarh Environment Conservation Board for emission of smoke and improper tarpaulin covering.
- Penalty for belated remittance of Provident Fund (2016–2019).

**Steel production:** 27,790,000 metric tonnes  _From plan config (annual report)._

> **YOUR COMMENT:** *(type here — leave blank if no issues)*

### SAIL

#### FY2023

**Targets (1)**
- Eco-restoration of mined-out areas and waste dumps at Meghahatuburu Iron Ore Mines  _2025–26_

**Initiatives (3)**
- [governance] **SAIL Sarathi (AI Chatbot)**: One of the most advanced customer-facing bots in the steel industry.
- [water] **Zero Liquid Discharge (ZLD)**: Pioneering projects towards 100% water recycling.
- [emissions] **CO2 Capture & Mineralisation (IIT Bombay)**: Part of decarbonization effort.

**Non-compliance (1)**
- Non-compliance of environmental standards at IISCO Steel Plant (ISP).

**Steel production:** 18,289,000 metric tonnes  _Reported as 18.289 MT crude steel production in BRSR PDF._

> **YOUR COMMENT:** *(type here — leave blank if no issues)*

#### FY2024

**Targets (1)**
- Achieve Zero Liquid Discharge across all SAIL plants  _Continuous_

**Initiatives (1)**
- [waste] **SAIL Green Tiles Plant**: Utilised 5.3 MT of slag.

**Non-compliance (1)**
- Specific environmental non-compliances mentioned for integrated plants.

**Steel production:** 19,240,000 metric tonnes  _From plan config. Gemini derived ~19.67M t from emissions/intensity._

> **YOUR COMMENT:** *(type here — leave blank if no issues)*

#### FY2025

**Targets (1)**
- Reduction of Specific PM Emission Load  _FY2024–25 (achieved)_

**Initiatives (1)**
- [energy] **Green Power Import from DVC**: Significant increase in renewable energy from 266 TJ to 1,400 TJ.

**Non-compliance (1)**
- Bhilai Steel Plant: Inefficient operation of Sewage Treatment Plant (STP) in violation of Water Act 1974.

**Steel production:** 19,170,000 metric tonnes  _From plan config. Gemini derived ~18.93M t from emissions/intensity._

> **YOUR COMMENT:** *(type here — leave blank if no issues)*

### Jindal Stainless

#### FY2023

**Targets (2)**
- Net Zero carbon emission target  _2050_
- Reduce carbon emission intensity by 50%  _2035_

**Initiatives (3)**
- [energy] **Oxygen Enrichment in Walking Beam Furnace**: Fuel saving of 3%.
- [water] **Water Fixture Replacement**: 2 m³/day fresh water saved.
- [water] **Floor Cleaning with Waste Water**: 50 m³/day fresh water saved.

**Scope 3 total:** 2,781,561 tCO2e

**Non-compliance (1)**
- No instances of regulatory penalties, environmental non-compliance, or fines reported.

**Steel production:** 1,710,000 metric tonnes  _From plan config. Gemini derived ~1.58M t from emissions/intensity — difference may reflect saleable vs crude denominator._

> **YOUR COMMENT:** *(type here — leave blank if no issues)*

#### FY2024

**Targets (2)**
- Achieve Net Zero emissions  _2050_
- Reduce emission intensity by 50%  _Medium-term (implied ~2035)_

**Initiatives (3)**
- [energy] **Floating & Rooftop Solar**: Generated 6,155,850 kWh from onsite solar generation.
- [emissions] **Chrome Palletisation Plant**: Reduction in overall emissions.
- [energy] **Waste Heat Recovery Boiler (WHRB)**: Abated 298.8 tonnes of propane equivalent.

**Scope 3 total:** 3,345,443 tCO2e

**Non-compliance (1)**
- No fines, penalties, or non-compliances reported for the year.

**Steel production:** 2,080,000 metric tonnes  _From plan config. Gemini derived ~1.76M t from BRSR — difference may reflect saleable vs crude denominator._

> **YOUR COMMENT:** *(type here — leave blank if no issues)*

#### FY2025

**Targets (3)**
- Carbon emission intensity reduction by 50%  _2035_
- Zero-Waste-to-Landfill certification  _2030_
- Female workforce representation  _2030_

**Initiatives (3)**
- [energy] **Smart cooling control (electrode temperature)**: Saved 1.66 lakh units of electricity annually (INR 10.8 lakhs).
- [water] **Optimum use of chemicals/water/energy at CPP-DM plant**: 12% reduction in HCl, 15% in NaOH; raw water reduced by 420 m3/year.
- [water] **Boiler waste water reuse**: Saved 2,532 m3 of water annually.

**Scope 3 total:** 3,216,693 tCO2e

**Steel production:** 2,430,000 metric tonnes  _From plan config (2.43 MnT stainless steel)._

> **YOUR COMMENT:** *(type here — leave blank if no issues)*

---

*End of review document.*
