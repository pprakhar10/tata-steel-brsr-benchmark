import { useState, useCallback } from 'react'
import { ESG_MAP, SUB_COMPONENT_TAGS, SUB_COMPONENT_PARENT } from './constants/esgMap'
import Sidebar from './components/Sidebar'
import ESGView from './components/ESGView'
import SearchPanel from './components/SearchPanel'
import BenchmarkPanel from './components/BenchmarkPanel'
import AboutPanel from './components/AboutPanel'

type ActiveView = 'E' | 'S' | 'G' | 'search' | 'benchmark' | 'about'

export default function App() {
  const [activeView, setActiveView] = useState<ActiveView>('about')
  const [highlightedTag, setHighlightedTag] = useState<string | null>(null)
  const [activateSubTag, setActivateSubTag] = useState<string | null>(null)
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
      <Sidebar
        activeView={activeView}
        onNavigate={setActiveView}
      />

      <main className="flex-1 overflow-y-auto">
        <div className="max-w-5xl mx-auto pt-16 pb-8 px-6 lg:pt-8">
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
