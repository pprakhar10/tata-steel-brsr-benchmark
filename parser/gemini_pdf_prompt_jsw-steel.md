## GEMINI HANDOFF — PDF Extraction + Data Verification: JSW Steel (FY2023, FY2024, FY2025)

You are processing 3 BRSR (Business Responsibility and Sustainability Report) PDF filings for **JSW Steel Limited**:
- JSW STEEL FY23.pdf — Financial Year 2022–23
- JSW STEEL FY24.pdf — Financial Year 2023–24
- JSW STEEL FY25.pdf — Financial Year 2024–25

All 3 years are on a **Standalone basis** (India operations only).

---

### Your Task

For each year (FY2023, FY2024, FY2025), produce a separate JSON object following the schema in the **Output Format** section.

You must do TWO things for each year:

**Part A — Data Verification**: Check the XBRL-extracted values listed below against what the PDF actually reports. For each verification task, provide the PDF-reported value, the unit used in the PDF, and whether it matches, corrects, or cannot be found.

**Part B — Enrichment Extraction**: Extract structured narrative content — targets, initiatives, management commentary, etc. — that does not appear in XBRL structured data.

---

### Part A — XBRL Values to Verify

The following values were extracted from JSW Steel's XBRL filings. Locate each in the PDF and confirm or correct them.

#### FY2023

| Tag | XBRL Value (normalized) | Raw value in XBRL | Raw unit in XBRL | What to check |
|---|---|---|---|---|
| TotalScope1Emissions | 46,941,683 tCO2e | 46,941,683 | Metric Tonnes | Confirm value and unit |
| TotalScope2Emissions | 2,417,702 tCO2e | 2,417,702 | Metric Tonnes | Confirm value and unit |
| TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput | 2.36 | 2.36 | (no unit in XBRL) | What unit does PDF use? tCO2e/tonne of steel? |
| TotalElectricityConsumption | 12,650,641 GJ | 12,650,641 | gigajoules | ⚠️ This is only ~2.6% of total energy (494M GJ), which is low for an integrated steel plant. Confirm this is the PDF value. Is electricity reported separately from total energy? |
| TotalEnergyConsumedFromRenewableAndNonRenewableSources | 494,384,430 GJ | 494,384,430 | gigajoules | Confirm total energy value and unit |
| TotalVolumeOfWaterWithdrawal | 86,267,847 kL | 86,267,847 | kilolitres | Confirm unit in PDF (kL / ML / m³) |
| WaterWithdrawalByGroundwater | 15,142 kL | 15,142 | kilolitres | ⚠️ Extremely low (15,142 kL groundwater for a 24M-tonne steel company). Confirm this is the PDF value or correct. |
| TotalWasteGenerated | 14,414,261 MT | 14,414,261.49 | (no unit) | What unit does PDF use for waste? |
| Sox | 40.8135 kilotonnes | 1.69 | kg/tcs (kg per tonne of crude steel) | XBRL reported in kg/tcs; normalized using FY2023 production of 24,150,000 t → 40.81 kt. Confirm: (1) PDF value in kg/tcs and (2) whether PDF also shows absolute value |
| Nox | 28.7385 kilotonnes | 1.19 | kg/tcs | Same as SOx — confirm PDF value and whether absolute is also shown |
| ParticulateMatter | 10.143 kilotonnes | 0.42 | kg/tcs | Same — confirm PDF value |
| WaterIntensityPerRupeeOfTurnover | 0.0393 | 0.0393 | (no unit) | What denominator does PDF use? Per rupee? Per crore? |

#### FY2024

| Tag | XBRL Value (normalized) | Raw value | Raw unit | What to check |
|---|---|---|---|---|
| TotalScope1Emissions | 52,106,566 tCO2e | 52,106,566 | Metric Tonnes | Confirm |
| TotalScope2Emissions | 1,061,079 tCO2e | 1,061,079 | Metric Tonnes | Confirm |
| TotalEnergyConsumedFromRenewableAndNonRenewableSources | 517,690,735 GJ | 517,690,735 | gigajoules | Confirm unit |
| TotalVolumeOfWaterWithdrawal | 89,191,228 kL | 89,191,228 | kilolitres | Confirm unit |
| ParticulateMatter | 8.308562 kilotonnes | 8,308,562 | kg | Normalized: 8,308,562 kg ÷ 1,000,000 = 8.31 kt. Confirm PDF value and unit. |
| Sox | NOT IN XBRL | — | — | ⚠️ SOx not reported in FY2024 XBRL. What does the FY2024 PDF report for SOx? Value and unit. |
| Nox | NOT IN XBRL | — | — | ⚠️ NOx not reported in FY2024 XBRL. What does the FY2024 PDF report? |

#### FY2025

| Tag | XBRL Value (normalized) | Raw value | Raw unit | What to check |
|---|---|---|---|---|
| TotalScope1Emissions | 53,100,752 tCO2e | 53,100,751.63 | Metric Tonnes | Confirm |
| TotalScope2Emissions | 1,653,057 tCO2e | 1,653,056.65 | Metric Tonnes | Confirm |
| TotalEnergyConsumedFromRenewableAndNonRenewableSources | 529,209,357 GJ | 529,209,356.78 | gigajoules | Confirm unit |
| TotalVolumeOfWaterWithdrawal | 95,735,451 kL | 95,735,450.66 | kilolitres | Confirm unit |
| ParticulateMatter | 8.764820 kilotonnes | 8,764,819.78 | kg | Normalized: 8,764,819.78 kg ÷ 1,000,000 = 8.76 kt. Confirm PDF value and unit. |
| Sox | NOT IN XBRL | — | — | ⚠️ SOx not reported in FY2025 XBRL. What does the FY2025 PDF report? |
| Nox | NOT IN XBRL | — | — | ⚠️ NOx not reported in FY2025 XBRL. What does the FY2025 PDF report? |

---

### Part B — Enrichment Extraction

For each year, extract the following from the BRSR section of the PDF. If a field is not present in a given year, set it to null or an empty array.

| Field | What to extract |
|---|---|
| targets | Net-zero target year, interim reduction targets (Scope 1/2/3), science-based targets status, any stated reduction % or absolute target with timeline |
| initiatives | Specific named projects undertaken — energy efficiency, water recycling, decarbonization, waste reduction, renewable energy capacity additions. Include: name/description, area (energy/water/emissions/waste/social), quantified outcome if stated |
| scope3Breakdown | Upstream vs downstream Scope 3 categories identified and quantified (if disclosed) |
| managementCommentary | Key ESG statements from MD/CEO commentary or Director's Report. 3–5 verbatim or close-paraphrase sentences |
| awardsAndRatings | ESG ratings received (CDP score, EcoVadis, Sustainalytics, DJSI, GRI, etc.), certifications, industry recognitions |
| nonCompliance | Any regulatory penalties, environmental non-compliance notices, legal proceedings related to environment or safety |
| forwardLooking | Stated goals for the next 1–3 years |
| qualitativePolicies | Brief description of the actual content of key policies — P1 (ethics/anti-corruption), P3 (OHS), P6 (environmental) |
| steelProduction | Crude steel production volume (metric tonnes) as reported in the PDF |
| reportingBoundary | What reporting boundary does the PDF declare? |

---

### Output Format

Return exactly 3 JSON objects, one per year, each matching this structure. Do not wrap them in an array — output them sequentially, clearly labelled.

```json
{
  "companyId": "jsw-steel",
  "year": "FY2023",
  "source": "PDF",
  "xbrlPatches": {
    "TotalElectricityConsumption": {
      "pdfValue": "<value from PDF>",
      "pdfUnit": "<unit from PDF>",
      "action": "CONFIRM | CORRECT | NOT_FOUND",
      "note": "<explanation if PDF differs from XBRL>"
    },
    "WaterWithdrawalByGroundwater": {
      "pdfValue": "<value>",
      "pdfUnit": "<unit>",
      "action": "CONFIRM | CORRECT | NOT_FOUND",
      "note": ""
    },
    "Sox": {
      "pdfValue": "<value in PDF — report in original PDF unit>",
      "pdfUnit": "<unit as printed in PDF>",
      "action": "CONFIRM | CORRECT | NOT_FOUND",
      "note": "<does PDF also show absolute value in addition to kg/tcs?>"
    },
    "Nox": {
      "pdfValue": "<value>",
      "pdfUnit": "<unit>",
      "action": "CONFIRM | CORRECT | NOT_FOUND",
      "note": ""
    },
    "ParticulateMatter": {
      "pdfValue": "<value>",
      "pdfUnit": "<unit>",
      "action": "CONFIRM | CORRECT | NOT_FOUND",
      "note": ""
    },
    "WaterIntensityPerRupeeOfTurnover": {
      "pdfValue": "<value>",
      "pdfUnit": "<unit — including denominator type>",
      "action": "CONFIRM | CORRECT | NOT_FOUND",
      "note": ""
    },
    "Sox_FY2024": {
      "pdfValue": "<SOx value from FY2024 PDF>",
      "pdfUnit": "<unit>",
      "action": "FOUND | NOT_FOUND",
      "note": "SOx not in FY2024 XBRL"
    },
    "Nox_FY2024": {
      "pdfValue": "<value>",
      "pdfUnit": "<unit>",
      "action": "FOUND | NOT_FOUND",
      "note": ""
    },
    "Sox_FY2025": {
      "pdfValue": "<value>",
      "pdfUnit": "<unit>",
      "action": "FOUND | NOT_FOUND",
      "note": ""
    },
    "Nox_FY2025": {
      "pdfValue": "<value>",
      "pdfUnit": "<unit>",
      "action": "FOUND | NOT_FOUND",
      "note": ""
    }
  },
  "enrichment": {
    "targets": [
      {
        "description": "<target description>",
        "metric": "<what is being targeted>",
        "baseline": "<baseline year and value if stated>",
        "targetValue": "<target value or % reduction>",
        "timeline": "<target year>"
      }
    ],
    "initiatives": [
      {
        "name": "<project or initiative name>",
        "area": "energy | water | emissions | waste | social | governance",
        "description": "<what was done>",
        "outcome": "<quantified result if stated, else null>"
      }
    ],
    "scope3Breakdown": {
      "totalScope3": "<value and unit if disclosed>",
      "categories": [
        { "categoryNumber": 1, "name": "Purchased goods and services", "value": "<if disclosed>" }
      ],
      "note": "<qualitative description of Scope 3 approach>"
    },
    "managementCommentary": "<3–5 key sentences from MD/CEO/Director ESG commentary>",
    "awardsAndRatings": [
      { "name": "<award/rating name>", "score": "<score or tier if applicable>", "year": "<year received>" }
    ],
    "nonCompliance": [
      { "description": "<incident or penalty>", "resolution": "<outcome if stated>" }
    ],
    "forwardLooking": [
      { "description": "<stated goal>", "timeline": "<year or period>" }
    ],
    "qualitativePolicies": {
      "P1_ethics": "<what the anti-corruption/ethics policy says>",
      "P3_ohs": "<what the OHS policy says>",
      "P6_environment": "<what the environmental policy says>"
    },
    "steelProduction": {
      "value": "<crude steel production in metric tonnes>",
      "unit": "metric tonnes",
      "note": "<source location in PDF>"
    },
    "reportingBoundary": "<Standalone / Consolidated / other>"
  }
}
```

---

### Rules

1. Do not invent values. If you cannot find something in the PDF, set `action: "NOT_FOUND"` and leave the value null.
2. For numeric values extracted from the PDF, preserve the exact number and unit as printed in the PDF — do not convert or round.
3. Produce 3 separate JSON objects (FY2023, FY2024, FY2025), each complete and independently readable.
4. Keep `managementCommentary` factual — paraphrase or quote the PDF, do not editorialize.
5. Top-priority verification items: (a) SOx/NOx for FY2024 and FY2025, (b) TotalElectricityConsumption and WaterWithdrawalByGroundwater for FY2023, (c) WaterIntensityPerRupeeOfTurnover denominator for all years.
