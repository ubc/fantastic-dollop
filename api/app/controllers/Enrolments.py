import logging

from fastapi import APIRouter, Depends, HTTPException

# http status codes
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

# data types used for data validation
from typing import List

# database table
from app.tables import EnrolmentTable, CourseTable

# validation models
from app.models.User import UserOut
from app.models.Enrolment import EnrolmentIn, EnrolmentNewIn, EnrolmentOut

# session data
from app.helpers import Token
from app.helpers import Permission

log = logging.getLogger(__name__)
router = APIRouter()


async def can(signedInUser: UserOut, courseId: int):
    # gotta make sure course exists first
    hasCourse = await CourseTable.has(courseId=courseId)
    if not hasCourse:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="Course not found.")
    # check if user has permission
    if signedInUser.isAdmin:
        return True
    raise Permission.denied


@router.get("/courses/{courseId}/users", response_model=List[EnrolmentOut])
async def getAll(
    courseId: int,
    signedInUser: UserOut=Depends(Token.getCurrentUser)
):
    await can(signedInUser, courseId)
    return await EnrolmentTable.getList(courseId)


@router.post("/courses/{courseId}/users", response_model=List[EnrolmentOut],
             status_code=HTTP_201_CREATED)
async def add(
    courseId: int,
    enrolments: List[EnrolmentNewIn],
    signedInUser: UserOut=Depends(Token.getCurrentUser)
):
    await can(signedInUser, courseId)
    return await EnrolmentTable.add(courseId, enrolments)


@router.post("/courses/{courseId}/users/{userId}",
             response_model=EnrolmentOut,
             status_code=HTTP_201_CREATED)
async def edit(
    courseId: int,
    userId: int,
    enrolment: EnrolmentIn,
    signedInUser: UserOut=Depends(Token.getCurrentUser)
):
    await can(signedInUser, courseId)
    if userId != enrolment.user_id:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail="User ID in route does not match user ID in request data.")

    return await EnrolmentTable.edit(courseId, enrolment)


@router.delete("/courses/{courseId}/users", status_code=HTTP_204_NO_CONTENT)
async def delete(
    courseId: int,
    enrolments: List[EnrolmentIn],
    signedInUser: UserOut=Depends(Token.getCurrentUser)
):
    await can(signedInUser, courseId)
    return await EnrolmentTable.delete(courseId, enrolments)
