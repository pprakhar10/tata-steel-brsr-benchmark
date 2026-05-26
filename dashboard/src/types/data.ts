export interface ValueObject {
  value: number | null
  rawValue: string | null
  rawUnit: string | null
  standardUnit: string | null
  normalized: boolean
  unitWarning: string | null
  dataType: string
  valueStatus: string
  patchSource: string | null
}

export interface YearMeta {
  reportingBasis: string
  basisWarning: string | null
}

export interface CompanyYearData {
  _meta: YearMeta
  [tag: string]: ValueObject | YearMeta
}

export interface CompanyData {
  companyId: string
  lastUpdated: string
  years: {
    FY2023: CompanyYearData
    FY2024: CompanyYearData
    FY2025: CompanyYearData
  }
}

export interface PeerRankYear {
  tata: number | null
  jsw: number | null
  sail: number | null
  jindal: number | null
}

export interface PeerRank {
  FY2023: PeerRankYear
  FY2024: PeerRankYear
  FY2025: PeerRankYear
}

export interface CompanyTrend {
  'FY2023-24': string
  'FY2024-25': string
}

export interface TrendDirection {
  tata: CompanyTrend
  jsw: CompanyTrend
  sail: CompanyTrend
  jindal: CompanyTrend
}

export interface IndicatorSections {
  about: string
  performanceAndDrivers: string
  tataPositioning: string
  targets: string
  comparabilityNotes: string | null
}

export interface IndicatorFlags {
  directionUnclear: boolean
  contextInsufficient: boolean
  externalSourceUsed: boolean
  trendAmbiguity: boolean
  flagNote: string | null
}

export interface IndicatorAnalysis {
  tag: string
  label: string
  principle: string
  topic: string
  direction: string
  peerRank: PeerRank
  trendDirection: TrendDirection
  sections: IndicatorSections
  flags: IndicatorFlags
  source: string
  userCorrection: string | null
  status: string
}

export interface ReviewStatus {
  status: string
  generatedAt: string
  approvedAt: string | null
}

export type ChartPattern = 'stacked' | 'line' | 'bar-pct' | 'bar' | 'none'

export type FY = 'FY2023' | 'FY2024' | 'FY2025'

export type CompanyKey = 'tata' | 'jsw' | 'sail' | 'jindal'

export const COMPANY_KEYS: CompanyKey[] = ['tata', 'jsw', 'sail', 'jindal']

export const COMPANY_LABELS: Record<CompanyKey, string> = {
  tata: 'Tata Steel',
  jsw: 'JSW',
  sail: 'SAIL',
  jindal: 'Jindal Stainless',
}

export const COMPANY_IDS: Record<CompanyKey, string> = {
  tata: 'tata-steel',
  jsw: 'jsw-steel',
  sail: 'sail',
  jindal: 'jindal-stainless',
}

export const FY_LABELS: FY[] = ['FY2023', 'FY2024', 'FY2025']

export const FY_DISPLAY: Record<FY, string> = {
  FY2023: 'FY2022-23',
  FY2024: 'FY2023-24',
  FY2025: 'FY2024-25',
}
