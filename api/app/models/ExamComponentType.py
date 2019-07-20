from datetime import datetime

# request body data validation
from pydantic import BaseModel

class ExamComponentTypeBase(BaseModel):
    name: str

class ExamComponentTypeOut(ExamComponentTypeBase):
    id: int
    created: datetime
    modified: datetime
