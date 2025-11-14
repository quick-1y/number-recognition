"""Diagnostics routes for health checks and metrics references."""
from __future__ import annotations

from fastapi import APIRouter

router = APIRouter(prefix="/diagnostics", tags=["diagnostics"])


@router.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/ready")
async def ready() -> dict[str, str]:
    return {"status": "ready"}


@router.get("/live")
async def live() -> dict[str, str]:
    return {"status": "alive"}
