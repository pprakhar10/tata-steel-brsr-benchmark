export default function AboutPanel() {
  return (
    <div className="flex flex-col gap-8">
      <div>
        <h2 className="text-2xl font-bold text-gray-900 mb-1">About</h2>
        <p className="text-sm text-gray-500">About this tool and how to get help.</p>
      </div>

      {/* About the tool */}
      <div className="bg-white rounded-xl border border-gray-200 shadow-sm p-6 flex flex-col gap-3">
        <h3 className="font-semibold text-gray-900 text-base">Steel BRSR Benchmark</h3>
        <p className="text-sm text-gray-700 leading-relaxed">
          This dashboard compares Business Responsibility and Sustainability Report (BRSR) disclosures
          across four Indian steel companies — Tata Steel, JSW Steel, SAIL, and Jindal Stainless —
          spanning FY2022-23 to FY2024-25.
        </p>
        <p className="text-sm text-gray-700 leading-relaxed">
          Data is sourced from company XBRL filings and PDF BRSR reports, cross-verified, and enriched
          with AI-generated analysis covering 98 ESG indicators across Environmental, Social, and
          Governance dimensions. Note that minor differences between XBRL and PDF figures may occur due to rounding or varying
          decimal precision in each filing format which may result in values used in the Benchmarking
          tool not matching exactly with the PDF version of BRSR reports.
        </p>
        <div className="mt-2 pt-4 border-t border-gray-100 flex items-center gap-3">
          <div className="w-9 h-9 rounded-full bg-indigo-100 flex items-center justify-center shrink-0">
            <span className="text-indigo-700 font-bold text-sm">TS</span>
          </div>
          <div>
            <p className="text-sm font-semibold text-gray-900">Corporate Sustainability, Tata Steel</p>
            <p className="text-xs text-gray-400">Developed internally for benchmarking and analysis</p>
          </div>
        </div>
      </div>

      {/* Help & feedback */}
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
          When flagging an inaccuracy, please mention the indicator name, the company, the financial year,
          and the value you believe is incorrect — along with a source reference if available.
        </p>
      </div>
    </div>
  )
}
