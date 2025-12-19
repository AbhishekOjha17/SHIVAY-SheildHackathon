"""
Action Systems Service - FastAPI application
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ambulance_dispatch.service import AmbulanceDispatchService
from hospital_notification.service import HospitalNotificationService
from police_alert.service import PoliceAlertService
from road_clearance.service import RoadClearanceService

app = FastAPI(
    title="Shivay Action Systems Service",
    description="Action and response execution systems",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
ambulance_service = AmbulanceDispatchService()
hospital_service = HospitalNotificationService()
police_service = PoliceAlertService()
road_clearance_service = RoadClearanceService()


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "service": "Shivay Action Systems",
        "status": "operational",
        "systems": [
            "ambulance_dispatch",
            "hospital_notification",
            "police_alert",
            "road_clearance",
        ],
    }


@app.post("/ambulance/dispatch")
async def dispatch_ambulance(request: dict):
    """Dispatch ambulance"""
    result = await ambulance_service.dispatch_ambulance(
        ambulance_id=request.get("ambulance_id"),
        case_id=request.get("case_id"),
        destination_lat=request.get("destination_lat"),
        destination_lng=request.get("destination_lng"),
        hospital_id=request.get("hospital_id"),
    )
    return result


@app.post("/hospital/notify")
async def notify_hospital(request: dict):
    """Notify hospital"""
    result = await hospital_service.notify_hospital(
        hospital_id=request.get("hospital_id"),
        case_id=request.get("case_id"),
        patient_info=request.get("patient_info", {}),
        eta_minutes=request.get("eta_minutes"),
    )
    return result


@app.post("/police/alert")
async def send_police_alert(request: dict):
    """Send police alert"""
    result = await police_service.send_alert(
        case_id=request.get("case_id"),
        severity=request.get("severity", "medium"),
        num_officers=request.get("num_officers", 3),
    )
    return result


@app.post("/road-clearance/request")
async def request_road_clearance(request: dict):
    """Request road clearance"""
    result = await road_clearance_service.request_clearance(
        case_id=request.get("case_id"),
        route=request.get("route", {}),
        priority=request.get("priority", "high"),
    )
    return result

