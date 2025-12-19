"""
Communication AI Agent
Handles outbound calls and SMS via Twilio/Exotel
"""
from typing import Dict, Any, Optional
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Gather
from loguru import logger
import os


class CommunicationAIAgent:
    """Agent for communication (calls, SMS)"""
    
    def __init__(self):
        """Initialize the agent"""
        self.twilio_client = None
        self._initialize_twilio()
    
    def _initialize_twilio(self):
        """Initialize Twilio client"""
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        
        if account_sid and auth_token:
            try:
                self.twilio_client = Client(account_sid, auth_token)
                logger.info("Twilio client initialized")
            except Exception as e:
                logger.error(f"Failed to initialize Twilio: {e}")
        else:
            logger.warning("Twilio credentials not found")
    
    async def make_outbound_call(
        self,
        to_number: str,
        message: str,
        case_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Make outbound call"""
        if not self.twilio_client:
            return {
                "success": False,
                "error": "Twilio client not initialized",
            }
        
        try:
            from_number = os.getenv("TWILIO_PHONE_NUMBER")
            
            call = self.twilio_client.calls.create(
                to=to_number,
                from_=from_number,
                url=f"https://your-domain.com/api/v1/calls/voice-response?message={message}",
                method="GET",
            )
            
            logger.info(f"Outbound call initiated: {call.sid}")
            
            return {
                "success": True,
                "call_sid": call.sid,
                "status": call.status,
            }
            
        except Exception as e:
            logger.error(f"Error making outbound call: {e}")
            return {
                "success": False,
                "error": str(e),
            }
    
    async def send_sms(
        self,
        to_number: str,
        message: str,
        case_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Send SMS"""
        if not self.twilio_client:
            return {
                "success": False,
                "error": "Twilio client not initialized",
            }
        
        try:
            from_number = os.getenv("TWILIO_PHONE_NUMBER")
            
            message_obj = self.twilio_client.messages.create(
                to=to_number,
                from_=from_number,
                body=message,
            )
            
            logger.info(f"SMS sent: {message_obj.sid}")
            
            return {
                "success": True,
                "message_sid": message_obj.sid,
                "status": message_obj.status,
            }
            
        except Exception as e:
            logger.error(f"Error sending SMS: {e}")
            return {
                "success": False,
                "error": str(e),
            }
    
    def generate_voice_response(self, message: str) -> str:
        """Generate TwiML voice response"""
        response = VoiceResponse()
        response.say(message, voice="alice", language="en-IN")
        
        # Add gather for user input
        gather = Gather(
            input="speech",
            action="/api/v1/calls/process-speech",
            method="POST",
        )
        gather.say("Please respond with your status.")
        response.append(gather)
        
        return str(response)
    
    async def process_speech_input(self, speech_result: str) -> Dict[str, Any]:
        """Process speech input from call"""
        logger.info(f"Processing speech input: {speech_result}")
        
        # In a real implementation, this would use NLP to understand the response
        return {
            "understood": True,
            "intent": "status_update",
            "entities": {},
        }

