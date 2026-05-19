import { BrowserRouter, Routes, Route, useLocation } from 'react-router-dom'
import { useTheme } from './hooks/useTheme'
import Navbar from './components/Navbar'
import Home from './pages/Home'
import AIPredictor from './pages/AIPredictor'
import Top50Stocks from './pages/Top50Stocks'
import WhyInvestIQ from './pages/WhyInvestIQ'
import About from './pages/About'

function AppRoutes({ theme }) {
  const location = useLocation()
  const isPredictor = location.pathname === '/AI-Predictor'

  return (
    <>
      <div style={{ display: isPredictor ? 'block' : 'none' }}>
        <AIPredictor theme={theme} />
      </div>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/top-50-stocks" element={<Top50Stocks />} />
        <Route path="/why-investiq" element={<WhyInvestIQ />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </>
  )
}

export default function App() {
  const { theme, toggleTheme } = useTheme()

  return (
    <BrowserRouter>
      <Navbar theme={theme} onToggleTheme={toggleTheme} />
      <AppRoutes theme={theme} />
    </BrowserRouter>
  )
}