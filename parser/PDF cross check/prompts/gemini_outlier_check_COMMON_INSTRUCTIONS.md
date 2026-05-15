# BRSR XBRL Outlier Verification - Common Instructions
# Read this before processing any individual company-year prompt

---

## What you are doing

You are cross-checking data values that were automatically extracted from XBRL filings against the company's actual BRSR (Business Responsibility and Sustainability Report) PDF. The XBRL parser flagged these values as statistical outliers - either much higher or lower than peer companies, or changing dramatically year-over-year. Your job is to verify whether the flagged value is correct as reported, or whether there is an error.

You are reading one specific company's BRSR PDF for one specific financial year. Every item in the checklist refers to a metric that should be findable in that PDF.

---

## Output format

For every checklist item, respond with one line in this exact format:

```
ITEM_# | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
```

Fields:

| Field | What to put |
|-------|-------------|
| ITEM_# | The item number from the checklist (e.g. ITEM_1) |
| VERDICT | One of the 6 verdict codes below |
| PDF_VALUE | The exact value as it appears in the PDF, including unit if shown. If NOT_FOUND, write — |
| PAGE_OR_SECTION | Page number, table name, or section heading where you found it. If NOT_FOUND, write — |
| NOTE | One sentence explanation. Required for CORRECTED and UNIT_ERROR. Optional but helpful for others. |

---

## Verdict codes

| Code | When to use |
|------|-------------|
| CONFIRMED | PDF value matches our XBRL value (within rounding). No change needed. |
| CORRECTED | PDF shows a clearly different value. Specify the correct value in PDF_VALUE. |
| UNIT_ERROR | The value is present but in a different unit than we assumed. Specify both the unit and value from the PDF (e.g. "25 MT - we assumed kilotonnes"). |
| EXPECTED | Value is correct and the large change is explained by something visible in the PDF (e.g. new plant commissioned, scope expansion, methodology change). Brief explanation in NOTE. |
| NOT_FOUND | You searched thoroughly but could not locate this metric in the PDF. |
| ZERO_REPORTED | Company explicitly reports zero or nil for this metric in the PDF. |

---

## Key context for all prompts

Four companies being benchmarked:
- Tata Steel Limited (integrated carbon steel, large-cap)
- JSW Steel Limited (integrated carbon steel, large-cap)
- SAIL - Steel Authority of India Limited (integrated carbon steel, PSU, large-cap)
- Jindal Stainless Limited (stainless steel via EAF, mid-cap - ~10x smaller than the others)

Financial years:
- FY2023 = April 2022 to March 2023
- FY2024 = April 2023 to March 2024
- FY2025 = April 2024 to March 2025

Standard units we use after normalization:
- Water: kilolitres (kL)
- Waste: metric tonnes (MT)
- Energy: Gigajoules (GJ)
- GHG emissions: tCO2e
- Air emissions: kilotonnes (kt)
- Financial: INR Crore

Crude steel production volumes (used for intensity cross-checks):

| Company | FY2023 | FY2024 | FY2025 |
|---------|--------|--------|--------|
| Tata Steel | 28,180,000 MT | 20,120,000 MT | 21,710,000 MT |
| JSW Steel | 24,150,000 MT | 26,430,000 MT | 27,790,000 MT |
| SAIL | 18,290,000 MT | 19,240,000 MT | 19,170,000 MT |
| Jindal Stainless | 1,710,000 MT | 2,080,000 MT | 2,430,000 MT |

Tata Steel reporting basis:
- FY2023: Consolidated (includes UK and Netherlands subsidiaries)
- FY2024 and FY2025: Standalone (India only)

This means Tata Steel FY2023 absolute volumes are legitimately larger. The FY2023 to FY2024 drop is not an error.

---

## Where to find common metrics in BRSR PDFs

- Water withdrawal and discharge: Principle 6, water withdrawal/discharge tables, split by source (groundwater, surface water, third party, others)
- Waste generated and disposal: Principle 6, waste management tables, split by type and by disposal method (reuse, recycling, incineration, landfill, other)
- Energy consumption: Principle 6, energy consumption tables, split by renewable and non-renewable sources
- GHG emissions: Principle 6, Scope 1 / Scope 2 / Scope 3 tables
- Air emissions (SOx, NOx, PM): Principle 6, air emissions table
- Wages: Principle 3 or Principle 5, employee benefits / remuneration tables
- Financial metrics (Turnover, Net Worth): Section A general disclosures at the start of the BRSR
- Safety (LTIFR, fatalities): Principle 3, safety of employees and workers tables
- Training: Principle 3, training and awareness programs tables, or HR metrics summary
- Procurement: Principle 2, responsible sourcing or supply chain disclosures
- Board composition: Section A, board details table

---

## What NOT to do

- Do not skip items because they look unimportant. Every item must get a verdict.
- Do not guess. If genuinely not found after a thorough search, use NOT_FOUND.
- Do not convert units yourself. Report what the PDF says verbatim, including its unit.
- Do not merge multiple items into one line. One line per ITEM_#.
- For CORRECTED verdicts: always write both the correct value and its unit in PDF_VALUE.
