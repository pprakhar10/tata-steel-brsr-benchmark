import type { ValueObject } from '../types/data'

const UNIT_FULL: Record<string, string> = {
  'tCO2e':     'Tonnes of CO2 Equivalent',
  'tCO2e/tcs': 'Tonnes CO2e per Tonne of Crude Steel',
  'tCO2e/₹':   'Tonnes CO2e per ₹ Turnover',
  'GJ':        'Gigajoules',
  'GJ/tcs':    'Gigajoules per Tonne of Crude Steel',
  'GJ/₹':      'Gigajoules per ₹ Turnover',
  'kt':        'Kilotonnes',
  'kL':        'Kilolitres',
  'L/tcs':     'Litres per Tonne of Crude Steel',
  'L/₹':       'Litres per ₹ Turnover',
  'MT':        'Metric Tonnes',
  'MT/tcs':    'Metric Tonnes per Tonne of Crude Steel',
  'MT/₹ Cr':   'Metric Tonnes per ₹ Crore Turnover',
  'per mn hrs':'Per Million Hours Worked',
  'no.':       'Number',
  '%':         'Percentage',
  '₹ Cr':      'Indian Rupees (Crores)',
}

export function formatUnitFull(unit: string): string {
  const full = UNIT_FULL[unit]
  return full ? `${full} (${unit})` : unit
}

export function formatValue(vObj: ValueObject | null | undefined): string {
  if (!vObj || vObj.value == null) return '—'
  const v = vObj.value
  if (v === 0) return '0'
  const abs = Math.abs(v)
  if (abs >= 1_000_000) return (v / 1_000_000).toFixed(1) + 'M'
  if (abs >= 1_000) return v.toLocaleString('en-IN', { minimumFractionDigits: 1, maximumFractionDigits: 1 })
  if (abs >= 0.01) return parseFloat(v.toPrecision(3)).toString()
  // Small numbers: fixed notation, 3 sig figs, no scientific notation
  const decimals = Math.min(Math.abs(Math.floor(Math.log10(abs))) + 2, 8)
  return v.toFixed(decimals).replace(/\.?0+$/, '')
}
