# BRSR XBRL Outlier Verification
# Company: Tata Steel Limited
# Year: FY2023 (April 2022 – March 2023)
# PDF to upload: "TATA STEEL FY23.pdf"
# Read COMMON_INSTRUCTIONS.md before starting

---

## Company context

- **Reporting basis:** CONSOLIDATED (includes Tata Steel Netherlands, Tata Steel UK, and all Indian subsidiaries). This is why many absolute values are larger than standalone peers.
- **Crude steel production:** 28,180,000 MT (consolidated, used as intensity denominator)
- **Sector:** Integrated carbon steel (blast furnace – basic oxygen furnace)
- **Revenue (approx):** ~₹2,43,000 Crore (consolidated)

> Note: Because this is consolidated, values for water, waste, energy will legitimately be larger than JSW/SAIL (which are standalone). Flag only if the value seems disproportionate even after accounting for consolidated scope.

---

## Checklist — verify each item in the FY2023 PDF

### WATER

**ITEM_1**
- Metric: Water Withdrawal From Groundwater
- Our XBRL value: **16,870,056 kL**
- Peer comparison: JSW=15,142 kL, SAIL=not reported, Jindal=10,413 kL — Tata is **1,320× higher**
- Find in PDF: Principle 6, water withdrawal table, row "Groundwater" under "Total volume of water withdrawal"
- Question: Is 16.87 million kL of groundwater withdrawal correct for consolidated Tata Steel? At ~600 kL/tonne that seems extremely high. Check if the PDF shows it in a different unit (e.g. million litres, cubic metres) or if there is a footnote.

**ITEM_2**
- Metric: Water Withdrawal Third Party
- Our XBRL value: **19,359,133 kL**
- Peer comparison: JSW=54,000 kL, Jindal=54,000 kL — Tata is **358× higher**
- Find in PDF: Same water withdrawal table, row "Third party water" or "Purchased/municipal water"
- Question: Is 19.36 million kL correct? Cross-check against total water withdrawal disclosed.

### WASTE

**ITEM_3**
- Metric: Waste Disposed — Incineration
- Our XBRL value: **11,682 MT**
- Peer comparison: JSW=2,916 MT, SAIL=35 MT, Jindal=not reported — Tata is **4× JSW, 333× SAIL**
- Find in PDF: Principle 6, waste management table, row "Incineration" under disposal methods
- Question: Is 11,682 MT disposed by incineration correct? This is unusually high for steel manufacturing — verify against PDF.

**ITEM_4**
- Metric: Waste Recovered Through Reuse
- Our XBRL value: **8,534,853 MT**
- Peer comparison: JSW=not reported, SAIL=not reported, Jindal=not reported — no peer data but value itself seems very large
- Find in PDF: Waste management table, row "Re-use" or "Reused" under recovery methods
- Question: Is 8.53 million MT recovered through reuse correct? For context, total crude steel production is 28.18M MT. Cross-check against total waste generated figure.

**ITEM_5**
- Metric: Waste Disposed — Other Disposal Operations
- Our XBRL value: **1,156 MT**
- Peer comparison: JSW=383,203 MT, SAIL=107 MT — Tata is **331× lower than JSW** (possible underreporting or different classification)
- Find in PDF: Waste management table, row "Other" under disposal methods
- Question: Is 1,156 MT correct, or should the "other disposal" category be much larger?

### PROCUREMENT / CSR

**ITEM_6**
- Metric: Procurement Value Percentage Share (% of total procurement from responsible sourcing / value chain)
- Our XBRL value: **0.70%**
- Peer comparison: JSW=33%, SAIL=33% — Tata is **47× lower**
- Find in PDF: Principle 2 or supply chain disclosures — "percentage of procurement from suppliers assessed for responsible sourcing" or similar
- Question: Is 0.70% correct? This is unusually low for a company with Tata Steel's stated sustainability commitments.

### BIOMEDICAL WASTE

**ITEM_7**
- Metric: Biomedical Waste Generated
- Our XBRL value: **180 MT**
- Peer comparison: JSW=0.03 MT, SAIL=141 MT, Jindal=not reported — Tata and SAIL are dramatically higher than JSW
- Find in PDF: Principle 6, waste type breakdown — look for "Biomedical waste" or "Bio-medical waste" or "Hazardous waste — biomedical"
- Question: Is 180 MT correct? Given consolidated scope (hospitals, townships across multiple countries), this may be plausible — confirm.

### YEAR-OVER-YEAR (values from FY2023 that changed dramatically by FY2024 or FY2025)

There are no self-outliers that require FY2023 PDF verification for Tata Steel (the FY2023→FY2024 changes are expected due to Consolidated→Standalone basis shift and are already documented).

---

## Training coverage — MANDATORY

**TRAINING**
- Metric: % of employees trained / training coverage (not in XBRL for any company)
- Look in: Principle 3 — "Training and Awareness Programs", HR metrics table, workforce development section
- Extract: 
  - % of employees trained (or total employees trained / total employees)
  - % of workers trained (or total workers trained / total workers)  
  - Average training hours per employee (if reported)
  - Total person-hours of training (if reported)

---

## Output

Respond with 8 lines total (ITEM_1 through ITEM_7, then TRAINING), using the format from COMMON_INSTRUCTIONS.md:

```
ITEM_1 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_2 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_3 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_4 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_5 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_6 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
ITEM_7 | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE
TRAINING | VERDICT | VALUE | PAGE_OR_SECTION | NOTE
```
