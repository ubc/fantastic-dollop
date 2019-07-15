from datetime import datetime

# request body data validation
from pydantic import BaseModel

class ExamBase(BaseModel):
    name: str
    course_id: int=None
    print_id: str=None

class ExamNewIn(ExamBase):
    pass

class ExamIn(ExamBase):
    id: int=None

class ExamOut(ExamBase):
    id: int
    course_id: int
    created: datetime
    modified: datetime
