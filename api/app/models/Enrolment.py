# request body data validation
from pydantic import BaseModel

from app.models.User import UserBase


class EnrolmentBase(BaseModel):
    user_id: int
    role_id: int


class EnrolmentOut(UserBase, EnrolmentBase):
    id: int
    role: str
    course_id: int


class EnrolmentNewIn(EnrolmentBase):
    pass


class EnrolmentIn(EnrolmentBase):
    id: int=None # make optional
    user_id: int=None # make optional
