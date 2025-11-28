from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON

from app.db.session import Base


class WebhookSubscription(Base):
    __tablename__ = "webhook_subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)
    secret = Column(String, nullable=True)
    active = Column(Boolean, default=True)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class WebhookDelivery(Base):
    __tablename__ = "webhook_deliveries"

    id = Column(Integer, primary_key=True, index=True)
    subscription_id = Column(Integer, nullable=False)
    status = Column(String, nullable=False)
    payload = Column(JSON, nullable=False)
    attempt = Column(Integer, default=1)
    response_code = Column(Integer, nullable=True)
    error = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
