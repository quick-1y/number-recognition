"""Schemas for automation scenarios."""
from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field


class ScenarioRule(BaseModel):
    name: str = Field(..., max_length=128)
    description: Optional[str] = Field(None, max_length=512)
    conditions: dict[str, Any]
    actions: dict[str, Any]
    is_active: bool = True
