from celery import Celery
from app.core.config import settings

celery = Celery(
    "worker",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND
)

celery.conf.task_routes = {
    "app.tasks.invoice.generate_invoice": {"queue": "invoice"},
}
