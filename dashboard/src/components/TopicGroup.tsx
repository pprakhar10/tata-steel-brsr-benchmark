import { useState, useMemo } from 'react'
import SubtopicGroup from './SubtopicGroup'

interface Props {
  topic: string
  entries: { subtopic: string | null; tag: string }[]
  highlightedTag: string | null
  activateSubTag: string | null
}

export default function TopicGroup({ topic, entries, highlightedTag, activateSubTag }: Props) {
  const [allExpanded, setAllExpanded] = useState(false)
  const [bulkVersion, setBulkVersion] = useState(0)

  function handleBulkToggle() {
    const next = !allExpanded
    setAllExpanded(next)
    setBulkVersion(v => v + 1)
  }

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
      <div className="flex items-center justify-between px-6 py-4 border-b border-gray-100">
        <h2 className="font-semibold text-gray-900 text-base">{topic}</h2>
        <button
          onClick={handleBulkToggle}
          className="text-xs font-medium text-indigo-600 border border-indigo-200 rounded-md px-3 py-1.5 bg-indigo-50 hover:bg-indigo-100 transition-colors shrink-0"
        >
          {allExpanded ? 'Minimize All' : 'Expand All'}
        </button>
      </div>
      <div className="px-6 py-5 flex flex-col gap-8">
        {subtopicGroups.map(({ subtopic, tags }) => (
          <SubtopicGroup
            key={subtopic ?? '__null__'}
            subtopic={subtopic}
            tags={tags}
            highlightedTag={highlightedTag}
            activateSubTag={activateSubTag}
            allExpanded={allExpanded}
            bulkVersion={bulkVersion}
          />
        ))}
      </div>
    </div>
  )
}
