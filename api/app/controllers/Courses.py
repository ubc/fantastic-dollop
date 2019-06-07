import logging

from fastapi import APIRouter, Depends, HTTPException

# http status codes
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT

# data types used for data validation
from typing import List

# database table
from app.tables import CourseTable

# validation models
from app.models.Course import CourseIn, CourseNewIn, CourseOut
from app.models.Token import TokenContext
from app.models.User import UserOut

from app.helpers import Permission, Token

log = logging.getLogger(__name__)
router = APIRouter()


async def can(action: str, context: TokenContext, courseId: int):
    # gotta make sure course exists first
    hasCourse = await CourseTable.has(courseId=courseId)
    if not hasCourse:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="Course not found.")
    # check if user has permission
    if context.signedInUser.isAdmin:
        return True
    if (
        courseId in context.roles and
        Permission.acl.check(context.roles[courseId], Permission.COURSE, action)
    ):
        return True
    raise Permission.denied


@router.get("/courses", response_model=List[CourseOut])
async def getAll(context: TokenContext=Depends(Token.getContext)):
    if context.signedInUser.isAdmin:
        return await CourseTable.getAll()
    else:
        return context.enroledCourses


@router.get("/courses/{courseId}", response_model=CourseOut)
async def get(courseId: int, context: TokenContext=Depends(Token.getContext)):
    await can(Permission.READ, context, courseId)
    ret = await CourseTable.get(courseId)
    if ret:
        return ret
    raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                        detail="Course not found.")


@router.post("/courses", response_model=CourseOut, status_code=HTTP_201_CREATED)
async def create(
    courseInfo: CourseNewIn,
    context: TokenContext=Depends(Token.getContext)
):
    if not context.signedInUser.isAdmin:
        raise Permission.denied
    exists = await CourseTable.has(name=courseInfo.name)
    if exists:
        raise HTTPException(status_code=HTTP_409_CONFLICT,
                            detail="Course name is taken.")
    return await CourseTable.add(courseInfo)


@router.post("/courses/{courseId}", response_model=CourseOut)
async def update(
    courseId: int,
    courseInfo: CourseIn,
    context: TokenContext=Depends(Token.getContext)
):
    await can(Permission.UPDATE, context, courseId)
    if courseId != courseInfo.id:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail="Course ID in route does not match course ID in request data.")
    exists = await CourseTable.has(name=courseInfo.name)
    if exists:
        raise HTTPException(status_code=HTTP_409_CONFLICT,
                            detail="Course name is taken.")
    return await CourseTable.edit(courseInfo)


@router.delete("/courses/{courseId}", status_code=HTTP_204_NO_CONTENT)
async def delete(courseId: int, context: TokenContext=Depends(Token.getContext)):
    await can(Permission.DELETE, context, courseId)
    await CourseTable.delete(courseId)
