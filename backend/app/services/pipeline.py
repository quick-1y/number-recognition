"""Video processing pipeline building blocks."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable


@dataclass
class FramePacket:
    channel_id: int
    frame_id: int
    image: Any
    timestamp: float


class Detector:
    """Placeholder YOLO detector interface."""

    def detect(self, frame: FramePacket) -> list[dict[str, Any]]:
        raise NotImplementedError


class Tracker:
    """Placeholder tracker interface."""

    def update(self, detections: Iterable[dict[str, Any]]) -> Iterable[dict[str, Any]]:
        raise NotImplementedError


class OCREngine:
    """Placeholder OCR engine interface."""

    def recognise(self, crops: Iterable[Any]) -> Iterable[dict[str, Any]]:
        raise NotImplementedError
