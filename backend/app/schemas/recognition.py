"""Schemas for recognition events."""
from __future__ import annotations

from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, Field


class RecognitionBase(BaseModel):
    channel_id: int
    plate_number: str
    confidence: float
    country_template: Optional[str] = None
    direction: Optional[str] = None
    track_id: Optional[str] = None
    timestamps: dict[str, Any]
    bbox: Optional[dict[str, Any]] = None
    metadata: Optional[dict[str, Any]] = None


class RecognitionCreate(RecognitionBase):
    pass


class Recognition(RecognitionBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
