from datetime import datetime

# request body data validation
from pydantic import BaseModel

class CourseBase(BaseModel):
    name: str
    description: str=None

class CourseNewIn(CourseBase):
    pass

class CourseIn(CourseBase):
    id: int=None

class CourseOut(CourseBase):
    id: int
    created: datetime
    modified: datetime

class CourseRoleOut(CourseOut):
    role: str=''
