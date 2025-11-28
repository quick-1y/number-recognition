from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, JSON

from app.db.session import Base


class Recognition(Base):
    __tablename__ = "recognitions"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    channel_id = Column(Integer, index=True)
    channel_name = Column(String, nullable=False)
    plate_number = Column(String, nullable=False)
    confidence = Column(Float, default=0.0)
    country_template = Column(String, nullable=True)
    bbox = Column(JSON, nullable=True)
    direction = Column(String, nullable=True)
    track_id = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    metadata = Column(JSON, nullable=True)
