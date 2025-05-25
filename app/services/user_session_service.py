from app.models.user import User
from app.models.user_session import UserSession


class SessionService:
    @staticmethod
    async def create_session(user: User, session_token: str, refresh_token: str, ip: str, user_agent: str):
        return await UserSession.create(
            user=user,
            session_token=session_token,
            refresh_token=refresh_token,
            ip_address=ip,
            user_agent=user_agent
        )

    @staticmethod
    async def get_session_by_token(token: str):
        return await UserSession.get_or_none(session_token=token)

    @staticmethod
    async def delete_session(token: str):
        session = await UserSession.get_or_none(session_token=token)
        if session:
            await session.delete()
