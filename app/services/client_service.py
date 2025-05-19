from app.models.client import Client
from app.models.user import User


class ClientService:
    @staticmethod
    async def get_all_by_user(user: User):
        return await Client.filter(user=user).all()

    @staticmethod
    async def create_client(user: User, **kwargs):
        return await Client.create(user=user, **kwargs)

    @staticmethod
    async def get_by_id(client_id: int, user: User):
        return await Client.get_or_none(id=client_id, user=user)
    
