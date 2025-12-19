"""
Voice Call API endpoints
"""
from fastapi import APIRouter, Depends, HTTPException, status, Request, Form, Response
from typing import Optional
from twilio.twiml.voice_response import VoiceResponse

from app.schemas.calls import CallCreate, CallResponse, CallStatusUpdate
from app.services.call_service import CallService
from app.core.dependencies import get_current_active_user

router = APIRouter()


@router.post("/inbound", response_class=Response)
async def handle_inbound_call(request: Request):
    """Handle inbound call from Twilio/Exotel"""
    service = CallService()
    
    # Get call parameters
    call_sid = request.form.get("CallSid")
    from_number = request.form.get("From")
    to_number = request.form.get("To")
    
    # Create call record
    call_data = CallCreate(
        call_id=call_sid,
        from_number=from_number,
        to_number=to_number,
        direction="inbound",
    )
    call = await service.create_call(call_data)
    
    # Generate TwiML response
    response = VoiceResponse()
    response.say("Welcome to Shivay Emergency Response. Please describe your emergency.")
    response.record(
        action="/api/v1/calls/recording",
        method="POST",
        max_length=60,
        finish_on_key="#",
    )
    
    return Response(content=str(response), media_type="application/xml")


@router.post("/outbound", response_model=CallResponse, status_code=status.HTTP_201_CREATED)
async def initiate_outbound_call(
    call_data: CallCreate,
    current_user: dict = Depends(get_current_active_user),
):
    """Initiate outbound call"""
    service = CallService()
    call = await service.create_outbound_call(call_data)
    return call


@router.get("/{call_id}", response_model=CallResponse)
async def get_call(
    call_id: str,
    current_user: dict = Depends(get_current_active_user),
):
    """Get call details"""
    service = CallService()
    call = await service.get_call_by_id(call_id)
    if not call:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Call {call_id} not found",
        )
    return call


@router.post("/recording")
async def handle_recording(request: Request):
    """Handle call recording"""
    service = CallService()
    
    call_sid = request.form.get("CallSid")
    recording_url = request.form.get("RecordingUrl")
    recording_duration = request.form.get("RecordingDuration")
    
    await service.update_call_recording(
        call_id=call_sid,
        recording_url=recording_url,
        duration=recording_duration,
    )
    
    response = VoiceResponse()
    response.say("Thank you. Your emergency has been recorded. Help is on the way.")
    response.hangup()
    
    return Response(content=str(response), media_type="application/xml")


@router.post("/status", response_model=CallResponse)
async def update_call_status(
    status_data: CallStatusUpdate,
    current_user: dict = Depends(get_current_active_user),
):
    """Update call status"""
    service = CallService()
    call = await service.update_call_status(status_data.call_id, status_data.status)
    if not call:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Call {status_data.call_id} not found",
        )
    return call

