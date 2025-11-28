"""High-level pipeline orchestration placeholder.

The pipeline simulates the ingest → detect → track → OCR → postprocess steps described in the
technical requirements. In production this module would wrap hardware-accelerated decoders,
YOLO-based detectors, tracker implementations, and OCR engines. Here we expose synchronous
hooks for tests and a simple example of how metadata flows between stages.
"""
from dataclasses import dataclass
from typing import Any, Callable
import uuid


@dataclass
class Frame:
    channel_id: int
    data: bytes
    timestamp_ms: int


@dataclass
class DetectionResult:
    bbox: list[int]
    confidence: float


@dataclass
class OcrResult:
    text: str
    confidence: float
    country_template: str | None


@dataclass
class RecognitionEvent:
    track_id: str
    detection: DetectionResult
    ocr: OcrResult
    metadata: dict[str, Any]


class Pipeline:
    def __init__(
        self,
        detector: Callable[[Frame], list[DetectionResult]],
        ocr_engine: Callable[[Frame, DetectionResult], OcrResult],
        rules_engine: Callable[[RecognitionEvent], None],
    ) -> None:
        self.detector = detector
        self.ocr_engine = ocr_engine
        self.rules_engine = rules_engine

    def process_frame(self, frame: Frame) -> list[RecognitionEvent]:
        results: list[RecognitionEvent] = []
        detections = self.detector(frame)
        for detection in detections:
            ocr_result = self.ocr_engine(frame, detection)
            recognition = RecognitionEvent(
                track_id=str(uuid.uuid4()),
                detection=detection,
                ocr=ocr_result,
                metadata={"ts": frame.timestamp_ms},
            )
            self.rules_engine(recognition)
            results.append(recognition)
        return results
