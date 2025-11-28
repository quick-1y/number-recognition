from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime

from app.db.session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="viewer")
    disabled = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
