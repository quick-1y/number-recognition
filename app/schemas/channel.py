from typing import Optional
from pydantic import BaseModel, Field


class ChannelBase(BaseModel):
    name: str
    rtsp_url: str
    roi: Optional[list[list[int]]] = None
    direction: str = Field(default="any", pattern="^(up|down|any)$")
    min_plate_px: int = 32
    max_plate_px: int = 512
    enabled: bool = True


class ChannelCreate(ChannelBase):
    pass


class ChannelUpdate(BaseModel):
    name: Optional[str] = None
    rtsp_url: Optional[str] = None
    roi: Optional[list[list[int]]] = None
    direction: Optional[str] = Field(default=None, pattern="^(up|down|any)$")
    min_plate_px: Optional[int] = None
    max_plate_px: Optional[int] = None
    enabled: Optional[bool] = None


class ChannelOut(ChannelBase):
    id: int

    class Config:
        from_attributes = True
