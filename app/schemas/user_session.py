from pydantic import BaseModel
from datetime import datetime

class UserSessionRead(BaseModel):
    id: int
    user_id: int
    session_token: str
    created_at: datetime
    last_access: datetime
    ip_address: str | None = None
    user_agent: str | None = None
