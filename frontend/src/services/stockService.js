import api from './api'

export async function fetchTickerInfo(ticker) {
  const { data } = await api.get(`/stock/info/${ticker}`)
  return data
}

export async function fetchStockPrice(ticker, startDate, endDate, theme = 'dark') {
  const { data } = await api.get('/stock/price', {
    params: { ticker, start_date: startDate, end_date: endDate, theme }
  })
  return data
}

export async function fetchStockIndicators(ticker, startDate, endDate, theme = 'dark') {
  const { data } = await api.get('/stock/indicators', {
    params: { ticker, start_date: startDate, end_date: endDate, theme }
  })
  return data
}
export async function fetchForecast(ticker, nDays, theme) {
  const { data } = await api.post('/stock/forecast', { ticker, n_days: nDays, theme })
  return data
}
