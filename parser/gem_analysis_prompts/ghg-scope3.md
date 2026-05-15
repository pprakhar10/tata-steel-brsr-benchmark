# BRSR Analysis: GHG Emissions & Scope 3

*Generated: 2026-04-28 | Metrics: 6 | Companies: 4 | Years: FY2022-23, FY2023-24, FY2024-25*


## Session context


You are analysing **GHG Emissions & Scope 3** disclosures from BRSR filings for 4 Indian steel companies across FY2022-23, FY2023-24, and FY2024-25. Coverage: BRSR Principle 6 — Environment (Essential & Leadership indicators).

You have access to all 12 company BRSR PDFs and SEBI/ICAI BRSR guidance in your knowledge base. Use PDF content to enrich your analysis — cite specific targets, commitments, methodology changes, and initiatives from the PDFs wherever relevant. The quantitative data table below has been standardised for cross-company comparability.

**Metrics covered in this session (6):** TotalScope1Emissions, TotalScope2Emissions, TotalScope3Emissions, TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput, TotalScope1AndScope2EmissionsIntensityPerRupeeOfTurnover, TotalScope3EmissionsPerRupeeOfTurnover

## Rules for your analysis

1. **Audience:** Internal senior management at Tata Steel. Technical steel industry terminology is appropriate (blast furnace, EAF, BF-BOF, tcs, tonne of crude steel, etc.).

2. **Ranking:**
   - Rank 1 = best performer, Rank 4 = worst performer.
   - Tied ranks are allowed — if two companies perform equally, both receive the same rank and the next rank is skipped (e.g., two at rank 1 → next is rank 3).
   - A null/missing value (—) is treated as the worst possible performance and ranked last.

3. **Metric direction:** For each metric, determine whether a higher value or lower value indicates better performance. State this clearly in the ABOUT section. If genuinely ambiguous, output `DIRECTION_UNCLEAR: [reason]`.

4. **Sources:**
   - Use the BRSR PDF disclosures in your knowledge base as the primary source.
   - If a target or context is not available in the BRSR but you can source it reliably elsewhere, include it and note: `(Source: [source name] — not from BRSR disclosure)`.
   - If no meaningful analysis is possible for a metric, output `CONTEXT_INSUFFICIENT: [reason]` rather than producing thin or speculative analysis.

5. **Data flags in the table:**
   - `(P)` = value was standardised or corrected for comparability. Company annual reports may show a different unit or value.
   - `—` = not reported / data not available.
   - `⚠consolidated` = Tata Steel FY2022-23 is on a Consolidated basis (includes Indian and international operations). Standalone values are noted where available. All other company-years are Standalone (Indian operations only).

6. **Trend direction:** Use `Improved`, `Worsened`, or `Stable`. If the trend is genuinely ambiguous (e.g., due to a reporting methodology change between years), output `AMBIGUOUS: [reason]`.

7. **Tata Steel positioning:** Write a combined narrative story anchored on FY2024-25 as the primary reference. Cover Tata's rank and gap from the best performer in the latest year (or, if Tata leads, who is closest and why). Then cover trajectory: has Tata's ranking changed across the 3 years — improved, declined, or held steady — and what drove that change?

8. **Targets:** Cite targets stated in BRSR first. External sources allowed with attribution. If nothing found: `"No targets identified for this metric."`

9. **Comparability notes:** Only include if the reader needs this to correctly interpret the numbers (unit conversions, scope boundary differences, methodology changes). Omit if not applicable.

10. **Technical depth:** Explanations may include steel process chemistry, production route differences, regulatory context, and industry benchmarks — users are technical professionals from the steel industry.

## Standardised data


> **(P)** = value standardised or corrected for comparability — company annual reports may show a different unit or number. **⚠consolidated** = Tata Steel FY2022-23 on Consolidated basis (includes international operations). **—** = not reported.


| Metric | Unit | Tata Steel FY23 | Tata Steel FY24 | Tata Steel FY25 | JSW Steel FY23 | JSW Steel FY24 | JSW Steel FY25 | SAIL FY23 | SAIL FY24 | SAIL FY25 | Jindal Stainless FY23 | Jindal Stainless FY24 | Jindal Stainless FY25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Scope 1 GHG Emissions | tCO2e | 75,750,000 ⚠consolidated | 56,000,000 | 61,000,000 | 46,941,683 | 52,106,566 | 53,100,752 | 47,603,938 | 52,622,079 | 52,178,648 | 2,584,460 | 2,992,334 | 2,995,798 |
| Scope 2 GHG Emissions | tCO2e | 5,200,000 ⚠consolidated | 7,000,000 | 5,000,000 | 2,417,702 | 1,061,079 | 1,653,057 | 3,020,822 | 2,446,630 | 4,796,073 | 735,913.0 | 787,140.2 | 622,511.0 |
| Scope 3 GHG Emissions | tCO2e | 13,100,000 ⚠consolidated | 15,000,000 | 23,000,000 | 1,280,553 | 6,967,897 | 8,693,479 | 5,620,400 | 5,300,064 | 4,839,242 | — | 3,345,443 | 3,216,693 |
| GHG Intensity (physical output) | tCO2e/tcs | 2.21 ⚠consolidated | 3.1 | 3.2 | 2.36 | 2.44 | 2.436 | 2.8 | 2.8 (P) | 3.01 | 2.1 | 2.15 | 1.85 |
| GHG Intensity (per ₹ turnover) | tCO2e/₹ | 3.3e-05 ⚠consolidated | 4e-05 | 5e-05 (P) | 3.78e-05 (P) | 3.97935e-05 | 4.35667e-05 | 4.879e-05 (P) | 5.02e-05 | 5.78014e-05 (P) | 9.5e-06 (P) | 9.85367e-06 | 9.0048e-06 (P) |
| Scope 3 Intensity (per ₹ turnover) | tCO2e/₹ | 5.4e-06 ⚠consolidated | 1e-05 | 2e-05 (P) | 9.8e-07 (P) | 5.21e-06 (P) | 6.91e-06 | 5.42e-06 (P) | 4.83e-06 | 4.9e-06 (P) | — | 8.722e-06 | 8.0051e-06 (P) |

## Required output format

Follow this structure EXACTLY for every metric. Do not add or remove sections. Use the exact header names shown.

```
#### INDICATOR: {exact_tag_name_from_table}

**DIRECTION:** lower_is_better | higher_is_better | DIRECTION_UNCLEAR: [reason]

**PEER_RANK:**
FY2023: Tata={1-4}, JSW={1-4}, SAIL={1-4}, Jindal={1-4}
FY2024: Tata={1-4}, JSW={1-4}, SAIL={1-4}, Jindal={1-4}
FY2025: Tata={1-4}, JSW={1-4}, SAIL={1-4}, Jindal={1-4}

**TREND_DIRECTION:**
Tata:   FY2023-24=Improved|Worsened|Stable|AMBIGUOUS: [reason], FY2024-25=Improved|Worsened|Stable|AMBIGUOUS: [reason]
JSW:    FY2023-24=..., FY2024-25=...
SAIL:   FY2023-24=..., FY2024-25=...
Jindal: FY2023-24=..., FY2024-25=...

**ABOUT:**
[2-3 sentences: what the metric measures, which BRSR principle and Essential/Leadership classification it falls under. Final sentence: "A lower/higher value indicates better performance" or "Direction is unclear: [reason]".]

**PERFORMANCE_AND_DRIVERS:**
[Integrated narrative covering all 4 companies across all 3 years with the WHY woven in. Cite specific numbers. Cover structural drivers — process type (BF-BOF vs EAF), captive power, technology investments, scale, reporting methodology. If any value was sourced outside BRSR, note: "(Source: [source name])".]

**TATA_POSITIONING:**
[Combined narrative story anchored on FY2024-25. State Tata's rank and the percentage gap from the best performer in the latest year (or, if Tata leads, who is closest and what % behind). Then cover trajectory across all 3 years: has Tata's ranking changed and why?]

**TARGETS:**
[Targets from BRSR first. External sources with attribution if BRSR has nothing. If none found: "No targets identified for this metric."]

**COMPARABILITY_NOTES:**
[Only include if reader needs this to interpret the numbers correctly. Omit section entirely if not applicable.]

**FLAGS:**
DIRECTION_UNCLEAR: yes|no
CONTEXT_INSUFFICIENT: yes|no
EXTERNAL_SOURCE_USED: yes|no
TREND_AMBIGUITY: yes|no
FLAG_NOTE: [explanation if any flag is yes — omit this line if all flags are no]
```

After all INDICATOR blocks, write one BENCHMARK block:

```
#### BENCHMARK: {topic_key}

**FY2022-23:**
[150-200 words. Overall leader and laggard for this theme in FY2022-23 with reasoning. Structural factors explaining genuine differences. Note Tata consolidated basis.]

**FY2023-24:**
[150-200 words. Same structure.]

**FY2024-25:**
[150-200 words. Most detailed — this is the primary year.]
```


---

Now produce the analysis for all 6 metrics listed above, followed by the BENCHMARK block for topic key `ghg-scope3`.