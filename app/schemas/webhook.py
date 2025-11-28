from datetime import datetime
from typing import Any, Optional
from pydantic import BaseModel


class WebhookSubscriptionCreate(BaseModel):
    url: str
    secret: Optional[str] = None
    active: bool = True
    description: Optional[str] = None


class WebhookSubscriptionOut(WebhookSubscriptionCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class WebhookDeliveryOut(BaseModel):
    id: int
    subscription_id: int
    status: str
    payload: dict[str, Any]
    attempt: int
    response_code: Optional[int] = None
    error: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
