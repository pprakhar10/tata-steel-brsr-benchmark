import { useMemo } from 'react'
import { ESG_MAP, ORDERED_TAGS, SUB_COMPONENT_TAGS } from '../constants/esgMap'
import TopicGroup from './TopicGroup'

interface Props {
  bucket: 'E' | 'S' | 'G'
  highlightedTag: string | null
}

export default function ESGView({ bucket, highlightedTag }: Props) {
  const topicGroups = useMemo(() => {
    const tags = ORDERED_TAGS.filter(tag => {
      const entry = ESG_MAP[tag]
      return entry?.esg === bucket && !SUB_COMPONENT_TAGS.has(tag)
    })

    const topicMap = new Map<string, { subtopic: string | null; tag: string }[]>()
    for (const tag of tags) {
      const entry = ESG_MAP[tag]!
      if (!topicMap.has(entry.topic)) topicMap.set(entry.topic, [])
      topicMap.get(entry.topic)!.push({ subtopic: entry.subtopic, tag })
    }

    return [...topicMap.entries()].map(([topic, entries]) => ({ topic, entries }))
  }, [bucket])

  return (
    <div className="flex flex-col gap-6">
      {topicGroups.map(({ topic, entries }) => (
        <TopicGroup
          key={topic}
          topic={topic}
          entries={entries}
          highlightedTag={highlightedTag}
        />
      ))}
    </div>
  )
}
