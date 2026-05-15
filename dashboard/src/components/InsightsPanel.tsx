import { useState } from 'react'
import { INDICATOR_ANALYSIS, COMPANY_DATA } from '../data/loader'
import { COMPANY_KEYS, COMPANY_LABELS, COMPANY_IDS, FY_DISPLAY, type CompanyYearData, type ValueObject } from '../types/data'
import { computeTrend, type TrendResult } from '../utils/trend'

interface Props {
  tag: string
}

function isMeta(v: unknown): v is { reportingBasis: string; basisWarning: string | null } {
  return typeof v === 'object' && v !== null && 'reportingBasis' in v
}

function getNumericValue(yearData: CompanyYearData | undefined, tag: string): number | null {
  if (!yearData) return null
  const v = yearData[tag]
  if (!v || isMeta(v)) return null
  return (v as ValueObject).value ?? null
}

const TREND_ICON: Record<TrendResult, { icon: string; cls: string }> = {
  up: { icon: '▲', cls: 'bg-emerald-100 text-emerald-700 ring-1 ring-emerald-300' },
  down: { icon: '▼', cls: 'bg-red-100 text-red-700 ring-1 ring-red-300' },
  flat: { icon: '●', cls: 'bg-gray-100 text-gray-500' },
  nodata: { icon: '—', cls: 'bg-gray-50 text-gray-400' },
}

const FLAG_LABELS: Record<string, string> = {
  directionUnclear: 'Direction Unclear',
  contextInsufficient: 'Context Insufficient',
  externalSourceUsed: 'External Source Used',
  trendAmbiguity: 'Trend Ambiguity',
}

const SECTION_LABELS: Record<string, string> = {
  about: 'About',
  performanceAndDrivers: 'Performance & Drivers',
  tataPositioning: 'Tata Positioning',
  targets: 'Targets & Programs',
  comparabilityNotes: 'Comparability Notes',
}

export default function InsightsPanel({ tag }: Props) {
  const [open, setOpen] = useState(false)
  const analysis = INDICATOR_ANALYSIS[tag]
  if (!analysis) return null

  const activeFlags = Object.entries(analysis.flags)
    .filter(([k, v]) => k !== 'flagNote' && v === true)
    .map(([k]) => k)

  return (
    <div className="mt-5 border-t border-gray-100 pt-4 pb-4">
      <button
        onClick={() => setOpen(o => !o)}
        className="w-full flex items-center justify-between px-4 py-3 text-left bg-indigo-50 border border-indigo-200 rounded-lg hover:bg-indigo-100 transition-colors"
      >
        <div>
          <div className="text-sm font-semibold text-indigo-700">
            {open ? 'Hide insights for' : 'View insights for'} {analysis.label}
          </div>
          <div className="text-xs text-indigo-400 mt-0.5">
            Trends, ranking changes and key observations
          </div>
        </div>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          className={`w-4 h-4 text-indigo-400 flex-shrink-0 ml-3 transition-transform duration-200 ${open ? 'rotate-180' : ''}`}
        >
          <path fillRule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clipRule="evenodd" />
        </svg>
      </button>

      {open && (
        <div className="pt-3 pb-3 px-1 flex flex-col gap-4">
          {/* Flag badges */}
          {activeFlags.length > 0 && (
            <div className="flex flex-wrap gap-2">
              {activeFlags.map(flag => (
                <span key={flag} className="px-2 py-1 rounded-full text-xs bg-amber-100 text-amber-800 font-medium ring-1 ring-amber-300">
                  ⚠ {FLAG_LABELS[flag] ?? flag}
                </span>
              ))}
            </div>
          )}

          {/* Trend table — FY2024 and FY2025 only; FY2023 is base year with no prior to compare */}
          <div>
            <div className="text-xs font-semibold text-gray-500 uppercase tracking-wide mb-2">Year-on-Year Trend</div>
            <div className="overflow-x-auto">
              <table className="w-full text-sm">
                <thead>
                  <tr className="border-b border-gray-100">
                    <th className="text-left py-1 pr-3 text-gray-400 font-medium text-xs w-16">Company</th>
                    {(['FY2024', 'FY2025'] as const).map(fy => (
                      <th key={fy} className="text-center py-1 px-2 text-gray-400 font-medium text-xs">{FY_DISPLAY[fy]}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {COMPANY_KEYS.map(key => {
                    const companyId = COMPANY_IDS[key]
                    const company = COMPANY_DATA[companyId]
                    const val23 = getNumericValue(company?.years['FY2023'], tag)
                    const val24 = getNumericValue(company?.years['FY2024'], tag)
                    const val25 = getNumericValue(company?.years['FY2025'], tag)

                    return (
                      <tr key={key} className="border-b border-gray-50 last:border-0">
                        <td className="py-1.5 pr-3 text-gray-600 text-xs font-medium">{COMPANY_LABELS[key]}</td>
                        {([
                          computeTrend(val24, val23, analysis.direction),
                          computeTrend(val25, val24, analysis.direction),
                        ] as TrendResult[]).map((result, i) => {
                          const fy = i === 0 ? 'FY2024' : 'FY2025'
                          const { icon, cls } = TREND_ICON[result]
                          return (
                            <td key={fy} className="text-center py-1.5 px-2">
                              <span className={`inline-flex items-center justify-center px-2 py-0.5 rounded-full text-xs font-semibold ${cls}`}>
                                {icon}
                              </span>
                            </td>
                          )
                        })}
                      </tr>
                    )
                  })}
                </tbody>
              </table>
            </div>
            <div className="mt-1.5 text-xs text-gray-400 flex gap-4 items-center">
              <span className="flex items-center gap-1"><span className="inline-flex items-center justify-center px-1.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-100 text-emerald-700 ring-1 ring-emerald-300">▲</span> Improved</span>
              <span className="flex items-center gap-1"><span className="inline-flex items-center justify-center px-1.5 py-0.5 rounded-full text-xs font-semibold bg-red-100 text-red-700 ring-1 ring-red-300">▼</span> Worsened</span>
              <span className="flex items-center gap-1"><span className="inline-flex items-center justify-center px-1.5 py-0.5 rounded-full text-xs font-semibold bg-gray-100 text-gray-500">●</span> No change</span>
              <span className="flex items-center gap-1"><span className="inline-flex items-center justify-center px-1.5 py-0.5 rounded-full text-xs font-semibold bg-gray-50 text-gray-400">—</span> No data</span>
            </div>
          </div>

          {/* AI sections */}
          {(Object.entries(SECTION_LABELS) as [keyof typeof SECTION_LABELS, string][]).map(([key, label]) => {
            const text = analysis.sections[key as keyof typeof analysis.sections]
            if (!text) return null
            return (
              <div key={key}>
                <div className="text-xs font-semibold text-gray-500 uppercase tracking-wide mb-1">{label}</div>
                <p className="text-sm text-gray-700 leading-relaxed">{text}</p>
              </div>
            )
          })}
        </div>
      )}
    </div>
  )
}
