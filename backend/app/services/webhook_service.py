"""Webhook delivery service."""
from __future__ import annotations

import hashlib
import hmac
import json
from collections import OrderedDict
from typing import Optional

import httpx

from ..schemas import webhook as webhook_schema


class WebhookService:
    def __init__(self) -> None:
        self._subscriptions: "OrderedDict[int, webhook_schema.WebhookSubscription]" = OrderedDict()
        self._counter = 0

    def list_subscriptions(self) -> list[webhook_schema.WebhookSubscription]:
        return list(self._subscriptions.values())

    def create_subscription(
        self, payload: webhook_schema.WebhookSubscriptionCreate
    ) -> webhook_schema.WebhookSubscription:
        self._counter += 1
        subscription = webhook_schema.WebhookSubscription(id=self._counter, **payload.model_dump())
        self._subscriptions[self._counter] = subscription
        return subscription

    async def dispatch(self, event: str, payload: dict) -> None:
        for subscription in self._subscriptions.values():
            if not subscription.is_active or event not in subscription.events.split(","):
                continue
            await self._deliver(subscription, payload)

    async def _deliver(
        self, subscription: webhook_schema.WebhookSubscription, payload: dict
    ) -> None:
        headers = {"Content-Type": "application/json"}
        body = json.dumps(payload)
        if subscription.secret:
            signature = hmac.new(
                subscription.secret.encode(), body.encode(), hashlib.sha256
            ).hexdigest()
            headers["X-Signature"] = signature
        async with httpx.AsyncClient() as client:
            try:
                await client.post(subscription.url, content=body, headers=headers, timeout=5)
            except httpx.HTTPError:
                # In production, the delivery would be retried with backoff and persisted.
                pass


webhook_service = WebhookService()
