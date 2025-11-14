"""FastAPI application entrypoint for the number recognition platform."""
from __future__ import annotations

from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

from .api.routes import auth, channels, diagnostics, events, lists, scenarios, webhooks
from .core.config import settings
from .monitoring.metrics import register_custom_metrics


@asynccontextmanager
def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Application lifespan that initialises monitoring instrumentation."""
    Instrumentator().instrument(app).expose(app, include_in_schema=False)
    register_custom_metrics()
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title="Number Recognition Platform",
        description="Edge-ready automatic number plate recognition (ANPR) system.",
        version=settings.VERSION,
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ALLOW_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(auth.router, prefix="/api")
    app.include_router(channels.router, prefix="/api")
    app.include_router(events.router, prefix="/api")
    app.include_router(lists.router, prefix="/api")
    app.include_router(scenarios.router, prefix="/api")
    app.include_router(webhooks.router, prefix="/api")
    app.include_router(diagnostics.router, prefix="/api")
    return app


app = create_app()
