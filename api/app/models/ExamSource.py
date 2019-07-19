from datetime import datetime

# request body data validation
from pydantic import BaseModel

class ExamSourceBase(BaseModel):
    exam_id: int=None
    file: str=None
    name: str
    page_count: int=None

class ExamSourceNewIn(ExamSourceBase):
    pass

class ExamSourceIn(ExamSourceBase):
    id: int=None

class ExamSourceOut(ExamSourceBase):
    id: int
    course_id: int
    exam_id: int
    file: str
    page_count: int
    created: datetime
    modified: datetime
