import logging

from fastapi import APIRouter, Depends, HTTPException

# http status codes
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

# data types used for data validation
from typing import List

# database table
from app.tables import EnrolmentTable, CourseTable

# validation models
from app.models.User import UserOut
from app.models.Enrolment import EnrolmentIn, EnrolmentNewIn, EnrolmentOut
from app.models.Course import CourseRoleOut
from app.models.Token import TokenContext

from app.helpers import ModelChecker, Permission, Token

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


@router.get("/users/me/courses",
            response_model=List[CourseRoleOut],
            tags=["enrolment"],
            summary='Get courses available to the signed in user.')
async def getMyCourses(
    context: TokenContext=Depends(Token.getContext)
):
    return context.enroledCourses


@router.get("/courses/{courseId}/users",
            response_model=List[EnrolmentOut],
            tags=["enrolment"],
            summary='Get a list of users enroled in a course.')
async def getUsersInCourse(
    courseId: int,
    signedInUser: UserOut=Depends(Token.getCurrentUser)
):
    await can(signedInUser, courseId)
    return await EnrolmentTable.getList(courseId)


@router.post("/courses/{courseId}/users",
             response_model=EnrolmentOut,
             status_code=HTTP_201_CREATED,
             tags=["enrolment"],
             summary='Add a user to a course.')
async def addUserToCourse(
    courseId: int,
    enrolments: EnrolmentNewIn,
    signedInUser: UserOut=Depends(Token.getCurrentUser)
):
    await can(signedInUser, courseId)
    return await EnrolmentTable.add(courseId, enrolments)


@router.post("/courses/{courseId}/users/{userId}",
             response_model=EnrolmentOut,
             status_code=HTTP_201_CREATED,
             tags=["enrolment"],
             summary="Edit a user's role in a course.")
async def editUserInCourse(
    courseId: int,
    userId: int,
    enrolment: EnrolmentIn,
    signedInUser: UserOut=Depends(Token.getCurrentUser)
):
    await can(signedInUser, courseId)
    await ModelChecker.checkIds({'user_id': userId}, enrolment)
    ret = await EnrolmentTable.getByCourseAndUserId(courseId, userId)
    if not ret:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="Enrolment not found.")
    enrolment = await ModelChecker.checkId(ret['id'], enrolment)

    return await EnrolmentTable.edit(courseId, enrolment)


@router.delete("/courses/{courseId}/users",
               status_code=HTTP_204_NO_CONTENT,
               tags=["enrolment"],
               summary='Delete a user from a course.')
async def deleteUserFromCourse(
    courseId: int,
    enrolments: List[EnrolmentIn],
    signedInUser: UserOut=Depends(Token.getCurrentUser)
):
    await can(signedInUser, courseId)
    return await EnrolmentTable.delete(courseId, enrolments)
