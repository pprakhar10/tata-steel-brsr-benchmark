import { COMPANY_DATA } from '../data/loader'
import { INDICATOR_ANALYSIS } from '../data/loader'
import { COMPANY_KEYS, COMPANY_LABELS, COMPANY_IDS, FY_LABELS, FY_DISPLAY, type CompanyYearData, type ValueObject } from '../types/data'
import { formatValue } from '../utils/format'
import { detectTies } from '../utils/ranks'
import { ESG_MAP } from '../constants/esgMap'
import RankBadge from './RankBadge'

interface Props {
  tag: string
}

function isMeta(v: unknown): v is { reportingBasis: string; basisWarning: string | null } {
  return typeof v === 'object' && v !== null && 'reportingBasis' in v
}

function getValueObj(yearData: CompanyYearData, tag: string): ValueObject | null {
  const v = yearData[tag]
  if (!v || isMeta(v)) return null
  return v as ValueObject
}

export default function DataTable({ tag }: Props) {
  const analysis = INDICATOR_ANALYSIS[tag]
  const isPct = ESG_MAP[tag]?.unit === '%'

  const hasMillions = COMPANY_KEYS.some(key => {
    const company = COMPANY_DATA[COMPANY_IDS[key]]
    return FY_LABELS.some(fy => {
      const vObj = company?.years[fy] ? getValueObj(company.years[fy]!, tag) : null
      return vObj?.value != null && Math.abs(vObj.value) >= 1_000_000
    })
  })

  return (
    <div className="overflow-x-auto">
      <table className="w-full text-sm border-collapse">
        <thead>
          <tr className="border-b border-gray-200">
            <th className="text-left py-2 pr-4 text-gray-500 font-medium w-28">Company</th>
            {FY_LABELS.map(fy => (
              <th key={fy} className="text-right py-2 px-3 text-gray-500 font-medium">{FY_DISPLAY[fy]}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {COMPANY_KEYS.map(key => {
            const companyId = COMPANY_IDS[key]
            const company = COMPANY_DATA[companyId]
            return (
              <tr key={key} className="border-b border-gray-100 last:border-0">
                <td className="py-2 pr-4 text-gray-700 font-medium">{COMPANY_LABELS[key]}</td>
                {FY_LABELS.map(fy => {
                  const yearData = company?.years[fy]
                  const vObj = yearData ? getValueObj(yearData, tag) : null
                  const rank = analysis?.peerRank[fy][key] ?? null
                  const tied = analysis ? detectTies(analysis.peerRank[fy]) : new Set()

                  return (
                    <td key={fy} className="py-2 px-3 text-right">
                      {vObj && vObj.value != null ? (
                        <div className="flex flex-row items-center justify-end gap-2">
                          <span className="text-gray-900">
                            {formatValue(vObj, hasMillions)}{isPct ? '%' : ''}
                          </span>
                          {rank != null && (
                            <RankBadge
                              rank={rank}
                              isTied={tied.has(key)}
                              companyLabel=""
                            />
                          )}
                        </div>
                      ) : (
                        <span className="text-gray-300">—</span>
                      )}
                    </td>
                  )
                })}
              </tr>
            )
          })}
        </tbody>
      </table>
      <p className="mt-1.5 text-xs text-gray-400">
        {hasMillions && 'M = million  ·  '}#1–#4 = peer rank (1 = best)
      </p>
    </div>
  )
}
