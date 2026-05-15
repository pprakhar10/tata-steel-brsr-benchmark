## GEMINI HANDOFF — PDF Extraction + Data Verification: Tata Steel (FY2023, FY2024, FY2025)

You are processing 3 BRSR (Business Responsibility and Sustainability Report) PDF filings for **Tata Steel Limited**:
- TATA STEEL FY23.pdf — Financial Year 2022–23
- TATA STEEL FY24.pdf — Financial Year 2023–24
- TATA STEEL FY25.pdf — Financial Year 2024–25

---

### CRITICAL CONTEXT: Reporting Boundary

**FY2023 is on a CONSOLIDATED basis** (includes UK, Netherlands, and other subsidiaries).
**FY2024 and FY2025 are on a STANDALONE basis** (India operations only).

This means FY2023 figures are larger by design — they cover a global footprint. Do not treat the drop from FY2023 to FY2024 as a negative trend; it is a reporting boundary change.

---

### Your Task

For each year (FY2023, FY2024, FY2025), produce a separate JSON object following the schema in the **Output Format** section.

You must do TWO things for each year:

**Part A — Data Verification**: Check the XBRL-extracted values listed below against what the PDF actually reports. For each verification task, provide the PDF-reported value, the unit used in the PDF, and whether it matches, corrects, or cannot be found.

**Part B — Enrichment Extraction**: Extract structured narrative content — targets, initiatives, management commentary, etc. — that does not appear in XBRL structured data.

---

### Part A — XBRL Values to Verify

The following values were extracted from Tata Steel's XBRL filings. Locate each in the PDF and confirm or correct them.

#### FY2023 (Consolidated basis)

| Tag | XBRL Value (normalized) | Raw value in XBRL | Raw unit in XBRL | What to check |
|---|---|---|---|---|
| TotalScope1Emissions | 75,750,000 tCO2e | 75.75 | Million tonnes CO2 equivalent | Confirm value and unit |
| TotalScope2Emissions | 5,200,000 tCO2e | 5.2 | Million tonnes CO2 equivalent | Confirm value and unit |
| TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput | **61** | 61 | (no unit in XBRL) | ⚠️ CRITICAL: Peers report ~2.3–2.8 tCO2e/tonne. 61 appears implausible for physical intensity. What value and unit does the PDF report for Scope 1+2 intensity per tonne of steel? |
| TotalElectricityConsumption | 67,000,000 GJ | 67 | petajoules | 67 PJ = 67M GJ. Confirm whether the PDF reports 67 PJ or a different number/unit. |
| TotalEnergyConsumedFromRenewableAndNonRenewableSources | 857,000,000 GJ | 857 | petajoules | 857 PJ total energy. Confirm value and unit in PDF. |
| TotalVolumeOfWaterWithdrawal | 201,372,353 kL | 201,372,353 | kilolitres | Confirm whether PDF uses kL or ML or m³. Report the PDF number and unit. |
| WaterWithdrawalByGroundwater | 16,870,056 kL | 16,870,056 | kilolitres | Same — confirm unit. |
| TotalWasteGenerated | 20,226,592 MT | 20,226,592 | (no unit) | What is the unit used in PDF for waste? |
| Sox | 51 kt/year | 51 | Kilotonnes/year | Confirm value and unit |
| Nox | 30 kt/year | 30 | Kilotonnes/year | Confirm value and unit |
| ParticulateMatter | 11 kt/year | 11 | Kilotonnes/year | Confirm value and unit |
| WaterIntensityPerRupeeOfTurnover | 0.08 | 0.08 | (no unit) | What is the denominator? Per rupee? Per crore? Per Rs. lakh? |

#### FY2024 (Standalone basis)

| Tag | XBRL Value (normalized) | Raw value | Raw unit | What to check |
|---|---|---|---|---|
| TotalScope1Emissions | 56,000,000 tCO2e | 56 | Million tonnes CO2 equivalent | Confirm |
| TotalScope2Emissions | 7,000,000 tCO2e | 7 | Million tonnes CO2 equivalent | Confirm |
| TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput | 3.1 | 3.1 | (no unit) | What unit does PDF use (tCO2e/tonne? tCO2e/Rs.Cr?)? |
| TotalEnergyConsumedFromRenewableAndNonRenewableSources | 545,962,401 GJ | 545,962,401.36 | gigajoules | Unit carried forward from FY23 (GJ). Confirm PDF uses GJ. |
| TotalVolumeOfWaterWithdrawal | 102,359,060 kL | 102,359,059.6 | kilolitres | Confirm unit |
| ParticulateMatter | 9 kt/year | 9 | Kilotonnes/year | Confirm value and unit |
| Sox | NOT IN XBRL | — | — | ⚠️ What does the FY2024 PDF report for SOx emissions? Value and unit. |
| Nox | NOT IN XBRL | — | — | ⚠️ What does the FY2024 PDF report for NOx emissions? Value and unit. |
| WaterIntensityPerRupeeOfTurnover | 0.0000627 | 0.0000626653 | (no unit) | Confirm denominator (per rupee? per crore?) |

#### FY2025 (Standalone basis)

| Tag | XBRL Value (normalized) | Raw value | Raw unit | What to check |
|---|---|---|---|---|
| TotalScope1Emissions | 61,000,000 tCO2e | 61 | Million tonnes CO2 equivalent | Confirm |
| TotalScope2Emissions | 5,000,000 tCO2e | 5 | Million tonnes CO2 equivalent | Confirm |
| TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput | 3.2 | 3.2 | (no unit) | What unit does PDF use? |
| TotalEnergyConsumedFromRenewableAndNonRenewableSources | 587,567,890 GJ | 587,567,890.25 | gigajoules | Confirm PDF uses GJ |
| TotalVolumeOfWaterWithdrawal | 110,829,245 kL | 110,829,245.15 | kilolitres | Confirm unit |
| ParticulateMatter | 8 kt/year | 8 | Kilotonnes/year | Confirm value and unit |
| Sox | NOT IN XBRL | — | — | ⚠️ What does the FY2025 PDF report for SOx emissions? Value and unit. |
| Nox | NOT IN XBRL | — | — | ⚠️ What does the FY2025 PDF report for NOx emissions? Value and unit. |

---

### Part B — Enrichment Extraction

For each year, extract the following from the BRSR section of the PDF. If a field is not present in a given year, set it to null or an empty array.

| Field | What to extract |
|---|---|
| targets | Net-zero target year, interim reduction targets (Scope 1/2/3), science-based targets status, any stated reduction % or absolute target with timeline |
| initiatives | Specific named projects undertaken — energy efficiency, water recycling, decarbonization, waste reduction, renewable energy capacity additions. Include: name/description, area (energy/water/emissions/waste/social), quantified outcome if stated (e.g. "reduced coal consumption by X tonnes") |
| scope3Breakdown | Upstream vs downstream Scope 3 categories identified and quantified (if disclosed). Categories (1–15 per GHG Protocol). |
| managementCommentary | Key ESG statements from MD/CEO commentary or Director's Report. 3–5 verbatim or close-paraphrase sentences that capture management's stated ESG priorities. |
| awardsAndRatings | ESG ratings received (CDP score, EcoVadis, Sustainalytics, DJSI, GRI, etc.), certifications, industry recognitions for sustainability |
| nonCompliance | Any regulatory penalties, environmental non-compliance notices, legal proceedings related to environment or safety mentioned in the BRSR |
| forwardLooking | Stated goals for the next 1–3 years (capex targets, renewable energy target, water reduction target, etc.) |
| qualitativePolicies | Brief description of the actual content of key policies — not just "yes we have a policy" but what the policy says. Cover: environmental policy (P6), occupational health and safety policy (P3), anti-corruption/ethics policy (P1). |
| steelProduction | Crude steel production volume (in metric tonnes) for the year as reported in the PDF. This is a critical denominator. |
| reportingBoundary | What reporting boundary does the PDF declare? (Consolidated/Standalone, India/Global) |

---

### Output Format

Return exactly 3 JSON objects, one per year, each matching this structure. Do not wrap them in an array — output them sequentially, clearly labelled.

```json
{
  "companyId": "tata-steel",
  "year": "FY2023",
  "source": "PDF",
  "xbrlPatches": {
    "TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput": {
      "pdfValue": "<value from PDF>",
      "pdfUnit": "<unit from PDF>",
      "action": "CONFIRM | CORRECT | NOT_FOUND",
      "note": "<explanation if correcting or if PDF differs from XBRL>"
    },
    "TotalElectricityConsumption": {
      "pdfValue": "<value>",
      "pdfUnit": "<unit>",
      "action": "CONFIRM | CORRECT | NOT_FOUND",
      "note": ""
    },
    "TotalEnergyConsumedFromRenewableAndNonRenewableSources": {
      "pdfValue": "<value>",
      "pdfUnit": "<unit>",
      "action": "CONFIRM | CORRECT | NOT_FOUND",
      "note": ""
    },
    "TotalVolumeOfWaterWithdrawal": {
      "pdfValue": "<value>",
      "pdfUnit": "<unit>",
      "action": "CONFIRM | CORRECT | NOT_FOUND",
      "note": ""
    },
    "WaterWithdrawalByGroundwater": {
      "pdfValue": "<value>",
      "pdfUnit": "<unit>",
      "action": "CONFIRM | CORRECT | NOT_FOUND",
      "note": ""
    },
    "WaterIntensityPerRupeeOfTurnover": {
      "pdfValue": "<value>",
      "pdfUnit": "<unit — including denominator type (per rupee / per crore / per lakh)>",
      "action": "CONFIRM | CORRECT | NOT_FOUND",
      "note": ""
    },
    "Sox_FY2024": {
      "pdfValue": "<value>",
      "pdfUnit": "<unit>",
      "action": "FOUND | NOT_FOUND",
      "note": "SOx not in XBRL for FY2024 — report PDF value here"
    },
    "Nox_FY2024": {
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
        "metric": "<what is being targeted — Scope1/Scope2/energy intensity/water/etc.>",
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
      "note": "<any qualitative description of Scope 3 approach>"
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
      "note": "<Consolidated or Standalone, source location in PDF>"
    },
    "reportingBoundary": "<Consolidated / Standalone / specify scope>"
  }
}
```

---

### Rules

1. Do not invent values. If you cannot find something in the PDF, set `action: "NOT_FOUND"` and leave the value null.
2. For `xbrlPatches`, only list tags where you found the value in the PDF (or specifically looked and did not find it). Do not list tags you did not check.
3. For numeric values extracted from the PDF, preserve the exact number and unit as printed in the PDF — do not convert or round.
4. Produce 3 separate JSON objects (FY2023, FY2024, FY2025), each complete and independently readable.
5. Keep `managementCommentary` factual — paraphrase or quote the PDF, do not editorialize.
6. For `xbrlPatches`, the top-priority items are: (a) TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput for FY2023, (b) Sox and Nox for FY2024 and FY2025, (c) WaterIntensityPerRupeeOfTurnover denominator clarification for all years.
