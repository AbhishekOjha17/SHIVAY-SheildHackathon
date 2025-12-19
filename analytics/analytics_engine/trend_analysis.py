"""
Trend Analysis Engine
"""
import pandas as pd
from typing import Dict, Any, List
from datetime import datetime, timedelta
from loguru import logger


class TrendAnalysisEngine:
    """Engine for trend analysis"""
    
    def analyze_trends(
        self,
        data: List[Dict[str, Any]],
        metric: str,
        start_date: datetime,
        end_date: datetime,
    ) -> Dict[str, Any]:
        """Analyze trends for a metric"""
        try:
            df = pd.DataFrame(data)
            
            if df.empty:
                return {
                    "trend": "stable",
                    "change_percentage": 0.0,
                    "data_points": [],
                }
            
            # Convert dates
            if "date" in df.columns:
                df["date"] = pd.to_datetime(df["date"])
                df = df.sort_values("date")
            
            # Calculate trend
            if len(df) > 1:
                first_value = df[metric].iloc[0]
                last_value = df[metric].iloc[-1]
                
                if first_value > 0:
                    change_percentage = ((last_value - first_value) / first_value) * 100
                else:
                    change_percentage = 0.0
                
                if change_percentage > 5:
                    trend = "increasing"
                elif change_percentage < -5:
                    trend = "decreasing"
                else:
                    trend = "stable"
            else:
                trend = "stable"
                change_percentage = 0.0
            
            # Prepare data points
            data_points = df.to_dict("records")
            
            return {
                "trend": trend,
                "change_percentage": round(change_percentage, 2),
                "data_points": data_points,
            }
            
        except Exception as e:
            logger.error(f"Error analyzing trends: {e}")
            return {
                "trend": "stable",
                "change_percentage": 0.0,
                "data_points": [],
            }

