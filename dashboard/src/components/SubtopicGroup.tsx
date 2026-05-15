import { useState } from 'react'
import IndicatorCard from './IndicatorCard'

interface Props {
  subtopic: string | null
  tags: string[]
  highlightedTag: string | null
  activateSubTag: string | null
}

export default function SubtopicGroup({ subtopic, tags, highlightedTag, activateSubTag }: Props) {
  const [open, setOpen] = useState(true)

  if (!subtopic) {
    return (
      <div className="flex flex-col gap-4">
        {tags.map(tag => (
          <IndicatorCard key={tag} tag={tag} highlight={highlightedTag === tag} activeSubTag={activateSubTag} />
        ))}
      </div>
    )
  }

  return (
    <div>
      <button
        onClick={() => setOpen(o => !o)}
        className="flex items-center gap-2 mb-4 text-left"
      >
        <span className="text-xs font-bold text-indigo-600 uppercase tracking-widest">{subtopic}</span>
        <span className="text-gray-400 text-xs">{open ? '▲' : '▼'}</span>
      </button>
      {open && (
        <div className="flex flex-col gap-4">
          {tags.map(tag => (
            <IndicatorCard key={tag} tag={tag} highlight={highlightedTag === tag} activeSubTag={activateSubTag} />
          ))}
        </div>
      )}
    </div>
  )
}
