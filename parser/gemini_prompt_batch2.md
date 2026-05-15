## GEMINI HANDOFF — indicators.json Batch 2 (Tags I–R, 120 tags)

### Context

You are helping build a BRSR (Business Responsibility and Sustainability Report) benchmark dashboard for 4 Indian steel companies: Tata Steel, JSW Steel, SAIL, and Jindal Stainless. Data is extracted from SEBI-mandated XBRL filings for FY2023–FY2025.

BRSR is India's ESG reporting framework under SEBI's LODR. It follows 9 NGRBC principles. This task is purely metadata annotation — you are assigning labels, categories, and types to XBRL tag names so the dashboard UI can display them meaningfully.

---

### BRSR Structure

**Section A** — General Disclosures (company identity, operations, financials, employees)
**Section B** — Management and Process Disclosures (policies, governance systems)
**Section C** — Principle-wise Performance Disclosures (actual metrics, per principle)
  - Each principle has **Essential** (mandatory) and **Leadership** (voluntary best-practice) indicators
**BRSR Core** — Enhanced subset for compulsory external assurance (from FY2023-24)

### The 9 NGRBC Principles
- **P1** — Ethics, Transparency and Accountability (Anti-Corruption, Conflict of Interest)
- **P2** — Sustainable Products and Services (R&D, Lifecycle, Sustainable Sourcing)
- **P3** — Employee and Worker Wellbeing (H&S, Benefits, Training, Wages)
- **P4** — Stakeholder Engagement (identifying and engaging stakeholders)
- **P5** — Human Rights (fair labour, non-discrimination, no child/forced labour)
- **P6** — Environment (GHG Emissions, Energy, Water, Waste, Air Emissions, Biodiversity)
- **P7** — Policy Advocacy (trade associations, lobbying, regulatory engagement)
- **P8** — Inclusive Growth (CSR, community development, supply chain inclusion)
- **P9** — Consumer Responsibility (product safety, complaints, data privacy)

---

### Tag Naming Patterns — CRITICAL

**Assurance metadata tags** (all map to: category='Governance', subcategory='Assurance Metadata', brsr.section='BRSR Core', comparableAcrossCompanies=true):
- `AssuranceSubTypeFor{X}` → Type of assurance (Limited/Reasonable) for indicator X; dataType='categorical'
- `AssurerHasAssured{X}` → Did external assurer cover X?; dataType='boolean'
- `Whether{X}IsAssuredByAssurer` → Same meaning; dataType='boolean'
- `TypeOfAssuranceFor{X}` → Limited / Reasonable / None; dataType='categorical'
- `RemarksForAssuranceOf{X}` → Free text remarks on assurance; dataType='text'
- For label: prefix with "Assurance Type:", "Assurer Verified:", or "Assurance Remarks:" as appropriate

**Text block / narrative tags** (`*ExplanatoryTextBlock`, `Describe*`, `Provide*`, `Notes*ExplanatoryTextBlock`):
- dataType='text', standardUnit=null, comparableAcrossCompanies=false
- suffix label with "(Narrative)"

**Boolean yes/no tags** (`Indicate*`, `Is*`, `Whether*` (not assurance)):
- dataType='boolean', standardUnit=null, comparableAcrossCompanies=true

**Numeric absolute tags** (`Number*`, `Net*`):
- dataType='numeric'

**Percentage tags** (`Percentage*`, `*AsAPercentageToTotalTurnover`):
- dataType='percentage', standardUnit='%'

**Name/text fields** (`NameOfTheExternalAgency*`, `Notes*`):
- dataType='text', comparableAcrossCompanies=false

---

### Standard Unit Reference

| Metric | standardUnit |
|---|---|
| GHG Emissions (Scope 1/2/3) | 'tCO2e' |
| Energy (fuel, electricity, total) | 'GJ' |
| Water (withdrawal, consumption, discharge) | 'kL' |
| Waste generated / recovered / disposed | 'metric tonnes' |
| Air emissions (NOx, SOx, PM, HAP, VOC, POP) | 'kilotonnes' |
| Financial amounts | 'INR Crore' |
| Percentages | '%' |
| Count / Number of X | null |
| Intensity ratios | null |
| Boolean / text / categorical | null |

**Note on NOx and Nox**: Both `NOx` and `Nox` are in this dataset — they are the same indicator (nitrogen oxides air emission) under different namespace versions. Both: standardUnit='kilotonnes', category='Environment', subcategory='Air Emissions', P6 Essential.

---

### Category & Subcategory Reference

**category** must be exactly one of: 'Environment' | 'Social' | 'Governance' | 'General'

| Subcategory | Category | Principles |
|---|---|---|
| GHG Emissions | Environment | P6 |
| Energy | Environment | P6 |
| Water | Environment | P6 |
| Waste Management | Environment | P6 |
| Air Emissions | Environment | P6 |
| Biodiversity | Environment | P6 |
| Resource Efficiency | Environment | P2, P6 |
| Employee H&S | Social | P3 |
| Employee Wellbeing | Social | P3 |
| Human Rights | Social | P5 |
| Workforce Composition | Social | P3, Section A |
| Stakeholder Engagement | Social | P4 |
| Consumer Responsibility | Social | P9 |
| CSR & Community | Social | P8 |
| Supply Chain | Social | P2, P5, P8 |
| Ethics & Anti-Corruption | Governance | P1 |
| Policy Advocacy | Governance | P7 |
| Board & Governance | Governance | Section A, Section B |
| Assurance Metadata | Governance | BRSR Core |
| Products & Services | Social | P2, P9 |
| Financial Performance | General | Section A |
| Operations | General | Section A |

---

### Field Rules

- **label**: 3–7 word human-readable title-case phrase. Clearly identifies what is measured. Do not start with "The" or "Whether". For assurance tags: prefix with "Assurance Type:", "Assurer Verified:", or "Assurance Remarks:". For text blocks: suffix with "(Narrative)".
- **brsr.principle**: P1–P9, Section A, Section B, or BRSR Core
- **brsr.section**: "Essential" | "Leadership" | "Section A" | "Section B" | "BRSR Core"
- **dataType**: "numeric" | "boolean" | "text" | "categorical" | "percentage"
- **standardUnit**: null for non-numeric; string for numeric (see table above)
- **category**: exactly one of 'Environment', 'Social', 'Governance', 'General'
- **subcategory**: from the table above (or closest match)
- **comparableAcrossCompanies**: false for text blocks/narratives/name fields; true for everything else

---

### Output Format

Return a JSON array of 120 objects, one per tag, in the exact order the tags appear in the TASK section. No extra commentary — only the JSON array.

```json
[
  {
    "canonicalTag": "NOx",
    "label": "NOx Emissions",
    "brsr": { "principle": "P6", "section": "Essential" },
    "dataType": "numeric",
    "standardUnit": "kilotonnes",
    "category": "Environment",
    "subcategory": "Air Emissions",
    "comparableAcrossCompanies": true
  }
]
```

---

### Task — Annotate these 120 tags (I–R range)

```
IndicateIfAnyIndependentAssessmentOrEvaluationOrAssuranceHasBeenCarriedOutByAnExternalAgencyForAirEmissionsOtherThanGHGEmissions
IndicateIfAnyIndependentAssessmentOrEvaluationOrAssuranceHasBeenCarriedOutByAnExternalAgencyForAreasOfWaterStress
IsTheEntityCompliantWithTheApplicableEnvironmentalLaw
IsThePremiseOrOfficeOfTheEntityAccessibleToDifferentlyAbledVisitorsAsPerTheRequirementsOfTheRightsOfPersonsWithDisabilitiesAct2016
IsThereAMechanismAvailableToReceiveAndRedressGrievancesForOtherThanPermanentEmployees
IsThereAMechanismAvailableToReceiveAndRedressGrievancesForOtherThanPermanentWorkers
IsThereAMechanismAvailableToReceiveAndRedressGrievancesForPermanentEmployees
IsThereAMechanismAvailableToReceiveAndRedressGrievancesForPermanentWorkers
IsThereAMechanismAvailableToReceiveAndRedressGrievancesForTheFollowingCategoriesOfEmployeesAndWorker
MechanismsInPlaceToInformConsumersOfAnyRiskOfDisruptionOrDiscontinuationOfEssentialServicesExplanatoryTextBlock
MechanismsToPreventAdverseConsequencesToTheComplainantInDiscriminationAndHarassmentCasesExplanatoryTextBlock
NOx
NameOfTheExternalAgencyIfAnyIndependentAssessmentOrEvaluationOrAssuranceHasBeenCarriedOutByAnExternalAgencyForAirEmissionsOtherThanGHGEmissionsExplanatoryTextBlock
NameOfTheExternalAgencyIfAnyIndependentAssessmentOrEvaluationOrAssuranceHasBeenCarriedOutByAnExternalAgencyForAreasOfWaterStressExplanatoryTextBlock
NameOfTheExternalAgencyIfAnyIndependentAssessmentOrEvaluationOrAssuranceHasBeenCarriedOutByAnExternalAgencyForEnergyConsumptionExplanatoryTextBlock
NameOfTheExternalAgencyInCaseAnyIndependentAssessmentOrEvaluationOrAssuranceHasBeenCarriedOutByAnExternalAgencyForWaterWithdrawalExplanatoryTextBlock
NameOfTheExternalAgencyThatUndertookIndependentAssessmentOrEvaluationOrAssuranceForEnergyConsumptionExplanatoryTextBlock
NameOfTheExternalAgencyThatUndertookIndependentAssessmentOrEvaluationOrAssuranceForGreenHouseGasEmissionsExplanatoryTextBlock
NameOfTheExternalAgencyThatUndertookIndependentAssessmentOrEvaluationOrAssuranceForTotalScope3EmissionsExplanatoryTextBlock
NameOfTheExternalAgencyThatUndertookIndependentAssessmentOrEvaluationOrAssuranceForWaterDischargedExplanatoryTextBlock
NameOfTheExternalAgencyThatUndertookIndependentAssessmentOrEvaluationOrAssuranceRelatedToWasteManagementExplanatoryTextBlock
NetWorth
NotesGeneralDisclosureExplanatoryTextBlock
NotesManagementAndProcessDisclosuresExplanatoryTextBlock
NotesPrinciple1ExplanatoryTextBlock
NotesPrinciple2ExplanatoryTextBlock
NotesPrinciple3ExplanatoryTextBlock
NotesPrinciple4ExplanatoryTextBlock
NotesPrinciple5ExplanatoryTextBlock
NotesPrinciple6ExplanatoryTextBlock
NotesPrinciple7ExplanatoryTextBlock
NotesPrinciple8ExplanatoryTextBlock
NotesPrinciple9ExplanatoryTextBlock
Nox
NumberOfAffiliationsWithTradeAndIndustryChambersOrAssociations
NumberOfComplaintsReceivedInRelationToIssuesOfConflictOfInterestOfTheDirectors
NumberOfComplaintsReceivedInRelationToIssuesOfConflictOfInterestOfTheKMPs
NumberOfCountriesWhereMarketServedByTheEntity
NumberOfDaysOfAccountsPayable
NumberOfDealersOrDistributorsToWhomSalesAreMade
NumberOfDirectorsAgainstWhomDisciplinaryActionWasTaken
NumberOfEmployeesAgainstWhomDisciplinaryActionWasTaken
NumberOfEmployeesOrWhoseFamilyMembersRehabilitatedAndPlacedInSuitableEmployment
NumberOfFemaleBoardOfDirectors
NumberOfFemaleEmployeesOrWorkers
NumberOfFemaleKeyManagementPersonnel
NumberOfForcedRecalls
NumberOfGreenCreditsHaveBeenGeneratedOrProcuredByTheListedEntity
NumberOfGreenCreditsHaveBeenGeneratedOrProcuredByTheTopTenValueChainPartners
NumberOfInstancesOfDataBreachesAlongWithImpact
NumberOfKMPsAgainstWhomDisciplinaryActionWasTaken
NumberOfStatesWhereMarketServedByTheEntity
NumberOfTradingHousesWherePurchasesAreMade
NumberOfVoluntaryRecalls
NumberOfWorkersAgainstWhomDisciplinaryActionWasTaken
NumberOfWorkersOrWhoseFamilyMembersRehabilitatedAndPlacedInSuitableEmployment
OtherHazardousWaste
OtherNonHazardousWasteGenerated
ParticulateMatter
PercentageOfCapex
PercentageOfChildLabourOfValueChainPartnersP5
PercentageOfChildLabourOfYourPlantsAndOfficesThatWereAssessedP5
PercentageOfComplaintsInRespectOfNumberOfEmployeesOrWorker
PercentageOfContributionOfExportsInTheTotalTurnoverOfTheEntity
PercentageOfCostIncurredOnWellBeingMeasuresWithRespectToTotalRevenueOfTheCompany
PercentageOfDataBreachesInvolvingPersonallyIdentifiableInformationOfCustomers
PercentageOfDirectlySourcedFromMSMEsOrSmallProducers
PercentageOfDiscriminationAtWorkPlaceOfValueChainPartnersP5
PercentageOfDiscriminationAtWorkPlaceOfYourPlantsAndOfficesThatWereAssessedP5
PercentageOfFemaleBoardOfDirectors
PercentageOfFemaleKeyManagementPersonnel
PercentageOfForcedLabourOrInvoluntaryLabourOfValueChainPartnersP5
PercentageOfForcedLabourOrInvoluntaryLabourOfYourPlantsAndOfficesThatWereAssessedP5
PercentageOfGrossWagesPaidToFemaleToTotalWagesPaid
PercentageOfHealthAndSafetyPracticesOfValueChainPartnersP3
PercentageOfHealthAndSafetyPracticesOfYourPlantsAndOfficesThatWereAssessedP3
PercentageOfInputsWereSourcedSustainably
PercentageOfInvestmentsInRelatedPartiesInTotalInvestments
PercentageOfLoansAndAdvancesGivenToRelatedPartiesInTotalLoansAndAdvances
PercentageOfPurchasesFromRelatedPartiesInTotalPurchasesForShareOfRelatedPartyTransactions
PercentageOfPurchasesFromTopTenTradingHousesInTotalPurchasesFromTradingHouses
PercentageOfPurchasesFromTradingHousesInTotalPurchasesForConcentrationOfPurchases
PercentageOfRAndD
PercentageOfSalesToDealersOrDistributorsInTotalSales
PercentageOfSalesToRelatedPartiesInTotalSalesForShareOfRelatedPartyTransactions
PercentageOfSalesToTopTenDealersOrDistributorsInTotalSalesToDealersOrDistributors
PercentageOfSexualHarassmentOfValueChainPartnersP5
PercentageOfSexualHarassmentOfYourPlantsAndOfficesThatWereAssessedP5
PercentageOfSourcedDirectlyFromWithinTheDistrictAndNeighbouringDistricts
PercentageOfValueChainPartnersByValueOfBusinessDoneWithSuchPartnersThatWereAssessedForEnvironmentalImpacts
PercentageOfWagesOfValueChainPartnersP5
PercentageOfWagesOfYourPlantsAndOfficesThatWereAssessedP5
PercentageOfWorkingConditionsOfValueChainPartnersP3
PercentageOfWorkingConditionsOfYourPlantsAndOfficesThatWereAssessedP3
PersistentOrganicPollutants
PlasticWaste
ProvideTheProcessesForConsultationBetweenStakeholdersAndTheBoardOnEconomicEnvironmentalAndSocialTopicsOrIfConsultationIsDelegatedHowIsFeedbackFromSuchConsultationsProvidedToTheBoardExplanatoryTextBlock
RadioactiveWaste
ReasonsForForcedRecall
ReasonsForVoluntaryRecall
RecyclingAndOrSafeDisposalAsAPercentageToTotalTurnover
RemarksForAssuranceOfComplaintsFiledUnderTheSexualHarassmentOfWomenAtWorkplace
RemarksForAssuranceOfDataBreachesInformationLikeNumberOfInstancesOfDataBreachesAlongWithImpactAndPercentageOfDataBreachesInvolvingPersonallyIdentifiableInformationOfCustomers
RemarksForAssuranceOfDescribeTheProcessesInPlaceToSafelyReclaimYourProductsForReusingRecyclingAndDisposingAtTheEndOfLifeForPlasticsIncludingPackagingEWasteHazardousWasteAndOtherWaste
RemarksForAssuranceOfDetailsOfConcentrationOfPurchasesAndSalesWithTradingHousesDealersAndRelatedPartiesAlongWithLoansAndAdvancesAndInvestmentsWithRelatedParties
RemarksForAssuranceOfDetailsOfGreenHouseGasEmissionsAndItsIntensity
RemarksForAssuranceOfDetailsOfMeasuresForTheWellBeingOfEmployeesAndWorkersAndSpendingOnIt
RemarksForAssuranceOfDetailsOfMedianOfRemunerationOrSalaryOrWagesAndWagesPaidToFemale
RemarksForAssuranceOfDetailsOfSafetyRelatedIncidents
RemarksForAssuranceOfDetailsOfTheDisclosuresRelatedToWaterDischarged
RemarksForAssuranceOfDetailsOfTheDisclosuresRelatedToWaterWithdrawal
RemarksForAssuranceOfDetailsOfTotalEnergyConsumptionInJoulesOrMultiplesAndEnergyIntensity
RemarksForAssuranceOfDetailsRelatedToWasteManagementByTheEntity
RemarksForAssuranceOfJobCreationInSmallerTownsDiscloseWagesPaidToPersonsEmployedIncludingEmployeesOrWorkersEmployedOnAPermanentOrNonPermanentOrOnContractBasis
RemarksForAssuranceOfNumberOfDaysOfAccountsPayables
RemarksForAssuranceOfPercentageOfInputMaterialInputsToTotalInputsByValueSourcedFromSuppliers
RemarksInCaseComplaintsReceivedInRelationToIssuesOfConflictOfInterestOfTheDirectors
RemarksInCaseComplaintsReceivedInRelationToIssuesOfConflictOfInterestOfTheKmps
ReportingBoundary
RevenueFromOperations
```
