"""Custom Prometheus metrics for the ANPR pipeline."""
from __future__ import annotations

from prometheus_client import Counter, Gauge

from ..core.config import settings

PIPELINE_LATENCY = Gauge(
    "pipeline_latency_ms",
    "End-to-end latency from frame ingestion to event emission.",
    namespace=settings.PROMETHEUS_NAMESPACE,
)

PIPELINE_FPS = Gauge(
    "pipeline_fps",
    "Processing frame rate per channel.",
    namespace=settings.PROMETHEUS_NAMESPACE,
    labelnames=("channel",),
)

OCR_ERRORS = Counter(
    "ocr_errors_total",
    "Total number of OCR failures.",
    namespace=settings.PROMETHEUS_NAMESPACE,
)

DROPPED_FRAMES = Counter(
    "dropped_frames_total",
    "Total number of frames dropped before processing.",
    namespace=settings.PROMETHEUS_NAMESPACE,
)


def register_custom_metrics() -> None:
    """Ensure metrics module is imported to register metrics."""
    # Import side-effects register the metrics; this function exists for readability.
    return None
