from sqlalchemy import Column, Integer, String, Boolean, JSON

from app.db.session import Base


class Channel(Base):
    __tablename__ = "channels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    rtsp_url = Column(String, nullable=False)
    roi = Column(JSON, nullable=True)
    direction = Column(String, default="any")
    min_plate_px = Column(Integer, default=32)
    max_plate_px = Column(Integer, default=512)
    enabled = Column(Boolean, default=True)
