import { useState, useCallback } from 'react'
import { ESG_MAP, SUB_COMPONENT_TAGS, SUB_COMPONENT_PARENT } from './constants/esgMap'
import Sidebar from './components/Sidebar'
import ESGView from './components/ESGView'
import SearchPanel from './components/SearchPanel'
import BenchmarkPanel from './components/BenchmarkPanel'
import AboutPanel from './components/AboutPanel'

type ActiveView = 'E' | 'S' | 'G' | 'search' | 'benchmark' | 'about'

export default function App() {
  const [activeView, setActiveView] = useState<ActiveView>('E')
  const [highlightedTag, setHighlightedTag] = useState<string | null>(null)
  const [activateSubTag, setActivateSubTag] = useState<string | null>(null)
  const [sidebarOpen, setSidebarOpen] = useState(false)

  const navigateToIndicator = useCallback((tag: string) => {
    const isSub = SUB_COMPONENT_TAGS.has(tag)
    const targetTag = isSub ? SUB_COMPONENT_PARENT[tag] : tag
    const entry = ESG_MAP[targetTag]
    if (!entry) return
    const bucket = entry.esg as ActiveView
    setActiveView(bucket)
    setHighlightedTag(targetTag)
    if (isSub) setActivateSubTag(tag)
    setTimeout(() => {
      document.getElementById(targetTag)?.scrollIntoView({ behavior: 'smooth', block: 'center' })
    }, 100)
    setTimeout(() => {
      setHighlightedTag(null)
      setActivateSubTag(null)
    }, 1600)
  }, [])

  return (
    <div className="flex h-dvh overflow-hidden bg-gray-50">
      {/* Hamburger — visible only below lg breakpoint */}
      <button
        onClick={() => setSidebarOpen(true)}
        className="lg:hidden fixed top-3 left-3 z-40 bg-gray-900 text-white p-2 rounded-lg shadow-md"
        aria-label="Open menu"
      >
        <svg xmlns="http://www.w3.org/2000/svg" className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
          <path strokeLinecap="round" strokeLinejoin="round" d="M4 6h16M4 12h16M4 18h16" />
        </svg>
      </button>

      <Sidebar
        activeView={activeView}
        onNavigate={setActiveView}
        isOpen={sidebarOpen}
        onClose={() => setSidebarOpen(false)}
      />

      <main className="flex-1 overflow-y-auto">
        {/* pt-14 on mobile reserves space below the fixed hamburger button */}
        <div className="max-w-5xl mx-auto py-8 px-6 pt-14 lg:pt-8">
          {activeView === 'E' || activeView === 'S' || activeView === 'G' ? (
            <ESGView bucket={activeView} highlightedTag={highlightedTag} activateSubTag={activateSubTag} />
          ) : activeView === 'search' ? (
            <SearchPanel onNavigate={navigateToIndicator} />
          ) : activeView === 'benchmark' ? (
            <BenchmarkPanel onNavigate={navigateToIndicator} />
          ) : (
            <AboutPanel />
          )}
        </div>
      </main>
    </div>
  )
}
