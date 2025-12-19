'use client'

import { useEffect, useState } from 'react'
import { useWebSocket } from '@/hooks/useWebSocket'
import { useEmergencyCases } from '@/hooks/useEmergencyCases'
import DashboardStats from '@/components/dashboard/DashboardStats'
import EmergencyCasesList from '@/components/dashboard/EmergencyCasesList'
import AmbulanceMap from '@/components/dashboard/AmbulanceMap'
import HospitalLoad from '@/components/dashboard/HospitalLoad'

export default function DashboardPage() {
  const { connected } = useWebSocket()
  const { cases, loading } = useEmergencyCases()

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-3xl font-bold mb-6">Shivay Emergency Dashboard</h1>
        
        <div className="mb-4">
          <span className={`px-3 py-1 rounded-full text-sm ${
            connected ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
          }`}>
            {connected ? 'Connected' : 'Disconnected'}
          </span>
        </div>

        <DashboardStats />
        
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-6">
          <EmergencyCasesList cases={cases} loading={loading} />
          <AmbulanceMap />
        </div>

        <div className="mt-6">
          <HospitalLoad />
        </div>
      </div>
    </div>
  )
}

