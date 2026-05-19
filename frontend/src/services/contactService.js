import api from './api'

export async function sendContactMessage(name, email, message) {
  const { data } = await api.post('/contact', { name, email, message })
  return data
}
