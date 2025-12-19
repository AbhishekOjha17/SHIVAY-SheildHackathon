'use client'

import { useEffect, useState } from 'react'
import apiClient from '@/lib/api/client'

export function useEmergencyCases() {
  const [cases, setCases] = useState<any[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const fetchCases = async () => {
      try {
        setLoading(true)
        const response = await apiClient.get('/emergency/')
        setCases(response.data.cases || [])
      } catch (err: any) {
        setError(err.message)
      } finally {
        setLoading(false)
      }
    }

    fetchCases()

    // Refresh every 30 seconds
    const interval = setInterval(fetchCases, 30000)

    return () => clearInterval(interval)
  }, [])

  return { cases, loading, error }
}

