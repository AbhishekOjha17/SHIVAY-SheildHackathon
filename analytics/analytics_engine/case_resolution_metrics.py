"""
Case Resolution Metrics
"""
from typing import Dict, Any, List
from datetime import datetime, timedelta
from loguru import logger


class CaseResolutionMetrics:
    """Metrics for case resolution"""
    
    def calculate_metrics(self, cases: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate resolution metrics"""
        if not cases:
            return {
                "total_cases": 0,
                "resolved_cases": 0,
                "resolution_rate": 0.0,
                "avg_resolution_time": 0.0,
            }
        
        total = len(cases)
        resolved = sum(1 for c in cases if c.get("status") == "resolved")
        resolution_rate = (resolved / total * 100) if total > 0 else 0.0
        
        # Calculate average resolution time
        resolution_times = []
        for case in cases:
            if case.get("status") == "resolved" and case.get("resolved_at"):
                created = case.get("created_at")
                resolved = case.get("resolved_at")
                if created and resolved:
                    try:
                        if isinstance(created, str):
                            created = datetime.fromisoformat(created)
                        if isinstance(resolved, str):
                            resolved = datetime.fromisoformat(resolved)
                        delta = resolved - created
                        resolution_times.append(delta.total_seconds() / 60)  # minutes
                    except:
                        pass
        
        avg_resolution_time = (
            sum(resolution_times) / len(resolution_times)
            if resolution_times
            else 0.0
        )
        
        return {
            "total_cases": total,
            "resolved_cases": resolved,
            "resolution_rate": round(resolution_rate, 2),
            "avg_resolution_time": round(avg_resolution_time, 2),
        }

