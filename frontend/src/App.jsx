import { useState } from 'react'
import { ArrowDown, ArrowRight, ArrowUpRight, BookOpen, Check, CircleHelp, Compass, FileText, Globe2, LoaderCircle, Search, Sparkles } from 'lucide-react'

const suggestions = [
  { icon: Globe2, label: 'Technology', topic: 'How are AI agents changing software development?' },
  { icon: Compass, label: 'Science', topic: 'What are the latest advances in fusion energy?' },
  { icon: BookOpen, label: 'Business', topic: 'How is the global semiconductor industry evolving?' },
]

function App() {
  const [topic, setTopic] = useState('')
  const [report, setReport] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  async function research(value = topic) {
    const cleanTopic = value.trim()
    if (!cleanTopic || loading) return
    setTopic(cleanTopic)
    setLoading(true)
    setError('')
    setReport(null)
    try {
      const response = await fetch('/api/research', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ topic: cleanTopic }),
      })
      const data = await response.json()
      if (!response.ok) throw new Error(data.detail || 'The report could not be generated.')
      setReport(data)
    } catch (err) {
      setError(err.message || 'Could not reach the research API. Make sure the backend is running.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app-shell">
      <aside className="sidebar">
        <a className="brand" href="#top" aria-label="Research Desk home">
          <span className="brand-mark"><Sparkles size={17} strokeWidth={2.2} /></span>
          <span>fieldnotes<span className="brand-dot">.</span></span>
        </a>
        <div className="side-label">WORKSPACE</div>
        <button className="nav-item active"><FileText size={17} /> New research <span className="nav-shortcut">⌘ N</span></button>
        <div className="sidebar-bottom">
          <div className="sidebar-note"><div className="note-icon"><Sparkles size={16} /></div><div><strong>Curiosity, organized.</strong><p>Turn a question into a clear, sourced report.</p></div></div>
          <a className="help-link" href="mailto:support@example.com"><CircleHelp size={16} /> Help & feedback</a>
          <div className="profile"><div className="avatar">R</div><div><strong>Researcher</strong><span>Personal workspace</span></div><ArrowDown size={15} /></div>
        </div>
      </aside>

      <main id="top" className="main-area">
        <header className="topbar"><div className="breadcrumb">Workspace <span>/</span> <b>New research</b></div><div className="topbar-right"><span className="status-dot" /> Your research stays yours</div></header>
        <div className={`content ${report ? 'content-results' : ''}`}>
          {!report && !loading && <section className="hero">
            <div className="eyebrow"><span className="eyebrow-line" /> YOUR NEXT DEEP DIVE</div>
            <h1>Good questions<br />lead <em>somewhere.</em></h1>
            <p className="hero-copy">A thoughtful research brief, grounded in real sources.<br className="desktop-break" /> Start with whatever’s on your mind.</p>
            <form className="search-card" onSubmit={(event) => { event.preventDefault(); research() }}>
              <label className="sr-only" htmlFor="topic">What would you like to explore?</label>
              <Search size={19} className="search-icon" />
              <input id="topic" value={topic} onChange={(event) => setTopic(event.target.value)} placeholder="What would you like to explore?" maxLength={500} />
              <button className="submit-button" type="submit" disabled={!topic.trim()} aria-label="Start research"><ArrowRight size={18} /></button>
              <div className="search-foot"><span><Sparkles size={13} /> Usually takes about a minute</span><span>{topic.length}/500</span></div>
            </form>
            <div className="suggestions"><span className="suggestion-heading">A FEW PLACES TO START</span><div className="suggestion-grid">{suggestions.map(({ icon: Icon, label, topic: prompt }) => <button key={label} className="suggestion" onClick={() => research(prompt)}><span className="suggestion-icon"><Icon size={16} /></span><span><small>{label}</small><strong>{prompt}</strong></span><ArrowUpRight size={15} className="suggestion-arrow" /></button>)}</div></div>
            {error && <div role="alert" className="error-banner">{error}</div>}
          </section>}

          {loading && <section className="loading-state" aria-live="polite"><div className="loader-orbit"><span /><Sparkles size={21} /></div><div className="eyebrow"><span className="eyebrow-line" /> WORKING ON YOUR BRIEF</div><h2>Following the question<br />where it leads.</h2><p>Looking for useful sources and bringing the findings together.</p><div className="loading-topic"><Search size={15} /> {topic}</div></section>}

          {report && <article className="report">
            <button className="back-button" onClick={() => { setReport(null); setError('') }}>← New research</button>
            <div className="report-kicker"><span className="eyebrow-line" /> RESEARCH BRIEF</div>
            <h1>{report.title}</h1>
            <p className="report-topic"><Search size={14} /> {topic}</p>
            <section className="report-section summary-section"><div className="section-index">01</div><div><h2>At a glance</h2><p>{report.summary}</p></div></section>
            <section className="report-section"><div className="section-index">02</div><div><h2>Key findings</h2><ul className="finding-list">{report.key_findings?.map((finding, index) => <li key={index}><span><Check size={14} /></span>{finding}</li>)}</ul></div></section>
            <section className="report-section"><div className="section-index">03</div><div><h2>Conclusion</h2><p>{report.conclusion}</p></div></section>
            <section className="report-section sources-section"><div className="section-index">04</div><div><h2>Sources <span className="source-count">{report.sources?.length || 0}</span></h2><ol className="source-list">{report.sources?.map((source, index) => <li key={`${source}-${index}`}><span className="source-number">{String(index + 1).padStart(2, '0')}</span><a href={source} target="_blank" rel="noreferrer">{source}<ArrowUpRight size={14} /></a></li>)}</ol></div></section>
            <div className="report-end"><span /><span>End of brief</span><span /></div>
          </article>}
        </div>
        <footer className="page-footer"><span>Made for the questions worth asking.</span><span>Powered by research, not guesswork <Sparkles size={12} /></span></footer>
      </main>
    </div>
  )
}

export default App
