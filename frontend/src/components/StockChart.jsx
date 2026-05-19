import { lazy, Suspense } from 'react'
import LoadingSkeleton from './LoadingSkeleton'

const Plot = lazy(() => import('react-plotly.js'))

const GRAPH_CONFIG = {
  displayModeBar: true,
  displaylogo: false,
modeBarButtonsToRemove: [
    'lasso2d', 'select2d', 'autoScale2d',
    'hoverClosestCartesian', 'hoverCompareCartesian', 'toggleSpikelines'
  ],
  toImageButtonOptions: {
    format: 'png',
    filename: 'InvestIQ_Chart',
    height: 600,
    width: 1200,
    scale: 2
  },
  modeBarButtonsToAdd: []
}

export default function StockChart({ figure, title }) {
  if (!figure) return null

  const config = {
    ...GRAPH_CONFIG,
    toImageButtonOptions: {
      ...GRAPH_CONFIG.toImageButtonOptions,
      filename: `InvestIQ_${title}_Chart`
    }
  }

const figureKey = `${title}_${figure.layout?.template?.layout?.colorway?.[0] ?? figure.layout?.paper_bgcolor ?? 'default'}`

  return (
    <Suspense fallback={<LoadingSkeleton height={500} />}>
      <div style={{ borderRadius: '15px', overflow: 'hidden', marginBottom: '20px' }}>
        <Plot
          key={figureKey}
          data={figure.data}
          layout={figure.layout}
          config={config}
          style={{ width: '100%' }}
          useResizeHandler
        />
      </div>
    </Suspense>
  )
}
