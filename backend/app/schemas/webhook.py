"""Schemas for webhook subscriptions."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class WebhookSubscriptionBase(BaseModel):
    name: str = Field(..., max_length=128)
    url: str = Field(..., max_length=512)
    secret: Optional[str] = Field(None, max_length=128)
    events: str = Field("recognition", max_length=128)
    is_active: bool = True


class WebhookSubscriptionCreate(WebhookSubscriptionBase):
    pass


class WebhookSubscription(WebhookSubscriptionBase):
    id: int

    class Config:
        from_attributes = True
