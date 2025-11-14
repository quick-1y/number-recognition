"""Pydantic schemas for channels."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class ChannelBase(BaseModel):
    name: str = Field(..., max_length=128)
    rtsp_url: str
    roi: Optional[str] = None
    direction: str = Field("any", pattern="^(any|up|down)$")
    min_plate_px: int = Field(ge=1)
    max_plate_px: int = Field(ge=1)
    enabled: bool = True


class ChannelCreate(ChannelBase):
    pass


class ChannelUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=128)
    rtsp_url: Optional[str] = None
    roi: Optional[str] = None
    direction: Optional[str] = Field(None, pattern="^(any|up|down)$")
    min_plate_px: Optional[int] = Field(None, ge=1)
    max_plate_px: Optional[int] = Field(None, ge=1)
    enabled: Optional[bool] = None


class Channel(ChannelBase):
    id: int

    class Config:
        from_attributes = True
