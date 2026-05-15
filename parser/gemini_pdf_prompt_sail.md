## GEMINI HANDOFF — PDF Extraction + Data Verification: SAIL (FY2023, FY2024, FY2025)

You are processing 3 BRSR (Business Responsibility and Sustainability Report) PDF filings for **Steel Authority of India Limited (SAIL)**:
- SAIL FY23.pdf — Financial Year 2022–23
- SAIL FY24.pdf — Financial Year 2023–24
- SAIL FY25.pdf — Financial Year 2024–25

All 3 years are on a **Standalone basis**.

---

### Your Task

For each year (FY2023, FY2024, FY2025), produce a separate JSON object following the schema in the **Output Format** section.

You must do TWO things for each year:

**Part A — Data Verification**: Check the XBRL-extracted values listed below against what the PDF actually reports. For each verification task, provide the PDF-reported value, the unit used in the PDF, and whether it matches, corrects, or cannot be found.

**Part B — Enrichment Extraction**: Extract structured narrative content — targets, initiatives, management commentary, etc.

---

### Part A — XBRL Values to Verify

#### FY2023

| Tag | XBRL Value (normalized) | Raw value in XBRL | Raw unit in XBRL | What to check |
|---|---|---|---|---|
| TotalScope1Emissions | 47,603,938 tCO2e | 47,603,938 | Tonnes of CO2 | Confirm value and unit |
| TotalScope2Emissions | 3,020,822 tCO2e | 3,020,822 | Tonnes of CO2 | Confirm value and unit |
| TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput | 2.8 | 2.8 | (no unit) | What unit does PDF use? tCO2e/tonne of steel? |
| TotalElectricityConsumption | 140,372,300 GJ | 140,372.3 | terajoules | ⚠️ CRITICAL UNIT CHECK: 140,372.3 TJ = 140,372,300 GJ. But compared to total energy (591M GJ), electricity = 24% which is plausible. Confirm: does PDF report electricity as ~140,372 TJ or ~140,372,300 GJ or a different number? |
| TotalEnergyConsumedFromRenewableAndNonRenewableSources | 591,044,300 GJ | 591,044.3 | terajoules | 591,044.3 TJ = 591,044,300 GJ. Confirm PDF value and unit. |
| TotalVolumeOfWaterWithdrawal | 55,285,451 kL | 55,285,451 | kilolitres | Confirm unit (kL / ML / m³) |
| WaterWithdrawalByGroundwater | 0 kL | 0 | kilolitres | Confirm — is groundwater withdrawal actually zero for SAIL? |
| TotalWasteGenerated | 12,724,292 MT | 12,724,291.85 | (no unit) | What unit does PDF use for waste? |
| Sox | "3 to 76" (text, not parsed) | "3 to 76" | (no unit) | ⚠️ SAIL reported SOx as a range ("3 to 76") in XBRL, which cannot be parsed as a number. What does the PDF actually report for SOx? Is it a range, a single value, or in µg/m³? |
| Nox | "3 to 87" (text, not parsed) | "3 to 87" | (no unit) | Same — what does PDF report for NOx? |
| ParticulateMatter | "31 to 99" (text, not parsed) | "31 to 99" | (no unit) | Same — what does PDF report for PM? |
| WaterIntensityPerRupeeOfTurnover | 0.05 | 0.05 | (no unit) | What denominator does PDF use? Per rupee? Per crore? |

#### FY2024

| Tag | XBRL Value (normalized) | Raw value | Raw unit | What to check |
|---|---|---|---|---|
| TotalScope1Emissions | 52,622,079 tCO2e | 52,622,079 | Tonnes of CO2 | Confirm |
| TotalScope2Emissions | 2,446,630 tCO2e | 2,446,630 | Tonnes of CO2 | Confirm |
| TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput | **0.0** | 0 | (no unit) | ⚠️ CRITICAL: This is clearly wrong — zero Scope 1+2 intensity is impossible. What does the FY2024 PDF report for this indicator? Value and unit. |
| TotalEnergyConsumedFromRenewableAndNonRenewableSources | 614,166,500 GJ | 614,166.5 | terajoules | Confirm PDF value and unit |
| TotalVolumeOfWaterWithdrawal | 57,396,487 kL | 57,396,487 | kilolitres | Confirm unit |
| ParticulateMatter | 0.58 | 0.58 | µg/m³ | ⚠️ SAIL FY2024 switched to µg/m³ (concentration). This cannot be converted to kilotonnes (mass) without stack flow rate data. Confirm the PDF uses µg/m³. What values does the PDF show for SOx, NOx, and PM in FY2024? |
| Sox | NOT IN XBRL | — | — | ⚠️ What does FY2024 PDF report for SOx? Value and unit. |
| Nox | NOT IN XBRL | — | — | ⚠️ What does FY2024 PDF report for NOx? Value and unit. |
| WaterIntensityPerRupeeOfTurnover | **52.33** | 52.334677037 | (no unit) | ⚠️ In FY2023 this was 0.05. A 1000× jump in one year is highly suspicious. What does the FY2024 PDF report for water intensity? What is the denominator? |

#### FY2025

| Tag | XBRL Value (normalized) | Raw value | Raw unit | What to check |
|---|---|---|---|---|
| TotalScope1Emissions | 52,178,648 tCO2e | 52,178,648 | Tonnes of CO2 | Confirm |
| TotalScope2Emissions | 4,796,073 tCO2e | 4,796,073 | Tonnes of CO2 | Confirm — Scope 2 roughly doubled vs FY2024. Genuine? |
| TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput | 3.01 | 3.01 | (no unit) | Confirm value and unit |
| TotalEnergyConsumedFromRenewableAndNonRenewableSources | 519,431,000 GJ | 519,431 | terajoules | Confirm PDF value and unit |
| TotalVolumeOfWaterWithdrawal | 129,577,216 kL | 129,577,216 | kilolitres | ⚠️ More than doubled vs FY2024 (57M→129M kL). Confirm whether this is correct or a unit change. |
| ParticulateMatter | 0.56 | 0.56 | µg/m³ | Confirm PM still in µg/m³ in FY2025 |
| Sox | NOT IN XBRL | — | — | What does FY2025 PDF report for SOx? Value and unit. |
| Nox | NOT IN XBRL | — | — | What does FY2025 PDF report for NOx? Value and unit. |
| WaterIntensityPerRupeeOfTurnover | 0.0890 | 0.0890416286 | (no unit) | FY2025 is back near FY2023 level (0.05). Does PDF clarify the denominator? Why did FY2024 show 52.33? |

---

### Part B — Enrichment Extraction

For each year, extract the following from the BRSR section of the PDF.

| Field | What to extract |
|---|---|
| targets | Net-zero target year, emission reduction targets, science-based targets status, any stated reduction % with timeline |
| initiatives | Specific named projects — energy efficiency, water recycling, decarbonization, waste reduction. Include: description, area, quantified outcome if stated |
| scope3Breakdown | Scope 3 categories identified and quantified (if disclosed) |
| managementCommentary | Key ESG statements from MD/Chairman commentary. 3–5 verbatim or close-paraphrase sentences |
| awardsAndRatings | ESG ratings, certifications, industry recognitions (CDP, GRI, Sustainalytics, etc.) |
| nonCompliance | Any regulatory penalties, environmental non-compliance notices, safety incidents mentioned |
| forwardLooking | Stated goals for the next 1–3 years |
| qualitativePolicies | P1 (ethics/anti-corruption), P3 (OHS), P6 (environmental) — what the policies actually say |
| steelProduction | Crude steel production volume (metric tonnes) as reported in the PDF |
| reportingBoundary | What reporting boundary does the PDF declare? |

---

### Output Format

Return exactly 3 JSON objects, one per year, each matching this structure. Do not wrap them in an array — output them sequentially, clearly labelled.

```json
{
  "companyId": "sail",
  "year": "FY2023",
  "source": "PDF",
  "xbrlPatches": {
    "TotalElectricityConsumption": {
      "pdfValue": "<value from PDF>",
      "pdfUnit": "<unit from PDF>",
      "action": "CONFIRM | CORRECT | NOT_FOUND",
      "note": "<explanation if PDF differs from XBRL>"
    },
    "Sox": {
      "pdfValue": "<value or range>",
      "pdfUnit": "<unit as printed in PDF>",
      "action": "CONFIRM | CORRECT | NOT_FOUND",
      "note": "<is it a range? what unit? µg/m³ or kt or something else?>"
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
    "TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput_FY2024": {
      "pdfValue": "<value from FY2024 PDF>",
      "pdfUnit": "<unit>",
      "action": "FOUND | NOT_FOUND",
      "note": "XBRL reports 0 for this — clearly wrong"
    },
    "WaterIntensityPerRupeeOfTurnover_FY2024": {
      "pdfValue": "<value from FY2024 PDF>",
      "pdfUnit": "<unit>",
      "action": "FOUND | NOT_FOUND",
      "note": "XBRL shows 52.33 vs FY2023=0.05 — investigate denominator change"
    },
    "TotalVolumeOfWaterWithdrawal_FY2025": {
      "pdfValue": "<value from FY2025 PDF>",
      "pdfUnit": "<unit>",
      "action": "CONFIRM | CORRECT | NOT_FOUND",
      "note": "XBRL shows 129M kL vs FY2024=57M kL — verify doubling"
    },
    "Sox_FY2024": {
      "pdfValue": "<SOx from FY2024 PDF>",
      "pdfUnit": "<unit>",
      "action": "FOUND | NOT_FOUND",
      "note": ""
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
      "categories": [],
      "note": "<qualitative description>"
    },
    "managementCommentary": "<3–5 key sentences from MD/Chairman ESG commentary>",
    "awardsAndRatings": [
      { "name": "<award/rating>", "score": "<score if applicable>", "year": "<year>" }
    ],
    "nonCompliance": [
      { "description": "<incident or penalty>", "resolution": "<outcome if stated>" }
    ],
    "forwardLooking": [
      { "description": "<stated goal>", "timeline": "<year or period>" }
    ],
    "qualitativePolicies": {
      "P1_ethics": "<ethics/anti-corruption policy content>",
      "P3_ohs": "<OHS policy content>",
      "P6_environment": "<environmental policy content>"
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
5. Top-priority verification items: (a) FY2024 emissions intensity (XBRL=0, clearly wrong), (b) FY2024 water intensity (XBRL=52.33, suspicious 1000× jump), (c) FY2025 water withdrawal doubling, (d) SOx/NOx/PM unit clarification across all years (FY2023 reported as ranges, FY2024+ may be µg/m³).
