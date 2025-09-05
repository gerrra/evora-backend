from fastapi import FastAPI

from app.api.health import router as health_router
from app.core.config import settings

app = FastAPI(title="Evora Orchestrator")

app.include_router(health_router)
