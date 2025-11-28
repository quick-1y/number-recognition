from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PlateListItemBase(BaseModel):
    plate_value: str
    comment: Optional[str] = None
    ttl: Optional[datetime] = None


class PlateListItemCreate(PlateListItemBase):
    pass


class PlateListItemOut(PlateListItemBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class PlateListBase(BaseModel):
    name: str
    type: str
    priority: int = 100
    schedule: Optional[str] = None
    active: bool = True


class PlateListCreate(PlateListBase):
    items: list[PlateListItemCreate] = []


class PlateListOut(PlateListBase):
    id: int
    items: list[PlateListItemOut] = []

    class Config:
        from_attributes = True
