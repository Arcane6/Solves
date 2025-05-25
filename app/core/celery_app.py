from celery import Celery
from app.core.config import settings

celery = Celery(
    "worker",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND
)

celery.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    enable_utc=True,
    timezone="UTC",
    task_publish_retry=False,
    signers=[settings.CELERY_SIGNING_KEY],
    task_default_delivery_mode=1
)

celery.conf.task_routes = {
    "app.tasks.invoice.generate_invoice": {"queue": "invoice"},
}
