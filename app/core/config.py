import secrets

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # Подставь свой URL по умолчанию, если нужно. Этот дефолт безопасен для локалки.
    DB_URL: str = "postgresql+psycopg://evora:evora@localhost:5432/evora"
    REDIS_URL: str = "redis://localhost:6379/0"

    # Без хардкода чувствительных строк: генерируем безопасный дефолт
    JWT_SECRET: SecretStr = SecretStr(secrets.token_urlsafe(32))

    STRIPE_PUBLIC_KEY: str | None = None
    STRIPE_SECRET_KEY: str | None = None


settings = Settings()
