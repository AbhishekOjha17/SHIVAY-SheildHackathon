"""
Ambulance Dispatch System
GPS tracking, route optimization, ETA calculation
"""
from typing import Dict, Any, Optional
from datetime import datetime, timedelta
from loguru import logger
import googlemaps
import os


class AmbulanceDispatchService:
    """Service for ambulance dispatch and tracking"""
    
    def __init__(self):
        """Initialize the service"""
        api_key = os.getenv("GOOGLE_MAPS_API_KEY")
        if api_key:
            self.gmaps = googlemaps.Client(key=api_key)
        else:
            self.gmaps = None
            logger.warning("Google Maps API key not found")
    
    async def dispatch_ambulance(
        self,
        ambulance_id: str,
        case_id: str,
        destination_lat: float,
        destination_lng: float,
        hospital_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Dispatch ambulance to emergency location"""
        logger.info(f"Dispatching ambulance {ambulance_id} to case {case_id}")
        
        # Get current ambulance location
        current_location = await self._get_ambulance_location(ambulance_id)
        
        if not current_location:
            return {
                "success": False,
                "error": "Ambulance location not found",
            }
        
        # Calculate route and ETA
        route_data = await self._calculate_route(
            current_location["lat"],
            current_location["lng"],
            destination_lat,
            destination_lng,
        )
        
        # Update ambulance status
        await self._update_ambulance_status(
            ambulance_id,
            status="dispatched",
            case_id=case_id,
            destination_hospital_id=hospital_id,
            eta_minutes=route_data.get("eta_minutes"),
            route_distance_km=route_data.get("distance_km"),
        )
        
        return {
            "success": True,
            "ambulance_id": ambulance_id,
            "case_id": case_id,
            "eta_minutes": route_data.get("eta_minutes"),
            "route_distance_km": route_data.get("distance_km"),
        }
    
    async def update_tracking(
        self,
        ambulance_id: str,
        lat: float,
        lng: float,
    ) -> Dict[str, Any]:
        """Update ambulance GPS tracking"""
        logger.info(f"Updating tracking for ambulance {ambulance_id}")
        
        # Update location in database
        await self._update_ambulance_location(ambulance_id, lat, lng)
        
        # Recalculate ETA if ambulance is en route
        ambulance = await self._get_ambulance(ambulance_id)
        if ambulance and ambulance.get("status") == "en_route":
            case = await self._get_case(ambulance.get("assigned_case"))
            if case:
                route_data = await self._calculate_route(
                    lat,
                    lng,
                    case["location_lat"],
                    case["location_lng"],
                )
                await self._update_ambulance_status(
                    ambulance_id,
                    eta_minutes=route_data.get("eta_minutes"),
                )
        
        return {
            "success": True,
            "ambulance_id": ambulance_id,
            "location": {"lat": lat, "lng": lng},
        }
    
    async def _calculate_route(
        self,
        origin_lat: float,
        origin_lng: float,
        dest_lat: float,
        dest_lng: float,
    ) -> Dict[str, Any]:
        """Calculate route using Google Maps"""
        if not self.gmaps:
            # Mock route calculation
            return {
                "eta_minutes": 15,
                "distance_km": 5.0,
                "route": [],
            }
        
        try:
            directions = self.gmaps.directions(
                (origin_lat, origin_lng),
                (dest_lat, dest_lng),
                mode="driving",
                traffic_model="best_guess",
            )
            
            if directions:
                route = directions[0]
                leg = route["legs"][0]
                
                duration_seconds = leg["duration"]["value"]
                distance_meters = leg["distance"]["value"]
                
                return {
                    "eta_minutes": int(duration_seconds / 60),
                    "distance_km": round(distance_meters / 1000, 2),
                    "route": route,
                }
        except Exception as e:
            logger.error(f"Error calculating route: {e}")
        
        return {
            "eta_minutes": 15,
            "distance_km": 5.0,
            "route": [],
        }
    
    async def _get_ambulance_location(self, ambulance_id: str) -> Optional[Dict[str, Any]]:
        """Get current ambulance location"""
        # In real implementation, query database
        return {"lat": 28.6139, "lng": 77.2090}
    
    async def _update_ambulance_location(self, ambulance_id: str, lat: float, lng: float):
        """Update ambulance location in database"""
        # In real implementation, update database
        pass
    
    async def _update_ambulance_status(self, ambulance_id: str, **kwargs):
        """Update ambulance status"""
        # In real implementation, update database
        pass
    
    async def _get_ambulance(self, ambulance_id: str) -> Optional[Dict[str, Any]]:
        """Get ambulance data"""
        # In real implementation, query database
        return None
    
    async def _get_case(self, case_id: str) -> Optional[Dict[str, Any]]:
        """Get case data"""
        # In real implementation, query database
        return None

