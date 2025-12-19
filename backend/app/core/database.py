"""
Database connection and configuration
"""
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from loguru import logger

from app.core.config import settings
from app.models.emergency import EmergencyCase
from app.models.transcript import CallerTranscript
from app.models.hospital import HospitalResource
from app.models.ambulance import AmbulanceTracking
from app.models.police import PoliceOfficerAction
from app.models.ai_recommendation import AIRecommendation
from app.models.location import LocationMetadata


# Global database client
client: AsyncIOMotorClient = None


async def init_db():
    """Initialize database connection"""
    global client
    
    try:
        client = AsyncIOMotorClient(
            settings.MONGODB_URL,
            maxPoolSize=10,
            minPoolSize=1,
        )
        
        # Initialize Beanie with document models
        await init_beanie(
            database=client[settings.MONGODB_DB_NAME],
            document_models=[
                EmergencyCase,
                CallerTranscript,
                HospitalResource,
                AmbulanceTracking,
                PoliceOfficerAction,
                AIRecommendation,
                LocationMetadata,
            ],
        )
        
        logger.info(f"Connected to MongoDB: {settings.MONGODB_DB_NAME}")
        
    except Exception as e:
        logger.error(f"Failed to connect to MongoDB: {e}")
        raise


async def close_db():
    """Close database connection"""
    global client
    
    if client:
        client.close()
        logger.info("MongoDB connection closed")


def get_database():
    """Get database instance"""
    return client[settings.MONGODB_DB_NAME]

