# BRSR XBRL Outlier Verification — Common Instructions
# Read this before processing any individual company-year prompt

---

## What you are doing

You are cross-checking data values that were automatically extracted from XBRL filings against the company's actual BRSR (Business Responsibility and Sustainability Report) PDF. The XBRL parser flagged these values as statistical outliers — either much higher or lower than peer companies, or changing dramatically year-over-year. Your job is to verify whether the flagged value is correct as reported, or whether there is an error.

You are reading **one specific company's BRSR PDF for one specific financial year**. Every item in the checklist refers to a metric that should be findable in that PDF.

---

## Output format

For every checklist item, respond with one line in this exact format:

```
ITEM_# | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
```

**Fields:**

| Field | What to put |
|-------|-------------|
| `ITEM_#` | The item number from the checklist (e.g. `ITEM_1`) |
| `VERDICT` | One of the 6 verdict codes below |
| `PDF_VALUE` | The exact value as it appears in the PDF (include unit if shown). If NOT_FOUND, write `—` |
| `PAGE_OR_SECTION` | Page number, table name, or section heading where you found it. If NOT_FOUND, write `—` |
| `NOTE` | One sentence explanation. Required for CORRECTED and UNIT_ERROR. Optional but helpful for others. |

---

## Verdict codes

| Code | When to use |
|------|-------------|
| `CONFIRMED` | PDF value matches our XBRL value (within rounding). No change needed. |
| `CORRECTED` | PDF shows a clearly different value. Specify the correct value in PDF_VALUE. |
| `UNIT_ERROR` | The value is present but in a different unit than we assumed. Specify both the unit and value from the PDF (e.g. "25 MT — we assumed kilotonnes"). |
| `EXPECTED` | Value is correct and the large change is explained by something visible in the PDF (e.g. new plant commissioned, scope expansion, methodology change). Brief explanation in NOTE. |
| `NOT_FOUND` | You searched thoroughly but could not locate this metric in the PDF. |
| `ZERO_REPORTED` | Company explicitly reports zero or nil for this metric in the PDF. |

---

## Training coverage — mandatory for every prompt

Every prompt includes a training coverage request at the end. This metric is absent from all XBRL filings. Use this output format:

```
TRAINING | VERDICT | VALUE | PAGE_OR_SECTION | NOTE
```

Where VERDICT is one of:
- `FOUND` — specify exact value and unit (e.g. "85% of employees trained")
- `NOT_REPORTED` — PDF explicitly states not applicable or not reported
- `NOT_FOUND` — could not locate despite searching

Look in: Section on Employee Well-being, Human Capital, Principle 3 disclosures, training and development tables, HR metrics summary. Training coverage is often reported as "% of employees/workers trained" or "number of person-hours of training".

---

## Key context for all prompts

**Four companies being benchmarked:**
- Tata Steel Limited (integrated carbon steel, large-cap)
- JSW Steel Limited (integrated carbon steel, large-cap)
- SAIL — Steel Authority of India Limited (integrated carbon steel, PSU, large-cap)
- Jindal Stainless Limited (stainless steel via EAF, mid-cap — ~10× smaller than the others)

**Financial years:** FY2023 = April 2022 – March 2023, FY2024 = April 2023 – March 2024, FY2025 = April 2024 – March 2025

**Standard units we use (after normalization):**
- Water: kilolitres (kL)
- Waste: metric tonnes (MT)
- Energy: Gigajoules (GJ)
- GHG emissions: tCO2e
- Air emissions: kilotonnes (kt)
- Financial: INR Crore

**Crude steel production volumes (for intensity cross-checks):**
| Company | FY2023 | FY2024 | FY2025 |
|---------|--------|--------|--------|
| Tata Steel | 28,180,000 MT | 20,120,000 MT | 21,710,000 MT |
| JSW Steel | 24,150,000 MT | 26,430,000 MT | 27,790,000 MT |
| SAIL | 18,290,000 MT | 19,240,000 MT | 19,170,000 MT |
| Jindal Stainless | 1,710,000 MT | 2,080,000 MT | 2,430,000 MT |

**Tata Steel FY2023 reporting basis:** Consolidated (includes UK and Netherlands subsidiaries). FY2024 and FY2025 are Standalone (India only). This explains why some Tata FY2023 values are much larger than FY2024.

---

## Tips for finding values in BRSR PDFs

- Water metrics: look for "Water Withdrawal" tables in Principle 6, usually split by source (groundwater, surface water, third party)
- Waste metrics: look for "Waste Management" tables in Principle 6, split by type and disposal method
- Energy metrics: look for "Energy Consumption" tables in Principle 6
- Air emissions: look for "Air Emissions" or "Emissions to Air" table in Principle 6
- Wages: look for "Employee Benefits" section, or Principle 5 / Principle 3 workforce tables
- Financial metrics (Turnover, Net Worth): look for Section A general disclosures table at the start of the BRSR
- Safety metrics (LTIFR, fatalities): look for Principle 3, "Safety of Employees and Workers" tables
- Training: look for Principle 3, "Training and Awareness Programs", or workforce well-being section

---

## What NOT to do

- Do not skip items because they look unimportant — every item must get a verdict
- Do not guess — if genuinely not found after a thorough search, use NOT_FOUND
- Do not convert units yourself — report what the PDF says verbatim, including its unit
- Do not merge multiple items into one line — one line per ITEM_#
