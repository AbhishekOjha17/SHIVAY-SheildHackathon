"""
FastAPI dependencies
"""
from typing import Generator
from fastapi import Depends, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient

from app.core.database import get_database
from app.core.security import get_current_user


async def get_db() -> Generator:
    """Get database dependency"""
    db = get_database()
    try:
        yield db
    finally:
        pass


async def get_current_active_user(user: dict = Depends(get_current_user)) -> dict:
    """Get current active user"""
    # Add user validation logic here
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not authenticated",
        )
    return user

