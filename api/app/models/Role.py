from datetime import datetime

# request body data validation
from pydantic import BaseModel

class RoleBase(BaseModel):
    name: str

class RoleOut(RoleBase):
    id: int
    created: datetime
    modified: datetime
