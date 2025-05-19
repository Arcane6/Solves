from fastapi import FastAPI
from fastapi.middleware import Middleware
from tortoise.contrib.fastapi import register_tortoise
from app.core.config import settings
from app.middlewares.authentication import AuthMiddleware
from contextlib import asynccontextmanager
from app.api.v1 import api_router
import logging


# logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up...")
    yield
    logger.info("Shutting down...")


def configure_database(app: FastAPI) -> None:

    register_tortoise(
        app=app,
        db_url=settings.DATABASE_URL,
        modules={
            "models": [
                "app.models.user",
                "app.models.user_session",
                "app.models.client",
                "app.models.plan",
                "app.models.subscription",
                "app.models.invoice",
                "app.models.overdue"
            ]
        },
        generate_schemas=False,
        add_exception_handlers=True,
    )
    logger.info("Database configured successfully")


def create_application() -> FastAPI:

    # middlewares

    middleware = [
        Middleware(AuthMiddleware)
    ]



    app = FastAPI(
        title=settings.PROJECT_NAME,
        description="Gerenciador de assinaturas",
        version="1.0.0",
        lifespan=lifespan,
        middleware=middleware,
        docs_url="/docs",
        redoc_url="/redoc",
    )

    app.include_router(api_router)
    configure_database(app)

    return app



app = create_application()