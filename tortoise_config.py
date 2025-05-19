from app.core.config import settings

TORTOISE_ORM = {
    "connections": {
        "default": settings.DATABASE_URL,
    },
    "apps": {
        "models": {
            "models": [
                "aerich.models",  # necessário para o Aerich
                "app.models.user",
                "app.models.client",
                "app.models.plan",
                "app.models.subscription",
                "app.models.invoice",
                "app.models.overdue",
                "app.models.user_session",
            ],
            "default_connection": "default",
        },
    },
}
