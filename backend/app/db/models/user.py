"""User model with RBAC roles."""
from __future__ import annotations

from sqlalchemy import Boolean, Column, Integer, String

from ..session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, nullable=False)
    full_name = Column(String(128), nullable=True)
    hashed_password = Column(String(256), nullable=False)
    role = Column(String(32), nullable=False, default="viewer")
    is_active = Column(Boolean, default=True, nullable=False)
