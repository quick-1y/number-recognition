from datetime import datetime
from typing import Any, Optional
from pydantic import BaseModel


class RecognitionCreate(BaseModel):
    channel_id: int
    channel_name: str
    plate_number: str
    confidence: float
    country_template: Optional[str] = None
    bbox: Optional[dict[str, Any]] = None
    direction: Optional[str] = None
    track_id: Optional[str] = None
    image_url: Optional[str] = None
    metadata: Optional[dict[str, Any]] = None


class RecognitionOut(RecognitionCreate):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True
