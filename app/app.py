from fastapi import FastAPI
from uvicorn import run as uvicorn_run

from app.apis.health_api import router as health_router
from app.settings import settings


def _register_api_handlers(app: FastAPI) -> FastAPI:
    app.include_router(health_router)
    return app


def create_app() -> FastAPI:
    """Create and return FastAPI application."""
    app = FastAPI()
    app = _register_api_handlers(app)
    return app


app = create_app()


def run_app(app: FastAPI = app) -> None:
    """Run FastAPI application."""
    uvicorn_run(app, host=settings.app_host, port=int(settings.app_port))
