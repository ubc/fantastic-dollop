import logging

from fastapi import APIRouter, Depends, HTTPException

# http status codes
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT

# data types used for data validation
from typing import List

# database table
from app.tables import CourseTable, ExamTable

# validation models
from app.models.Exam import ExamIn, ExamNewIn, ExamOut
from app.models.Token import TokenContext

from app.helpers import ModelChecker, Permission, Token

log = logging.getLogger(__name__)
router = APIRouter()


async def can(action: str, context: TokenContext, courseId: int,
              examId: int=None):
    # gotta make sure course exists first
    hasCourse = await CourseTable.has(courseId=courseId)
    if not hasCourse:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="Course not found.")
    if examId:
        hasExam = await ExamTable.has(courseId, examId)
        if not hasExam:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                                detail="Exam not found in course.")
    # check if user has permission
    if context.signedInUser.isAdmin:
        return True
    if (
        courseId in context.roles and
        Permission.acl.check(context.roles[courseId], Permission.EXAM, action)
    ):
        return True
    raise Permission.denied


@router.get("/courses/{courseId}/exams", response_model=List[ExamOut])
async def getAll(courseId: int, context: TokenContext=Depends(Token.getContext)):
    await can(Permission.READ, context, courseId)
    return await ExamTable.getAll(courseId)


@router.get("/courses/{courseId}/exams/{examId}", response_model=ExamOut)
async def get(courseId: int, examId: int,
              context: TokenContext=Depends(Token.getContext)):
    await can(Permission.READ, context, courseId, examId)
    return await ExamTable.get(examId)


@router.post("/courses/{courseId}/exams", response_model=ExamOut,
             status_code=HTTP_201_CREATED)
async def create(
    courseId: int,
    examInfo: ExamNewIn,
    context: TokenContext=Depends(Token.getContext)
):
    await can(Permission.CREATE, context, courseId)
    examInfo.course_id = courseId
    return await ExamTable.add(examInfo)


@router.post("/courses/{courseId}/exams/{examId}", response_model=ExamOut)
async def update(
    courseId: int,
    examId: int,
    examInfo: ExamIn,
    context: TokenContext=Depends(Token.getContext)
):
    await can(Permission.UPDATE, context, courseId, examId)
    examInfo.id = examId
    examInfo.course_id = courseId
    return await ExamTable.edit(examInfo)


@router.delete("/courses/{courseId}/exams/{examId}",
               status_code=HTTP_204_NO_CONTENT)
async def delete(courseId: int, examId: int,
                 context: TokenContext=Depends(Token.getContext)):
    await can(Permission.DELETE, context, courseId, examId)
    await ExamTable.delete(courseId)
