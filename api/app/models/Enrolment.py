from datetime import datetime

# request body data validation
from pydantic import BaseModel

from app.models.User import UserBase

class EnrolmentUserOut(UserBase):
    created: datetime
    modified: datetime
    role: str
    role_id: int
