"""
generate_narrative_prompts.py — Generate Custom GPT prompt files for company narratives
and multi-year trend summaries.

Produces 2 prompt files in parser/narrative_prompts/:
  company_narratives.md  — 12 company-year narratives (4 companies × 3 years)
  trend_summaries.md     — 4 multi-year trend summaries (4 companies)

Run: python parser/generate_narrative_prompts.py
"""

import json
from pathlib import Path
from datetime import date

BASE          = Path(__file__).parent.parent
ANALYSIS_DIR  = BASE / "dashboard" / "src" / "data" / "analysis"
ENRICHMENT_DIR = BASE / "dashboard" / "src" / "data" / "pdf_enrichment"
OUT_DIR       = BASE / "parser" / "narrative_prompts"

COMPANIES = [
    ("tata-steel",       "Tata Steel"),
    ("jsw-steel",        "JSW Steel"),
    ("sail",             "SAIL"),
    ("jindal-stainless", "Jindal Stainless"),
]
COMPANY_KEYS = {"tata-steel": "tata", "jsw-steel": "jsw",
                "sail": "sail", "jindal-stainless": "jindal"}

YEARS = ["FY2023", "FY2024", "FY2025"]
YEAR_LABELS = {"FY2023": "FY2022-23", "FY2024": "FY2023-24", "FY2025": "FY2024-25"}

TOPIC_ORDER = [
    "ghg-scope3", "energy", "water", "waste", "air-emissions",
    "health-safety", "workforce-diversity", "training-development",
    "ethics-compliance", "governance-related-party",
    "financial-profile", "stakeholder-human-rights", "csr-products-consumer",
]
TOPIC_NAMES = {
    "ghg-scope3":              "GHG Emissions & Scope 3",
    "energy":                  "Energy Consumption",
    "water":                   "Water Management",
    "waste":                   "Waste Management",
    "air-emissions":           "Air Emissions",
    "health-safety":           "Health & Safety",
    "workforce-diversity":     "Workforce & Diversity",
    "training-development":    "Training & Development",
    "ethics-compliance":       "Ethics & Compliance",
    "governance-related-party": "Governance & Related Party Transactions",
    "financial-profile":       "Financial Profile",
    "stakeholder-human-rights": "Stakeholder Engagement & Human Rights",
    "csr-products-consumer":   "CSR, Products & Consumer Responsibility",
}


# ---------------------------------------------------------------------------
# Data loaders
# ---------------------------------------------------------------------------

def load_benchmark(topic: str, year: str) -> str:
    path = ANALYSIS_DIR / "benchmarks" / f"{topic}-{year}.json"
    if not path.exists():
        return ""
    return json.loads(path.read_text(encoding="utf-8")).get("narrative", "")


def load_all_indicator_ranks() -> dict:
    """
    Returns {year: {company_key: {tag: rank}}} for all indicators.
    Also returns trend data: {company_key: {tag: {FY2023-24: ..., FY2024-25: ...}}}
    """
    ind_dir = ANALYSIS_DIR / "indicators"
    ranks = {yr: {ck: {} for _, ck in COMPANY_KEYS.items()} for yr in YEARS}
    trends = {ck: {} for ck in COMPANY_KEYS.values()}

    for path in ind_dir.glob("*.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        tag = data["tag"]
        peer_rank = data.get("peerRank", {})
        trend_dir = data.get("trendDirection", {})

        for yr in YEARS:
            yr_ranks = peer_rank.get(yr, {})
            for cid, ck in COMPANY_KEYS.items():
                r = yr_ranks.get(ck)
                if r is not None:
                    ranks[yr][ck][tag] = r

        for cid, ck in COMPANY_KEYS.items():
            td = trend_dir.get(ck, {})
            if td:
                trends[ck][tag] = td

    return ranks, trends


def load_enrichment_targets(company_id: str) -> list:
    """Return up to 5 target strings from the FY2025 PDF enrichment."""
    path = ENRICHMENT_DIR / f"{company_id}-FY2025.json"
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    targets = (data.get("enrichment") or {}).get("targets", [])
    return [t.get("description", "") for t in targets[:5] if t.get("description")]


# ---------------------------------------------------------------------------
# Rank summary helpers
# ---------------------------------------------------------------------------

def rank_summary_table(ranks_for_year: dict, company_id: str, year: str) -> str:
    """
    Compact rank distribution for one company-year.
    E.g. "Rank 1: 12 indicators | Rank 2: 18 | Rank 3: 25 | Rank 4: 38 | Not reported: 5"
    """
    ck = COMPANY_KEYS[company_id]
    cr = ranks_for_year.get(ck, {})
    dist = {1: 0, 2: 0, 3: 0, 4: 0}
    for r in cr.values():
        if r in dist:
            dist[r] += 1
    total = sum(dist.values())
    not_reported = 98 - total
    parts = [f"Rank {r}: {dist[r]}" for r in [1, 2, 3, 4]]
    if not_reported:
        parts.append(f"Not reported: {not_reported}")
    return " | ".join(parts)


def top_bottom_tags(ranks_for_year: dict, company_id: str, n: int = 5) -> tuple:
    """Return (top_n tags at rank 1, bottom_n tags at rank 4)."""
    ck = COMPANY_KEYS[company_id]
    cr = ranks_for_year.get(ck, {})
    rank1 = [tag for tag, r in cr.items() if r == 1][:n]
    rank4 = [tag for tag, r in cr.items() if r == 4][:n]
    return rank1, rank4


def trend_change_summary(trends: dict, company_id: str) -> str:
    """Summarise how many indicators improved/worsened/stable across each period."""
    ck = COMPANY_KEYS[company_id]
    ct = trends.get(ck, {})
    for period in ("FY2023-24", "FY2024-25"):
        counts = {"Improved": 0, "Worsened": 0, "Stable": 0, "AMBIGUOUS": 0}
        for tag, td in ct.items():
            v = td.get(period, "")
            if v.startswith("AMBIGUOUS"):
                counts["AMBIGUOUS"] += 1
            elif v in counts:
                counts[v] += 1
    lines = []
    for period in ("FY2023-24", "FY2024-25"):
        imp = sum(1 for td in ct.values() if td.get(period, "").startswith("Improved"))
        wor = sum(1 for td in ct.values() if td.get(period, "").startswith("Worsened"))
        sta = sum(1 for td in ct.values() if td.get(period, "").startswith("Stable"))
        amb = sum(1 for td in ct.values() if td.get(period, "").startswith("AMBIGUOUS"))
        lines.append(f"  {period}: Improved={imp}, Worsened={wor}, Stable={sta}, Ambiguous={amb}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Build company narratives prompt (session 14)
# ---------------------------------------------------------------------------

def build_company_narratives_prompt(ranks, trends) -> str:
    parts = []

    parts.append(f"# BRSR ESG Company Narratives — All 4 Companies × 3 Years")
    parts.append(f"*Generated: {date.today()} | Session 14 of 15*\n")

    parts.append("""## Your task

Write 12 executive ESG narratives — one for each company-year combination (4 companies × 3 years).

**Audience:** Senior management at Tata Steel, using these narratives to benchmark peers.
**Length:** 200-300 words per narrative. Plain prose — no bullet points or headers.
**Focus:** What does the data say about that company's overall ESG position in that year?
Cover: key environmental strengths/weaknesses, social performance, governance highlights,
notable rankings versus peers, and the structural or strategic factors driving performance.
Use your BRSR PDF knowledge to enrich the analysis — cite specific initiatives, targets, or
disclosures from the PDFs where they strengthen the narrative.

**Important:** Tata Steel FY2022-23 was filed on a Consolidated basis (includes international
operations). All other company-years are Standalone (Indian operations only).

## Required output format

Use this exact header for each narrative:

```
## COMPANY_NARRATIVE: {company_id} / {year}
{narrative text}
```

Company IDs: `tata-steel`, `jsw-steel`, `sail`, `jindal-stainless`
Years: `FY2023` (covers FY2022-23), `FY2024` (covers FY2023-24), `FY2025` (covers FY2024-25)

Write all 12 narratives in this order:
FY2023: tata-steel → jsw-steel → sail → jindal-stainless
FY2024: tata-steel → jsw-steel → sail → jindal-stainless
FY2025: tata-steel → jsw-steel → sail → jindal-stainless
""")

    # For each year: rank summaries + benchmark texts
    for yr in YEARS:
        yr_label = YEAR_LABELS[yr]
        parts.append(f"---\n\n## {yr_label} data (for writing {yr} narratives)\n")

        # Rank distribution table
        parts.append("### Rank distribution across 98 indicators\n")
        rank_lines = []
        for cid, cname in COMPANIES:
            summary = rank_summary_table(ranks[yr], cid, yr)
            rank_lines.append(f"- **{cname}:** {summary}")
        parts.append("\n".join(rank_lines) + "\n")

        # Top/bottom per company
        parts.append("### Top and bottom indicators per company\n")
        for cid, cname in COMPANIES:
            r1, r4 = top_bottom_tags(ranks[yr], cid)
            r1_str = ", ".join(r1) if r1 else "none"
            r4_str = ", ".join(r4) if r4 else "none"
            parts.append(f"**{cname}**")
            parts.append(f"  Best (rank 1): {r1_str}")
            parts.append(f"  Worst (rank 4): {r4_str}\n")

        # Benchmark texts for this year
        parts.append(f"### Benchmark analyses ({yr_label})\n")
        for topic in TOPIC_ORDER:
            text = load_benchmark(topic, yr)
            if text:
                topic_name = TOPIC_NAMES.get(topic, topic)
                parts.append(f"**{topic_name}**\n{text}\n")

    parts.append("---\n\nNow write all 12 COMPANY_NARRATIVE blocks in the order specified above.")

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Build trend summaries prompt (session 15)
# ---------------------------------------------------------------------------

def build_trend_summaries_prompt(ranks, trends) -> str:
    parts = []

    parts.append(f"# BRSR ESG Multi-Year Trend Summaries — All 4 Companies")
    parts.append(f"*Generated: {date.today()} | Session 15 of 15*\n")

    parts.append("""## Your task

Write 4 multi-year trend narratives — one per company covering FY2022-23, FY2023-24, FY2024-25.

**Audience:** Senior management at Tata Steel.
**Length:** 200-300 words per summary. Plain prose — no bullet points.
**Focus:** Trajectory across all 3 years. Which ESG themes improved, worsened or stayed flat?
What structural or strategic factors drove those trends?
Anchor on FY2024-25 as the current state, but explain how the company got there.
Use your BRSR PDF knowledge to reference strategy shifts, technology investments, or disclosures
that explain the trend.

**Important:** Tata Steel FY2022-23 was Consolidated; FY2023-24 and FY2024-25 are Standalone.
This affects year-on-year comparisons for Tata — note it where relevant.

## Required output format

```
## TREND_SUMMARY: {company_id}
{trend narrative}
```

Company IDs: `tata-steel`, `jsw-steel`, `sail`, `jindal-stainless`
Write in this order: tata-steel → jsw-steel → sail → jindal-stainless
""")

    # Trend movement summary per company
    parts.append("---\n\n## Indicator trend movements (across 98 indicators)\n")
    for cid, cname in COMPANIES:
        parts.append(f"**{cname}**")
        parts.append(trend_change_summary(trends, cid))

        # Rank trajectory
        parts.append("  Rank distribution by year:")
        for yr in YEARS:
            summary = rank_summary_table(ranks[yr], cid, yr)
            parts.append(f"    {YEAR_LABELS[yr]}: {summary}")
        parts.append("")

    # Targets from PDF enrichment
    parts.append("## Key stated targets from BRSR (FY2024-25 filings)\n")
    for cid, cname in COMPANIES:
        targets = load_enrichment_targets(cid)
        if targets:
            parts.append(f"**{cname}:**")
            for t in targets:
                parts.append(f"  - {t}")
            parts.append("")

    # All benchmark texts across all 3 years per topic
    parts.append("---\n\n## Benchmark analyses across all 3 years\n")
    for topic in TOPIC_ORDER:
        topic_name = TOPIC_NAMES.get(topic, topic)
        parts.append(f"### {topic_name}\n")
        for yr in YEARS:
            text = load_benchmark(topic, yr)
            if text:
                parts.append(f"**{YEAR_LABELS[yr]}**\n{text}\n")

    parts.append("---\n\nNow write all 4 TREND_SUMMARY blocks in the order specified above.")

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Loading indicator ranks and trends...")
    ranks, trends = load_all_indicator_ranks()

    print("Building company narratives prompt (session 14)...")
    prompt_14 = build_company_narratives_prompt(ranks, trends)
    path_14 = OUT_DIR / "company_narratives.md"
    path_14.write_text(prompt_14, encoding="utf-8")
    print(f"  OK company_narratives.md  ({len(prompt_14):,} chars)")

    print("Building trend summaries prompt (session 15)...")
    prompt_15 = build_trend_summaries_prompt(ranks, trends)
    path_15 = OUT_DIR / "trend_summaries.md"
    path_15.write_text(prompt_15, encoding="utf-8")
    print(f"  OK trend_summaries.md  ({len(prompt_15):,} chars)")

    print(f"\nDone. Prompt files in: {OUT_DIR}")
    print("\nWorkflow:")
    print("  1. Open company_narratives.md -> paste into Custom GPT")
    print("     -> save output to parser/narrative_outputs/company_narratives.md")
    print("  2. Open trend_summaries.md -> paste into Custom GPT")
    print("     -> save output to parser/narrative_outputs/trend_summaries.md")
    print("  3. Run: python parser/process_narrative_outputs.py")


if __name__ == "__main__":
    main()
