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

export function formatValue(vObj: ValueObject | null | undefined, forceMillions = false): string {
  if (!vObj || vObj.value == null) return '—'
  const v = vObj.value
  if (v === 0) return '0'
  const abs = Math.abs(v)
  if (abs >= 1_000_000 || forceMillions) {
    const inM = v / 1_000_000
    const absM = Math.abs(inM)
    if (absM >= 10) return inM.toFixed(1) + 'M'
    if (absM >= 1)  return inM.toFixed(2) + 'M'
    // Small fractions of a million (e.g. 0.05M)
    return parseFloat(inM.toPrecision(3)).toString() + 'M'
  }
  if (abs >= 1_000) {
    const hasDecimal = v !== Math.floor(v)
    return v.toLocaleString('en-IN', { minimumFractionDigits: hasDecimal ? 1 : 0, maximumFractionDigits: 1 })
  }
  if (abs >= 0.01) return parseFloat(v.toPrecision(3)).toString()
  // Small numbers: fixed notation, 3 sig figs, no scientific notation
  const decimals = Math.min(Math.abs(Math.floor(Math.log10(abs))) + 2, 8)
  return v.toFixed(decimals).replace(/\.?0+$/, '')
}
