import { useState, useEffect, useRef } from 'react'
import { ESG_MAP, ORDERED_TAGS, SUB_COMPONENT_TAGS } from '../constants/esgMap'
import { INDICATOR_ANALYSIS } from '../data/loader'
import { type FY } from '../types/data'
import IndicatorResultCard from './IndicatorResultCard'

const SEARCHABLE_TAGS = ORDERED_TAGS.filter(
  tag => !SUB_COMPONENT_TAGS.has(tag) && !!INDICATOR_ANALYSIS[tag]
)

interface Props {
  onNavigate: (tag: string) => void
}

const FY_OPTIONS: { fy: FY; label: string; sublabel: string }[] = [
  { fy: 'FY2023', label: 'FY2022-23', sublabel: 'Base year' },
  { fy: 'FY2024', label: 'FY2023-24', sublabel: 'Year 2' },
  { fy: 'FY2025', label: 'FY2024-25', sublabel: 'Latest' },
]

export default function SearchPanel({ onNavigate }: Props) {
  const [selectedFY, setSelectedFY] = useState<FY | null>(null)
  const [query, setQuery] = useState('')
  const inputRef = useRef<HTMLInputElement>(null)

  useEffect(() => {
    if (selectedFY) inputRef.current?.focus()
  }, [selectedFY])

  const results = selectedFY
    ? SEARCHABLE_TAGS.filter(tag =>
        (ESG_MAP[tag]?.label ?? '').toLowerCase().includes(query.toLowerCase())
      )
    : []

  return (
    <div className="flex flex-col gap-8">
      <div>
        <h2 className="text-2xl font-bold text-gray-900 mb-1">Search Indicators</h2>
        <p className="text-sm text-gray-500">Select a financial year, then search by indicator name.</p>
      </div>

      {/* FY selector */}
      <div>
        <p className="text-xs font-bold uppercase tracking-widest text-gray-400 mb-3">Select Financial Year</p>
        <div className="grid grid-cols-3 gap-4">
          {FY_OPTIONS.map(({ fy, label, sublabel }) => (
            <button
              key={fy}
              onClick={() => setSelectedFY(fy)}
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

      {selectedFY && (
        <>
          <div>
            <p className="text-xs font-bold uppercase tracking-widest text-gray-400 mb-3">Search Indicators</p>
            <input
              ref={inputRef}
              type="text"
              value={query}
              onChange={e => setQuery(e.target.value)}
              placeholder="e.g. scope, intensity, water..."
              className="w-full border-2 border-gray-200 rounded-xl px-5 py-4 text-base focus:outline-none focus:border-indigo-400"
            />
          </div>
          <div className="flex flex-col gap-2">
            {results.length === 0 ? (
              <p className="text-sm text-gray-400 py-8 text-center">No indicators match your search.</p>
            ) : (
              results.map(tag => (
                <IndicatorResultCard
                  key={tag}
                  tag={tag}
                  selectedFY={selectedFY}
                  onClick={() => onNavigate(tag)}
                />
              ))
            )}
          </div>
        </>
      )}
    </div>
  )
}
