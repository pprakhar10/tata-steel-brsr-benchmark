type ActiveView = 'E' | 'S' | 'G' | 'search' | 'benchmark' | 'about'

interface Props {
  activeView: ActiveView
  onNavigate: (view: ActiveView) => void
}

const ESG_ITEMS: { view: ActiveView; label: string; desc: string }[] = [
  { view: 'E', label: 'E', desc: 'Environment' },
  { view: 'S', label: 'S', desc: 'Social' },
  { view: 'G', label: 'G', desc: 'Governance' },
]

const TOOL_ITEMS: { view: ActiveView; label: string }[] = [
  { view: 'search', label: 'Search' },
  { view: 'benchmark', label: 'Benchmark' },
  { view: 'about', label: 'About & Help' },
]

export default function Sidebar({ activeView, onNavigate }: Props) {
  return (
    <aside className="w-52 shrink-0 h-screen sticky top-0 bg-gray-900 text-white flex flex-col py-6 px-3 gap-6">
      <div className="px-2 text-sm font-bold text-white">Steel BRSR Benchmark</div>
      <nav className="flex flex-col gap-1">
        {ESG_ITEMS.map(({ view, label, desc }) => (
          <button
            key={view}
            onClick={() => onNavigate(view)}
            className={`flex items-center gap-3 px-3 py-2 rounded-lg text-sm font-medium text-left transition-colors ${
              activeView === view
                ? 'bg-indigo-600 text-white'
                : 'text-gray-300 hover:bg-gray-700 hover:text-white'
            }`}
          >
            <span className="w-6 h-6 rounded bg-white/10 flex items-center justify-center text-xs font-bold">
              {label}
            </span>
            {desc}
          </button>
        ))}
      </nav>

      <div className="px-2 text-xs font-semibold uppercase tracking-widest text-gray-400 mt-2">Tools</div>
      <nav className="flex flex-col gap-1">
        {TOOL_ITEMS.map(({ view, label }) => (
          <button
            key={view}
            onClick={() => onNavigate(view)}
            className={`px-3 py-2 rounded-lg text-sm font-medium text-left transition-colors ${
              activeView === view
                ? 'bg-indigo-600 text-white'
                : 'text-gray-300 hover:bg-gray-700 hover:text-white'
            }`}
          >
            {label}
          </button>
        ))}
      </nav>
    </aside>
  )
}
