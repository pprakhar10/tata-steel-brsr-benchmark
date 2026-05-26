// Red-box overlay helper — boxes are percentage-based so they scale with any image size
interface Box { top: string; left: string; width: string; height: string }

function AnnotatedImage({
  src, alt, caption, boxes,
}: {
  src: string
  alt: string
  caption?: string
  boxes: Box[]
}) {
  return (
    <div className="flex flex-col gap-1.5">
      <div className="relative rounded-lg overflow-hidden border border-gray-200 shadow-sm bg-gray-50">
        <img src={src} alt={alt} className="w-full block" />
        {boxes.map((box, i) => (
          <div
            key={i}
            style={{
              position: 'absolute',
              top: box.top,
              left: box.left,
              width: box.width,
              height: box.height,
              border: '2.5px solid #ef4444',
              borderRadius: '5px',
              pointerEvents: 'none',
              boxShadow: '0 0 0 2px rgba(239,68,68,0.15)',
            }}
          />
        ))}
      </div>
      {caption && (
        <p className="text-xs text-gray-400 text-center italic">{caption}</p>
      )}
    </div>
  )
}

function SectionDivider() {
  return <div className="border-t border-gray-100" />
}

export default function AboutPanel() {
  return (
    <div className="flex flex-col gap-8">

      {/* Page title */}
      <div>
        <h2 className="text-2xl font-bold text-gray-900 mb-1">How to use & Help</h2>
        <p className="text-sm text-gray-500">Guide to using this tool and how to get help.</p>
      </div>

      {/* ── About the Tool ─────────────────────────────────────── */}
      <div className="bg-white rounded-xl border border-gray-200 shadow-sm p-6 flex flex-col gap-4">
        <h3 className="font-semibold text-gray-900 text-base">About this Tool</h3>
        <p className="text-sm text-gray-700 leading-relaxed">
          This dashboard compares Business Responsibility and Sustainability Report (BRSR) disclosures
          across four Indian steel companies — Tata Steel, JSW Steel, SAIL, and Jindal Stainless —
          spanning FY2022-23 to FY2024-25.
        </p>
        <p className="text-sm text-gray-700 leading-relaxed">
          Data is sourced from company XBRL filings and PDF BRSR reports, cross-verified, and enriched
          with AI-generated analysis covering 98 ESG indicators across Environmental, Social, and
          Governance dimensions. Minor differences between XBRL and PDF figures may occur due to
          rounding or varying decimal precision, which may result in values not matching exactly
          with the PDF version of BRSR reports.
        </p>

        {/* Standalone vs consolidated callout */}
        <div className="p-4 rounded-lg bg-amber-50 border border-amber-100">
          <p className="text-sm font-semibold text-amber-800 mb-1.5">Note on reporting basis</p>
          <p className="text-sm text-amber-700 leading-relaxed">
            Standalone entity values (e.g. Tata Steel Limited) have been prioritised across all
            indicators and all companies. Where standalone figures are not publicly disclosed,
            consolidated or group-level figures have been used instead. Any such instance is clearly
            noted in the <strong>Comparability Notes</strong> section of that indicator — accessible
            by clicking the <strong>"View insights"</strong> button at the bottom of each indicator card.
          </p>
        </div>

        <div className="pt-2 border-t border-gray-100 flex items-center gap-3">
          <div className="w-9 h-9 rounded-full bg-indigo-100 flex items-center justify-center shrink-0">
            <span className="text-indigo-700 font-bold text-sm">TS</span>
          </div>
          <div>
            <p className="text-sm font-semibold text-gray-900">Corporate Sustainability, Tata Steel</p>
            <p className="text-xs text-gray-400">Developed internally for benchmarking and analysis</p>
          </div>
        </div>
      </div>

      {/* ── How to Use ─────────────────────────────────────────── */}
      <div className="bg-white rounded-xl border border-gray-200 shadow-sm p-6 flex flex-col gap-8">
        <h3 className="font-semibold text-gray-900 text-base">How to Use</h3>

        {/* A — View Insights ───────────────────────────────────── */}
        <div className="flex flex-col gap-4">
          <p className="text-xs font-bold text-indigo-600 uppercase tracking-widest">Viewing Insights</p>
          <p className="text-sm text-gray-700 leading-relaxed">
            Every indicator card has a <strong>"View insights for…"</strong> button at the bottom
            (highlighted below). Clicking it opens an AI-generated analysis panel with five sections:
          </p>
          <ul className="flex flex-col gap-1 text-sm text-gray-700 list-disc list-inside leading-relaxed">
            <li><strong>Year-on-Year Trend</strong> — arrows showing whether each company improved or worsened year-on-year</li>
            <li><strong>About</strong> — what the metric measures and which direction is better</li>
            <li><strong>Performance & Drivers</strong> — what the data shows and why</li>
            <li><strong>Tata Positioning</strong> — where Tata Steel sits relative to peers</li>
            <li><strong>Targets & Programs</strong> — targets disclosed in each company's BRSR</li>
            <li><strong>Comparability Notes</strong> — caveats on reporting boundary (standalone vs. consolidated)</li>
          </ul>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <AnnotatedImage
              src="/screenshots/ss-insights-closed.png"
              alt="Indicator card showing the View Insights button at the bottom"
              caption='"View insights for…" button at the bottom of any indicator card'
              boxes={[{ top: '89%', left: '1%', width: '97%', height: '8%' }]}
            />
            <AnnotatedImage
              src="/screenshots/ss-insights-open.png"
              alt="Insights panel open — Hide insights button at top, Comparability Notes at bottom"
              caption="The open insights panel — Comparability Notes is at the bottom"
              boxes={[
                { top: '0.5%', left: '0.5%', width: '98%', height: '8.5%' },
                { top: '92%',  left: '0.5%', width: '98%', height: '7%'   },
              ]}
            />
          </div>
        </div>

        <SectionDivider />

        {/* B — Stacked Charts ──────────────────────────────────── */}
        <div className="flex flex-col gap-4">
          <p className="text-xs font-bold text-indigo-600 uppercase tracking-widest">Stacked Charts & Breakdown</p>
          <p className="text-sm text-gray-700 leading-relaxed">
            Indicators such as <strong>Total Waste Generated</strong>, <strong>Total Water Withdrawal</strong>,
            and <strong>Total Energy Consumed</strong> are composed of multiple sub-components.
            These cards show a <strong>Breakdown</strong> dropdown in the top-right corner with three modes:
          </p>
          <ul className="flex flex-col gap-1 text-sm text-gray-700 list-disc list-inside leading-relaxed">
            <li><strong>Stacked</strong> (default) — all sub-components stacked to show total composition for a selected year. Use the FY selector next to the dropdown to change the year.</li>
            <li><strong>Total</strong> — a grouped bar chart showing the aggregate across all three years</li>
            <li><strong>Individual sub-component</strong> (e.g. E-Waste, Plastic Waste) — drill into one sub-component across all three years for peer comparison</li>
          </ul>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <AnnotatedImage
              src="/screenshots/ss-stacked-closed.png"
              alt="Waste indicator card in default stacked view with Breakdown dropdown visible"
              caption="The Breakdown dropdown and FY selector in the top-right corner of the card"
              boxes={[{ top: '16%', left: '55%', width: '41%', height: '6%' }]}
            />
            <AnnotatedImage
              src="/screenshots/ss-stacked-open.png"
              alt="Breakdown dropdown open showing list of sub-components"
              caption="Click the dropdown to select a specific sub-component to drill into"
              boxes={[{ top: '13%', left: '63%', width: '30%', height: '38%' }]}
            />
          </div>
        </div>

        <SectionDivider />

        {/* C — Hover & Touch ───────────────────────────────────── */}
        <div className="flex flex-col gap-4">
          <p className="text-xs font-bold text-indigo-600 uppercase tracking-widest">Reading Chart Values</p>
          <p className="text-sm text-gray-700 leading-relaxed">
            Exact values for every company and year are always shown in the data table below each
            chart. To read values directly on the chart without scrolling down:
          </p>
          <ul className="flex flex-col gap-1 text-sm text-gray-700 list-disc list-inside leading-relaxed">
            <li><strong>Desktop</strong> — hover your cursor over any bar group. A tooltip appears showing all four companies' values for that year.</li>
            <li><strong>iPad / tablet</strong> — tap any bar to bring up the same tooltip. Tap elsewhere on the chart or screen to dismiss it.</li>
          </ul>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <AnnotatedImage
              src="/screenshots/ss-insights-closed.png"
              alt="Chart without tooltip — hover or tap the bar area to see values"
              caption="Hover (desktop) or tap (iPad) anywhere in the bar chart area"
              boxes={[{ top: '18%', left: '5%', width: '89%', height: '31%' }]}
            />
            <AnnotatedImage
              src="/screenshots/ss-tooltip.png"
              alt="Chart with tooltip showing all four company values for FY2022-23"
              caption="Tooltip showing exact values for all four companies in that year"
              boxes={[{ top: '22%', left: '14%', width: '50%', height: '28%' }]}
            />
          </div>
        </div>

        <SectionDivider />

        {/* D — Benchmark Tool ──────────────────────────────────── */}
        <div className="flex flex-col gap-4">
          <p className="text-xs font-bold text-indigo-600 uppercase tracking-widest">Benchmark Tool</p>
          <p className="text-sm text-gray-700 leading-relaxed">
            The <strong>Benchmark</strong> page (in the sidebar or bottom navigation) gives a
            summary view of where Tata Steel ranks across all 98 indicators for a selected year.
          </p>
          <ul className="flex flex-col gap-1 text-sm text-gray-700 list-disc list-inside leading-relaxed">
            <li>Select a <strong>financial year</strong> — FY2022-23 (base year), FY2023-24, or FY2024-25 (latest)</li>
            <li>Select a <strong>rank</strong> — #1 Leading, #2 Strong, #3 Moderate, or #4 Lagging</li>
            <li>The list below updates to show all indicators where Tata Steel holds that rank in that year</li>
            <li>Click any indicator row in the list to jump directly to that indicator in the ESG view</li>
          </ul>
          <AnnotatedImage
            src="/screenshots/ss-benchmark.png"
            alt="Benchmark tool showing financial year selector and rank selector"
            caption="Select a year (top) and a rank (below) to filter all 98 indicators"
            boxes={[
              { top: '17%', left: '32%', width: '62%', height: '12%' },
              { top: '34%', left: '32%', width: '62%', height: '14%' },
            ]}
          />
        </div>
      </div>

      {/* ── Help & Feedback ────────────────────────────────────── */}
      <div className="bg-white rounded-xl border border-gray-200 shadow-sm p-6 flex flex-col gap-4">
        <h3 className="font-semibold text-gray-900 text-base">Help & Feedback</h3>
        <p className="text-sm text-gray-700 leading-relaxed">
          For any queries, help with using this tool, or to flag inaccurate data or analysis,
          please write to the Corporate Sustainability team.
        </p>
        <div className="flex items-start gap-4 p-4 rounded-lg bg-indigo-50 border border-indigo-100">
          <div className="w-10 h-10 rounded-full bg-indigo-600 flex items-center justify-center shrink-0 mt-0.5">
            <span className="text-white font-bold text-sm">PP</span>
          </div>
          <div className="flex flex-col gap-1">
            <p className="font-semibold text-gray-900 text-sm">Mr. Prakhar Prateek</p>
            <p className="text-xs text-gray-500">Corporate Sustainability, Tata Steel</p>
            <a
              href="mailto:prakhar.prateek@tatasteel.com"
              className="text-sm text-indigo-600 hover:text-indigo-800 font-medium mt-1 transition-colors"
            >
              prakhar.prateek@tatasteel.com
            </a>
          </div>
        </div>
        <p className="text-xs text-gray-400 leading-relaxed">
          When flagging an inaccuracy, please mention the indicator name, the company, the financial
          year, and the value you believe is incorrect — along with a source reference if available.
        </p>
      </div>

    </div>
  )
}
