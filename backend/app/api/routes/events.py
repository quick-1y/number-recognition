"""Recognition event endpoints."""
from __future__ import annotations

from fastapi import APIRouter, HTTPException, status

from ...schemas import recognition as recognition_schema
from ...services.recognition_service import recognition_service
from ...services.webhook_service import webhook_service

router = APIRouter(prefix="/events", tags=["events"])


@router.get("", response_model=list[recognition_schema.Recognition])
async def list_events(limit: int = 100) -> list[recognition_schema.Recognition]:
    return recognition_service.list_events(limit=limit)


@router.post(
    "",
    response_model=recognition_schema.Recognition,
    status_code=status.HTTP_201_CREATED,
)
async def create_event(
    payload: recognition_schema.RecognitionCreate,
) -> recognition_schema.Recognition:
    event = recognition_service.add_event(payload)
    await webhook_service.dispatch("recognition", event.model_dump())
    return event
