"""
process_ai_analysis.py — Parse Custom GPT outputs and write analysis JSON

Reads 13 topic files from parser/ai_analysis_outputs/,
parses indicator blocks and benchmark sections,
writes analysis JSON to dashboard/src/data/analysis/,
then calls Claude Sonnet for company narratives (12 calls) and trend summaries (4 calls).

Run: python parser/process_ai_analysis.py
"""

import json
import os
import re
import sys
import time
from datetime import date
from pathlib import Path

import anthropic

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

BASE          = Path(__file__).parent.parent
INPUTS_DIR    = BASE / "parser" / "ai_analysis_outputs"
ANALYSIS_DIR  = BASE / "dashboard" / "src" / "data" / "analysis"
INDICATORS_JSON = BASE / "dashboard" / "src" / "data" / "indicators.json"
ENRICHMENT_DIR  = BASE / "dashboard" / "src" / "data" / "pdf_enrichment"

# ---------------------------------------------------------------------------
# Company / year constants
# ---------------------------------------------------------------------------

COMPANIES = [
    ("tata-steel",       "Tata Steel",       "Tata"),
    ("jsw-steel",        "JSW Steel",        "JSW"),
    ("sail",             "SAIL",             "SAIL"),
    ("jindal-stainless", "Jindal Stainless", "Jindal"),
]
YEARS = ["FY2023", "FY2024", "FY2025"]

COMPANY_SHORT_TO_KEY = {
    "Tata":   "tata",
    "JSW":    "jsw",
    "SAIL":   "sail",
    "Jindal": "jindal",
}

SONNET_MODEL = "claude-sonnet-4-6"

# ---------------------------------------------------------------------------
# Import TOPIC_TAGS and TOPIC_NAMES from generate_analysis_prompts
# ---------------------------------------------------------------------------

sys.path.insert(0, str(BASE / "parser"))
from generate_analysis_prompts import TOPIC_TAGS, TOPIC_NAMES  # noqa: E402

# ---------------------------------------------------------------------------
# 1. Reverse lookup helpers
# ---------------------------------------------------------------------------

def build_indicator_lookup() -> dict:
    """Both canonical tag names AND display labels → canonical tag."""
    lookup = {}
    for topic_tags in TOPIC_TAGS.values():
        for canonical_tag, display_label, _ in topic_tags:
            lookup[canonical_tag] = canonical_tag
            lookup[display_label] = canonical_tag
    return lookup


def build_tag_to_topic() -> dict:
    """canonical_tag → topic_key."""
    result = {}
    for topic_key, tags in TOPIC_TAGS.items():
        for canonical_tag, _, _ in tags:
            result[canonical_tag] = topic_key
    return result


# ---------------------------------------------------------------------------
# 2. Section extraction
# ---------------------------------------------------------------------------

SECTION_HEADERS = [
    "DIRECTION:", "PEER_RANK:", "TREND_DIRECTION:", "ABOUT:",
    "PERFORMANCE_AND_DRIVERS:", "TATA_POSITIONING:", "TARGETS:",
    "COMPARABILITY_NOTES:", "FLAGS:",
]


def _find_section(block: str, header: str) -> str | None:
    """Extract the text content of a named section from a block, or None."""
    positions = []
    for h in SECTION_HEADERS:
        m = re.search(r"(?:^|\n)" + re.escape(h), block)
        if m:
            positions.append((m.start(), m.end(), h))
    positions.sort()

    for i, (_, content_start, h) in enumerate(positions):
        if h == header:
            content_end = positions[i + 1][0] if i + 1 < len(positions) else len(block)
            return block[content_start:content_end].strip()
    return None


# ---------------------------------------------------------------------------
# 3. Structured field parsers
# ---------------------------------------------------------------------------

def parse_direction(text: str) -> str:
    if not text:
        return "unknown"
    t = text.strip()
    if t.startswith("lower_is_better"):
        return "lower_is_better"
    if t.startswith("higher_is_better"):
        return "higher_is_better"
    return t  # preserves DIRECTION_UNCLEAR: [reason]


def parse_peer_rank(text: str) -> dict:
    """Returns {FY2023: {tata: n, jsw: n, sail: n, jindal: n}, ...}"""
    result = {}
    pattern = re.compile(
        r"FY(\d{4}):\s*Tata=(\d+),\s*JSW=(\d+),\s*SAIL=(\d+),\s*Jindal=(\d+)"
    )
    for m in pattern.finditer(text or ""):
        yr = f"FY{m.group(1)}"
        result[yr] = {
            "tata":   int(m.group(2)),
            "jsw":    int(m.group(3)),
            "sail":   int(m.group(4)),
            "jindal": int(m.group(5)),
        }
    return result


def parse_trend_direction(text: str) -> dict:
    """Returns {tata: {FY2023-24: ..., FY2024-25: ...}, ...}"""
    result = {}
    for short_name, company_key in COMPANY_SHORT_TO_KEY.items():
        # FY2023-24 value may be "AMBIGUOUS: [reason]" containing commas —
        # non-greedy match stops at the FIRST occurrence of ", FY2024-25="
        pattern = re.compile(
            rf"{re.escape(short_name)}:\s*FY2023-24=(.+?),\s*FY2024-25=(.+?)(?:\n|$)"
        )
        m = pattern.search(text or "")
        if m:
            result[company_key] = {
                "FY2023-24": m.group(1).strip(),
                "FY2024-25": m.group(2).strip(),
            }
    return result


def parse_flags(text: str) -> dict:
    def _flag(key: str) -> bool:
        m = re.search(rf"{key}:\s*(yes|no)", text or "", re.IGNORECASE)
        return bool(m) and m.group(1).lower() == "yes"

    note_m = re.search(r"FLAG_NOTE:\s*(.+?)(?:\n|$)", text or "", re.IGNORECASE)
    return {
        "directionUnclear":    _flag("DIRECTION_UNCLEAR"),
        "contextInsufficient": _flag("CONTEXT_INSUFFICIENT"),
        "externalSourceUsed":  _flag("EXTERNAL_SOURCE_USED"),
        "trendAmbiguity":      _flag("TREND_AMBIGUITY"),
        "flagNote":            note_m.group(1).strip() if note_m else None,
    }


# ---------------------------------------------------------------------------
# 4. parse_indicator_block
# ---------------------------------------------------------------------------

def parse_indicator_block(block: str, indicator_lookup: dict) -> dict | None:
    """Parse one INDICATOR block. Returns dict including _canonical_tag, or None."""
    first_line = block.split("\n")[0]
    raw_name = first_line[len("INDICATOR:"):].strip()

    canonical_tag = indicator_lookup.get(raw_name)
    if canonical_tag is None:
        print(f"  WARNING: Cannot map '{raw_name}' to canonical tag — skipping")
        return None

    return {
        "_canonical_tag":   canonical_tag,
        "rawIndicatorName": raw_name,
        "direction":        parse_direction(_find_section(block, "DIRECTION:") or ""),
        "peerRank":         parse_peer_rank(_find_section(block, "PEER_RANK:")),
        "trendDirection":   parse_trend_direction(_find_section(block, "TREND_DIRECTION:")),
        "sections": {
            "about":                _find_section(block, "ABOUT:")                  or "",
            "performanceAndDrivers": _find_section(block, "PERFORMANCE_AND_DRIVERS:") or "",
            "tataPositioning":      _find_section(block, "TATA_POSITIONING:")       or "",
            "targets":              _find_section(block, "TARGETS:")                or "",
            "comparabilityNotes":   _find_section(block, "COMPARABILITY_NOTES:"),
        },
        "flags": parse_flags(_find_section(block, "FLAGS:")),
    }


# ---------------------------------------------------------------------------
# 5. parse_benchmark_block
# ---------------------------------------------------------------------------

BENCH_YEAR_MAP = {
    "FY2022-23": "FY2023",
    "FY2023-24": "FY2024",
    "FY2024-25": "FY2025",
}


def parse_benchmark_block(block: str) -> dict:
    """Parse BENCHMARK block → {FY2023: text, FY2024: text, FY2025: text}"""
    positions = [(m.start(), m.group(1)) for m in
                 re.finditer(r"\n(FY\d{4}-\d{2}):", block)]
    result = {}
    for i, (pos, label) in enumerate(positions):
        end = positions[i + 1][0] if i + 1 < len(positions) else len(block)
        content = block[pos:end]
        content = re.sub(r"^\s*FY\d{4}-\d{2}:\s*", "", content, count=1).strip()
        year_key = BENCH_YEAR_MAP.get(label)
        if year_key:
            result[year_key] = content
    return result


# ---------------------------------------------------------------------------
# 6. parse_gem_output — parse one topic file
# ---------------------------------------------------------------------------

def parse_gem_output(topic_key: str) -> dict:
    """
    Returns {
        "indicators": {canonical_tag: parsed_dict},
        "benchmark":  {"FY2023": text, "FY2024": text, "FY2025": text}
    }
    """
    text = (INPUTS_DIR / f"{topic_key}.md").read_text(encoding="utf-8")
    indicator_lookup = build_indicator_lookup()

    # Split file into top-level INDICATOR and BENCHMARK blocks
    pattern = re.compile(r"^(?:INDICATOR|BENCHMARK):", re.MULTILINE)
    positions = [(m.start(), m.group(0).rstrip(":")) for m in pattern.finditer(text)]

    indicators_out = {}
    benchmark_out = {}

    for i, (pos, btype) in enumerate(positions):
        end = positions[i + 1][0] if i + 1 < len(positions) else len(text)
        block = text[pos:end].strip()

        if btype == "INDICATOR":
            parsed = parse_indicator_block(block, indicator_lookup)
            if parsed:
                canonical_tag = parsed.pop("_canonical_tag")
                indicators_out[canonical_tag] = parsed
        elif btype == "BENCHMARK":
            benchmark_out = parse_benchmark_block(block)

    return {"indicators": indicators_out, "benchmark": benchmark_out}


# ---------------------------------------------------------------------------
# 7. write_indicator_files
# ---------------------------------------------------------------------------

def write_indicator_files(all_parsed: dict, indicators_meta: dict, tag_to_topic: dict) -> int:
    out_dir = ANALYSIS_DIR / "indicators"
    out_dir.mkdir(parents=True, exist_ok=True)

    written = 0
    for topic_key, topic_data in all_parsed.items():
        for canonical_tag, parsed in topic_data["indicators"].items():
            meta = indicators_meta.get(canonical_tag, {})
            brsr = meta.get("brsr", {})

            record = {
                "tag":       canonical_tag,
                "label":     meta.get("label") or parsed.get("rawIndicatorName", canonical_tag),
                "principle": brsr.get("principle") or brsr.get("section", ""),
                "topic":     tag_to_topic.get(canonical_tag, topic_key),
                "direction": parsed["direction"],
                "peerRank":       parsed["peerRank"],
                "trendDirection": parsed["trendDirection"],
                "sections":       parsed["sections"],
                "flags":          parsed["flags"],
                "source":         "CustomGPT",
                "userCorrection": None,
                "status":         "pending_review",
            }

            (out_dir / f"{canonical_tag}.json").write_text(
                json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8"
            )
            written += 1

    return written


# ---------------------------------------------------------------------------
# 8. write_benchmark_files
# ---------------------------------------------------------------------------

def write_benchmark_files(all_parsed: dict) -> int:
    out_dir = ANALYSIS_DIR / "benchmarks"
    out_dir.mkdir(parents=True, exist_ok=True)

    written = 0
    for topic_key, topic_data in all_parsed.items():
        for year, narrative in topic_data["benchmark"].items():
            record = {
                "topic":     topic_key,
                "year":      year,
                "narrative": narrative,
                "source":    "CustomGPT",
            }
            (out_dir / f"{topic_key}-{year}.json").write_text(
                json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8"
            )
            written += 1

    return written


# ---------------------------------------------------------------------------
# 9. Sonnet call with retry
# ---------------------------------------------------------------------------

def call_sonnet(client: anthropic.Anthropic, prompt: str) -> str:
    for attempt in range(4):
        try:
            msg = client.messages.create(
                model=SONNET_MODEL,
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}],
            )
            return msg.content[0].text.strip()
        except anthropic.RateLimitError:
            if attempt == 3:
                raise
            wait = 30 * (2 ** attempt)
            print(f"    Rate limit — waiting {wait}s...")
            time.sleep(wait)


# ---------------------------------------------------------------------------
# 10. Company narrative synthesis (12 calls)
# ---------------------------------------------------------------------------

def _build_company_narrative_prompt(
    company_id: str, company_name: str, year: str,
    all_parsed: dict, enrichment: dict,
) -> str:
    company_key_map = {
        "tata-steel": "tata", "jsw-steel": "jsw",
        "sail": "sail", "jindal-stainless": "jindal",
    }
    company_key = company_key_map[company_id]
    is_tata = company_id == "tata-steel"

    topic_summaries = []
    for topic_key, topic_data in all_parsed.items():
        topic_name = TOPIC_NAMES.get(topic_key, topic_key)
        lines = [f"### {topic_name}"]
        for tag, indicator in topic_data["indicators"].items():
            rank = indicator["peerRank"].get(year, {}).get(company_key, "—")
            trend_y = {
                "FY2023": indicator["trendDirection"].get(company_key, {}).get("FY2023-24", "—"),
                "FY2024": indicator["trendDirection"].get(company_key, {}).get("FY2023-24", "—"),
                "FY2025": indicator["trendDirection"].get(company_key, {}).get("FY2024-25", "—"),
            }.get(year, "—")

            perf = indicator["sections"].get("performanceAndDrivers", "")[:250]
            tata_pos = indicator["sections"].get("tataPositioning", "")[:150] if is_tata else ""

            entry = f"[{tag}] Rank={rank}, Trend={trend_y}"
            if perf:
                entry += f"\n  {perf}"
            if tata_pos:
                entry += f"\n  Tata positioning: {tata_pos}"
            lines.append(entry)
        topic_summaries.append("\n".join(lines))

    enrichment_block = ""
    targets = (enrichment.get("enrichment") or {}).get("targets", [])
    if targets:
        t_lines = [f"- {t.get('description', '')}" for t in targets[:4]]
        enrichment_block = "\nKey targets:\n" + "\n".join(t_lines)

    body = "\n\n".join(topic_summaries)

    return (
        f"Write a 200-300 word internal ESG narrative for {company_name}, {year}. "
        f"Audience: senior management at Tata Steel benchmarking peer performance. "
        f"Summarise {company_name}'s overall sustainability position across environmental, social and governance themes. "
        f"Highlight notable strengths, weaknesses and key drivers. Be direct and analytical. "
        f"Do not use bullet points. Cite specific metrics where it adds precision.\n"
        f"{enrichment_block}\n\n"
        f"ESG data for {company_name} {year}:\n\n{body}"
    )


def synthesise_company_narratives(
    client: anthropic.Anthropic,
    all_parsed: dict,
    enrichments: dict,
) -> int:
    out_dir = ANALYSIS_DIR / "companies"
    out_dir.mkdir(parents=True, exist_ok=True)

    written = 0
    for company_id, company_name, _ in COMPANIES:
        for year in YEARS:
            out_path = out_dir / f"{company_id}-{year}.json"
            if out_path.exists():
                print(f"    Skip (exists): {company_id} {year}")
                continue

            print(f"    Narrative: {company_name} {year}...")
            prompt = _build_company_narrative_prompt(
                company_id, company_name, year, all_parsed,
                enrichments.get(f"{company_id}-{year}", {}),
            )
            narrative = call_sonnet(client, prompt)
            out_path.write_text(
                json.dumps({
                    "companyId": company_id,
                    "year":      year,
                    "narrative": narrative,
                    "source":    "ClaudeSonnet",
                }, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            written += 1

    return written


# ---------------------------------------------------------------------------
# 11. Trend narrative synthesis (4 calls)
# ---------------------------------------------------------------------------

def _build_trend_prompt(
    company_id: str, company_name: str,
    all_parsed: dict,
) -> str:
    company_key_map = {
        "tata-steel": "tata", "jsw-steel": "jsw",
        "sail": "sail", "jindal-stainless": "jindal",
    }
    company_key = company_key_map[company_id]
    is_tata = company_id == "tata-steel"

    topic_summaries = []
    for topic_key, topic_data in all_parsed.items():
        topic_name = TOPIC_NAMES.get(topic_key, topic_key)
        lines = [f"### {topic_name}"]
        for tag, indicator in topic_data["indicators"].items():
            trend = indicator["trendDirection"].get(company_key, {})
            fy2324 = trend.get("FY2023-24", "—")
            fy2425 = trend.get("FY2024-25", "—")
            ranks_by_year = {yr: indicator["peerRank"].get(yr, {}).get(company_key, "—")
                             for yr in YEARS}
            perf = indicator["sections"].get("performanceAndDrivers", "")[:200]
            tata_pos = indicator["sections"].get("tataPositioning", "")[:150] if is_tata else ""

            entry = (
                f"[{tag}] Rank: FY23={ranks_by_year['FY2023']} "
                f"FY24={ranks_by_year['FY2024']} FY25={ranks_by_year['FY2025']} | "
                f"Trend: FY23-24={fy2324}, FY24-25={fy2425}"
            )
            if perf:
                entry += f"\n  {perf}"
            if tata_pos:
                entry += f"\n  {tata_pos}"
            lines.append(entry)
        topic_summaries.append("\n".join(lines))

    body = "\n\n".join(topic_summaries)

    return (
        f"Write a 200-300 word multi-year ESG trend narrative for {company_name}, "
        f"covering FY2022-23, FY2023-24, and FY2024-25. "
        f"Audience: senior management at Tata Steel. "
        f"Identify which ESG themes improved, worsened or remained flat, and what structural or strategic factors drove those trends. "
        f"Be direct and analytical. Do not use bullet points.\n\n"
        f"Trend data:\n\n{body}"
    )


def synthesise_trends(
    client: anthropic.Anthropic,
    all_parsed: dict,
) -> int:
    out_dir = ANALYSIS_DIR / "trends"
    out_dir.mkdir(parents=True, exist_ok=True)

    written = 0
    for company_id, company_name, _ in COMPANIES:
        out_path = out_dir / f"{company_id}.json"
        if out_path.exists():
            print(f"    Skip (exists): {company_id} trend")
            continue

        print(f"    Trend: {company_name}...")
        prompt = _build_trend_prompt(company_id, company_name, all_parsed)
        narrative = call_sonnet(client, prompt)
        out_path.write_text(
            json.dumps({
                "companyId": company_id,
                "narrative": narrative,
                "source":    "ClaudeSonnet",
            }, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        written += 1

    return written


# ---------------------------------------------------------------------------
# 12. write_review_status
# ---------------------------------------------------------------------------

def write_review_status() -> None:
    (ANALYSIS_DIR / "_review_status.json").write_text(
        json.dumps({
            "status":      "pending_review",
            "generatedAt": date.today().isoformat(),
            "approvedAt":  None,
        }, indent=2),
        encoding="utf-8",
    )


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY environment variable not set.")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)

    print("Loading metadata...")
    indicators_meta = json.loads(INDICATORS_JSON.read_text(encoding="utf-8"))
    tag_to_topic    = build_tag_to_topic()

    enrichments = {}
    for cid, _, _ in COMPANIES:
        for yr in YEARS:
            key = f"{cid}-{yr}"
            p = ENRICHMENT_DIR / f"{key}.json"
            if p.exists():
                enrichments[key] = json.loads(p.read_text(encoding="utf-8"))

    # ── Step 1: Parse all 13 GPT output files ────────────────────────────────
    print("\nParsing Custom GPT outputs...")
    all_parsed = {}
    for topic_key in TOPIC_TAGS:
        path = INPUTS_DIR / f"{topic_key}.md"
        if not path.exists():
            print(f"  WARNING: Missing {topic_key}.md — skipping")
            continue
        print(f"  {topic_key}...", end=" ", flush=True)
        all_parsed[topic_key] = parse_gem_output(topic_key)
        n_ind   = len(all_parsed[topic_key]["indicators"])
        n_bench = len(all_parsed[topic_key]["benchmark"])
        print(f"{n_ind} indicators, {n_bench} benchmark years")

    # ── Step 2: Write indicator JSON ─────────────────────────────────────────
    print("\nWriting indicator files...")
    n = write_indicator_files(all_parsed, indicators_meta, tag_to_topic)
    print(f"  {n} indicator files written")

    # ── Step 3: Write benchmark JSON ─────────────────────────────────────────
    print("\nWriting benchmark files...")
    n = write_benchmark_files(all_parsed)
    print(f"  {n} benchmark files written")

    # ── Step 4: Company narratives (12 Sonnet calls) ─────────────────────────
    print("\nGenerating company narratives (12 Sonnet calls)...")
    n = synthesise_company_narratives(client, all_parsed, enrichments)
    print(f"  {n} new company narratives written")

    # ── Step 5: Trend summaries (4 Sonnet calls) ─────────────────────────────
    print("\nGenerating trend summaries (4 Sonnet calls)...")
    n = synthesise_trends(client, all_parsed)
    print(f"  {n} new trend narratives written")

    # ── Step 6: Review status ────────────────────────────────────────────────
    print("\nWriting review status...")
    write_review_status()

    # ── Summary ──────────────────────────────────────────────────────────────
    ind_count   = len(list((ANALYSIS_DIR / "indicators").glob("*.json")))
    bench_count = len(list((ANALYSIS_DIR / "benchmarks").glob("*.json")))
    comp_count  = len(list((ANALYSIS_DIR / "companies").glob("*.json")))
    trend_count = len(list((ANALYSIS_DIR / "trends").glob("*.json")))

    print(f"\n=== Done ===")
    print(f"  Indicators: {ind_count}  (expected 98)")
    print(f"  Benchmarks: {bench_count}  (expected 39)")
    print(f"  Companies:  {comp_count}  (expected 12)")
    print(f"  Trends:     {trend_count}  (expected 4)")


if __name__ == "__main__":
    main()
