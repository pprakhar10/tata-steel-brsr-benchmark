export type TrendResult = 'up' | 'down' | 'flat' | 'nodata'

export function computeTrend(
  curr: number | null,
  prev: number | null,
  direction: string,
): TrendResult {
  if (curr == null || prev == null) return 'nodata'
  if (curr === prev) return 'flat'
  const lowerIsBetter = direction.includes('lower')
  const improved = lowerIsBetter ? curr < prev : curr > prev
  return improved ? 'up' : 'down'
}
