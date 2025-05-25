# app/api/v1/health.py
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from tortoise import connections
from kombu import Connection
from app.core.config import settings
from app.core.celery_app import celery

router = APIRouter(prefix="/health", tags=["health"])

@router.get("/", status_code=status.HTTP_200_OK)
async def health_check():

    results = {
        "db": "unknown", 
        "broker": "unknown", 
        "celery": "unknown"
    }

    # Checa DB
    try:
        conn = connections.get("default")
        await conn.execute_query("SELECT 1;")
        results["db"] = "ok"
    except Exception:
        results["db"] = "fail"


    # Checa RabbitMQ broker
    try:
        with Connection(settings.CELERY_BROKER_URL) as broker_conn:
            broker_conn.connect()
        results["broker"] = "ok"
    except Exception:
        results["broker"] = "fail"


    # Checa Celery workers
    try:
        inspect = celery.control.inspect(timeout=1)
        ping = inspect.ping() or {}
        results["celery"] = "ok" if ping else "fail"
    except Exception:
        results["celery"] = "fail"

    overall_status = status.HTTP_200_OK if all(v == "ok" for v in results.values()) else status.HTTP_503_SERVICE_UNAVAILABLE
    return JSONResponse({
        "status": "ok" if overall_status == status.HTTP_200_OK else "fail",
        "components": results
    })
