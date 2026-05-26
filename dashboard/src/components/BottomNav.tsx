type ActiveView = 'E' | 'S' | 'G' | 'search' | 'benchmark' | 'about'

interface Props {
  activeView: ActiveView
  onNavigate: (view: ActiveView) => void
}

interface NavItem {
  view: ActiveView
  label: string
  badge?: string
  icon?: React.ReactNode
}

const NAV_ITEMS: NavItem[] = [
  { view: 'E', label: 'Environment', badge: 'E' },
  { view: 'S', label: 'Social', badge: 'S' },
  { view: 'G', label: 'Governance', badge: 'G' },
  {
    view: 'search',
    label: 'Search',
    icon: (
      <svg xmlns="http://www.w3.org/2000/svg" className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.75}>
        <path strokeLinecap="round" strokeLinejoin="round" d="M21 21l-4.35-4.35M17 11A6 6 0 105 11a6 6 0 0012 0z" />
      </svg>
    ),
  },
  {
    view: 'benchmark',
    label: 'Benchmark',
    icon: (
      <svg xmlns="http://www.w3.org/2000/svg" className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.75}>
        <path strokeLinecap="round" strokeLinejoin="round" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
      </svg>
    ),
  },
  {
    view: 'about',
    label: 'Help',
    icon: (
      <svg xmlns="http://www.w3.org/2000/svg" className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.75}>
        <path strokeLinecap="round" strokeLinejoin="round" d="M13 16h-1v-4h-1m1-4h.01M12 2a10 10 0 100 20A10 10 0 0012 2z" />
      </svg>
    ),
  },
]

export default function BottomNav({ activeView, onNavigate }: Props) {
  return (
    <nav className="lg:hidden fixed bottom-0 left-0 right-0 z-50 bg-gray-900 border-t border-gray-700 flex">
      {NAV_ITEMS.map(({ view, label, badge, icon }) => {
        const active = activeView === view
        return (
          <button
            key={view}
            onClick={() => onNavigate(view)}
            aria-current={active ? 'page' : undefined}
            className={`relative flex-1 flex flex-col items-center justify-center gap-1.5 py-3 transition-colors ${
              active ? 'text-white' : 'text-gray-400 hover:text-gray-200'
            }`}
          >
            {/* Active indicator bar at top */}
            <span className={`absolute top-0 h-0.5 w-10 rounded-b transition-colors ${active ? 'bg-indigo-500' : 'bg-transparent'}`} />

            {badge ? (
              <span className={`w-7 h-7 rounded flex items-center justify-center text-xs font-bold transition-colors ${
                active ? 'bg-indigo-600 text-white' : 'bg-white/10 text-gray-300'
              }`}>
                {badge}
              </span>
            ) : (
              <span className={active ? 'text-white' : 'text-gray-400'}>{icon}</span>
            )}

            <span className="text-xs font-medium leading-none">{label}</span>
          </button>
        )
      })}
    </nav>
  )
}
