from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import Counter, Histogram, make_asgi_app

from app.api.v1 import auth, channels, health, plate_lists, recognitions, webhooks
from app.core.config import settings
from app.db import session as db_session

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Metrics
ocr_errors = Counter("ocr_errors_total", "Total OCR errors")
processing_latency = Histogram("frame_processing_latency_ms", "Frame processing latency", unit="ms")
fps_metric = Histogram("channel_fps", "Observed FPS per channel", buckets=(1, 5, 10, 15, 20, 30))

# Routers
app.include_router(health.router, prefix="/health")
app.include_router(auth.router, prefix=settings.api_v1_prefix)
app.include_router(channels.router, prefix=settings.api_v1_prefix)
app.include_router(plate_lists.router, prefix=settings.api_v1_prefix)
app.include_router(recognitions.router, prefix=settings.api_v1_prefix)
app.include_router(webhooks.router, prefix=settings.api_v1_prefix)


@app.on_event("startup")
async def startup_event():
    # Create tables on startup for demo purposes
    async with db_session.engine.begin() as conn:
        await conn.run_sync(db_session.Base.metadata.create_all)


app.mount("/metrics", make_asgi_app())
