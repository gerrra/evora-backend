from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = ConfigDict(env_file=".env")
    
    DB_URL: str = "postgresql+psycopg://user:pass@localhost:5432/evora"
    REDIS_URL: str = "redis://localhost:6379/0"
    JWT_SECRET: str = "change-me"
    STRIPE_PUBLIC_KEY: str | None = None
    STRIPE_SECRET_KEY: str | None = None


settings = Settings()
