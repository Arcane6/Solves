from pydantic import BaseModel
from datetime import datetime

class SubscriptionBase(BaseModel):
    client_id: int
    plan_id: int
    payment_day: int

class SubscriptionCreate(SubscriptionBase):
    pass

class SubscriptionRead(SubscriptionBase):
    id: int
    is_active: bool
    last_payment_date: datetime | None
    is_delinquent: bool
    created_at: datetime
    updated_at: datetime

class SubscriptionUpdate(BaseModel):
    payment_day: int | None = None
    is_active: bool | None = None
    is_delinquent: bool | None = None
    last_payment_date: datetime | None = None
