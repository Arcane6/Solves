from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserCreate, UserRead
from app.services.user_service import UserService
from app.models.user import User

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)

async def register_user(user_in: UserCreate):
    existing = await UserService.get_user_by_email(user_in.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email já está em uso")

    hashed = UserService.hash_password(user_in.password)
    user = await User.create(
        email=user_in.email,
        hashed_password=hashed,
        full_name=user_in.full_name
    )
    return user
