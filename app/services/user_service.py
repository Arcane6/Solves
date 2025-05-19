from app.models.user import User
from tortoise.exceptions import DoesNotExist
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    
    @staticmethod
    async def get_user_by_id(user_id: int) -> User:
        return await User.get_or_none(email=user_id)
    
    @staticmethod
    async def get_user_by_email(email: str) -> User:
        return await User.get_or_none(email=email)

    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)
    
    @staticmethod
    def hash_password(password):
        return pwd_context.hash(password)