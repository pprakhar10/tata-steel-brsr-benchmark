type ActiveView = 'E' | 'S' | 'G' | 'search' | 'benchmark' | 'about'

interface Props {
  activeView: ActiveView
  onNavigate: (view: ActiveView) => void
  isOpen: boolean
  onClose: () => void
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

export default function Sidebar({ activeView, onNavigate, isOpen, onClose }: Props) {
  const handleNav = (view: ActiveView) => {
    onNavigate(view)
    onClose()
  }

  return (
    <>
      {/* Backdrop — mobile/tablet overlay, hidden on lg+ */}
      {isOpen && (
        <div
          className="fixed inset-0 bg-black/50 z-20 lg:hidden"
          onClick={onClose}
          aria-hidden="true"
        />
      )}

      {/* Sidebar panel */}
      <aside
        className={`
          fixed lg:sticky top-0 left-0 h-dvh z-30 w-52 shrink-0
          bg-gray-900 text-white flex flex-col py-6 px-3 gap-6
          transition-transform duration-200 ease-in-out
          ${isOpen ? 'translate-x-0' : '-translate-x-full'}
          lg:translate-x-0
        `}
      >
        {/* Close button — mobile/tablet only */}
        <button
          onClick={onClose}
          className="lg:hidden absolute top-3 right-3 text-gray-400 hover:text-white p-1"
          aria-label="Close menu"
        >
          <svg xmlns="http://www.w3.org/2000/svg" className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
            <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>

        <div className="px-2 text-sm font-bold text-white">Steel BRSR Benchmark</div>

        <nav className="flex flex-col gap-1">
          {ESG_ITEMS.map(({ view, label, desc }) => (
            <button
              key={view}
              onClick={() => handleNav(view)}
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
              onClick={() => handleNav(view)}
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
    </>
  )
}
