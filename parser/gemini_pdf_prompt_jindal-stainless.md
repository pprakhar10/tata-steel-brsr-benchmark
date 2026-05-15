## GEMINI HANDOFF — PDF Extraction + Data Verification: Jindal Stainless (FY2023, FY2024, FY2025)

You are processing 3 BRSR (Business Responsibility and Sustainability Report) PDF filings for **Jindal Stainless Limited**:
- JINDAL STAINLESS FY23.pdf — Financial Year 2022–23
- JINDAL STAINLESS FY24.pdf — Financial Year 2023–24
- JINDAL STAINLESS FY25.pdf — Financial Year 2024–25

All 3 years are on a **Standalone basis**.

### Important Scale Context

Jindal Stainless is **significantly smaller** than the other 3 companies (Tata Steel, JSW Steel, SAIL) in this benchmark:
- Produces ~1.7–2.4 million tonnes of **stainless steel** vs ~18–28 million tonnes of carbon steel for the others
- Different process chemistry: electric arc furnace (EAF) based, not blast furnace — results in lower Scope 1 GHG intensity per tonne, different energy mix, different waste profile
- Absolute values for emissions, energy, water, waste will naturally be ~10× lower than peers

---

### Your Task

For each year (FY2023, FY2024, FY2025), produce a separate JSON object following the schema in the **Output Format** section.

**Part A — Data Verification**: Check XBRL-extracted values against the PDF.
**Part B — Enrichment Extraction**: Extract targets, initiatives, management commentary, etc.

---

### Part A — XBRL Values to Verify

#### FY2023

| Tag | XBRL Value (normalized) | Raw value in XBRL | Raw unit in XBRL | What to check |
|---|---|---|---|---|
| TotalScope1Emissions | 2,584,460 tCO2e | 2,584,460 | TCO2E | Confirm value and unit |
| TotalScope2Emissions | 735,913 tCO2e | 735,913 | TCO2E | Confirm value and unit |
| TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput | 2.1 | 2.1 | (no unit) | What unit does PDF use? tCO2e/tonne of stainless steel? |
| TotalElectricityConsumption | 3,571,159 GJ | 3,571,159 | gigajoules | Confirm |
| TotalEnergyConsumedFromRenewableAndNonRenewableSources | 30,275,547 GJ | 30,275,547 | gigajoules | Confirm |
| TotalVolumeOfWaterWithdrawal | 11,681,607 kL | 11,681,607 | kilolitres | Confirm unit (kL / ML / m³) |
| WaterWithdrawalByGroundwater | 10,413 kL | 10,413 | kilolitres | Confirm value and unit |
| TotalWasteGenerated | 1,628,584 MT | 1,628,583.65 | (no unit) | What unit does PDF use for waste? |
| Sox | 0.85189 kilotonnes | 851.89 | MT (metric tonnes) | Normalized: 851.89 MT ÷ 1000 = 0.852 kt. Confirm PDF value and unit. |
| Nox | 1.98068 kilotonnes | 1,980.68 | MT | Normalized: 1,980.68 MT ÷ 1000 = 1.981 kt. Confirm PDF value and unit. |
| ParticulateMatter | 2.08413 kilotonnes | 2,084.13 | MT | Normalized: 2,084.13 MT ÷ 1000 = 2.084 kt. Confirm PDF value and unit. |
| WaterIntensityPerRupeeOfTurnover | **335** | 335 | (no unit) | ⚠️ CRITICAL: Peers report 0.04–0.08 for this indicator. 335 is ~4000× higher. What does the PDF report? What is the denominator? Per rupee? Per crore? Per Rs. lakh? This may be a denominator mismatch — the PDF likely clarifies the unit. |

#### FY2024

| Tag | XBRL Value (normalized) | Raw value | Raw unit | What to check |
|---|---|---|---|---|
| TotalScope1Emissions | 2,992,334 tCO2e | 2,992,333.83 | TCO2E | Confirm |
| TotalScope2Emissions | 787,140 tCO2e | 787,140.25 | TCO2E | Confirm |
| TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput | 2.15 | 2.15 | (no unit) | Confirm value and unit |
| TotalEnergyConsumedFromRenewableAndNonRenewableSources | 35,143,709 GJ | 35,143,709.12 | gigajoules | Confirm unit |
| TotalVolumeOfWaterWithdrawal | 13,320,439 kL | 13,320,439 | kilolitres | Confirm unit |
| ParticulateMatter | 1.31327 kilotonnes | 1,313.27 | MT | Confirm PDF value and unit |
| Sox | NOT IN XBRL | — | — | ⚠️ SOx not reported in FY2024 XBRL. What does FY2024 PDF report for SOx? Value and unit. |
| Nox | NOT IN XBRL | — | — | ⚠️ NOx not reported in FY2024 XBRL. What does FY2024 PDF report? |
| WaterIntensityPerRupeeOfTurnover | 333 | 333.0084732506 | (no unit) | ⚠️ Still ~333 — what denominator does the FY2024 PDF show? |

#### FY2025

| Tag | XBRL Value (normalized) | Raw value | Raw unit | What to check |
|---|---|---|---|---|
| TotalScope1Emissions | 2,995,798 tCO2e | 2,995,798 | TCO2E | Confirm |
| TotalScope2Emissions | 622,511 tCO2e | 622,511 | TCO2E | Confirm |
| TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput | 1.85 | 1.85 | (no unit) | Confirm value and unit |
| TotalEnergyConsumedFromRenewableAndNonRenewableSources | 32,046,976 GJ | 32,046,976 | gigajoules | Confirm unit |
| TotalVolumeOfWaterWithdrawal | 15,077,894 kL | 15,077,894 | kilolitres | Confirm unit |
| ParticulateMatter | 1.60147 kilotonnes | 1,601.47 | MT | Confirm PDF value and unit |
| Sox | NOT IN XBRL | — | — | ⚠️ What does FY2025 PDF report for SOx? |
| Nox | NOT IN XBRL | — | — | ⚠️ What does FY2025 PDF report for NOx? |
| WaterIntensityPerRupeeOfTurnover | 0.0000359 | 0.0000358664 | (no unit) | ⚠️ This dropped from ~333 (FY2023/FY2024) to 0.000036 in FY2025. That is a ~9-million-fold change. This is almost certainly a denominator change — FY2023/24 were probably per crore or per lakh, FY2025 switched to per rupee (or vice versa). What does the FY2025 PDF show? |

---

### Part B — Enrichment Extraction

For each year, extract the following from the BRSR section of the PDF.

| Field | What to extract |
|---|---|
| targets | Net-zero target year, emission reduction targets, science-based targets, any stated reduction % with timeline |
| initiatives | Specific named projects — energy efficiency, water recycling, decarbonization, waste reduction, EAF optimization. Include: description, area, quantified outcome |
| scope3Breakdown | Scope 3 categories identified and quantified (if disclosed) |
| managementCommentary | Key ESG statements from MD/CEO commentary. 3–5 verbatim or close-paraphrase sentences |
| awardsAndRatings | ESG ratings, certifications, industry recognitions |
| nonCompliance | Any regulatory penalties, environmental non-compliance, safety incidents |
| forwardLooking | Stated goals for the next 1–3 years |
| qualitativePolicies | P1 (ethics/anti-corruption), P3 (OHS), P6 (environmental) — what the policies actually say |
| steelProduction | Crude stainless steel production volume (metric tonnes) as reported in the PDF |
| reportingBoundary | What reporting boundary does the PDF declare? |

---

### Output Format

Return exactly 3 JSON objects, one per year, each matching this structure. Do not wrap them in an array — output them sequentially, clearly labelled.

```json
{
  "companyId": "jindal-stainless",
  "year": "FY2023",
  "source": "PDF",
  "xbrlPatches": {
    "WaterIntensityPerRupeeOfTurnover": {
      "pdfValue": "<value from PDF>",
      "pdfUnit": "<unit — including exact denominator (per rupee / per crore / per lakh / per Rs.)>",
      "action": "CONFIRM | CORRECT | NOT_FOUND",
      "note": "<XBRL shows 335 — what does PDF show and what is the denominator?>"
    },
    "Sox": {
      "pdfValue": "<value from PDF in original unit>",
      "pdfUnit": "<unit as printed>",
      "action": "CONFIRM | CORRECT | NOT_FOUND",
      "note": "<XBRL raw: 851.89 MT — confirm PDF matches>"
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
    },
    "WaterIntensityPerRupeeOfTurnover_FY2024": {
      "pdfValue": "<value from FY2024 PDF>",
      "pdfUnit": "<unit — exact denominator>",
      "action": "FOUND | NOT_FOUND",
      "note": "FY2024 XBRL=333, FY2025 XBRL=0.0000359 — denominator likely changed"
    },
    "WaterIntensityPerRupeeOfTurnover_FY2025": {
      "pdfValue": "<value from FY2025 PDF>",
      "pdfUnit": "<unit — exact denominator>",
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
    "managementCommentary": "<3–5 key sentences from MD/CEO ESG commentary>",
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
      "value": "<crude stainless steel production in metric tonnes>",
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
5. Top-priority verification items: (a) WaterIntensityPerRupeeOfTurnover denominator for all 3 years (9-million-fold change between FY2024 and FY2025 indicates a unit change), (b) SOx/NOx for FY2024 and FY2025, (c) confirm stainless steel production volumes.
