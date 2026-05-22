type ActiveView = 'E' | 'S' | 'G' | 'search' | 'benchmark' | 'about'

interface Props {
  activeView: ActiveView
  onNavigate: (view: ActiveView) => void
}

const NAV_ITEMS: { view: ActiveView; label: string; icon: React.ReactNode }[] = [
  {
    view: 'E',
    label: 'Environment',
    icon: (
      <svg xmlns="http://www.w3.org/2000/svg" className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.75}>
        <path strokeLinecap="round" strokeLinejoin="round" d="M12 3C7 3 3 7.5 3 12c0 4 3 7.4 7 8.7V18c-2-.6-3.5-2.3-3.5-4.5 0-2.5 2-4.5 4.5-4.5h1V3z" />
        <path strokeLinecap="round" strokeLinejoin="round" d="M12 3c5 0 9 4.5 9 9 0 4-3 7.4-7 8.7V18c2-.6 3.5-2.3 3.5-4.5 0-2.5-2-4.5-4.5-4.5H12V3z" />
      </svg>
    ),
  },
  {
    view: 'S',
    label: 'Social',
    icon: (
      <svg xmlns="http://www.w3.org/2000/svg" className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.75}>
        <path strokeLinecap="round" strokeLinejoin="round" d="M17 20h5v-2a4 4 0 00-3-3.87M9 20H4v-2a4 4 0 013-3.87m10-4a4 4 0 11-8 0 4 4 0 018 0zM7 7a4 4 0 110 8 4 4 0 010-8z" />
      </svg>
    ),
  },
  {
    view: 'G',
    label: 'Governance',
    icon: (
      <svg xmlns="http://www.w3.org/2000/svg" className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.75}>
        <path strokeLinecap="round" strokeLinejoin="round" d="M3 21h18M3 10h18M5 6l7-3 7 3M4 10v11M20 10v11M8 10v11M12 10v11M16 10v11" />
      </svg>
    ),
  },
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
    label: 'About',
    icon: (
      <svg xmlns="http://www.w3.org/2000/svg" className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.75}>
        <path strokeLinecap="round" strokeLinejoin="round" d="M13 16h-1v-4h-1m1-4h.01M12 2a10 10 0 100 20A10 10 0 0012 2z" />
      </svg>
    ),
  },
]

export default function BottomNav({ activeView, onNavigate }: Props) {
  return (
    <nav className="lg:hidden fixed bottom-0 left-0 right-0 z-50 bg-white border-t border-gray-200 flex">
      {NAV_ITEMS.map(({ view, label, icon }) => {
        const active = activeView === view
        return (
          <button
            key={view}
            onClick={() => onNavigate(view)}
            className={`flex-1 flex flex-col items-center justify-center gap-0.5 py-2 text-xs font-medium transition-colors ${
              active ? 'text-indigo-600' : 'text-gray-400 hover:text-gray-600'
            }`}
            aria-current={active ? 'page' : undefined}
          >
            <span className={active ? 'text-indigo-600' : 'text-gray-400'}>{icon}</span>
            <span className="leading-none">{label}</span>
          </button>
        )
      })}
    </nav>
  )
}
