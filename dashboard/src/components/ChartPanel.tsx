import {
  BarChart, Bar, LineChart, Line,
  XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer,
} from 'recharts'
import { ESG_MAP, COMPOSITE_INDICATORS } from '../constants/esgMap'
import { COMPANY_DATA } from '../data/loader'
import { COMPANY_KEYS, COMPANY_LABELS, COMPANY_IDS, FY_LABELS, FY_DISPLAY, type CompanyYearData, type ValueObject, type FY } from '../types/data'

interface Props {
  tag: string
  selectedView?: string
  selectedFY?: FY
}

const COMPANY_COLORS: Record<string, string> = {
  tata: '#6366f1',
  jsw: '#f59e0b',
  sail: '#10b981',
  jindal: '#ef4444',
}

const SUBCOMP_COLORS = [
  '#6366f1', '#f59e0b', '#10b981', '#ef4444',
  '#8b5cf6', '#06b6d4', '#f97316', '#84cc16',
]

function isMeta(v: unknown): v is { reportingBasis: string } {
  return typeof v === 'object' && v !== null && 'reportingBasis' in v
}

function getValue(yearData: CompanyYearData | undefined, tag: string): number | null {
  if (!yearData) return null
  const v = yearData[tag]
  if (!v || isMeta(v)) return null
  return (v as ValueObject).value ?? null
}

function buildGroupedData(tag: string) {
  return FY_LABELS.map(fy => {
    const point: Record<string, string | number | null> = { fy: FY_DISPLAY[fy] }
    COMPANY_KEYS.forEach(key => {
      point[key] = getValue(COMPANY_DATA[COMPANY_IDS[key]]?.years[fy], tag)
    })
    return point
  })
}

function tooltipFormatter(unit: string) {
  return (value: number | string, name: string) => [`${value} ${unit}`, name]
}

function buildStackedData(parentTag: string, selectedFY: FY) {
  const subTags = COMPOSITE_INDICATORS[parentTag] ?? []
  return COMPANY_KEYS.map(key => {
    const yearData = COMPANY_DATA[COMPANY_IDS[key]]?.years[selectedFY]
    const point: Record<string, string | number | null> = { company: COMPANY_LABELS[key] }
    subTags.forEach(st => {
      point[st] = getValue(yearData, st)
    })
    return point
  })
}

export default function ChartPanel({ tag, selectedView = 'stacked', selectedFY = 'FY2025' }: Props) {
  const entry = ESG_MAP[tag]
  if (!entry) return null
  const { chartPattern } = entry

  if (chartPattern === 'none') return null

  if (chartPattern === 'line') {
    const data = buildGroupedData(tag)
    return (
      <ResponsiveContainer width="100%" height={220}>
        <LineChart data={data} margin={{ top: 8, right: 16, left: 8, bottom: 0 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
          <XAxis dataKey="fy" tick={{ fontSize: 11 }} />
          <YAxis tick={{ fontSize: 11 }} width={60} />
          <Tooltip formatter={tooltipFormatter(entry.unit)} />
          <Legend wrapperStyle={{ fontSize: 12 }} />
          {COMPANY_KEYS.map(key => (
            <Line
              key={key}
              type="monotone"
              dataKey={key}
              name={COMPANY_LABELS[key]}
              stroke={COMPANY_COLORS[key]}
              strokeWidth={2}
              dot={{ r: 4 }}
              connectNulls
            />
          ))}
        </LineChart>
      </ResponsiveContainer>
    )
  }

  if (chartPattern === 'stacked' && selectedView === 'stacked') {
    const subTags = COMPOSITE_INDICATORS[tag] ?? []
    const data = buildStackedData(tag, selectedFY)
    return (
      <ResponsiveContainer width="100%" height={220}>
        <BarChart data={data} margin={{ top: 8, right: 16, left: 8, bottom: 0 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
          <XAxis dataKey="company" tick={{ fontSize: 11 }} />
          <YAxis tick={{ fontSize: 11 }} width={60} />
          <Tooltip formatter={tooltipFormatter(entry.unit)} />
          <Legend wrapperStyle={{ fontSize: 11 }} />
          {subTags.map((st, i) => (
            <Bar
              key={st}
              dataKey={st}
              name={ESG_MAP[st]?.label ?? st}
              stackId="stack"
              fill={SUBCOMP_COLORS[i % SUBCOMP_COLORS.length]}
            />
          ))}
        </BarChart>
      </ResponsiveContainer>
    )
  }

  // bar, bar-pct, or stacked in total/subcomp mode
  const displayTag = (chartPattern === 'stacked' && selectedView !== 'stacked' && selectedView !== 'total')
    ? selectedView
    : tag
  const data = buildGroupedData(displayTag)
  const yDomain: [number, number] | undefined = chartPattern === 'bar-pct' ? [0, 100] : undefined
  const displayUnit = ESG_MAP[displayTag]?.unit ?? entry.unit

  return (
    <ResponsiveContainer width="100%" height={220}>
      <BarChart data={data} margin={{ top: 8, right: 16, left: 8, bottom: 0 }}>
        <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
        <XAxis dataKey="fy" tick={{ fontSize: 11 }} />
        <YAxis tick={{ fontSize: 11 }} width={60} domain={yDomain} />
        <Tooltip formatter={tooltipFormatter(displayUnit)} />
        <Legend wrapperStyle={{ fontSize: 12 }} />
        {COMPANY_KEYS.map(key => (
          <Bar
            key={key}
            dataKey={key}
            name={COMPANY_LABELS[key]}
            fill={COMPANY_COLORS[key]}
          />
        ))}
      </BarChart>
    </ResponsiveContainer>
  )
}
