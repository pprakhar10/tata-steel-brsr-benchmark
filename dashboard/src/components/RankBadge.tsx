interface Props {
  rank: number | null
  isTied: boolean
  companyLabel: string
}

export default function RankBadge({ rank, isTied, companyLabel }: Props) {
  if (rank == null) return null
  return (
    <span
      className={`inline-flex items-center gap-1 px-1.5 py-0.5 rounded text-xs ring-1 bg-gray-100 text-gray-600 ring-gray-300 ${isTied ? 'font-bold' : 'font-medium'}`}
    >
      {companyLabel} #{rank}
    </span>
  )
}
