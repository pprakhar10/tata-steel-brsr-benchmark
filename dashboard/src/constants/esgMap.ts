import type { ChartPattern } from '../types/data'

export interface ESGMapEntry {
  esg: 'E' | 'S' | 'G'
  topic: string
  subtopic: string | null
  label: string
  unit: string
  chartPattern: ChartPattern
}

export const ESG_MAP: Record<string, ESGMapEntry> = {
  // ── E: GHG Emissions ──────────────────────────────────────────────────────
  TotalScope1Emissions: { esg: 'E', topic: 'GHG Emissions', subtopic: null, label: 'Scope 1 GHG', unit: 'tCO2e', chartPattern: 'bar' },
  TotalScope2Emissions: { esg: 'E', topic: 'GHG Emissions', subtopic: null, label: 'Scope 2 GHG', unit: 'tCO2e', chartPattern: 'bar' },
  TotalScope3Emissions: { esg: 'E', topic: 'GHG Emissions', subtopic: null, label: 'Scope 3 GHG', unit: 'tCO2e', chartPattern: 'bar' },
  TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput: { esg: 'E', topic: 'GHG Emissions', subtopic: null, label: 'GHG Intensity (physical)', unit: 'tCO2e/tcs', chartPattern: 'line' },
  TotalScope1AndScope2EmissionsIntensityPerRupeeOfTurnover: { esg: 'E', topic: 'GHG Emissions', subtopic: null, label: 'GHG Intensity (per ₹)', unit: 'tCO2e/₹', chartPattern: 'line' },
  TotalScope3EmissionsPerRupeeOfTurnover: { esg: 'E', topic: 'GHG Emissions', subtopic: null, label: 'Scope 3 Intensity (per ₹)', unit: 'tCO2e/₹', chartPattern: 'line' },

  // ── E: Energy — Energy Mix ────────────────────────────────────────────────
  TotalEnergyConsumedFromRenewableAndNonRenewableSources: { esg: 'E', topic: 'Energy', subtopic: 'Energy Mix', label: 'Total Energy', unit: 'GJ', chartPattern: 'stacked' },
  TotalEnergyConsumedFromRenewableSources: { esg: 'E', topic: 'Energy', subtopic: 'Energy Mix', label: 'Total Energy — Renewable', unit: 'GJ', chartPattern: 'none' },
  TotalEnergyConsumedFromNonRenewableSources: { esg: 'E', topic: 'Energy', subtopic: 'Energy Mix', label: 'Total Energy — Non-Renewable', unit: 'GJ', chartPattern: 'none' },

  // ── E: Energy — Electricity ───────────────────────────────────────────────
  TotalElectricityConsumptionFromRenewableSources: { esg: 'E', topic: 'Energy', subtopic: 'Electricity', label: 'Electricity — Renewable', unit: 'GJ', chartPattern: 'bar' },
  TotalElectricityConsumptionFromNonRenewableSources: { esg: 'E', topic: 'Energy', subtopic: 'Electricity', label: 'Electricity — Non-Renewable', unit: 'GJ', chartPattern: 'bar' },

  // ── E: Energy — Fuel ──────────────────────────────────────────────────────
  TotalFuelConsumptionFromRenewableSources: { esg: 'E', topic: 'Energy', subtopic: 'Fuel', label: 'Fuel — Renewable', unit: 'GJ', chartPattern: 'bar' },
  TotalFuelConsumptionFromNonRenewableSources: { esg: 'E', topic: 'Energy', subtopic: 'Fuel', label: 'Fuel — Non-Renewable', unit: 'GJ', chartPattern: 'bar' },

  // ── E: Energy — Energy Other Sources ─────────────────────────────────────
  EnergyConsumptionThroughOtherSourcesFromRenewableSources: { esg: 'E', topic: 'Energy', subtopic: 'Energy Other Sources', label: 'Other Energy — Renewable', unit: 'GJ', chartPattern: 'bar' },
  EnergyConsumptionThroughOtherSourcesFromNonRenewableSources: { esg: 'E', topic: 'Energy', subtopic: 'Energy Other Sources', label: 'Other Energy — Non-Renewable', unit: 'GJ', chartPattern: 'bar' },

  // ── E: Energy — Energy Intensity ─────────────────────────────────────────
  EnergyIntensityInTermOfPhysicalOutput: { esg: 'E', topic: 'Energy', subtopic: 'Energy Intensity', label: 'Energy Intensity (physical)', unit: 'GJ/tcs', chartPattern: 'line' },
  EnergyIntensityPerRupeeOfTurnover: { esg: 'E', topic: 'Energy', subtopic: 'Energy Intensity', label: 'Energy Intensity (per ₹)', unit: 'GJ/₹', chartPattern: 'line' },

  // ── E: Air Emissions ──────────────────────────────────────────────────────
  SOx: { esg: 'E', topic: 'Air Emissions', subtopic: null, label: 'SOx', unit: 'kt', chartPattern: 'bar' },
  NOx: { esg: 'E', topic: 'Air Emissions', subtopic: null, label: 'NOx', unit: 'kt', chartPattern: 'bar' },
  ParticulateMatter: { esg: 'E', topic: 'Air Emissions', subtopic: null, label: 'Particulate Matter (PM)', unit: 'kt', chartPattern: 'bar' },

  // ── E: Water — Water Withdrawal ───────────────────────────────────────────
  TotalVolumeOfWaterWithdrawal: { esg: 'E', topic: 'Water', subtopic: 'Water Withdrawal', label: 'Total Water Withdrawal', unit: 'kL', chartPattern: 'stacked' },
  WaterWithdrawalByGroundwater: { esg: 'E', topic: 'Water', subtopic: 'Water Withdrawal', label: 'Groundwater', unit: 'kL', chartPattern: 'none' },
  WaterWithdrawalBySurfaceWater: { esg: 'E', topic: 'Water', subtopic: 'Water Withdrawal', label: 'Surface Water', unit: 'kL', chartPattern: 'none' },
  WaterWithdrawalBySeawaterOrDesalinatedWater: { esg: 'E', topic: 'Water', subtopic: 'Water Withdrawal', label: 'Seawater / Desalinated', unit: 'kL', chartPattern: 'none' },
  WaterWithdrawalByThirdPartyWater: { esg: 'E', topic: 'Water', subtopic: 'Water Withdrawal', label: 'Third-party Water', unit: 'kL', chartPattern: 'none' },
  WaterWithdrawalByOthers: { esg: 'E', topic: 'Water', subtopic: 'Water Withdrawal', label: 'Other Sources', unit: 'kL', chartPattern: 'none' },

  // ── E: Water — Water Consumption & Discharge ──────────────────────────────
  TotalVolumeOfWaterConsumption: { esg: 'E', topic: 'Water', subtopic: 'Water Consumption & Discharge', label: 'Total Water Consumption', unit: 'kL', chartPattern: 'bar' },
  TotalWaterDischargedInKilolitres: { esg: 'E', topic: 'Water', subtopic: 'Water Consumption & Discharge', label: 'Total Water Discharged', unit: 'kL', chartPattern: 'stacked' },
  WaterDischargeToGroundwater: { esg: 'E', topic: 'Water', subtopic: 'Water Consumption & Discharge', label: 'Discharge → Groundwater', unit: 'kL', chartPattern: 'none' },
  WaterDischargeToSurfaceWater: { esg: 'E', topic: 'Water', subtopic: 'Water Consumption & Discharge', label: 'Discharge → Surface Water', unit: 'kL', chartPattern: 'none' },
  WaterDischargeToSeawater: { esg: 'E', topic: 'Water', subtopic: 'Water Consumption & Discharge', label: 'Discharge → Seawater', unit: 'kL', chartPattern: 'none' },
  WaterDischargeBySentToThirdParties: { esg: 'E', topic: 'Water', subtopic: 'Water Consumption & Discharge', label: 'Discharge → Third Parties', unit: 'kL', chartPattern: 'none' },
  WaterDischargeToOthers: { esg: 'E', topic: 'Water', subtopic: 'Water Consumption & Discharge', label: 'Discharge → Others', unit: 'kL', chartPattern: 'none' },

  // ── E: Water — Water Intensity ────────────────────────────────────────────
  WaterIntensityInTermOfPhysicalOutput: { esg: 'E', topic: 'Water', subtopic: 'Water Intensity', label: 'Water Intensity (physical)', unit: 'L/tcs', chartPattern: 'line' },
  WaterIntensityPerRupeeOfTurnover: { esg: 'E', topic: 'Water', subtopic: 'Water Intensity', label: 'Water Intensity (per ₹)', unit: 'L/₹', chartPattern: 'line' },

  // ── E: Waste — Waste Totals ───────────────────────────────────────────────
  TotalWasteGenerated: { esg: 'E', topic: 'Waste', subtopic: 'Waste Totals', label: 'Total Waste Generated', unit: 'MT', chartPattern: 'stacked' },
  TotalWasteRecovered: { esg: 'E', topic: 'Waste', subtopic: 'Waste Totals', label: 'Total Waste Recovered', unit: 'MT', chartPattern: 'stacked' },
  TotalWasteDisposed: { esg: 'E', topic: 'Waste', subtopic: 'Waste Totals', label: 'Total Waste Disposed', unit: 'MT', chartPattern: 'stacked' },

  // ── E: Waste — Waste Recovery ─────────────────────────────────────────────
  WasteRecoveredThroughRecycled: { esg: 'E', topic: 'Waste', subtopic: 'Waste Recovery', label: 'Recycled', unit: 'MT', chartPattern: 'none' },
  WasteRecoveredThroughReUsed: { esg: 'E', topic: 'Waste', subtopic: 'Waste Recovery', label: 'Re-used', unit: 'MT', chartPattern: 'none' },
  WasteRecoveredThroughOtherRecoveryOperations: { esg: 'E', topic: 'Waste', subtopic: 'Waste Recovery', label: 'Other Recovery', unit: 'MT', chartPattern: 'none' },

  // ── E: Waste — Waste Disposal ─────────────────────────────────────────────
  WasteDisposedByIncineration: { esg: 'E', topic: 'Waste', subtopic: 'Waste Disposal', label: 'Incineration', unit: 'MT', chartPattern: 'none' },
  WasteDisposedByLandfilling: { esg: 'E', topic: 'Waste', subtopic: 'Waste Disposal', label: 'Landfilling', unit: 'MT', chartPattern: 'none' },
  WasteDisposedByOtherDisposalOperations: { esg: 'E', topic: 'Waste', subtopic: 'Waste Disposal', label: 'Other Disposal', unit: 'MT', chartPattern: 'none' },

  // ── E: Waste — Waste By Type ──────────────────────────────────────────────
  BatteryWaste: { esg: 'E', topic: 'Waste', subtopic: 'Waste By Type', label: 'Battery Waste', unit: 'MT', chartPattern: 'none' },
  EWaste: { esg: 'E', topic: 'Waste', subtopic: 'Waste By Type', label: 'E-Waste', unit: 'MT', chartPattern: 'none' },
  BioMedicalWaste: { esg: 'E', topic: 'Waste', subtopic: 'Waste By Type', label: 'Bio-Medical Waste', unit: 'MT', chartPattern: 'none' },
  ConstructionAndDemolitionWaste: { esg: 'E', topic: 'Waste', subtopic: 'Waste By Type', label: 'Construction & Demolition Waste', unit: 'MT', chartPattern: 'none' },
  OtherHazardousWaste: { esg: 'E', topic: 'Waste', subtopic: 'Waste By Type', label: 'Other Hazardous Waste', unit: 'MT', chartPattern: 'none' },
  OtherNonHazardousWasteGenerated: { esg: 'E', topic: 'Waste', subtopic: 'Waste By Type', label: 'Other Non-Hazardous Waste', unit: 'MT', chartPattern: 'none' },
  PlasticWaste: { esg: 'E', topic: 'Waste', subtopic: 'Waste By Type', label: 'Plastic Waste', unit: 'MT', chartPattern: 'none' },
  RadioactiveWaste: { esg: 'E', topic: 'Waste', subtopic: 'Waste By Type', label: 'Radioactive Waste', unit: 'MT', chartPattern: 'none' },

  // ── E: Waste — Waste Intensity ────────────────────────────────────────────
  WasteIntensityInTermOfPhysicalOutput: { esg: 'E', topic: 'Waste', subtopic: 'Waste Intensity', label: 'Waste Intensity (physical)', unit: 'MT/tcs', chartPattern: 'line' },
  WasteIntensityPerRupeeOfTurnover: { esg: 'E', topic: 'Waste', subtopic: 'Waste Intensity', label: 'Waste Intensity (per ₹ Cr)', unit: 'MT/₹ Cr', chartPattern: 'line' },

  // ── S: Health & Safety — TRIFR ───────────────────────────────────────────
  TRIFR_Employees: { esg: 'S', topic: 'Health & Safety', subtopic: 'TRIFR', label: 'Employee TRIFR', unit: 'per mn hrs', chartPattern: 'line' },
  TRIFR_Workers: { esg: 'S', topic: 'Health & Safety', subtopic: 'TRIFR', label: 'Worker TRIFR', unit: 'per mn hrs', chartPattern: 'line' },

  // ── S: Health & Safety — LTIFR ───────────────────────────────────────────
  LTIFR_Employees: { esg: 'S', topic: 'Health & Safety', subtopic: 'LTIFR', label: 'Employee LTIFR', unit: 'per mn hrs', chartPattern: 'line' },
  LTIFR_Workers: { esg: 'S', topic: 'Health & Safety', subtopic: 'LTIFR', label: 'Worker LTIFR', unit: 'per mn hrs', chartPattern: 'line' },

  // ── S: Health & Safety — Fatalities ──────────────────────────────────────
  Fatalities_Employees: { esg: 'S', topic: 'Health & Safety', subtopic: 'Fatalities', label: 'Employee Fatalities', unit: 'no.', chartPattern: 'bar' },
  Fatalities_Workers: { esg: 'S', topic: 'Health & Safety', subtopic: 'Fatalities', label: 'Worker Fatalities', unit: 'no.', chartPattern: 'bar' },

  // ── S: Health & Safety — Work-Related Injuries ───────────────────────────
  TotalNumberOfAffectedEmployees: { esg: 'S', topic: 'Health & Safety', subtopic: 'Work-Related Injuries', label: 'Affected Employees (injury)', unit: 'no.', chartPattern: 'bar' },
  TotalNumberOfAffectedWorkers: { esg: 'S', topic: 'Health & Safety', subtopic: 'Work-Related Injuries', label: 'Affected Workers (injury)', unit: 'no.', chartPattern: 'bar' },

  // ── S: Health & Safety — Rehabilitation ──────────────────────────────────
  NumberOfEmployeesOrWhoseFamilyMembersRehabilitatedAndPlacedInSuitableEmployment: { esg: 'S', topic: 'Health & Safety', subtopic: 'Rehabilitation', label: 'Employees Rehabilitated', unit: 'no.', chartPattern: 'bar' },
  NumberOfWorkersOrWhoseFamilyMembersRehabilitatedAndPlacedInSuitableEmployment: { esg: 'S', topic: 'Health & Safety', subtopic: 'Rehabilitation', label: 'Workers Rehabilitated', unit: 'no.', chartPattern: 'bar' },

  // ── S: Workforce & Diversity — Headcount ─────────────────────────────────
  TotalNumberOfEmployees: { esg: 'S', topic: 'Workforce & Diversity', subtopic: 'Headcount', label: 'Total Employees', unit: 'no.', chartPattern: 'bar' },
  PercentageOfFemaleEmployees: { esg: 'S', topic: 'Workforce & Diversity', subtopic: 'Headcount', label: 'Female Employees (%)', unit: '%', chartPattern: 'bar-pct' },
  TotalNumberOfWorkers: { esg: 'S', topic: 'Workforce & Diversity', subtopic: 'Headcount', label: 'Total Workers', unit: 'no.', chartPattern: 'bar' },
  PercentageOfFemaleWorkers: { esg: 'S', topic: 'Workforce & Diversity', subtopic: 'Headcount', label: 'Female Workers (%)', unit: '%', chartPattern: 'bar-pct' },
  PercentageOfGrossWagesPaidToFemaleToTotalWagesPaid: { esg: 'S', topic: 'Workforce & Diversity', subtopic: 'Headcount', label: 'Female Wage %', unit: '%', chartPattern: 'bar-pct' },

  // ── S: Workforce & Diversity — Board ─────────────────────────────────────
  TotalNumberOfBoardOfDirectors: { esg: 'S', topic: 'Workforce & Diversity', subtopic: 'Board', label: 'Board of Directors (total)', unit: 'no.', chartPattern: 'bar' },
  PercentageOfFemaleBoardOfDirectors: { esg: 'S', topic: 'Workforce & Diversity', subtopic: 'Board', label: 'Board of Directors (female %)', unit: '%', chartPattern: 'bar-pct' },

  // ── S: Workforce & Diversity — Leadership ────────────────────────────────
  TotalNumberOfKeyManagementPersonnel: { esg: 'S', topic: 'Workforce & Diversity', subtopic: 'Leadership', label: 'KMPs (total)', unit: 'no.', chartPattern: 'bar' },
  PercentageOfFemaleKeyManagementPersonnel: { esg: 'S', topic: 'Workforce & Diversity', subtopic: 'Leadership', label: 'KMPs (female %)', unit: '%', chartPattern: 'bar-pct' },

  // ── S: Training ───────────────────────────────────────────────────────────
  TrainingCoverage_Employees_HealthSafety: { esg: 'S', topic: 'Training', subtopic: null, label: 'Employee H&S Training Coverage', unit: '%', chartPattern: 'bar-pct' },
  TrainingCoverage_Employees_SkillUpgradation: { esg: 'S', topic: 'Training', subtopic: null, label: 'Employee Skill Training Coverage', unit: '%', chartPattern: 'bar-pct' },
  TrainingCoverage_Workers_HealthSafety: { esg: 'S', topic: 'Training', subtopic: null, label: 'Worker H&S Training Coverage', unit: '%', chartPattern: 'bar-pct' },
  TrainingCoverage_Workers_SkillUpgradation: { esg: 'S', topic: 'Training', subtopic: null, label: 'Worker Skill Training Coverage', unit: '%', chartPattern: 'bar-pct' },

  // ── S: Labour Practices ───────────────────────────────────────────────────
  PercentageOfCostIncurredOnWellBeingMeasuresWithRespectToTotalRevenueOfTheCompany: { esg: 'S', topic: 'Labour Practices', subtopic: null, label: 'Wellbeing Cost (% revenue)', unit: '%', chartPattern: 'bar-pct' },
  TotalComplaintsReportedUnderSexualHarassmentOfWomenAtWorkplace: { esg: 'S', topic: 'Labour Practices', subtopic: null, label: 'POSH Complaints (total)', unit: 'no.', chartPattern: 'bar' },
  ComplaintsOnPOSHUpHeld: { esg: 'S', topic: 'Labour Practices', subtopic: null, label: 'POSH Complaints (upheld)', unit: 'no.', chartPattern: 'bar' },

  // ── G: Financial Profile ──────────────────────────────────────────────────
  Turnover: { esg: 'G', topic: 'Financial Profile', subtopic: null, label: 'Turnover', unit: '₹ Cr', chartPattern: 'bar' },
  NetWorth: { esg: 'G', topic: 'Financial Profile', subtopic: null, label: 'Net Worth', unit: '₹ Cr', chartPattern: 'bar' },
  PercentageOfContributionOfExportsInTheTotalTurnoverOfTheEntity: { esg: 'G', topic: 'Financial Profile', subtopic: null, label: 'Export Contribution (% turnover)', unit: '%', chartPattern: 'bar-pct' },

  // ── G: Sustainability Investment ──────────────────────────────────────────
  PercentageOfCapex: { esg: 'G', topic: 'Sustainability Investment', subtopic: null, label: 'Capex on ESG/Sustainability (%)', unit: '%', chartPattern: 'bar-pct' },
  PercentageOfRAndD: { esg: 'G', topic: 'Sustainability Investment', subtopic: null, label: 'R&D & Capex in Env/Social Technologies (%)', unit: '%', chartPattern: 'bar-pct' },

  // ── G: Supply Chain ───────────────────────────────────────────────────────
  PercentageOfDirectlySourcedFromMSMEsOrSmallProducers: { esg: 'G', topic: 'Supply Chain', subtopic: null, label: 'Sourced from MSMEs (%)', unit: '%', chartPattern: 'bar-pct' },
  PercentageOfInputsWereSourcedSustainably: { esg: 'G', topic: 'Supply Chain', subtopic: null, label: 'Inputs Sourced Sustainably (%)', unit: '%', chartPattern: 'bar-pct' },
  PercentageOfSourcedDirectlyFromWithinTheDistrictAndNeighbouringDistricts: { esg: 'G', topic: 'Supply Chain', subtopic: null, label: 'Local Sourcing (%)', unit: '%', chartPattern: 'bar-pct' },
  PercentageOfValueChainPartnersByValueOfBusinessDoneWithSuchPartnersThatWereAssessedForEnvironmentalImpacts: { esg: 'G', topic: 'Supply Chain', subtopic: null, label: 'Value Chain Partners — Env Assessment (%)', unit: '%', chartPattern: 'bar-pct' },
  NumberOfTradingHousesWherePurchasesAreMade: { esg: 'G', topic: 'Supply Chain', subtopic: null, label: 'Number of Trading Houses', unit: 'no.', chartPattern: 'bar' },

  // ── G: Consumer Responsibility ────────────────────────────────────────────
  EnvironmentalAndSocialParametersRelevantToTheProductAsAPercentageToTotalTurnover: { esg: 'G', topic: 'Consumer Responsibility', subtopic: null, label: 'Products with env/social info (% turnover)', unit: '%', chartPattern: 'bar-pct' },
  RecyclingAndOrSafeDisposalAsAPercentageToTotalTurnover: { esg: 'G', topic: 'Consumer Responsibility', subtopic: null, label: 'Products with recycling/safe disposal info (% turnover)', unit: '%', chartPattern: 'bar-pct' },
  NumberOfDealersOrDistributorsToWhomSalesAreMade: { esg: 'G', topic: 'Consumer Responsibility', subtopic: null, label: 'Number of Dealers/Distributors', unit: 'no.', chartPattern: 'bar' },

  // ── G: Related Party Transactions ─────────────────────────────────────────
  PercentageOfInvestmentsInRelatedPartiesInTotalInvestments: { esg: 'G', topic: 'Related Party Transactions', subtopic: null, label: 'RPT Investments (%)', unit: '%', chartPattern: 'bar-pct' },
  PercentageOfLoansAndAdvancesGivenToRelatedPartiesInTotalLoansAndAdvances: { esg: 'G', topic: 'Related Party Transactions', subtopic: null, label: 'RPT Loans & Advances (%)', unit: '%', chartPattern: 'bar-pct' },
  PercentageOfPurchasesFromRelatedPartiesInTotalPurchasesForShareOfRelatedPartyTransactions: { esg: 'G', topic: 'Related Party Transactions', subtopic: null, label: 'RPT Purchases (%)', unit: '%', chartPattern: 'bar-pct' },
  PercentageOfSalesToRelatedPartiesInTotalSalesForShareOfRelatedPartyTransactions: { esg: 'G', topic: 'Related Party Transactions', subtopic: null, label: 'RPT Sales (%)', unit: '%', chartPattern: 'bar-pct' },

  // ── G: ESG Credits ────────────────────────────────────────────────────────
  NumberOfGreenCreditsHaveBeenGeneratedOrProcuredByTheListedEntity: { esg: 'G', topic: 'ESG Credits', subtopic: null, label: 'Green Credits Generated/Procured', unit: 'no.', chartPattern: 'bar' },
}

export const ORDERED_TAGS: string[] = [
  // E — GHG Emissions
  'TotalScope1Emissions', 'TotalScope2Emissions', 'TotalScope3Emissions',
  'TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput',
  'TotalScope1AndScope2EmissionsIntensityPerRupeeOfTurnover',
  'TotalScope3EmissionsPerRupeeOfTurnover',
  // E — Energy Mix
  'TotalEnergyConsumedFromRenewableAndNonRenewableSources',
  'TotalEnergyConsumedFromRenewableSources', 'TotalEnergyConsumedFromNonRenewableSources',
  // E — Electricity
  'TotalElectricityConsumptionFromRenewableSources', 'TotalElectricityConsumptionFromNonRenewableSources',
  // E — Fuel
  'TotalFuelConsumptionFromRenewableSources', 'TotalFuelConsumptionFromNonRenewableSources',
  // E — Energy Other Sources
  'EnergyConsumptionThroughOtherSourcesFromRenewableSources',
  'EnergyConsumptionThroughOtherSourcesFromNonRenewableSources',
  // E — Energy Intensity
  'EnergyIntensityInTermOfPhysicalOutput', 'EnergyIntensityPerRupeeOfTurnover',
  // E — Air Emissions
  'SOx', 'NOx', 'ParticulateMatter',
  // E — Water Withdrawal
  'TotalVolumeOfWaterWithdrawal', 'WaterWithdrawalByGroundwater', 'WaterWithdrawalBySurfaceWater',
  'WaterWithdrawalBySeawaterOrDesalinatedWater', 'WaterWithdrawalByThirdPartyWater', 'WaterWithdrawalByOthers',
  // E — Water Consumption & Discharge
  'TotalVolumeOfWaterConsumption', 'TotalWaterDischargedInKilolitres',
  'WaterDischargeToGroundwater', 'WaterDischargeToSurfaceWater', 'WaterDischargeToSeawater',
  'WaterDischargeBySentToThirdParties', 'WaterDischargeToOthers',
  // E — Water Intensity
  'WaterIntensityInTermOfPhysicalOutput', 'WaterIntensityPerRupeeOfTurnover',
  // E — Waste Totals
  'TotalWasteGenerated', 'TotalWasteRecovered', 'TotalWasteDisposed',
  // E — Waste Recovery
  'WasteRecoveredThroughRecycled', 'WasteRecoveredThroughReUsed',
  'WasteRecoveredThroughOtherRecoveryOperations',
  // E — Waste Disposal
  'WasteDisposedByIncineration', 'WasteDisposedByLandfilling', 'WasteDisposedByOtherDisposalOperations',
  // E — Waste By Type
  'BatteryWaste', 'EWaste', 'BioMedicalWaste', 'ConstructionAndDemolitionWaste',
  'OtherHazardousWaste', 'OtherNonHazardousWasteGenerated', 'PlasticWaste', 'RadioactiveWaste',
  // E — Waste Intensity
  'WasteIntensityInTermOfPhysicalOutput', 'WasteIntensityPerRupeeOfTurnover',
  // S — Health & Safety — TRIFR
  'TRIFR_Employees', 'TRIFR_Workers',
  // S — Health & Safety — LTIFR
  'LTIFR_Employees', 'LTIFR_Workers',
  // S — Health & Safety — Fatalities
  'Fatalities_Employees', 'Fatalities_Workers',
  // S — Health & Safety — Work-Related Injuries
  'TotalNumberOfAffectedEmployees', 'TotalNumberOfAffectedWorkers',
  // S — Health & Safety — Rehabilitation
  'NumberOfEmployeesOrWhoseFamilyMembersRehabilitatedAndPlacedInSuitableEmployment',
  'NumberOfWorkersOrWhoseFamilyMembersRehabilitatedAndPlacedInSuitableEmployment',
  // S — Workforce & Diversity — Headcount
  'TotalNumberOfEmployees', 'PercentageOfFemaleEmployees',
  'TotalNumberOfWorkers', 'PercentageOfFemaleWorkers',
  'PercentageOfGrossWagesPaidToFemaleToTotalWagesPaid',
  // S — Workforce & Diversity — Board
  'TotalNumberOfBoardOfDirectors', 'PercentageOfFemaleBoardOfDirectors',
  // S — Workforce & Diversity — Leadership
  'TotalNumberOfKeyManagementPersonnel', 'PercentageOfFemaleKeyManagementPersonnel',
  // S — Training
  'TrainingCoverage_Employees_HealthSafety', 'TrainingCoverage_Employees_SkillUpgradation',
  'TrainingCoverage_Workers_HealthSafety', 'TrainingCoverage_Workers_SkillUpgradation',
  // S — Labour Practices
  'PercentageOfCostIncurredOnWellBeingMeasuresWithRespectToTotalRevenueOfTheCompany',
  'TotalComplaintsReportedUnderSexualHarassmentOfWomenAtWorkplace', 'ComplaintsOnPOSHUpHeld',
  // G — Financial Profile
  'Turnover', 'NetWorth', 'PercentageOfContributionOfExportsInTheTotalTurnoverOfTheEntity',
  // G — Sustainability Investment
  'PercentageOfCapex', 'PercentageOfRAndD',
  // G — Supply Chain
  'PercentageOfDirectlySourcedFromMSMEsOrSmallProducers', 'PercentageOfInputsWereSourcedSustainably',
  'PercentageOfSourcedDirectlyFromWithinTheDistrictAndNeighbouringDistricts',
  'PercentageOfValueChainPartnersByValueOfBusinessDoneWithSuchPartnersThatWereAssessedForEnvironmentalImpacts',
  'NumberOfTradingHousesWherePurchasesAreMade',
  // G — Consumer Responsibility
  'EnvironmentalAndSocialParametersRelevantToTheProductAsAPercentageToTotalTurnover',
  'RecyclingAndOrSafeDisposalAsAPercentageToTotalTurnover',
  'NumberOfDealersOrDistributorsToWhomSalesAreMade',
  // G — Related Party Transactions
  'PercentageOfInvestmentsInRelatedPartiesInTotalInvestments',
  'PercentageOfLoansAndAdvancesGivenToRelatedPartiesInTotalLoansAndAdvances',
  'PercentageOfPurchasesFromRelatedPartiesInTotalPurchasesForShareOfRelatedPartyTransactions',
  'PercentageOfSalesToRelatedPartiesInTotalSalesForShareOfRelatedPartyTransactions',
  // G — ESG Credits
  'NumberOfGreenCreditsHaveBeenGeneratedOrProcuredByTheListedEntity',
]

export const SUB_COMPONENT_TAGS: Set<string> = new Set(
  Object.values({
    TotalEnergyConsumedFromRenewableAndNonRenewableSources: [
      'TotalEnergyConsumedFromRenewableSources', 'TotalEnergyConsumedFromNonRenewableSources',
    ],
    TotalVolumeOfWaterWithdrawal: [
      'WaterWithdrawalByGroundwater', 'WaterWithdrawalBySurfaceWater',
      'WaterWithdrawalBySeawaterOrDesalinatedWater', 'WaterWithdrawalByThirdPartyWater', 'WaterWithdrawalByOthers',
    ],
    TotalWaterDischargedInKilolitres: [
      'WaterDischargeToGroundwater', 'WaterDischargeToSurfaceWater',
      'WaterDischargeToSeawater', 'WaterDischargeBySentToThirdParties', 'WaterDischargeToOthers',
    ],
    TotalWasteGenerated: [
      'BatteryWaste', 'EWaste', 'BioMedicalWaste', 'ConstructionAndDemolitionWaste',
      'OtherHazardousWaste', 'OtherNonHazardousWasteGenerated', 'PlasticWaste', 'RadioactiveWaste',
    ],
    TotalWasteRecovered: [
      'WasteRecoveredThroughRecycled', 'WasteRecoveredThroughReUsed', 'WasteRecoveredThroughOtherRecoveryOperations',
    ],
    TotalWasteDisposed: [
      'WasteDisposedByIncineration', 'WasteDisposedByLandfilling', 'WasteDisposedByOtherDisposalOperations',
    ],
  } as Record<string, string[]>).flat()
)

export const COMPOSITE_INDICATORS: Record<string, string[]> = {
  TotalEnergyConsumedFromRenewableAndNonRenewableSources: [
    'TotalEnergyConsumedFromRenewableSources',
    'TotalEnergyConsumedFromNonRenewableSources',
  ],
  TotalVolumeOfWaterWithdrawal: [
    'WaterWithdrawalByGroundwater',
    'WaterWithdrawalBySurfaceWater',
    'WaterWithdrawalBySeawaterOrDesalinatedWater',
    'WaterWithdrawalByThirdPartyWater',
    'WaterWithdrawalByOthers',
  ],
  TotalWaterDischargedInKilolitres: [
    'WaterDischargeToGroundwater',
    'WaterDischargeToSurfaceWater',
    'WaterDischargeToSeawater',
    'WaterDischargeBySentToThirdParties',
    'WaterDischargeToOthers',
  ],
  TotalWasteGenerated: [
    'BatteryWaste',
    'EWaste',
    'BioMedicalWaste',
    'ConstructionAndDemolitionWaste',
    'OtherHazardousWaste',
    'OtherNonHazardousWasteGenerated',
    'PlasticWaste',
    'RadioactiveWaste',
  ],
  TotalWasteRecovered: [
    'WasteRecoveredThroughRecycled',
    'WasteRecoveredThroughReUsed',
    'WasteRecoveredThroughOtherRecoveryOperations',
  ],
  TotalWasteDisposed: [
    'WasteDisposedByIncineration',
    'WasteDisposedByLandfilling',
    'WasteDisposedByOtherDisposalOperations',
  ],
}

export const SUB_COMPONENT_PARENT: Record<string, string> = Object.fromEntries(
  Object.entries(COMPOSITE_INDICATORS).flatMap(([parent, children]) =>
    children.map(child => [child, parent])
  )
)
