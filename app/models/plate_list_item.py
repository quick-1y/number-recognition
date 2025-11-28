from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.session import Base


class PlateListItem(Base):
    __tablename__ = "plate_list_items"

    id = Column(Integer, primary_key=True, index=True)
    plate_value = Column(String, nullable=False)
    comment = Column(Text, nullable=True)
    ttl = Column(DateTime, nullable=True)
    plate_list_id = Column(Integer, ForeignKey("plate_lists.id", ondelete="CASCADE"))
    created_at = Column(DateTime, default=datetime.utcnow)

    plate_list = relationship("PlateList", back_populates="items")
