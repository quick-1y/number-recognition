"""Recognition event model."""
from __future__ import annotations

from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, JSON, String
from sqlalchemy.orm import relationship

from ..session import Base


class Recognition(Base):
    __tablename__ = "recognitions"

    id = Column(Integer, primary_key=True)
    channel_id = Column(Integer, ForeignKey("channels.id", ondelete="CASCADE"), nullable=False)
    plate_number = Column(String(32), index=True, nullable=False)
    confidence = Column(Float, nullable=False)
    country_template = Column(String(16), nullable=True)
    direction = Column(String(16), nullable=True)
    track_id = Column(String(64), nullable=True)
    timestamps = Column(JSON, nullable=False, default=dict)
    bbox = Column(JSON, nullable=True)
    metadata = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    channel = relationship("Channel")
