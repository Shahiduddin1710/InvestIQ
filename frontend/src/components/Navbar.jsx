import { NavLink } from 'react-router-dom'
import { Moon, Sun } from 'lucide-react'
import { motion } from 'framer-motion'

import { useState } from 'react'

export default function Navbar({ theme, onToggleTheme }) {
  const [menuOpen, setMenuOpen] = useState(false)

  const links = [
    { to: '/', label: 'Home' },
    { to: '/AI-Predictor', label: 'AI Predictor' },
    { to: '/top-50-stocks', label: 'Top 50 Stocks' },
    { to: '/why-investiq', label: 'Why InvestIQ?' },
    { to: '/about', label: 'About' },
  ]

  return (
   <nav className="navbar" style={{ minHeight: '64px', padding: '0 16px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', position: 'relative', gap: '8px' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
        <img src="/assets/name.png" alt="InvestIQ" style={{ height: '40px' }} />
      </div>

      {/* Hamburger */}
      <button
        onClick={() => setMenuOpen(o => !o)}
        style={{ display: 'none', flexDirection: 'column', gap: '5px', background: 'none', border: 'none', cursor: 'pointer', padding: '4px' }}
        className="nav-hamburger"
        aria-label="Toggle menu"
      >
        <span style={{ display: 'block', width: '25px', height: '2px', background: 'var(--text)' }} />
        <span style={{ display: 'block', width: '25px', height: '2px', background: 'var(--text)' }} />
        <span style={{ display: 'block', width: '25px', height: '2px', background: 'var(--text)' }} />
      </button>

      <div className={`nav-links-wrap${menuOpen ? ' open' : ''}`}>
        {links.map(({ to, label }) => (
          <NavLink
            key={to}
            to={to}
            end={to === '/'}
            className={({ isActive }) => `nav-link${isActive ? ' active' : ''}`}
            onClick={() => setMenuOpen(false)}
          >
            {label}
          </NavLink>
        ))}
        <motion.button
          className="theme-toggle-btn"
          style={{ marginLeft: '8px' }}
          onClick={onToggleTheme}
          whileTap={{ scale: 0.95 }}
        >
          {theme === 'dark'
            ? <><Moon size={14} /> Dark</>
            : <><Sun size={14} /> Light</>
          }
        </motion.button>
        <img src="/assets/line.gif" alt="line" style={{ height: '40px', marginLeft: '12px' }} />
      </div>
    </nav>
  )
}
