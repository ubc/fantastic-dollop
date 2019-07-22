from datetime import datetime

from pydantic import BaseModel


class ExamComponentSourceBase(BaseModel):
    exam_component_id: int
    exam_source_id: int


class ExamComponentSourceNewIn(ExamComponentSourceBase):
    exam_component_id: int=None # make optional


class ExamComponentSourceIn(ExamComponentSourceBase):
    id: int=None # make optional
    exam_component_id: int=None # make optional


class ExamComponentSourceOut(ExamComponentSourceBase):
    id: int
    course_id: int
    exam_id: int
    created: datetime
    modified: datetime
