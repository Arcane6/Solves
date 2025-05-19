from pydantic import BaseModel
from datetime import datetime

class InvoiceBase(BaseModel):
    subscription_id: int
    month: int
    year: int
    due_date: datetime
    status: str  # "pendente", "paga", "vencida"


class InvoiceCreate(InvoiceBase):
    pass

class InvoiceRead(InvoiceBase):
    id: int
    created_at: datetime
    updated_at: datetime
