from datetime import datetime

# request body data validation
from pydantic import BaseModel

class ExamComponentBase(BaseModel):
    exam_id: int
    exam_component_type_id: int
    mark: int=0
    comment: str=None
    page_start: int
    page_end: int
    sequence: int

class ExamComponentNewIn(ExamComponentBase):
    pass

class ExamComponentIn(ExamComponentBase):
    id: int=None

class ExamComponentOut(ExamComponentBase):
    id: int
    course_id: int
    created: datetime
    modified: datetime
