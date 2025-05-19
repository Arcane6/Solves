from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal

class PlanBase(BaseModel):
    name: str
    price: Decimal
    recurrence: str  # "mensal" ou "anual"
    description: str | None = None

class PlanCreate(PlanBase):
    pass

class PlanRead(PlanBase):
    id: int
    user_id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

class PlanUpdate(BaseModel):
    name: str | None = None
    price: Decimal | None = None
    recurrence: str | None = None
    description: str | None = None
    is_active: bool | None = None
