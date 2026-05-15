interface Props {
  rank: number | null
  isTied: boolean
  companyLabel: string
}

const RANK_COLORS: Record<number, string> = {
  1: 'bg-emerald-100 text-emerald-800 ring-emerald-300',
  2: 'bg-blue-100 text-blue-800 ring-blue-300',
  3: 'bg-amber-100 text-amber-800 ring-amber-300',
  4: 'bg-red-100 text-red-800 ring-red-300',
}

export default function RankBadge({ rank, isTied, companyLabel }: Props) {
  if (rank == null) return null
  const colors = RANK_COLORS[rank] ?? 'bg-gray-100 text-gray-600 ring-gray-300'
  return (
    <span
      className={`inline-flex items-center gap-1 px-1.5 py-0.5 rounded text-xs ring-1 ${colors} ${isTied ? 'font-bold' : 'font-medium'}`}
    >
      {companyLabel} #{rank}
    </span>
  )
}
