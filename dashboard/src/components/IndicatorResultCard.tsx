import { ESG_MAP, SUB_COMPONENT_TAGS, SUB_COMPONENT_PARENT } from '../constants/esgMap'
import { INDICATOR_ANALYSIS } from '../data/loader'
import { COMPANY_KEYS, COMPANY_LABELS, type FY } from '../types/data'
import { detectTies, isAllSameRank } from '../utils/ranks'
import RankBadge from './RankBadge'

interface Props {
  tag: string
  selectedFY: FY
  onClick?: () => void
}

export default function IndicatorResultCard({ tag, selectedFY, onClick }: Props) {
  const entry = ESG_MAP[tag]
  const analysis = INDICATOR_ANALYSIS[tag]
  if (!entry || !analysis) return null

  const ranks = analysis.peerRank[selectedFY]
  const tied = detectTies(ranks)
  const allSame = isAllSameRank(ranks)

  const breadcrumb = entry.subtopic
    ? `${entry.topic} › ${entry.subtopic}`
    : entry.topic

  const isSub = SUB_COMPONENT_TAGS.has(tag)
  const parentLabel = isSub ? (ESG_MAP[SUB_COMPONENT_PARENT[tag]]?.label ?? null) : null

  return (
    <button
      onClick={onClick}
      className={`w-full text-left bg-white rounded-lg border border-gray-200 px-4 py-3 shadow-sm transition-colors ${onClick ? 'hover:border-indigo-400 hover:shadow-md cursor-pointer' : 'cursor-default'}`}
    >
      <div className="font-semibold text-gray-900 text-sm">{entry.label}</div>
      <div className="text-xs text-gray-400 mt-0.5">{breadcrumb}</div>
      {parentLabel && (
        <div className="text-xs text-indigo-400 mt-0.5 mb-2">↳ Breakdown of {parentLabel}</div>
      )}
      {!parentLabel && <div className="mb-2" />}
      <div className="flex flex-wrap gap-1.5">
        {allSame
          ? <span className="text-xs text-gray-400 italic">All companies equal — no ranking</span>
          : COMPANY_KEYS.map(key => (
              <RankBadge
                key={key}
                rank={ranks[key]}
                isTied={tied.has(key)}
                companyLabel={COMPANY_LABELS[key]}
              />
            ))
        }
      </div>
    </button>
  )
}
