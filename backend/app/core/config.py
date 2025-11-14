"""Centralised settings for the ANPR platform."""
from __future__ import annotations

from functools import lru_cache
from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    VERSION: str = "0.1.0"
    PROJECT_NAME: str = "number-recognition"

    API_V1_PREFIX: str = "/api"
    DATABASE_URL: str = "postgresql+asyncpg://anpr:anpr@postgres/anpr"
    S3_ENDPOINT: str = "http://minio:9000"
    S3_BUCKET: str = "anpr-events"
    S3_ACCESS_KEY: str = "anpr"
    S3_SECRET_KEY: str = "anpr_secret"
    JWT_SECRET_KEY: str = "change-me"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_SECONDS: int = 3600
    CORS_ALLOW_ORIGINS: List[str] = ["*"]
    PROMETHEUS_NAMESPACE: str = "anpr"

    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
