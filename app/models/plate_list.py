from sqlalchemy import Column, Integer, String, Enum, Boolean
from sqlalchemy.orm import relationship

from app.db.session import Base


class PlateList(Base):
    __tablename__ = "plate_lists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    priority = Column(Integer, default=100)
    schedule = Column(String, nullable=True)
    active = Column(Boolean, default=True)

    items = relationship("PlateListItem", back_populates="plate_list", cascade="all, delete-orphan")
