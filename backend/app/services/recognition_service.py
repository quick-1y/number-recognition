"""Recognition event storage and retrieval."""
from __future__ import annotations

from collections import deque
from datetime import datetime

from ..schemas import recognition as recognition_schema


class RecognitionService:
    def __init__(self) -> None:
        self._events: deque[recognition_schema.Recognition] = deque(maxlen=1000)
        self._counter = 0

    def add_event(self, payload: recognition_schema.RecognitionCreate) -> recognition_schema.Recognition:
        self._counter += 1
        event = recognition_schema.Recognition(
            id=self._counter, created_at=datetime.utcnow(), **payload.model_dump()
        )
        self._events.appendleft(event)
        return event

    def list_events(self, limit: int = 100) -> list[recognition_schema.Recognition]:
        return list(list(self._events)[:limit])


recognition_service = RecognitionService()
