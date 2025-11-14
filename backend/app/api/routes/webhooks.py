"""Webhook subscription endpoints."""
from __future__ import annotations

from fastapi import APIRouter, HTTPException, status

from ...schemas import webhook as webhook_schema
from ...services.webhook_service import webhook_service

router = APIRouter(prefix="/webhooks", tags=["webhooks"])


@router.get("", response_model=list[webhook_schema.WebhookSubscription])
async def list_webhook_subscriptions() -> list[webhook_schema.WebhookSubscription]:
    return webhook_service.list_subscriptions()


@router.post(
    "",
    response_model=webhook_schema.WebhookSubscription,
    status_code=status.HTTP_201_CREATED,
)
async def create_webhook_subscription(
    payload: webhook_schema.WebhookSubscriptionCreate,
) -> webhook_schema.WebhookSubscription:
    return webhook_service.create_subscription(payload)
