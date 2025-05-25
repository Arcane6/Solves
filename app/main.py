# app/main.py
from app.core.logger import logger
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.middlewares.authentication import AuthMiddleware
from app.api.v1 import api_router
from app.dependencies.rate_limiter import limiter



models = [
            "app.models.user",
            "app.models.user_session",
            "app.models.client",
            "app.models.plan",
            "app.models.subscription",
            "app.models.invoice",
            "app.models.overdue",
            "app.models.log"
        ]

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up...")
    yield
    logger.info("Shutting down...")


def configure_database(app: FastAPI):
    register_tortoise(
        app,
        db_url=settings.DATABASE_URL,
        modules={"models": models},
        generate_schemas=False,
        add_exception_handlers=True,
        
    )
    logger.info("Database configured successfully")

def create_application() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description="Gerenciador de assinaturas",
        version="1.0.0",
        lifespan=lifespan,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )

    # Middlewares
    app.add_middleware(AuthMiddleware)
    app.state.limiter = limiter
    app.add_middleware(SlowAPIMiddleware)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://127.0.0.1"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Rotas
    app.include_router(api_router, prefix=settings.API_V1_STR)

    # Banco
    configure_database(app)

    return app

app = create_application()

# Tratador de exceção de rate-limit
@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request, exc):
    return JSONResponse(
        status_code=429,
        content={"detail": "Too many requests, please try again later."},
    )

