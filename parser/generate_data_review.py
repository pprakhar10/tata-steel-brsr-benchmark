"""
generate_data_review.py — Produces parser/review/data_review.md + data_review.html

Run: python parser/generate_data_review.py
Output: parser/review/data_review.md  (edit this to add comments)
        parser/review/data_review.html (open in browser to read)
"""

import json
import markdown as md_lib
from pathlib import Path
from datetime import date

BASE = Path(__file__).parent.parent
DATA_DIR = BASE / "dashboard" / "src" / "data" / "companies"
ENRICH_DIR = BASE / "dashboard" / "src" / "data" / "pdf_enrichment"
VAL_REPORT = BASE / "parser" / "validation_report.json"
OUT_MD   = BASE / "parser" / "review" / "data_review.md"
OUT_HTML = BASE / "parser" / "review" / "data_review.html"

COMPANIES = [
    ("tata-steel",       "Tata Steel"),
    ("jsw-steel",        "JSW Steel"),
    ("sail",             "SAIL"),
    ("jindal-stainless", "Jindal Stainless"),
]
YEARS = ["FY2023", "FY2024", "FY2025"]

KEY_INDICATORS = [
    # GHG
    ("TotalScope1Emissions",                                        "Scope 1 GHG",              "tCO2e"),
    ("TotalScope2Emissions",                                        "Scope 2 GHG",              "tCO2e"),
    ("TotalScope1AndScope2EmissionsIntensityInTermOfPhysicalOutput","GHG Intensity",             "tCO2e/tcs"),
    # Energy
    ("TotalEnergyConsumedFromRenewableAndNonRenewableSources",      "Total Energy",             "GJ"),
    ("TotalEnergyConsumedFromRenewableSources",                     "Renewable Energy",         "GJ"),
    # Air emissions
    ("Sox",                                                         "SOx",                      "kilotonnes"),
    ("Nox",                                                         "NOx",                      "kilotonnes"),
    ("ParticulateMatter",                                           "Particulate Matter",       "kilotonnes"),
    # Water
    ("TotalVolumeOfWaterWithdrawal",                                "Water Withdrawal",         "kL"),
    ("TotalVolumeOfWaterConsumption",                               "Water Consumption",        "kL"),
    ("WaterIntensityPerRupeeOfTurnover",                            "Water Intensity",          "L/₹ or kL/Cr — NOT uniform"),
    # Waste
    ("TotalWasteGenerated",                                         "Total Waste",              "metric tonnes"),
    ("TotalWasteRecovered",                                         "Waste Recovered",          "metric tonnes"),
    ("TotalWasteDisposed",                                          "Waste Disposed",           "metric tonnes"),
    # Safety
    ("LostTimeInjuryFrequencyRate",                                 "LTIFR",                    ""),
    ("NumberOfFatalities",                                          "Fatalities",               ""),
    # Workforce
    ("TotalNumberOfEmployees",                                      "Total Employees",          ""),
    ("PercentageOfFemaleEmployees",                                  "Female Employees",         "%"),
    ("PercentageOfEmployeesCoveredUnderTraining",                   "Training Coverage",        "%"),
]

COMMENT_PLACEHOLDER = "> **YOUR COMMENT:** *(type here — leave blank if no issues)*"


# ─── loaders ──────────────────────────────────────────────────────────────────

def load(company_id):
    with open(DATA_DIR / f"{company_id}.json", encoding="utf-8") as f:
        return json.load(f)

def load_enrichment(company_id, year):
    path = ENRICH_DIR / f"{company_id}-{year}.json"
    if not path.exists():
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def load_validation():
    with open(VAL_REPORT, encoding="utf-8") as f:
        return json.load(f)


# ─── value formatter ──────────────────────────────────────────────────────────

def fmt_val(v_obj):
    if v_obj is None:
        return "—"
    val = v_obj.get("value")
    if val is None:
        return "null ⚠️"

    if isinstance(val, float):
        if abs(val) >= 1_000_000:
            s = f"{val:,.0f}"
        elif abs(val) >= 1_000:
            s = f"{val:,.1f}"
        elif abs(val) >= 1:
            s = f"{val:.3f}"
        else:
            s = f"{val:.6f}"
    elif isinstance(val, int):
        s = f"{val:,}"
    else:
        s = str(val)

    if not v_obj.get("normalized", True):
        s += " ⚠️"
    if v_obj.get("patchSource") == "PDF":
        s += " 📄"
    return s


# ─── section writers ──────────────────────────────────────────────────────────

def write_header(lines):
    lines += [
        f"# BRSR Data Review — {date.today()}",
        "",
        "**Instructions:** Read each section. Where you see `YOUR COMMENT`, type your note on that line.",
        "Leave blank if the data looks correct. Save the file when done, then tell Claude to read it.",
        "",
        "**Legend:** ⚠️ = value null or not normalized &nbsp;|&nbsp; 📄 = overridden by PDF patch",
        "",
        "---",
        "",
    ]


def write_reporting_basis(lines, company_data_map):
    lines += ["## 1. Reporting Basis", ""]
    lines += ["| Company | FY2023 | FY2024 | FY2025 |",
              "|:--------|:------:|:------:|:------:|"]
    notes = []
    for cid, cname in COMPANIES:
        data = company_data_map[cid]
        cells = []
        for yr in YEARS:
            meta = data["years"].get(yr, {}).get("_meta", {})
            basis = meta.get("reportingBasis", "unknown")
            warn  = meta.get("basisWarning")
            cells.append("⚠️ Consolidated" if basis == "consolidated" else "✓ Standalone")
            if warn:
                notes.append(f"- **{cname} {yr}:** {warn}")
        lines.append(f"| {cname} | {cells[0]} | {cells[1]} | {cells[2]} |")
    lines.append("")
    lines += notes
    lines += ["", COMMENT_PLACEHOLDER, "", "---", ""]


def write_validation_summary(lines, val):
    s = val["summary"]
    lines += ["## 2. Validation Summary", ""]
    lines += [
        f"| | Count |",
        f"|:--|:--|",
        f"| Blocking flags | **{s['blocking']}** (must be 0) |",
        f"| Warning flags  | {s['warnings']} |",
        "",
    ]

    peer = val.get("peerOutliers", [])
    high = [f for f in peer if f.get("ratio", 1) > 50]
    lines += [f"### Peer outliers with ratio > 50× &nbsp; ({len(high)} of {len(peer)} total)", ""]
    lines += ["| Company | Year | Metric | Value | Peer Median | Ratio | Likely cause |",
              "|:--------|:-----|:-------|------:|------------:|------:|:-------------|"]
    for f in high[:60]:
        v = f"{f['value']:,.0f}" if abs(f['value']) >= 1 else f"{f['value']:.4f}"
        m = f"{f['peerMedian']:,.0f}" if abs(f['peerMedian']) >= 1 else f"{f['peerMedian']:.4f}"
        cause = f.get("suspectedCause", "")[:70]
        lines.append(f"| {f['company']} | {f['year']} | {f['tag']} | {v} | {m} | {f['ratio']:.0f}x | {cause} |")
    if len(high) > 60:
        lines.append(f"*... {len(high)-60} more in validation_report.json*")
    lines.append("")
    lines += [COMMENT_PLACEHOLDER, ""]

    self_out = val.get("selfOutliers", [])
    non_exp = [f for f in self_out
               if not (f["company"] == "tata-steel" and f.get("yearFrom") == "FY2023")]
    lines += [f"### Year-over-year outliers &nbsp; ({len(non_exp)} shown — {len(self_out)-len(non_exp)} Tata FY23 suppressed as expected basis change)", ""]
    lines += ["| Company | Metric | Period | Change | Direction |",
              "|:--------|:-------|:-------|-------:|:----------|"]
    for f in non_exp[:50]:
        lines.append(
            f"| {f['company']} | {f['tag']} "
            f"| {f.get('yearFrom','?')}→{f.get('yearTo','?')} "
            f"| {f.get('changePct',0):.0f}% "
            f"| {f.get('direction','')} |"
        )
    if len(non_exp) > 50:
        lines.append(f"*... {len(non_exp)-50} more*")
    lines += ["", COMMENT_PLACEHOLDER, "", "---", ""]


def write_patches(lines, company_data_map):
    lines += ["## 3. PDF Patches Applied", "",
              "Values the parser stored from XBRL that were overridden by PDF-confirmed data.", ""]
    for cid, cname in COMPANIES:
        data = company_data_map[cid]
        patches = [
            (yr, tag, v)
            for yr in YEARS
            for tag, v in data["years"].get(yr, {}).items()
            if tag != "_meta" and isinstance(v, dict) and v.get("patchSource") == "PDF"
        ]
        if not patches:
            continue
        lines += [f"### {cname}", ""]
        lines += ["| Year | Metric | Patched value | Raw PDF value | Unit | Note |",
                  "|:----|:-------|:-------------|:-------------|:-----|:-----|"]
        for yr, tag, v in patches:
            val  = v.get("value", "")
            raw  = v.get("rawValue", "")
            unit = (v.get("rawUnit") or "")[:35]
            note = (v.get("unitWarning") or "")[:70]
            lines.append(f"| {yr} | {tag} | {val} | {raw} | {unit} | {note} |")
        lines += ["", COMMENT_PLACEHOLDER, ""]
    lines += ["---", ""]


def build_concern(tag, yr, company_data_map):
    """Return a list of concern strings for this metric+year, one per company that has an issue."""
    concerns = []
    for cid, cname in COMPANIES:
        v_obj = company_data_map[cid]["years"].get(yr, {}).get(tag)
        if v_obj is None:
            continue
        val = v_obj.get("value")
        parts = []
        if val is None:
            parts.append("value nulled")
        if not v_obj.get("normalized", True):
            parts.append("not normalized")
        if v_obj.get("patchSource") == "PDF":
            parts.append("PDF-patched")
        warn = v_obj.get("unitWarning")
        if warn:
            parts.append(warn[:120])
        if parts:
            concerns.append(f"**{cname}:** {'; '.join(parts)}")
    return concerns


def write_key_metrics(lines, company_data_map):
    lines += ["## 4. Key Metrics by Financial Year", "",
              "One table per year. Each row = one metric. Last column lists concerns for specific companies.",
              "Add your comment in the `> YOUR COMMENT` block after each table.", ""]

    for yr in YEARS:
        lines += [f"### {yr}", ""]
        lines += [
            "| Metric | Unit | Tata Steel | JSW Steel | SAIL | Jindal Stainless | Concerns |",
            "|:-------|:-----|----------:|----------:|-----:|-----------------:|:---------|",
        ]
        for tag, label, unit in KEY_INDICATORS:
            cells = []
            for cid, _ in COMPANIES:
                v_obj = company_data_map[cid]["years"].get(yr, {}).get(tag)
                cells.append(fmt_val(v_obj))
            concerns = build_concern(tag, yr, company_data_map)
            concern_str = "<br>".join(concerns) if concerns else ""
            unit_str = unit if unit else "—"
            lines.append(
                f"| {label} | {unit_str} | {cells[0]} | {cells[1]} | {cells[2]} | {cells[3]} | {concern_str} |"
            )
        lines += ["", COMMENT_PLACEHOLDER, "", "---", ""]


def write_enrichment(lines):
    lines += ["## 5. PDF Enrichment Summaries", "",
              "Targets, initiatives, and non-compliance extracted from company BRSR PDFs.", ""]

    for cid, cname in COMPANIES:
        lines += [f"### {cname}", ""]
        for yr in YEARS:
            enrich = load_enrichment(cid, yr)
            lines += [f"#### {yr}", ""]
            if not enrich:
                lines += ["*Enrichment file missing.*", ""]
                continue
            e = enrich.get("enrichment", {})

            targets = e.get("targets", [])
            if targets:
                lines.append(f"**Targets ({len(targets)})**")
                for t in targets:
                    lines.append(f"- {t.get('description','')}  _{t.get('timeline','')}_")
                lines.append("")

            initiatives = e.get("initiatives", [])
            if initiatives:
                lines.append(f"**Initiatives ({len(initiatives)})**")
                for i in initiatives[:5]:
                    lines.append(f"- [{i.get('area','')}] **{i.get('name','')}**: {i.get('outcome','')[:100]}")
                if len(initiatives) > 5:
                    lines.append(f"- *... {len(initiatives)-5} more*")
                lines.append("")

            s3 = e.get("scope3Breakdown", {})
            if s3.get("totalScope3"):
                lines.append(f"**Scope 3 total:** {s3['totalScope3']}")
                lines.append("")

            nc = e.get("nonCompliance", [])
            if nc:
                lines.append(f"**Non-compliance ({len(nc)})**")
                for n in nc[:3]:
                    lines.append(f"- {n.get('description','')[:120]}")
                lines.append("")

            prod = e.get("steelProduction", {})
            if prod.get("value"):
                lines.append(f"**Steel production:** {prod['value']:,} {prod.get('unit','')}  _{prod.get('note','')}_")
                lines.append("")

            lines += [COMMENT_PLACEHOLDER, ""]

    lines += ["---", "",
              "*End of review document.*", ""]


# ─── HTML wrapper ─────────────────────────────────────────────────────────────

HTML_STYLE = """
<style>
  body { font-family: Segoe UI, Arial, sans-serif; max-width: 1300px;
         margin: 40px auto; padding: 0 24px; font-size: 13.5px; color: #1a1a1a; }
  h1   { font-size: 22px; border-bottom: 3px solid #333; padding-bottom: 6px; }
  h2   { font-size: 17px; margin-top: 36px; border-bottom: 2px solid #ccc; padding-bottom: 4px; }
  h3   { font-size: 14px; margin-top: 24px; color: #333; }
  h4   { font-size: 13px; margin-top: 16px; color: #555; }
  table { border-collapse: collapse; width: 100%; margin: 10px 0 18px; font-size: 13px; }
  th   { background: #2c3e50; color: #fff; padding: 7px 10px; text-align: left; }
  td   { border: 1px solid #ddd; padding: 6px 10px; }
  tr:nth-child(even) td { background: #f7f7f7; }
  blockquote { background: #fffbea; border-left: 4px solid #f0a500;
               margin: 8px 0 18px; padding: 8px 14px; font-style: italic; color: #555; }
  code { background: #eef; padding: 1px 5px; border-radius: 3px; font-size: 12px; }
  hr   { border: none; border-top: 1px solid #ddd; margin: 28px 0; }
  ul   { margin: 4px 0; padding-left: 20px; }
  li   { margin-bottom: 3px; }
</style>
"""


def to_html(md_text):
    body = md_lib.markdown(md_text, extensions=["tables", "fenced_code"])
    return f"<!DOCTYPE html>\n<html><head><meta charset='utf-8'>{HTML_STYLE}</head><body>\n{body}\n</body></html>"


# ─── main ─────────────────────────────────────────────────────────────────────

def main():
    print("Loading data...")
    company_data_map = {cid: load(cid) for cid, _ in COMPANIES}
    val = load_validation()

    lines = []
    write_header(lines)
    write_reporting_basis(lines, company_data_map)
    write_validation_summary(lines, val)
    write_patches(lines, company_data_map)
    write_key_metrics(lines, company_data_map)
    write_enrichment(lines)

    md_text = "\n".join(lines)

    OUT_MD.parent.mkdir(exist_ok=True)
    OUT_MD.write_text(md_text, encoding="utf-8")
    print(f"Markdown: {OUT_MD}")

    OUT_HTML.write_text(to_html(md_text), encoding="utf-8")
    print(f"HTML:     {OUT_HTML}")
    print("\nOpen HTML in browser, or open MD in VS Code and use Ctrl+Shift+V for preview.")
    print('Add your comments after the "> YOUR COMMENT:" lines, save, then tell Claude to read the file.')

if __name__ == "__main__":
    main()
