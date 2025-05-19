from pydantic import BaseModel, EmailStr
from datetime import datetime

class ClientBase(BaseModel):
    name: str
    phone: str
    email: EmailStr
    address: str | None = None

class ClientCreate(ClientBase):
    pass

class ClientRead(ClientBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

class ClientUpdate(BaseModel):
    name: str | None = None
    phone: str | None = None
    email: EmailStr | None = None
    address: str | None = None
