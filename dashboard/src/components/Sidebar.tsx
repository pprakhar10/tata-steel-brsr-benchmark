import { useState } from 'react'

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
  { view: 'about', label: 'How to use & Help' },
]

export default function Sidebar({ activeView, onNavigate }: Props) {
  const [open, setOpen] = useState(false)

  const handleNav = (view: ActiveView) => {
    onNavigate(view)
    setOpen(false)
  }

  return (
    <>
      {/* Hamburger / close button — visible only below lg */}
      <button
        className="lg:hidden fixed top-3 left-3 z-50 w-9 h-9 flex items-center justify-center rounded-lg bg-gray-900 text-white shadow-md"
        onClick={() => setOpen(o => !o)}
        aria-label={open ? 'Close navigation' : 'Open navigation'}
      >
        {open ? (
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5">
            <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" />
          </svg>
        ) : (
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5">
            <path strokeLinecap="round" strokeLinejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
          </svg>
        )}
      </button>

      {/* Backdrop — tap to close, shown when open on mobile/tablet */}
      {open && (
        <div
          className="lg:hidden fixed inset-0 z-40 bg-black/50"
          onClick={() => setOpen(false)}
        />
      )}

      {/* Sidebar panel */}
      <aside
        className={[
          // Layout: fixed overlay on mobile/tablet, part of flex flow on desktop
          'fixed lg:relative top-0 left-0 h-full lg:h-dvh',
          'w-52 shrink-0 flex flex-col overflow-y-auto',
          'bg-gray-900 text-white py-6 px-3 gap-6',
          // Stack: above backdrop on mobile/tablet, normal on desktop
          'z-50 lg:z-auto',
          // Slide animation: off-screen when closed, on-screen when open; always visible on desktop
          'transition-transform duration-200 ease-in-out',
          open ? 'translate-x-0' : '-translate-x-full',
          'lg:translate-x-0',
        ].join(' ')}
      >
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
