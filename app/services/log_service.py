from app.models.log import AuditLog

class AuditService:
    @staticmethod
    async def log(user: int, action: str, metadata: dict = None):
        await AuditLog.create(user=user, action=action, metadata=metadata or {})