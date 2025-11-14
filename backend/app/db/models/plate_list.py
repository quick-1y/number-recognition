"""Models describing plate lists and list items."""
from __future__ import annotations

from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..session import Base


class PlateList(Base):
    __tablename__ = "plate_lists"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True, nullable=False)
    list_type = Column(String(32), nullable=False)
    priority = Column(Integer, default=0, nullable=False)

    items = relationship("PlateListItem", back_populates="plate_list", cascade="all, delete")


class PlateListItem(Base):
    __tablename__ = "plate_list_items"

    id = Column(Integer, primary_key=True)
    plate_list_id = Column(Integer, ForeignKey("plate_lists.id", ondelete="CASCADE"))
    pattern = Column(String(64), nullable=False)
    comment = Column(String(256), nullable=True)
    ttl = Column(DateTime, nullable=True)

    plate_list = relationship("PlateList", back_populates="items")
