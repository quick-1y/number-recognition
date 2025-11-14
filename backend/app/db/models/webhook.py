"""Webhook subscription and delivery models."""
from __future__ import annotations

from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, JSON, String

from ..session import Base


class WebhookSubscription(Base):
    __tablename__ = "webhook_subscriptions"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    url = Column(String(512), nullable=False)
    secret = Column(String(128), nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    events = Column(String(128), default="recognition", nullable=False)


class WebhookDelivery(Base):
    __tablename__ = "webhook_deliveries"

    id = Column(Integer, primary_key=True)
    subscription_id = Column(
        Integer, ForeignKey("webhook_subscriptions.id", ondelete="CASCADE"), nullable=False
    )
    payload = Column(JSON, nullable=False)
    status_code = Column(Integer, nullable=True)
    response_body = Column(String, nullable=True)
    attempts = Column(Integer, default=0, nullable=False)
    last_attempt_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    success = Column(Boolean, default=False, nullable=False)
