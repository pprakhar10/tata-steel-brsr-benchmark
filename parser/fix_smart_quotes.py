import pathlib, json

files = [
    'dashboard/src/data/analysis/indicators/NumberOfTradingHousesWherePurchasesAreMade.json',
    'dashboard/src/data/analysis/indicators/PercentageOfInvestmentsInRelatedPartiesInTotalInvestments.json',
]

# Smart quote characters and their ASCII replacements
REPLACEMENTS = [
    ('“', '"'),  # left double quotation mark
    ('”', '"'),  # right double quotation mark
    ('‘', "'"),  # left single quotation mark
    ('’', "'"),  # right single quotation mark
]

base = pathlib.Path('.')
for fpath in files:
    f = base / fpath
    text = f.read_text(encoding='utf-8')
    count = sum(text.count(ch) for ch, _ in REPLACEMENTS)
    for ch, repl in REPLACEMENTS:
        text = text.replace(ch, repl)
    f.write_text(text, encoding='utf-8')
    print(f'Fixed {fpath}: {count} smart-quote chars replaced')

# Verify all 98 files now parse
bad = []
for f in pathlib.Path('dashboard/src/data/analysis/indicators').glob('*.json'):
    try:
        json.loads(f.read_text(encoding='utf-8'))
    except Exception as e:
        bad.append((f.name, str(e)))

if bad:
    print(f'\nStill broken ({len(bad)}):')
    for name, err in bad:
        print(f'  {name} -> {err}')
else:
    print(f'\nAll indicator JSON files parse cleanly.')
