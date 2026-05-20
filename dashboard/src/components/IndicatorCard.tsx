import { useState, useEffect, useRef } from 'react'
import { ESG_MAP, COMPOSITE_INDICATORS } from '../constants/esgMap'
import { INDICATOR_ANALYSIS } from '../data/loader'
import { type FY } from '../types/data'
import { formatUnitFull } from '../utils/format'
import DataTable from './DataTable'
import ChartPanel from './ChartPanel'
import InsightsPanel from './InsightsPanel'

interface Props {
  tag: string
  highlight?: boolean
  activeSubTag?: string | null
}

const FY_OPTIONS: FY[] = ['FY2023', 'FY2024', 'FY2025']
const FY_DISPLAY: Record<FY, string> = {
  FY2023: 'FY2022-23',
  FY2024: 'FY2023-24',
  FY2025: 'FY2024-25',
}

export default function IndicatorCard({ tag, highlight, activeSubTag }: Props) {
  const entry = ESG_MAP[tag]
  const analysis = INDICATOR_ANALYSIS[tag]
  const cardRef = useRef<HTMLDivElement>(null)
  const [flashing, setFlashing] = useState(false)

  const isStacked = entry?.chartPattern === 'stacked'
  const [selectedView, setSelectedView] = useState<string>('stacked')
  const [selectedFY, setSelectedFY] = useState<FY>('FY2025')

  useEffect(() => {
    if (highlight) {
      setFlashing(true)
      const t = setTimeout(() => setFlashing(false), 1500)
      return () => clearTimeout(t)
    }
  }, [highlight])

  useEffect(() => {
    if (activeSubTag && isStacked) setSelectedView(activeSubTag)
  }, [activeSubTag, isStacked])

  if (!entry || !analysis) return null

  const insightsTag =
    isStacked && selectedView !== 'stacked' && selectedView !== 'total'
      ? selectedView
      : tag

  const subcomps = isStacked ? (COMPOSITE_INDICATORS[tag] ?? []) : []

  return (
    <div
      id={tag}
      ref={cardRef}
      className={`bg-white rounded-xl border shadow-sm transition-all duration-300 ${flashing ? 'ring-4 ring-yellow-400 bg-yellow-50' : 'border-gray-200'}`}
    >
      {/* Card header */}
      <div className="px-5 pt-4 pb-3 border-b border-gray-100">
        <div className="flex items-start justify-between gap-4">
          <div>
            <h3 className="font-semibold text-gray-900">
              {entry.label}
              {isStacked && selectedView !== 'stacked' && selectedView !== 'total' && (
                <span className="text-gray-400 font-normal"> — {ESG_MAP[selectedView]?.label ?? selectedView}</span>
              )}
            </h3>
            {entry.unit && <span className="text-xs text-gray-400">{formatUnitFull(entry.unit)}</span>}
          </div>
          {isStacked && (
            <div className="flex items-center gap-2 shrink-0">
              <span className="text-xs text-indigo-500 font-medium">Breakdown:</span>
              <select
                value={selectedView}
                onChange={e => setSelectedView(e.target.value)}
                className="text-xs border border-indigo-200 rounded px-2 py-1 bg-indigo-50 text-indigo-700 font-medium focus:outline-none focus:ring-2 focus:ring-indigo-400"
              >
                <option value="stacked">Stacked</option>
                <option value="total">Total</option>
                {subcomps.map(st => (
                  <option key={st} value={st}>{ESG_MAP[st]?.label ?? st}</option>
                ))}
              </select>
              {selectedView === 'stacked' && (
                <select
                  value={selectedFY}
                  onChange={e => setSelectedFY(e.target.value as FY)}
                  className="text-xs border border-gray-200 rounded px-2 py-1 bg-white text-gray-700 focus:outline-none focus:ring-2 focus:ring-indigo-400"
                >
                  {FY_OPTIONS.map(fy => (
                    <option key={fy} value={fy}>{FY_DISPLAY[fy]}</option>
                  ))}
                </select>
              )}
            </div>
          )}
        </div>
      </div>

      {/* Chart */}
      {entry.chartPattern !== 'none' && (
        <div className="px-5 pt-4">
          <ChartPanel tag={tag} selectedView={selectedView} selectedFY={selectedFY} />
        </div>
      )}
      {isStacked && selectedView === 'stacked' && (
        <p className="px-5 mt-1 text-xs text-indigo-400 text-center">
          ↑ Select a sub-component from Breakdown to drill down
        </p>
      )}

      {/* Data table */}
      <div className="px-5 pt-4">
        <DataTable tag={insightsTag} />
      </div>

      {/* Insights */}
      <div className="px-5">
        <InsightsPanel tag={insightsTag} />
      </div>
    </div>
  )
}
