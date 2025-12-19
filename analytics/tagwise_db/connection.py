"""
Tagwise Database Connection
Stores tagged incident data for analytics
"""
from motor.motor_asyncio import AsyncIOMotorClient
from loguru import logger
import os


class TagwiseDatabase:
    """Tagwise database connection"""
    
    def __init__(self):
        """Initialize database connection"""
        self.client = None
        self.db = None
        self._connect()
    
    def _connect(self):
        """Connect to MongoDB"""
        try:
            mongodb_url = os.getenv("TAGWISE_DB_URL", "mongodb://localhost:27017")
            db_name = os.getenv("TAGWISE_DB_NAME", "shivay_tagwise")
            
            self.client = AsyncIOMotorClient(mongodb_url)
            self.db = self.client[db_name]
            
            logger.info(f"Connected to Tagwise database: {db_name}")
        except Exception as e:
            logger.error(f"Failed to connect to Tagwise database: {e}")
    
    async def tag_incident(
        self,
        incident_id: str,
        tags: dict,
    ):
        """Tag an incident"""
        try:
            await self.db.incidents.update_one(
                {"incident_id": incident_id},
                {"$set": {"tags": tags, "incident_id": incident_id}},
                upsert=True,
            )
            logger.info(f"Tagged incident: {incident_id}")
        except Exception as e:
            logger.error(f"Error tagging incident: {e}")
    
    async def get_tagged_incidents(self, filters: dict = None):
        """Get tagged incidents"""
        try:
            query = filters or {}
            cursor = self.db.incidents.find(query)
            incidents = await cursor.to_list(length=None)
            return incidents
        except Exception as e:
            logger.error(f"Error getting tagged incidents: {e}")
            return []

