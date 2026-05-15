import json
from collections import defaultdict
import os

with open('parser/validation_report.json') as f:
    report = json.load(f)
with open('dashboard/src/data/indicators.json') as f:
    ind = json.load(f)

company_data = {}
for cid in ['tata-steel', 'jsw-steel', 'sail', 'jindal-stainless']:
    path = f'dashboard/src/data/companies/{cid}.json'
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            company_data[cid] = json.load(f)

peer_all = report['peerOutliers']
self_all = report['selfOutliers']

ALWAYS_EXCLUDE = {
    'AnyIndependentAssessmentOrEvaluationOrAssuranceHasBeenCarriedOutByAnExternalAgencyForWaterWithdrawal',
    'IndicateIfAnyIndependentAssessmentOrEvaluationOrAssuranceHasBeenCarriedOutByAnExternalAgencyForAirEmissionsOtherThanGHGEmissions',
    'WhetherAnyIndependentAssessmentOrEvaluationOrAssuranceHasBeenCarriedOutByAnExternalAgencyForWasteManagement',
    'WhetherAnyIndependentAssessmentOrEvaluationOrAssuranceHasBeenCarriedOutByAnExternalAgencyForWaterDischarged',
    'NumberOfFemaleKeyManagementPersonnel',
}

def is_assurer_tag(tag):
    return 'IsAssuredByAssurer' in tag or tag.startswith('AssurerHasAssured')

def get_label(tag):
    return ind.get(tag, {}).get('label', tag)

def get_unit(tag, rawUnit=None):
    if rawUnit and str(rawUnit) not in ('null', 'None', ''):
        return rawUnit
    u = ind.get(tag, {}).get('standardUnit')
    return u if u else '?'

def get_company_value(cid, year, tag):
    try:
        return company_data[cid]['years'][year].get(tag, {})
    except Exception:
        return {}

by_cy = defaultdict(lambda: {'peer': {}, 'self': {}, 'assurer_changes': []})

for o in peer_all:
    tag = o['tag']
    if tag in ALWAYS_EXCLUDE:
        continue
    if is_assurer_tag(tag):
        by_cy[(o['company'], o['year'])]['assurer_changes'].append(o['year'])
        continue
    key = (o['company'], o['year'])
    if tag not in by_cy[key]['peer'] or o['ratio'] > by_cy[key]['peer'][tag]['ratio']:
        by_cy[key]['peer'][tag] = o

for o in self_all:
    tag = o['tag']
    if tag in ALWAYS_EXCLUDE:
        continue
    if is_assurer_tag(tag):
        year = o['yearTo']
        by_cy[(o['company'], year)]['assurer_changes'].append(f"{o['yearFrom']}->{o['yearTo']}")
        continue
    year = o['yearTo']
    key = (o['company'], year)
    if tag not in by_cy[key]['peer']:
        if tag not in by_cy[key]['self'] or abs(o.get('changePct', 0)) > abs(by_cy[key]['self'][tag].get('changePct', 0)):
            by_cy[key]['self'][tag] = o

COMPANY_META = {
    'tata-steel': {
        'name': 'Tata Steel Limited',
        'sector': 'Integrated carbon steel (blast furnace - basic oxygen furnace)',
        'pdf_prefix': 'TATA STEEL',
        'basis': {
            'FY2023': 'CONSOLIDATED (includes Tata Steel Netherlands, Tata Steel UK, and all Indian subsidiaries)',
            'FY2024': 'STANDALONE (India operations only)',
            'FY2025': 'STANDALONE (India operations only)',
        },
        'production': {'FY2023': '28,180,000 MT', 'FY2024': '20,120,000 MT', 'FY2025': '21,710,000 MT'},
    },
    'jsw-steel': {
        'name': 'JSW Steel Limited',
        'sector': 'Integrated carbon steel (blast furnace - basic oxygen furnace)',
        'pdf_prefix': 'JSW STEEL',
        'basis': {'FY2023': 'STANDALONE', 'FY2024': 'STANDALONE', 'FY2025': 'STANDALONE'},
        'production': {'FY2023': '24,150,000 MT', 'FY2024': '26,430,000 MT', 'FY2025': '27,790,000 MT'},
    },
    'sail': {
        'name': 'SAIL - Steel Authority of India Limited',
        'sector': 'Integrated carbon steel (blast furnace - basic oxygen furnace), PSU',
        'pdf_prefix': 'SAIL',
        'basis': {'FY2023': 'STANDALONE', 'FY2024': 'STANDALONE', 'FY2025': 'STANDALONE'},
        'production': {'FY2023': '18,290,000 MT', 'FY2024': '19,240,000 MT', 'FY2025': '19,170,000 MT'},
    },
    'jindal-stainless': {
        'name': 'Jindal Stainless Limited',
        'sector': 'Stainless steel (electric arc furnace), mid-cap (~10x smaller than Tata/JSW/SAIL)',
        'pdf_prefix': 'JINDAL STAINLESS',
        'basis': {'FY2023': 'STANDALONE', 'FY2024': 'STANDALONE', 'FY2025': 'STANDALONE'},
        'production': {'FY2023': '1,710,000 MT', 'FY2024': '2,080,000 MT', 'FY2025': '2,430,000 MT'},
    },
}

YEAR_LABEL = {
    'FY2023': 'April 2022 - March 2023',
    'FY2024': 'April 2023 - March 2024',
    'FY2025': 'April 2024 - March 2025',
}
YEAR_SHORT = {'FY2023': 'FY23', 'FY2024': 'FY24', 'FY2025': 'FY25'}


def build_prompt(cid, year):
    meta = COMPANY_META[cid]
    key = (cid, year)
    p_items = sorted(by_cy[key]['peer'].values(), key=lambda x: get_label(x['tag']))
    s_items = sorted(by_cy[key]['self'].values(), key=lambda x: get_label(x['tag']))
    has_assurer = len(by_cy[key]['assurer_changes']) > 0

    L = []

    L.append(f'# BRSR XBRL Outlier Verification')
    L.append(f'# Company: {meta["name"]}')
    L.append(f'# Year: {year} ({YEAR_LABEL[year]})')
    L.append(f'# PDF to upload: "{meta["pdf_prefix"]} {YEAR_SHORT[year]}.pdf"')
    L.append(f'# Also read: gemini_outlier_check_COMMON_INSTRUCTIONS.md (paste that first, then this)')
    L.append('')
    L.append('---')
    L.append('')
    L.append('## Company context')
    L.append('')
    L.append(f'- **Reporting basis:** {meta["basis"][year]}')
    L.append(f'- **Crude steel production this year:** {meta["production"][year]}')
    L.append(f'- **Sector:** {meta["sector"]}')
    L.append('')

    if cid == 'tata-steel' and year == 'FY2023':
        L.append('> **Important:** FY2023 is Consolidated. Tata Steel absolute volumes (water, waste, energy) are legitimately larger than standalone peers because they include European plants. Flag only if values seem wrong even after accounting for consolidated scope.')
    elif cid == 'tata-steel':
        L.append('> **Important:** FY2024 and FY2025 are Standalone (India only). Large drops from FY2023 figures are expected due to the Consolidated to Standalone basis change, not data errors.')
    elif cid == 'sail':
        L.append('> **Note:** SAIL is a PSU. Air emissions FY2023 were in mg/Nm3 concentration units (non-comparable with peers). FY2024/FY2025 switched to kg/tcs mass intensity. Wages may be reported in absolute INR rather than INR Crore - check units carefully.')
    elif cid == 'jindal-stainless':
        L.append('> **Note:** Jindal Stainless is ~10x smaller than Tata/JSW/SAIL and uses electric arc furnace (not blast furnace). Lower absolute volumes for water, energy, and waste are expected. Intensity metrics (per tonne, per rupee) should still be broadly comparable.')

    L.append('')
    L.append('---')
    L.append('')
    L.append('## Checklist')
    L.append('')
    L.append('Verify every item below. Do not skip any item. For each, find the value in the PDF and give a verdict.')
    L.append('')

    item_num = 0

    # Section A: peer outliers
    if p_items:
        L.append('### Section A - Peer outliers')
        L.append('')
        L.append('Our value is compared to the median of the other 3 companies for the same metric and same year.')
        L.append('')

        for o in p_items:
            item_num += 1
            tag = o['tag']
            label = get_label(tag)
            std_unit = get_unit(tag)  # always use standardUnit for display
            our_val = o['value']
            peer_med = o['peerMedian']
            ratio = o['ratio']
            cause = o.get('suspectedCause', '')
            cv = get_company_value(cid, year, tag)
            unit_warn = cv.get('unitWarning')
            raw_val = cv.get('rawValue')
            raw_unit = cv.get('rawUnit')

            if ratio >= 1:
                direction = f'{ratio:.1f}x higher than peer median of {peer_med:,.4g} {std_unit}'
            elif ratio > 0:
                inv = 1.0 / ratio
                direction = f'{inv:.1f}x lower than peer median of {peer_med:,.4g} {std_unit}'
            else:
                direction = f'vs peer median of {peer_med:,.4g} {std_unit} (our value is near zero)'

            L.append(f'**ITEM_{item_num}**')
            L.append(f'- Tag: `{tag}`')
            L.append(f'- Metric: {label}')
            L.append(f'- Our normalized value: **{our_val:,.6g} {std_unit}**')
            # Show raw XBRL value if unit differs from standard (so Gemini knows what the PDF will show)
            if raw_val is not None and raw_unit and str(raw_unit) not in ('null', 'None', '', str(std_unit)):
                L.append(f'- Raw value in PDF/XBRL: {raw_val} {raw_unit} (we converted to {std_unit})')
            L.append(f'- Peer comparison: {direction}')
            if unit_warn:
                L.append(f'- Unit warning from parser: {unit_warn}')
            if cause:
                L.append(f'- Suspected cause: {cause}')
            L.append(f'- Task: Find this metric in the PDF and confirm or correct the value.')
            L.append('')

    # Section B: self-outliers
    if s_items:
        L.append('### Section B - Year-over-year outliers')
        L.append('')
        L.append('These values changed dramatically from the prior year. Verify the current year value is correct.')
        L.append('')

        for o in s_items:
            item_num += 1
            tag = o['tag']
            label = get_label(tag)
            std_unit = get_unit(tag)
            yr_from = o['yearFrom']
            yr_to = o['yearTo']
            val_from = o['valueFrom']
            val_to = o['valueTo']
            chg = o.get('changePct', 0)
            # Get raw value for the TO year (the year being verified)
            cv_to = get_company_value(cid, yr_to, tag)
            raw_val_to = cv_to.get('rawValue')
            raw_unit_to = cv_to.get('rawUnit')

            L.append(f'**ITEM_{item_num}**')
            L.append(f'- Tag: `{tag}`')
            L.append(f'- Metric: {label}')
            L.append(f'- Change: {val_from:,.6g} {std_unit} ({yr_from}) -> {val_to:,.6g} {std_unit} ({yr_to}), change = {chg:+.0f}%')
            if raw_val_to is not None and raw_unit_to and str(raw_unit_to) not in ('null', 'None', '', str(std_unit)):
                L.append(f'- Raw value in PDF/XBRL for {yr_to}: {raw_val_to} {raw_unit_to} (we converted to {std_unit})')
            L.append(f'- Task: Verify the {yr_to} value ({val_to:,.6g} {std_unit}) in the PDF. Is this correct?')
            L.append('')

    # Section C: assurer
    if has_assurer:
        item_num += 1
        L.append('### Section C - External assurance')
        L.append('')
        L.append(f'**ITEM_{item_num}**')
        L.append(f'- Issue: XBRL data shows a change in external assurance coverage in {year}')
        L.append(f'- Task: Find the external assurance statement in the PDF (usually at the start or end of the BRSR).')
        L.append(f'  - Was this BRSR externally assured for {year}?')
        L.append(f'  - If yes: who was the assurer, what level (reasonable / limited), and what scope?')
        L.append(f'  - If no: confirm the BRSR was not externally assured.')
        L.append('')

    # Section D: training
    item_num += 1
    L.append('### Section D - Training coverage')
    L.append('')
    L.append(f'**ITEM_{item_num}**')
    L.append(f'- Issue: Training coverage % is absent from XBRL for ALL companies in ALL years. Must be extracted from PDF.')
    L.append(f'- Look in: Principle 3 training tables, HR metrics, workforce development section, "Training and Awareness Programs"')
    L.append(f'- Extract all of the following that are present:')
    L.append(f'  - % permanent employees trained on health and safety')
    L.append(f'  - % permanent employees trained on skill upgradation')
    L.append(f'  - % permanent workers trained on health and safety')
    L.append(f'  - % permanent workers trained on skill upgradation')
    L.append(f'  - Average training hours per employee')
    L.append(f'  - Total training person-hours')
    L.append(f'- If the training table reports number trained rather than %, also provide the denominator (total headcount) so % can be calculated.')
    L.append('')

    # Output format
    L.append('---')
    L.append('')
    L.append('## Required output')
    L.append('')
    L.append(f'Respond with exactly {item_num} lines. Use this format from COMMON_INSTRUCTIONS.md:')
    L.append('')
    L.append('```')
    for i in range(1, item_num + 1):
        L.append(f'ITEM_{i} | VERDICT | PDF_VALUE | PAGE_OR_SECTION | NOTE')
    L.append('```')
    L.append('')
    L.append('Verdicts: CONFIRMED / CORRECTED / UNIT_ERROR / EXPECTED / NOT_FOUND / ZERO_REPORTED')
    L.append('For CORRECTED and UNIT_ERROR: always write the correct value AND its unit in PDF_VALUE.')
    L.append('For the training item: use FOUND / NOT_FOUND / NOT_REPORTED, and list all values found in PDF_VALUE.')

    return '\n'.join(L)


os.makedirs('parser/PDF cross check/prompts', exist_ok=True)

companies = ['tata-steel', 'jsw-steel', 'sail', 'jindal-stainless']
years = ['FY2023', 'FY2024', 'FY2025']

for c in companies:
    for y in years:
        content = build_prompt(c, y)
        fname = f'parser/PDF cross check/prompts/gemini_outlier_check_{c}-{y}.md'
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        key = (c, y)
        p = len(by_cy[key]['peer'])
        s = len(by_cy[key]['self'])
        has_a = len(by_cy[key]['assurer_changes']) > 0
        total = p + s + (1 if has_a else 0) + 1
        print(f'Written: {fname}  ({p} peer + {s} self + {"1 assurer" if has_a else "0 assurer"} + 1 training = {total} items)')
