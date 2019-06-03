import logging

from fastapi import APIRouter, Depends, HTTPException

# http status codes
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT

# data types used for data validation
from typing import List

# database table
from app.tables import EnrolmentTable, UserTable

# validation models
from app.models.User import UserIn, UserNewIn, UserOut
from app.models.Enrolment import EnrolmentUserOut

# session data
from app.helpers import Token
from app.helpers import Permission

log = logging.getLogger(__name__)
router = APIRouter()


# check permissions, only users fiddling with their own accounts or admins
# can use these functions
def can(signedInUser: UserOut, courseId: int):
    if signedInUser.isAdmin:
        return True
    return False

@router.get("/courses/{courseId}/users", response_model=List[EnrolmentUserOut])
async def getAll(
    courseId: int,
    signedInUser: UserOut=Depends(Token.getCurrentUser)
):
    if not can(signedInUser, courseId):
        raise Permission.denied
    return await EnrolmentTable.getEnroled(courseId)
