import axios from 'axios'

const api = axios.create({
  baseURL: `http://api:8000/`,
  headers: {
    "Content-Type": `application/json`,
  },
})

export async function generateGraph(body) {
  return await api.post(`get-graph`, body)
}