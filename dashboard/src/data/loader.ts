import type { CompanyData, IndicatorAnalysis } from '../types/data'

import tataRaw from './companies/tata-steel.json'
import jswRaw from './companies/jsw-steel.json'
import sailRaw from './companies/sail.json'
import jindalRaw from './companies/jindal-stainless.json'

export const COMPANY_DATA: Record<string, CompanyData> = {
  'tata-steel': tataRaw as unknown as CompanyData,
  'jsw-steel': jswRaw as unknown as CompanyData,
  'sail': sailRaw as unknown as CompanyData,
  'jindal-stainless': jindalRaw as unknown as CompanyData,
}

const indicatorModules = import.meta.glob('./analysis/indicators/*.json', { eager: true })

export const INDICATOR_ANALYSIS: Record<string, IndicatorAnalysis> = Object.fromEntries(
  Object.entries(indicatorModules).map(([path, mod]) => {
    const tag = path.replace('./analysis/indicators/', '').replace('.json', '')
    return [tag, (mod as { default: IndicatorAnalysis }).default]
  }),
)
