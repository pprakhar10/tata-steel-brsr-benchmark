"""
process_narrative_outputs.py — Parse Custom GPT narrative outputs → analysis JSON

Reads:
  parser/narrative_outputs/company_narratives.md
  parser/narrative_outputs/trend_summaries.md

Writes:
  dashboard/src/data/analysis/companies/{id}-{year}.json  × 12
  dashboard/src/data/analysis/trends/{id}.json             × 4
  dashboard/src/data/analysis/_review_status.json

Run: python parser/process_narrative_outputs.py
"""

import json
import re
from datetime import date
from pathlib import Path

BASE          = Path(__file__).parent.parent
OUTPUTS_DIR   = BASE / "parser" / "narrative_outputs"
ANALYSIS_DIR  = BASE / "dashboard" / "src" / "data" / "analysis"

VALID_COMPANY_IDS = {"tata-steel", "jsw-steel", "sail", "jindal-stainless"}
VALID_YEARS       = {"FY2023", "FY2024", "FY2025"}


# ---------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------

def parse_company_narratives(text: str) -> list[dict]:
    """
    Parse output containing blocks like:
      ## COMPANY_NARRATIVE: tata-steel / FY2025
      [narrative text]
    Returns list of {companyId, year, narrative} dicts.
    """
    # Accept with or without leading ## marker
    pattern = re.compile(
        r"^(?:##\s+)?COMPANY_NARRATIVE:\s*([a-z\-]+)\s*/\s*(FY\d{4})\s*$",
        re.MULTILINE,
    )
    positions = [(m.start(), m.group(1).strip(), m.group(2).strip())
                 for m in pattern.finditer(text)]

    results = []
    for i, (pos, company_id, year) in enumerate(positions):
        if company_id not in VALID_COMPANY_IDS:
            print(f"  WARNING: Unknown company_id '{company_id}' — skipping")
            continue
        if year not in VALID_YEARS:
            print(f"  WARNING: Unknown year '{year}' — skipping")
            continue

        end = positions[i + 1][0] if i + 1 < len(positions) else len(text)
        block = text[pos:end]
        # Strip the header line
        narrative = re.sub(r"^(?:##\s+)?COMPANY_NARRATIVE:.*\n", "", block, count=1).strip()

        if narrative:
            results.append({
                "companyId": company_id,
                "year":      year,
                "narrative": narrative,
                "source":    "CustomGPT",
            })

    return results


def parse_trend_summaries(text: str) -> list[dict]:
    """
    Parse output containing blocks like:
      ## TREND_SUMMARY: tata-steel
      [narrative text]
    Returns list of {companyId, narrative} dicts.
    """
    pattern = re.compile(
        r"^(?:##\s+)?TREND_SUMMARY:\s*([a-z\-]+)\s*$",
        re.MULTILINE,
    )
    positions = [(m.start(), m.group(1).strip()) for m in pattern.finditer(text)]

    results = []
    for i, (pos, company_id) in enumerate(positions):
        if company_id not in VALID_COMPANY_IDS:
            print(f"  WARNING: Unknown company_id '{company_id}' — skipping")
            continue

        end = positions[i + 1][0] if i + 1 < len(positions) else len(text)
        block = text[pos:end]
        narrative = re.sub(r"^(?:##\s+)?TREND_SUMMARY:.*\n", "", block, count=1).strip()

        if narrative:
            results.append({
                "companyId": company_id,
                "narrative": narrative,
                "source":    "CustomGPT",
            })

    return results


# ---------------------------------------------------------------------------
# Writers
# ---------------------------------------------------------------------------

def write_company_narratives(records: list[dict]) -> int:
    out_dir = ANALYSIS_DIR / "companies"
    out_dir.mkdir(parents=True, exist_ok=True)

    written = 0
    for record in records:
        cid  = record["companyId"]
        year = record["year"]
        path = out_dir / f"{cid}-{year}.json"
        path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
        written += 1

    return written


def write_trend_summaries(records: list[dict]) -> int:
    out_dir = ANALYSIS_DIR / "trends"
    out_dir.mkdir(parents=True, exist_ok=True)

    written = 0
    for record in records:
        cid  = record["companyId"]
        path = out_dir / f"{cid}.json"
        path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
        written += 1

    return written


def write_review_status():
    path = ANALYSIS_DIR / "_review_status.json"
    path.write_text(
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
    ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)

    # ── Company narratives ───────────────────────────────────────────────────
    cn_path = OUTPUTS_DIR / "company_narratives.md"
    if not cn_path.exists():
        print(f"ERROR: Missing {cn_path}")
        print("  Run Custom GPT session 14 and save output to that path first.")
    else:
        print("Parsing company narratives...")
        text = cn_path.read_text(encoding="utf-8")
        records = parse_company_narratives(text)
        n = write_company_narratives(records)
        print(f"  {n} company narrative files written  (expected 12)")

    # ── Trend summaries ──────────────────────────────────────────────────────
    ts_path = OUTPUTS_DIR / "trend_summaries.md"
    if not ts_path.exists():
        print(f"ERROR: Missing {ts_path}")
        print("  Run Custom GPT session 15 and save output to that path first.")
    else:
        print("Parsing trend summaries...")
        text = ts_path.read_text(encoding="utf-8")
        records = parse_trend_summaries(text)
        n = write_trend_summaries(records)
        print(f"  {n} trend summary files written  (expected 4)")

    # ── Review status ────────────────────────────────────────────────────────
    print("Writing _review_status.json...")
    write_review_status()

    # ── Summary ──────────────────────────────────────────────────────────────
    comp_dir  = ANALYSIS_DIR / "companies"
    trend_dir = ANALYSIS_DIR / "trends"
    comp_count  = len(list(comp_dir.glob("*.json"))) if comp_dir.exists() else 0
    trend_count = len(list(trend_dir.glob("*.json"))) if trend_dir.exists() else 0

    print(f"\n=== Done ===")
    print(f"  Companies:  {comp_count}/12")
    print(f"  Trends:     {trend_count}/4")
    print(f"  Status:     pending_review")


if __name__ == "__main__":
    main()
