from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    full_name: str

class UserCreate(UserBase):
    password: str  # Senha em texto puro para criação

class UserRead(UserBase):
    id: int
    is_active: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime

class UserUpdate(BaseModel):
    full_name: str | None = None
    password: str | None = None

class UserInDB(UserRead):
    hashed_password: str  # Usado apenas internamente
