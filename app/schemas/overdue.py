from pydantic import BaseModel
from datetime import datetime

class OverdueBase(BaseModel):
    invoice_id: int
    days_late: int
    status: str  # "pendente", "negociado", "quitado"

class OverdueCreate(OverdueBase):
    pass

class OverdueRead(OverdueBase):
    id: int
    created_at: datetime
    updated_at: datetime
