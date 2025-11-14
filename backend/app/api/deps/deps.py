"""Common API dependencies."""
from __future__ import annotations

from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from ...core.security import TokenError, decode_access_token
from ...db.session import get_db


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)]
) -> dict[str, str | int]:
    try:
        payload = decode_access_token(token)
    except TokenError as exc:
        raise exc

    if "sub" not in payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return payload


async def get_current_active_user(
    user: Annotated[dict[str, str | int], Depends(get_current_user)]
) -> dict[str, str | int]:
    if not user.get("is_active", True):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Inactive user")
    return user


async def get_admin_user(
    user: Annotated[dict[str, str | int], Depends(get_current_active_user)]
) -> dict[str, str | int]:
    if user.get("role") != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient rights")
    return user


DbSession = Annotated[AsyncSession, Depends(get_db)]
