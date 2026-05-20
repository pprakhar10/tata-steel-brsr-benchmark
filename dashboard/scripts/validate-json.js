import { readFileSync, readdirSync } from 'fs'
import { join, dirname } from 'path'
import { fileURLToPath } from 'url'

const __dirname = dirname(fileURLToPath(import.meta.url))

const DIRS = [
  join(__dirname, '../src/data/analysis/indicators'),
  join(__dirname, '../src/data/companies'),
]

let errors = 0
for (const dir of DIRS) {
  for (const file of readdirSync(dir).filter(f => f.endsWith('.json'))) {
    const full = join(dir, file)
    try {
      JSON.parse(readFileSync(full, 'utf8'))
    } catch (e) {
      console.error(`INVALID: ${file}\n  ${e.message}\n`)
      errors++
    }
  }
}

if (errors === 0) console.log(`All JSON files valid. (${DIRS.length} directories scanned)`)
else { console.error(`\n${errors} file(s) have invalid JSON.`); process.exit(1) }
