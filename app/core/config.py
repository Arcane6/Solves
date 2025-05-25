import os
from dotenv import load_dotenv


load_dotenv()

class Settings():
    PROJECT_NAME: str = "Subscription Manager"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv("SECRET_KEY", None)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    DATABASE_URL: str = os.getenv("DATABASE_URL", None)
    TIMEZONE: str = "UTC"
    CELERY_BROKER_URL: str = os.getenv("CELERY_BROKER_URL", None)
    CELERY_RESULT_BACKEND: str = os.getenv("CELERY_RESULT_BACKEND", "rpc://")
    CELERY_SIGNING_KEY: str = os.getenv("CELERY_SIGNING_KEY", None)



settings = Settings()