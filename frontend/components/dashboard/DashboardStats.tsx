'use client'

import { useEffect, useState } from 'react'
import apiClient from '@/lib/api/client'

export default function DashboardStats() {
  const [stats, setStats] = useState({
    total_cases: 0,
    active_cases: 0,
    resolved_cases: 0,
  })

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const response = await apiClient.get('/analytics/dashboard')
        setStats(response.data)
      } catch (error) {
        console.error('Error fetching stats:', error)
      }
    }

    fetchStats()
    const interval = setInterval(fetchStats, 30000)
    return () => clearInterval(interval)
  }, [])

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div className="bg-white p-6 rounded-lg shadow">
        <h3 className="text-sm font-medium text-gray-500">Total Cases</h3>
        <p className="text-3xl font-bold mt-2">{stats.total_cases}</p>
      </div>
      <div className="bg-white p-6 rounded-lg shadow">
        <h3 className="text-sm font-medium text-gray-500">Active Cases</h3>
        <p className="text-3xl font-bold mt-2 text-yellow-600">{stats.active_cases}</p>
      </div>
      <div className="bg-white p-6 rounded-lg shadow">
        <h3 className="text-sm font-medium text-gray-500">Resolved Cases</h3>
        <p className="text-3xl font-bold mt-2 text-green-600">{stats.resolved_cases}</p>
      </div>
    </div>
  )
}

