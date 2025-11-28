from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Number Recognition"
    api_v1_prefix: str = "/api/v1"
    database_url: str = "sqlite+aiosqlite:///./data/dev.db"
    secret_key: str = "change-me"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    storage_bucket: str = "plates"
    storage_endpoint: str = "http://minio:9000"
    storage_access_key: str = "minioadmin"
    storage_secret_key: str = "minioadmin"
    webhook_signature_header: str = "X-Signature"
    cors_origins: list[str] = ["*"]
    enable_tls: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
