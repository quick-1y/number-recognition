"""Schemas for plate lists and items."""
from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class PlateListItemBase(BaseModel):
    pattern: str = Field(..., max_length=64)
    comment: Optional[str] = Field(None, max_length=256)
    ttl: Optional[datetime] = None


class PlateListItemCreate(PlateListItemBase):
    pass


class PlateListItem(PlateListItemBase):
    id: int

    class Config:
        from_attributes = True


class PlateListBase(BaseModel):
    name: str = Field(..., max_length=128)
    list_type: str = Field(..., pattern="^(white|black|info)$")
    priority: int = 0


class PlateListCreate(PlateListBase):
    items: list[PlateListItemCreate] | None = None


class PlateList(PlateListBase):
    id: int
    items: list[PlateListItem] = []

    class Config:
        from_attributes = True
