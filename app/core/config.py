import os
from dotenv import load_dotenv


load_dotenv()

class Settings():
    PROJECT_NAME: str = "Subscription Manager"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "super-secret")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 dias
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgres://user:pass@localhost:5432/subscriptions")
    TIMEZONE: str = "UTC"
    CELERY_BROKER_URL: str = os.getenv("CELERY_BROKER_URL", "amqp://guest:guest@localhost:5672//")
    CELERY_RESULT_BACKEND: str = os.getenv("CELERY_RESULT_BACKEND", "rpc://")



settings = Settings()