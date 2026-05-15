import { useState } from 'react'
import { ORDERED_TAGS, SUB_COMPONENT_TAGS } from '../constants/esgMap'
import { INDICATOR_ANALYSIS } from '../data/loader'
import { type FY } from '../types/data'
import IndicatorResultCard from './IndicatorResultCard'

const BENCHMARKABLE_TAGS = ORDERED_TAGS.filter(
  tag => !SUB_COMPONENT_TAGS.has(tag) && !!INDICATOR_ANALYSIS[tag]
)

const FY_OPTIONS: { fy: FY; label: string; sublabel: string }[] = [
  { fy: 'FY2023', label: 'FY2022-23', sublabel: 'Base year' },
  { fy: 'FY2024', label: 'FY2023-24', sublabel: 'Year 2' },
  { fy: 'FY2025', label: 'FY2024-25', sublabel: 'Latest' },
]

const RANK_OPTIONS: { rank: number; label: string; activeCls: string; inactiveCls: string }[] = [
  { rank: 1, label: 'Leading',  activeCls: 'border-emerald-600 bg-emerald-600 text-white shadow-lg', inactiveCls: 'border-emerald-200 bg-white text-emerald-700 hover:border-emerald-400 hover:shadow-md' },
  { rank: 2, label: 'Strong',   activeCls: 'border-blue-600 bg-blue-600 text-white shadow-lg',       inactiveCls: 'border-blue-200 bg-white text-blue-700 hover:border-blue-400 hover:shadow-md' },
  { rank: 3, label: 'Moderate', activeCls: 'border-amber-500 bg-amber-500 text-white shadow-lg',     inactiveCls: 'border-amber-200 bg-white text-amber-700 hover:border-amber-400 hover:shadow-md' },
  { rank: 4, label: 'Lagging',  activeCls: 'border-red-600 bg-red-600 text-white shadow-lg',         inactiveCls: 'border-red-200 bg-white text-red-700 hover:border-red-400 hover:shadow-md' },
]

interface Props {
  onNavigate: (tag: string) => void
}

export default function BenchmarkPanel({ onNavigate }: Props) {
  const [selectedFY, setSelectedFY] = useState<FY | null>(null)
  const [selectedRank, setSelectedRank] = useState<number | null>(null)

  const results =
    selectedFY && selectedRank != null
      ? BENCHMARKABLE_TAGS.filter(
          tag => INDICATOR_ANALYSIS[tag]?.peerRank[selectedFY]?.tata === selectedRank
        )
      : []

  const fyLabel = FY_OPTIONS.find(f => f.fy === selectedFY)?.label ?? ''

  return (
    <div className="flex flex-col gap-8">
      <div>
        <h2 className="text-2xl font-bold text-gray-900 mb-1">Benchmark</h2>
        <p className="text-sm text-gray-500">See where Tata Steel ranks across all indicators for a given year.</p>
      </div>

      {/* FY selector */}
      <div>
        <p className="text-xs font-bold uppercase tracking-widest text-gray-400 mb-3">Select Financial Year</p>
        <div className="grid grid-cols-3 gap-4">
          {FY_OPTIONS.map(({ fy, label, sublabel }) => (
            <button
              key={fy}
              onClick={() => { setSelectedFY(fy); setSelectedRank(null) }}
              className={`flex flex-col items-center justify-center py-7 rounded-xl border-2 font-medium transition-all ${
                selectedFY === fy
                  ? 'border-indigo-600 bg-indigo-600 text-white shadow-lg'
                  : 'border-gray-200 bg-white text-gray-700 hover:border-indigo-400 hover:shadow-md'
              }`}
            >
              <span className="text-xl font-bold">{label}</span>
              <span className={`text-xs mt-1 ${selectedFY === fy ? 'text-indigo-200' : 'text-gray-400'}`}>
                {sublabel}
              </span>
            </button>
          ))}
        </div>
      </div>

      {/* Rank selector */}
      {selectedFY && (
        <div>
          <p className="text-xs font-bold uppercase tracking-widest text-gray-400 mb-3">Select Tata Steel's Rank</p>
          <div className="grid grid-cols-4 gap-4">
            {RANK_OPTIONS.map(({ rank, label, activeCls, inactiveCls }) => (
              <button
                key={rank}
                onClick={() => setSelectedRank(rank)}
                className={`flex flex-col items-center justify-center py-7 rounded-xl border-2 font-medium transition-all ${
                  selectedRank === rank ? activeCls : inactiveCls
                }`}
              >
                <span className="text-3xl font-bold">#{rank}</span>
                <span className="text-xs mt-1 font-semibold uppercase tracking-wide opacity-80">{label}</span>
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Results */}
      {selectedFY && selectedRank != null && (
        <div className="flex flex-col gap-2">
          {results.length === 0 ? (
            <p className="text-sm text-gray-400 py-8 text-center">
              No indicators found for Rank {selectedRank} in {fyLabel}.
            </p>
          ) : (
            results.map(tag => (
              <IndicatorResultCard key={tag} tag={tag} selectedFY={selectedFY} onClick={() => onNavigate(tag)} />
            ))
          )}
        </div>
      )}
    </div>
  )
}
