import type { CompanyKey } from '../types/data'

export function detectTies(ranks: Partial<Record<CompanyKey, number | null>>): Set<CompanyKey> {
  const byRank = new Map<number, CompanyKey[]>()
  for (const [key, rank] of Object.entries(ranks) as [CompanyKey, number | null][]) {
    if (rank == null) continue
    const group = byRank.get(rank) ?? []
    group.push(key)
    byRank.set(rank, group)
  }
  const tied = new Set<CompanyKey>()
  for (const group of byRank.values()) {
    if (group.length > 1) group.forEach(k => tied.add(k))
  }
  return tied
}

export function isAllSameRank(ranks: Partial<Record<CompanyKey, number | null>>): boolean {
  const values = (Object.values(ranks) as (number | null)[]).filter((v): v is number => v != null)
  if (values.length === 0) return false
  return values.every(v => v === values[0])
}
