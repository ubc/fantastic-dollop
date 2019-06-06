from typing import Dict, List

# request body data validation
from pydantic import BaseModel

from app.models.Course import CourseOut
from app.models.Enrolment import EnrolmentOut
from app.models.User import UserOut

class TokenContext(BaseModel):
    signedInUser: UserOut
    enroledCourses: List[CourseOut]
    roles: Dict[int, str]
