"""Authentication endpoints."""
from __future__ import annotations

from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext

from ...core.config import settings
from ...core.security import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# This demo user store would be replaced with database-backed implementation.
FAKE_USERS_DB = {
    "admin": {
        "username": "admin",
        "full_name": "Default Admin",
        "hashed_password": pwd_context.hash("admin"),
        "role": "admin",
        "is_active": True,
    }
}


@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> dict[str, str]:
    user = FAKE_USERS_DB.get(form_data.username)
    if not user or not pwd_context.verify(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = create_access_token(
        {
            "sub": user["username"],
            "role": user["role"],
            "full_name": user["full_name"],
            "is_active": user["is_active"],
        },
        expires_delta=settings.JWT_EXPIRATION_SECONDS,
    )
    return {"access_token": token, "token_type": "bearer"}
