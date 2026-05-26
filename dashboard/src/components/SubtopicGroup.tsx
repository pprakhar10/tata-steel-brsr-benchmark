import { useState, useEffect } from 'react'
import IndicatorCard from './IndicatorCard'

interface Props {
  subtopic: string | null
  tags: string[]
  highlightedTag: string | null
  activateSubTag: string | null
  allExpanded: boolean
  bulkVersion: number
}

export default function SubtopicGroup({ subtopic, tags, highlightedTag, activateSubTag, allExpanded, bulkVersion }: Props) {
  const [open, setOpen] = useState(false)

  // Sync to topic-level Expand All / Minimize All
  useEffect(() => {
    if (bulkVersion === 0) return
    setOpen(allExpanded)
  }, [bulkVersion])

  // Auto-open when a search-highlighted indicator lives in this subtopic
  useEffect(() => {
    if (highlightedTag !== null && tags.includes(highlightedTag)) {
      setOpen(true)
    }
  }, [highlightedTag, tags])

  if (!subtopic) {
    // No subtopic label — visibility controlled only by topic-level Expand All / Minimize All
    return (
      <div className="flex flex-col gap-4">
        {open && tags.map(tag => (
          <IndicatorCard
            key={tag}
            tag={tag}
            highlight={highlightedTag === tag}
            activeSubTag={activateSubTag}
          />
        ))}
      </div>
    )
  }

  return (
    <div>
      <button
        onClick={() => setOpen(o => !o)}
        className="w-full flex items-center justify-between mb-4 text-left"
      >
        <span className="text-xs font-bold text-indigo-600 uppercase tracking-widest">{subtopic}</span>
        <svg
          xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"
          className={`w-3.5 h-3.5 text-indigo-400 transition-transform duration-200 ${open ? 'rotate-180' : ''}`}
        >
          <path fillRule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clipRule="evenodd" />
        </svg>
      </button>
      {open && (
        <div className="flex flex-col gap-4">
          {tags.map(tag => (
            <IndicatorCard
              key={tag}
              tag={tag}
              highlight={highlightedTag === tag}
              activeSubTag={activateSubTag}
            />
          ))}
        </div>
      )}
    </div>
  )
}
