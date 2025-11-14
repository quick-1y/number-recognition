"""Channel model describing video inputs."""
from __future__ import annotations

from sqlalchemy import Boolean, Column, Integer, String

from ..session import Base


class Channel(Base):
    __tablename__ = "channels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False, unique=True)
    rtsp_url = Column(String(512), nullable=False)
    roi = Column(String, nullable=True)
    direction = Column(String(16), nullable=False, default="any")
    min_plate_px = Column(Integer, nullable=False, default=32)
    max_plate_px = Column(Integer, nullable=False, default=256)
    enabled = Column(Boolean, default=True, nullable=False)
