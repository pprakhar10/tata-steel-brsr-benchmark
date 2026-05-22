import { useState, useMemo, useEffect } from 'react'
import SubtopicGroup from './SubtopicGroup'

interface Props {
  topic: string
  entries: { subtopic: string | null; tag: string }[]
  highlightedTag: string | null
  activateSubTag: string | null
}

export default function TopicGroup({ topic, entries, highlightedTag, activateSubTag }: Props) {
  const hasSubtopics = entries.some(e => e.subtopic !== null)
  const [open, setOpen] = useState(hasSubtopics)

  useEffect(() => {
    if (highlightedTag !== null && entries.some(e => e.tag === highlightedTag)) {
      setOpen(true)
    }
  }, [highlightedTag, entries])

  const subtopicGroups = useMemo(() => {
    const map = new Map<string, string[]>()
    for (const { subtopic, tag } of entries) {
      const key = subtopic ?? '__null__'
      if (!map.has(key)) map.set(key, [])
      map.get(key)!.push(tag)
    }
    return [...map.entries()].map(([key, tags]) => ({
      subtopic: key === '__null__' ? null : key,
      tags,
    }))
  }, [entries])

  return (
    <div className="bg-white rounded-xl border border-gray-200 shadow-sm overflow-hidden">
      <button
        onClick={() => setOpen(o => !o)}
        className="w-full flex items-center justify-between px-6 py-4 text-left hover:bg-gray-50 transition-colors"
      >
        <h2 className="font-semibold text-gray-900 text-base">{topic}</h2>
        <span className="text-gray-400 text-sm">{open ? '▲' : '▼'}</span>
      </button>
      {open && (
        <div className="border-t border-gray-100 px-6 py-5 flex flex-col gap-8">
          {subtopicGroups.map(({ subtopic, tags }) => (
            <SubtopicGroup
              key={subtopic ?? '__null__'}
              subtopic={subtopic}
              tags={tags}
              highlightedTag={highlightedTag}
              activateSubTag={activateSubTag}
            />
          ))}
        </div>
      )}
    </div>
  )
}
