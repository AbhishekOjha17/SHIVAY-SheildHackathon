'use client'

interface EmergencyCasesListProps {
  cases: any[]
  loading: boolean
}

export default function EmergencyCasesList({ cases, loading }: EmergencyCasesListProps) {
  if (loading) {
    return (
      <div className="bg-white p-6 rounded-lg shadow">
        <h2 className="text-xl font-bold mb-4">Emergency Cases</h2>
        <p>Loading...</p>
      </div>
    )
  }

  return (
    <div className="bg-white p-6 rounded-lg shadow">
      <h2 className="text-xl font-bold mb-4">Emergency Cases</h2>
      <div className="space-y-4">
        {cases.length === 0 ? (
          <p className="text-gray-500">No active cases</p>
        ) : (
          cases.map((caseItem) => (
            <div key={caseItem.case_id} className="border-b pb-4">
              <div className="flex justify-between items-start">
                <div>
                  <h3 className="font-semibold">{caseItem.case_id}</h3>
                  <p className="text-sm text-gray-600">{caseItem.emergency_type}</p>
                  <p className="text-sm text-gray-500">{caseItem.location_address}</p>
                </div>
                <span className={`px-2 py-1 rounded text-xs ${
                  caseItem.severity_level === 'critical' ? 'bg-red-100 text-red-800' :
                  caseItem.severity_level === 'high' ? 'bg-orange-100 text-orange-800' :
                  'bg-yellow-100 text-yellow-800'
                }`}>
                  {caseItem.severity_level}
                </span>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  )
}

