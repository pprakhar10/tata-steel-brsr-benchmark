# BRSR Benchmark Dashboard — Project Context

## What this project is

A BRSR (Business Responsibility and Sustainability Report) comparison dashboard for 4 Indian steel companies across FY2023–FY2025. Built from scratch after a previous attempt failed due to building UI on unvalidated data.

This is a global instruction that all work must be broken down into parts so that each task does not take more than 5 minutes. As I've seen that Claude and other LLMs ends up making mistakes when tasks are more than 5 minutes.

**Companies:** Tata Steel, JSW Steel, SAIL, Jindal Stainless
**Years:** FY2023, FY2024, FY2025 (3 XBRL files per company = 12 files total)

## Full plan

Saved at: `C:\Users\pprak\.claude\plans\flickering-wibbling-pizza.md`
Read this before doing any work in this project.

---

## AI Analysis Review Protocol

### Data correction impact check
When the user provides corrected values for any indicator (standalone replacement, missing FY filled, XBRL error fixed), before updating the analysis text, check ALL of:
1. `trendDirection` — does the new value change the FY-on-FY direction for any company?
2. `peerRank` — does the new value change the ranking for that company-year?
3. `performanceAndDrivers` — does the numeric mention need updating?
4. `tataPositioning` — does rank or trend framing change?
5. `comparabilityNotes` — does the note about consolidated boundary or data availability change?
6. `flags.trendAmbiguity` — can this flag now be cleared?

### AI analysis presentation rules (enforced in Phase B cleanup)
- **No "targets not found"** — if no targets are known for a KPI, omit or set to null; never mention absence
- **No source citations in `about`** — state facts directly; do not name SEBI/ICAI/BRSR standards as sources
- **No `(P)` references in analysis text** — patched values are finalized; users must not see this label
- **No internal rule references** — never mention ranking rules, "treated as worst", "ranked last as instructed", "standardised table shows X as missing", "standardised dataset as instructed"
- **No `(C)` or `(India)` markers in DataTable cells** — consolidated context goes only in `comparabilityNotes` text

### Review batch schedule (remaining 92 indicators)
- **Batch E-1**: Energy (11) + Air Emissions (3) = 14 indicators
- **Batch E-2**: Water (15) + Waste (19) = 34 indicators
- **Batch S**: Social (26 indicators)
- **Batch G**: Governance (18 indicators)

---

## Critical facts — read before touching any data

- **PDF is the source of truth. XBRL is secondary.** Indian companies rarely make errors in their published BRSR PDFs. XBRL is a new regulatory requirement and filing errors are common — wrong units, absolute values instead of scaled, field mismatches. When Gemini or PDF cross-check produces a different value from XBRL, default to trusting the PDF. Do not defend XBRL values when PDF clearly contradicts them.

- **Amount* tags are calculation inputs, not standalone metrics.** Tags like `AmountOfAccountsPayableDuringTheYear`, `AmountOfTotalSales`, `AmountOfTotalPurchases`, etc. are only used as denominators/numerators to derive ratio metrics (e.g. days payable, % of RPT). The derived percentage/days value is the actual metric. These 19 tags are in **Group E of `EXCLUDED_TAGS`** in `config.py` — they never reach the dashboard or AI analysis. Do not patch or null them. Exception: `TotalRevenueOfTheCompany` / `RevenueFromOperations` / `Turnover` are kept as standalone company size metrics.

- XBRL files span **4 different SEBI namespace versions** (`2021-09-30`, `2023-06-30`, `2024-04-30`, `2025-05-31`). Tag count nearly doubles from FY23 (445) to FY24 (871). The parser must detect the namespace from the root element.
- **Tata Steel FY2023 = Consolidated basis. All other company-years = Standalone.** Confirmed via the `ReportingBoundary` XBRL tag. The FY23→FY24 drop in Tata Steel's absolute figures is a reporting basis change, NOT an outlier or data error.
- Companies report the same metrics in different units (e.g. Scope 1: Tata = Million tCO2e, JSW = Metric Tonnes, SAIL = Tonnes of CO2, Jindal = TCO2E). Unit normalization is mandatory.
- **Standard units:** GHG → tCO2e | Water → kL | Waste → metric tonnes | Energy → GJ | Air emissions → kilotonnes. SEBI guidance takes precedence; Tata Steel's units used where SEBI is silent.
- **When unit normalization is ambiguous — stop and ask the user. Never guess.**

## PDF phase discoveries (confirmed, do not re-derive)

- **Water intensity units are NOT uniform:** Tata/JSW/SAIL = L/₹ (litres per rupee). Jindal = kL/Rs.Crore. Not directly comparable — AI analysis and dashboard must flag this.
- **SAIL air emissions changed methodology FY2024:** FY2023 = mg/Nm³ concentration (non-normalizable, excluded from cross-company comparison). FY2024/FY2025 = kg/tcs mass intensity (normalizable, comparable with peers). This is confirmed and patched.
- **XBRL filing errors patched:** Tata FY2023 GHG intensity (61→null), SAIL FY2024 GHG intensity (0→2.8 tCO2e/tcs), Jindal FY2025 water intensity (0.0000359→358.67 kL/Rs.Crore), SAIL FY2024 water intensity (52.33→null, filing error, correct value unknown).
- **All patches live in `parser/apply_patches.py`.** Re-run this after any re-parse. Do not manually edit company JSONs.
- **Tata/JSW SOx/NOx** not in FY2024/FY2025 XBRL — added from PDF in apply_patches.py.
- SAIL FY2024 air emission values (user-verified via PDF screenshot): SOx=1.10, NOx=0.76, PM=0.58 kg/tcs. FY2025: SOx=0.95, NOx=0.80, PM=0.56 kg/tcs.
- **Tata FY2023 GHG intensity patched to 2.21 tCO2e/tcs** (user confirmed from ESG factsheet in FY2022-23 Integrated Report; XBRL had filing error of 61).
- **Workforce/safety data extracted from dimensional XBRL contexts** (parser only extracts DCYMain; these tags use D_Employees etc.). All 4 companies × 3 years now have: TotalNumberOfEmployees, PercentageOfFemaleEmployees, NumberOfFatalities, LostTimeInjuryFrequencyRate.
- **Implausible LTIFR=0 flags:** JSW FY2023 (LTIFR=0 + 6 fatalities), SAIL FY2023/FY2024 (LTIFR=0 + 11 fatalities), Jindal FY2023 (LTIFR=0 + 3 fatalities) — all flagged with unitWarning. SAIL FY2023/FY2024 also have identical employee counts suggesting prior-year context reuse.
- **Training coverage %** not found in XBRL for any company-year under any tag name — needs PDF extraction.
- **Jindal water intensity L/Rs equivalent** added as `lrsEquivalent` field: 335→0.0000335, 333→0.0000333, 358.67→0.0000359 L/Rs. Lower than peers — consistent with EAF stainless process being less water-intensive than BF-BOF.
- **Phase 3b was enrichment + ad-hoc spot-checks only — NOT systematic outlier verification.** Phase 3c (systematic Gemini outlier check) is required before data can be considered clean for AI analysis.

---

## Exclusion list (48 tags — confirmed by user, do not re-derive)

Full list in memory: `C:\Users\pprak\.claude\projects\c--Prakhar-claude-code-Offline-expense-tracker\memory\brsr_xbrl_exclusion_list.md`

- **Group A:** Company identity (address, CIN, email, phone, website, year of incorporation)
- **Group B:** Period metadata (date tags — redundant with XBRL context IDs)
- **Group C:** Web link tags only (boolean policy-existence tags ARE retained)
- **Group D:** XBRL domain/scaffolding labels (structural, no data value)

Everything else (~397 tags) is retained. **No indicator is excluded from AI analysis without explicit user approval.**

---

## File structure

```
XBRL/                        # Input XML — never touched by UI
  TATA STEEL/                # 3 files: FY23, FY24, FY25
  JSW STEEL/
  SAIL/
  JINDAL STAINLESS/
BRSR guidance/               # SEBI BRSR Template.pdf, SEBI BRSR Guidance.pdf, ICAI BRSR guidance.pdf
BRSR PDF all company/        # Company BRSR annual report PDFs (PDF enrichment phase)
parser/                      # Python scripts
  config.py                  # Exclusions, unit maps, tag aliases, company registry
  parse_xbrl.py              # XML → per-company JSON
  normalize.py               # Unit normalization
  validate.py                # Outlier detection + consistency checks (0 blocking, 712 warnings)
  run_all.py                 # Entry point: parse all companies
  apply_patches.py           # ✅ PDF-verified corrections to company JSONs — re-run after any re-parse
  generate_data_review.py          # ✅ Generates parser/review/data_review.md + .html (18 key metrics)
  generate_comparison_table.py     # ✅ Generates parser/review/comparison_table.html (112 metrics, all 4 companies side-by-side)
  generate_comparison_excel.py     # ✅ Generates parser/review/comparison_table.xlsx (same, Excel format for SharePoint sharing)
  generate_analysis_prompts.py      # ✅ Generates 13 Custom GPT prompt files
  gem_analysis_prompts/             # ✅ 13 prompt .md files (one per BRSR theme)
  ai_analysis_outputs/              # Custom GPT session outputs (13/13 done)
  process_ai_analysis.py            # 🔄 Parses GPT outputs → analysis JSON (ready to run)
  generate_analysis_review_excel.py # ⬜ Generates analysis_review.xlsx
  apply_analysis_review.py          # ⬜ Applies Excel review corrections
  approve_analysis.py               # ⬜ Sets analysis status to approved
  gemini_pdf_prompt_*.md           # Phase 3b Gemini enrichment prompts (reference only)
  gemini_pdf_out_*.md              # Phase 3b Gemini enrichment outputs (reference only)
  gemini_outlier_check_*.md        # Phase 3c — systematic outlier verification prompts
  gemini_outlier_out_*.md          # Phase 3c — Gemini outlier verdicts
  review/
    data_review.md                 # ✅ Key metrics review (18 indicators)
    data_review.html               # ✅ Browser-viewable version
    comparison_table.html          # ✅ Full 112-metric cross-company review table (browser, contenteditable notes)
    comparison_table.xlsx          # ✅ Same as above in Excel — shared via SharePoint for team review + Comments column
dashboard/                   # React app (to be built)
  src/data/                  # Generated JSON only — never raw XML/PDF
    companies.json
    indicators.json
    companies/               # Per-company normalized XBRL data
    pdf_enrichment/          # PDF-extracted narratives per company-year
    analysis/                # Pre-computed AI analysis + _review_status.json
```

---

## Current status

| Step | Status |
|------|--------|
| Parser + normalization | ✅ Done |
| indicators.json | ✅ Done |
| validate.py (0 blocking, 712 warnings) | ✅ Done |
| PDF enrichment extraction (Phase 3b) | ✅ Done — enrichment only, not systematic outlier check |
| apply_patches.py (all known patches) | ✅ Done |
| generate_data_review.py → data_review.html | ✅ Done |
| **Phase 3c — Gemini PDF cross-check (Tata Steel FY2023/24/25)** | ✅ Done — patches applied |
| **Phase 3c — Gemini PDF cross-check (SAIL FY2023/24/25)** | ✅ Done — patches applied |
| **Phase 3c — Gemini PDF cross-check (JSW Steel FY2023/24/25)** | ✅ Done — patches applied |
| **Phase 3c — Gemini PDF cross-check (Jindal Stainless FY2023/24/25)** | ✅ Done — patches applied |
| Re-run validate.py + generate_data_review.py after all Phase 3c patches | ✅ Done |
| Cross-company comparison table (HTML + Excel, 99 metrics) | ✅ Done — `comparison_table.html` + `comparison_table.xlsx` |
| FY2022-23 manual Excel review → `patch_fy23_review()` | ✅ Done — fully applied 2026-04-27 |
| FY2023-24 manual Excel review → `patch_fy24_review()` | ✅ Done — fully applied 2026-04-27 |
| FY2024-25 manual Excel review → `patch_fy25_review()` | ✅ Done — applied 2026-04-27 |
| Regenerate comparison_table.html + .xlsx after all review patches | ✅ Done — 98 metric rows × 3 years |
| generate_analysis_prompts.py (13 prompt files) | ✅ Done — 2026-04-28 |
| Custom GPT sessions (13 topics) | ✅ Done — 13/13 complete |
| process_ai_analysis.py (parse GPT outputs → JSON) | ✅ Done — 98 indicators + 39 benchmarks written |
| Custom GPT sessions 14-15 (company + trend narratives) | ✅ Done — via generate_narrative_prompts.py |
| generate_narrative_prompts.py + process_narrative_outputs.py | ✅ Done — 12 company + 4 trend JSONs written |
| generate_analysis_review_excel.py | ✅ Done — analysis_review.xlsx generated (12-col compact layout) |
| apply_analysis_review.py | ⬜ Pending — Phase 4-D (build after user finishes Excel review) |
| approve_analysis.py | ⬜ Pending — Phase 4-E |
| Dashboard UI — Phase 5-A: Scaffold | ✅ Done |
| Dashboard UI — Phase 5-B: Types + Constants | ✅ Done |
| Dashboard UI — Phase 5-C: Layout + Sidebar | ✅ Done |
| Dashboard UI — Phase 5-D: Shared primitives | ✅ Done |
| Dashboard UI — Phase 5-E: DataTable + InsightsPanel + ChartPanel + IndicatorCard | ✅ Done |
| Dashboard UI — Phase 5-F: Prototype Preview (5 cards) | ✅ Done — awaiting user design review |
| Dashboard UI — Phase 5-G: Full ESG View | ✅ Done |
| Dashboard UI — Phase 5-H: Search Panel | ✅ Done |
| Dashboard UI — Phase 5-I: Benchmark Panel | ✅ Done |
| Dashboard UI — About & Help page | ✅ Done (added beyond original plan) |
| Dashboard UI — Phase 5-J: Polish + Build | ⬜ Pending |
| AI Analysis Cleanup — Phase A: DataTable (C)/(P) suffix removal | ✅ Done |
| AI Analysis Cleanup — Phase B: Global JSON cleanup (41 files) | ✅ Done |
| Manual review — Batch E-1: Energy (11) + Air Emissions (3) | ⬜ Next |
| Manual review — Batch E-2: Water (15) + Waste (19) | ⬜ Pending |
| Manual review — Batch S: Social (26) | ⬜ Pending |
| Manual review — Batch G: Governance (18) | ⬜ Pending |

**Next action:** User provides corrections for Batch E-1 (Energy + Air Emissions indicators). Phase 5-J (npm run build) can run anytime. Phase 4-D/E after all batches reviewed.

**TAG_GROUPS changes applied 2026-04-27 (cumulative):**
- Removed: GHG/Energy/Water/Waste Intensity PPP, Scope 3 entity metric, Waste Intensity entity metric, Total Wages Paid, Gross Wages Paid to Female, Avg Training Hours (Employees + Workers)
- Renamed: `PercentageOfRAndD` label → "R&D & Capex in Env/Social Technologies (% of total R&D & Capex)"
- Renamed: `PercentageOfFemaleEmployees` label → "Female Employees (%)"
- Water intensity unit hint → "L/₹"
- Table is now 98 metric rows (was ~112)

**patch_fy25_review() corrections applied 2026-04-27:**
- Tata: Turnover (→132,517 Cr), energy (9 tags), GHG+Scope3 intensities, water intensity (→0.074 L/₹), water discharge to groundwater (→0), waste intensity physical (→0.8), workers rehab (→19), employees (→43,089), female % (→8.9%), female wage % (→6%), LTIFR/TRIFR/Fatalities split
- JSW: NetWorth (→72,050 Cr), water intensity (→0.0424 L/₹), NOx (→31.96 kt), PM (→10.84 kt), related party purchases/sales
- SAIL: Turnover (→101,716 Cr), NetWorth (→55,656 Cr), GHG+Scope3+Waste intensities to per-rupee, water intensity (→0.089 L/₹), related party ×4
- Jindal: NetWorth (→16,197 Cr), groundwater withdrawal (→0), water intensity (→0.03587 L/₹), related party ×3
- All: LTIFR_Employees (from D_Employees XBRL), LTIFR_Workers, TRIFR_Employees/Workers, Fatalities_Employees/Workers

**Tata Steel energy corrections applied 2026-04-27 (all 3 years):**
- FY2023: Total=733,550,000 GJ, intensity=24.5 GJ/tcs, 0.00032 GJ/₹
- FY2024: Total=569,330,000 GJ, intensity=28.3 GJ/tcs, 0.00040 GJ/₹
- FY2025: Total=587,560,000 GJ, intensity=28.3 GJ/tcs, 0.00044 GJ/₹

**Water intensity L/₹ standardization applied 2026-04-27:**
- All companies, all years now stored in L/₹ (SAIL/Jindal FY2023 were kL/₹, converted)

---

## Phase 3c — File locations

```
parser/PDF cross check/
  prompts/                                        ← 12 prompt files + common instructions
    gemini_outlier_check_COMMON_INSTRUCTIONS.md   ← paste first in every Gemini window
    gemini_outlier_check_{company}-{year}.md      ← 12 files, one per company-year
  prompts/Output/                                 ← save Gemini outputs here
    gemini_outlier_check_{company}-{year}.md      ← Gemini responses (12 files)
parser/generate_prompts.py                        ← regenerates all 12 prompt files
```

**Item counts per prompt (for reference):**
| Company | FY2023 | FY2024 | FY2025 |
|---------|--------|--------|--------|
| Tata Steel | 23 | 44 | 48 |
| JSW Steel | 18 | 52 | 42 |
| SAIL | 22 | 50 | 64 |
| Jindal Stainless | 16 | 52 | 47 |

---

## Phase 3c — Gemini reliability note (READ BEFORE PROCESSING ANY COMPANY)

**Gemini incorrectly flags TJ energy tags as UNIT_ERROR.** When Gemini says "XBRL value is 1000x higher than PDF" for an energy volume tag (electricity/total energy), it is comparing the numeric GJ value against the numeric TJ value without performing the unit conversion. Example: our stored 1.40245e+08 GJ = 140,245 TJ — these are the same quantity. Gemini sees 140,245,000 vs 140,245 and says "1000x error." **Do not apply these as corrections.** The TJ→GJ conversion in normalize.py (×1000) is correct. The only exception is when the PDF shows a genuinely different TJ number than what the XBRL stored (e.g. SAIL FY2024 electricity: XBRL had 143,445 TJ but PDF shows 613,900 TJ — that IS a real discrepancy and should be corrected).

**Rule:** For TJ energy UNIT_ERROR items, check if the Gemini-provided TJ value matches what the XBRL raw stored (our normalized ÷ 1000). If they match, ignore. If they differ, apply the PDF value × 1000 as the corrected GJ value.

---

## Phase 3c — Tata Steel patches applied (confirmed, do not re-derive)

**FY2023:** All 22 peer outliers confirmed by PDF. Training coverage added: 100% employees & workers (H&S + skill upgradation) — Principle 3 Essential Indicator 8.

**FY2024 corrections:**
- `RevenueFromOperations`, `TotalRevenueOfTheCompany`, `AmountOfTotalSales` — XBRL filed in absolute rupees, not INR Crore. Corrected: ÷ 1e7. PDF confirms 1,40,987 Crore.
- `EnergyIntensityPerRupeeOfTurnoverAdjustingForPurchasingPowerParity` — unit documented as GJ/Million USD. Our 8,860 GJ = 0.00886 PJ vs PDF 0.0098 PJ (~10% gap, exchange rate difference). Value retained with warning.
- `EnergyIntensityPerRupeeOfTurnover` — unit documented as GJ/Rs. Our 0.000387 GJ/Rs = 0.00387 PJ/Crore vs PDF 0.0043 PJ/Crore (~10% gap). Value retained with warning.
- `TotalScope3EmissionsPerRupeeOfTurnover` — 10× correction: 1e-5 → 0.0001 MnT/Crore (PDF Page 69).
- `WasteIntensityPerRupeeOfTurnoverAdjustingForPurchasingPowerParity` — 10× correction: 2.73e-5 → 0.000273 MT/USD (PDF Page 65).
- Training coverage added: 100%.

**FY2025 corrections:**
- `EnergyIntensityPerRupeeOfTurnoverAdjustingForPurchasingPowerParity` — unit documented as GJ/Million USD. Our 9,160 GJ = 0.00916 PJ vs PDF 0.0092 PJ (0.4% gap — confirmed).
- `NetWorth` — nulled. XBRL FY2025 tag contained FY2024 comparative value (1,38,041 Crore). Actual FY2025 not filed.
- `WaterDischargeToGroundwater` + `WaterDischargeToGroundwaterWithTreatment` — corrected 0 → 3,000 kL (PDF: 3 Million Litres, Principle 6 Q4).
- `NumberOfWorkersOrWhoseFamilyMembersRehabilitatedAndPlacedInSuitableEmployment` — corrected 19 → 24 (PDF standalone value, Principle 3 Leadership Q3).
- Training coverage added: 100%.

**Key discoveries applicable to other companies:**
- **Financial tags (Amount*, Revenue*, NetWorth, Wages) may be in absolute rupees in XBRL**, not INR Crore. Check each company's Gemini output for similar UNIT_ERROR verdicts on financial metrics. Fix only where Gemini confirms the correct Crore value.
- **Energy intensity unit**: XBRL has no unit tag. Our values are in GJ; PDF shows PJ. 1 GJ = 1e-6 PJ. Verify per company — the ~10% gap for Tata FY2024 is exchange rate/denominator, not a data error.
- **Training coverage (TrainingCoverage_* fields)**: Not in XBRL for any company. Add from each company's Gemini output as PDF-sourced fields.

---

## Phase 3c — SAIL patches applied (confirmed, do not re-derive)

**FY2023:** Training coverage added: Employees H&S 30.4%, Skill 32.6%; Workers H&S 100%, Skill NA; avg hrs 4.88 (emp) / 9.18 (workers); total 8,94,411 person-hours (Principle 3, Page 184). All TJ energy volume tags (ITEM_2, 6, 11, 14, 15) were CORRECTLY stored — Gemini incorrectly flagged them. No value corrections.

**FY2024 corrections:**
- `AmountOfTotalSales` — XBRL filed partial figure (1,725 Crore). PDF Section A Q24 confirms 1,04,545.09 Crore. Corrected.
- `TotalElectricityConsumptionFromNonRenewableSources` — genuine XBRL discrepancy: 143,445 TJ → 613,900 TJ (PDF Principle 6 Q1 Page 23). Converted to 613,900,000 GJ.
- `RevenueFromOperations` — 10× error: 1,096,725 → 109,672.5 Crore (PDF Principle 6 Q1).
- `TotalRevenueOfTheCompany` — 1,05,375 → 1,04,545.09 Crore (PDF Section A Q24).
- `WasteIntensityPerRupeeOfTurnover` — 10× low: 12.77 → 128 Tonnes/Crore (PDF Principle 6 Q9).
- `TotalScope1AndScope2EmissionsIntensityPerRupeeOfTurnover` — 10× low: 50.21 → 502 tCO2e/Crore (PDF Principle 6 Q7).
- `AmountOfAccountsPayableDuringTheYear` — nulled (filing error, PDF only shows days payable, not absolute amount).
- Training coverage added: Employees H&S 40.6%, Skill 34.7%; Workers H&S 100%, Skill NA (Principle 3, Q8, Page 13).

**FY2025 corrections:**
- 17 financial Amount* tags — all filed in absolute INR, not Crore. Corrected via ÷ 1e7. Verified against PDF values. See `apply_patches.py` for all 17 values.
- `RevenueFromOperations` — corrected to 1,01,716 Crore (PDF Section A Q24).
- `TotalScope1AndScope2EmissionsIntensityPerRupeeOfTurnover` — XBRL stored in kg/Rs (0.0578014). Converted to 578.014 tCO2e/Crore (÷ 1000 × 1e7). PDF Principle 6 Q7 confirms 578.
- `WasteIntensityPerRupeeOfTurnover` — XBRL stored in kg/Rs (0.0143497). Converted to 143.5 Tonne/Crore. PDF confirms ~0.000014 Tonne/Rs.
- `AmountOfAccountsPayableDuringTheYear` — nulled (same reason as FY2024).
- Training coverage added: Employees H&S 15%, Skill 34%; Workers H&S 100%, Skill NA (Principle 3, Q8).

**Key discoveries applicable to JSW and Jindal:**
- **SAIL FY2025 = Tata Steel FY2024 pattern:** All financial Amount* tags filed in absolute INR. Check for same in JSW FY2024/FY2025 and Jindal FY2024/FY2025. If Gemini gives UNIT_ERROR verdict on Amount* tags with the note "filed in absolute INR," apply ÷ 1e7.
- **kg/Rs intensity unit:** SAIL FY2025 stored `EmissionsIntensityPerRupeeOfTurnover` and `WasteIntensityPerRupeeOfTurnover` as kg/Rs. Check JSW/Jindal for same. Conversion: value_in_kg_Rs ÷ 1000 × 1e7 = Tonne/Crore.
- **10× intensity error (FY2024 SAIL):** `WasteIntensityPerRupeeOfTurnover` and `EmissionsIntensityPerRupeeOfTurnover` both needed 10× correction in FY2024. Pattern may reappear in other companies.
- **TJ energy tags:** Do NOT correct these based on Gemini UNIT_ERROR alone — check if XBRL raw TJ value matches PDF TJ value first.

---

## Phase 3c — JSW Steel patches applied (confirmed, do not re-derive)

**FY2023:**
- `Turnover`: 10x filing error → 130,039 Crore (raw was 130039000000; PDF Page 255 confirms ~130,000 Crore)
- Training coverage: 100% all 4 categories (Page 267)

**FY2024:**
- `Turnover` / `RevenueFromOperations` / `TotalRevenueOfTheCompany`: absolute INR → 133,609 Crore (÷ 1e7, PDF Page 4)
- `PercentageOfCostIncurredOnWellBeingMeasures`: 0.04% → 0.035% (PDF Page 14 rounding error)
- `GrievanceMechanism_NonPermanent` + `GrievanceMechanism_Workers`: False → True (PDF Page 15 filing error)
- `LocalSourcing%`: 65% confirmed but scope is "within India" not "within district" (note added)
- `WaterIntensityPerRupeeOfTurnover`: kL/₹ (3.89951e-05) → L/₹ (0.0389) (PDF Page 24)
- `TotalScope3EmissionsPerRupeeOfTurnover`: unit documented (kgCO2/₹ stored as tCO2/₹; value correct)
- Training coverage: 100% all 4 categories (Page 15)

**FY2025:**
- `Turnover` / `RevenueFromOperations` / `TotalRevenueOfTheCompany`: absolute INR → 125,678 Crore (same pattern as FY2024)
- `WellbeingCost%`: 0.03% → 0.0253% (PDF Page 9)
- `EPR WasteCollectionPlan`: False → True (PDF Page 8)
- `WaterIntensityPerRupeeOfTurnover`: kL/₹ → L/₹ = 0.0424 (pattern consistent with FY2024)
- Training coverage: 100% all 4 categories (Page 9)

---

## Phase 3c — Jindal Stainless patches applied (confirmed, do not re-derive)

**FY2023:**
- `WasteRecoveredThroughOtherRecoveryOperations`: 489.94 → 201 MT (PDF Page 29, sum of Other recovery ops)
- Training coverage: 100% all 4 categories, >150,000 person-hours (Pages 11, 18)

**FY2024:**
- `TotalRevenueOfTheCompany`: 1,000 → 38,356 Crore (filing error; PDF Section A Q24)
- 7 intensity tags: values PDF-confirmed correct; units documented as per-Crore (Jindal files per-Crore, not per-rupee): `EnergyIntensity` = GJ/Crore INR (916.25) and GJ/Crore USD (20524), GHG PPP = tCO2e/Crore USD (2207.22), Scope3 = tCO2e/Crore INR (87.22), WasteIntensity = MT/Crore INR (41.31) and MT/Crore USD (925.42), WaterIntensity PPP = kL/Crore USD (7459.39)
- Training coverage: Emp H&S 50.04%, Skill 32.21%; Workers H&S 19.27%, Skill 3.73%; 166,000 person-hours

**FY2025:**
- `RevenueFromOperations`: absolute INR → 40,181.68 Crore (÷ 1e7, PDF Page 4)
- `TotalRevenueOfTheCompany`: XBRL had Net Worth instead of Turnover → corrected to 40,181.68 Crore
- `NumberOfDealersOrDistributors`: 478 → 367 (XBRL had trading houses count; PDF Page 16)
- `WaterWithdrawalByGroundwater`: 0 → 19,102 kL (XBRL swapped FY2024/FY2025 values; PDF Page 34)
- 8 intensity tags: values confirmed (per-rupee stored × 1e7 = per-Crore PDF value); units documented
- Training coverage: 100% all 4 categories, 166,000 person-hours (Pages 12, 22)

**Key pattern for Jindal:** Intensity tags in FY2024 are filed per-Crore (numeric value = per-Crore). In FY2025 they are filed per-rupee (numeric value = per-rupee, multiply by 1e7 to get per-Crore). Both are correct when units are properly applied.

---

## Implementation order (do not skip or reorder)

1. ✅ `parser/config.py` → `parse_xbrl.py` → `normalize.py` → `run_all.py`
2. ✅ Gemini Pro generates `indicators.json` labels
3. ✅ `parser/validate.py` → 0 blocking flags
4. ✅ Gemini PDF enrichment → `pdf_enrichment/*.json`; patches in `parser/apply_patches.py`
5. ✅ `parser/generate_data_review.py` → `parser/review/data_review.html`
6. ✅ **Phase 3c — Systematic outlier PDF verification:** All 12 company-years done. Patches in `apply_patches.py`. `data_review.html` regenerated.
7. ✅ Re-run `validate.py` + `generate_data_review.py` after all Phase 3c patches applied
8. ✅ **User reviews data_review.html** ← GATE complete
9. ✅ Phase 4-A/B/C: Custom GPT 13 analysis sessions + 2 narrative sessions → all JSONs written → `analysis_review.xlsx` generated
10. 🔄 **User reviews `analysis_review.xlsx`** ← CURRENT GATE (column L = Changes Required)
11. ⬜ `parser/apply_analysis_review.py` → record corrections into indicator JSONs
12. ⬜ `parser/approve_analysis.py` → set status=approved ← GATE
13. ⬜ Dashboard scaffold + Screens

---

## Model routing (data quality first, tokens second)

| Task | Model |
|---|---|
| `config.py`, `parse_xbrl.py`, `normalize.py`, `validate.py` | **Claude Sonnet** — critical path, no outsourcing |
| Tag alias map (diff 4 namespace schemas) | **Gemini Pro** → Claude reviews output |
| `indicators.json` labels + BRSR mappings (~397 tags) | **Gemini Pro** (large tag list + BRSR PDFs) |
| PDF extraction → `pdf_enrichment/*.json` | **Gemini Pro** → Claude reviews numeric patches |
| Phase 3c outlier verification → `gemini_outlier_out_*.md` | **Gemini Pro** → Claude applies corrections |
| Per-indicator AI summaries (~397 × 3 years) | **Claude Haiku** |
| Executive narratives, benchmarks, trends, outlier commentary | **Claude Sonnet** |
| `generate_review_report.py` | **Claude Sonnet** |
| TypeScript types, React hooks, screen calculations | **Claude Sonnet** |
| JSX/Tailwind boilerplate, recharts config, Vite scaffold | **GitHub Copilot** |

---

## Dashboard design decisions

- **No company select/deselect toggle** — all 4 companies always shown
- **Two view modes:** Financial Year View (one year, 4 companies side-by-side) | Trends View (all 3 years, 4 companies)
- **Four sections:** Executive | Environment | Social | Governance
- **Outlier commentary toggle** ("Show technical notes") — localStorage, default on; turns off outlier panels for senior management presentations
- **Consolidated basis warning** — amber banner whenever Tata Steel FY2023 data is in view
- **App never accesses XML/PDF** — only reads final JSON from `src/data/`

---

## Validation rules (validate.py)

- **Peer outliers:** Tata/JSW/SAIL → flag if ratio > 5×; Jindal vs large-cap trio → flag if ratio > 20× (smaller company, different steel type). Intensity metrics: 5× rule applies regardless of company.
- **Too-good-to-be-true:** LTIFR = 0 for >5,000 employees → flag as implausible. 100% on large workforce metrics → flag for PDF verification.
- **YoY > 50% change** → flag. Tata FY23→FY24 auto-suppressed (expected basis change).
- **Cross-field consistency:** energy components must sum, waste components must sum, water withdrawal ≥ consumption.
- Blocking flags must reach zero before proceeding. Warning flags must each have an explanation.

## AI analysis rules

- **No indicator excluded from AI analysis** except the 48 pre-agreed tags. Never silently drop an indicator without user approval.
- Implausible values must be called out in analysis and confirmed as not a normalization failure.
- Per-indicator: every retained tag gets a 2–4 sentence Haiku summary per year.
- Executive (Sonnet): 200–300 words per company-year, senior management quality.
- Analysis not shown in UI until `_review_status.json` `status = "approved"`.
- User reviews `review_report.md` in VS Code (`Ctrl+Shift+V`) before approving.