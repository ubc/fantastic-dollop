import logging

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

# http status codes
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT

# data types used for data validation
from typing import List

# database table
from app.tables import CourseTable, ExamTable, ExamSourceTable

# validation models
from app.models.Exam import ExamIn, ExamNewIn, ExamOut
from app.models.ExamSource import ExamSourceNewIn, ExamSourceOut
from app.models.Token import TokenContext

from app.helpers import ModelChecker, Permission, Token

# file management
from depot.manager import DepotManager

log = logging.getLogger(__name__)
router = APIRouter()


async def can(action: str, context: TokenContext, courseId: int,
              examId: int, examSourceId: int=None):
    # gotta make sure course exists first
    hasCourse = await CourseTable.has(courseId=courseId)
    if not hasCourse:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="Course not found.")
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


@router.get("/courses/{courseId}/exams/{examId}/sources",
            response_model=List[ExamSourceOut])
async def getAll(courseId: int, examId: int,
                 context: TokenContext=Depends(Token.getContext)):
    await can(Permission.READ, context, courseId, examId)
    return await ExamSourceTable.getAll(examId)


@router.get("/courses/{courseId}/exams/{examId}/sources/{sourceId}",
            response_model=ExamSourceOut)
async def get(courseId: int, examId: int, sourceId: int,
              context: TokenContext=Depends(Token.getContext)):
    await can(Permission.READ, context, courseId, examId)
    return await ExamSourceTable.get(sourceId)


@router.post("/courses/{courseId}/exams/{examId}/sources",
             response_model=ExamSourceOut)
async def create(
    courseId: int,
    examId: int,
    context: TokenContext=Depends(Token.getContext),
    file: UploadFile = File(...)
):
    await can(Permission.CREATE, context, courseId, examId)
    depot = DepotManager.get()
    fileId = depot.create(file.file, file.filename)
    newSource = ExamSourceNewIn(
        exam_id = examId,
        file=fileId,
        name=file.filename,
        page_count=1
    )
    return await ExamSourceTable.add(newSource)


@router.delete("/courses/{courseId}/exams/{examId}/sources/{sourceId}",
               status_code=HTTP_204_NO_CONTENT)
async def delete(
    courseId: int,
    examId: int,
    sourceId: int,
    context: TokenContext=Depends(Token.getContext)
):
    await can(Permission.DELETE, context, courseId, examId)
    await ExamSourceTable.delete(sourceId)

#@router.post("/courses/{courseId}/exams", response_model=ExamOut,
#             status_code=HTTP_201_CREATED)
#async def create(
#    courseId: int,
#    examInfo: ExamNewIn,
#    context: TokenContext=Depends(Token.getContext)
#):
#    await can(Permission.CREATE, context, courseId)
#    examInfo.course_id = courseId
#    return await ExamTable.add(examInfo)
#
#
#@router.post("/courses/{courseId}/exams/{examId}", response_model=ExamOut)
#async def update(
#    courseId: int,
#    examId: int,
#    examInfo: ExamIn,
#    context: TokenContext=Depends(Token.getContext)
#):
#    await can(Permission.UPDATE, context, courseId, examId)
#    examInfo.id = examId
#    examInfo.course_id = courseId
#    return await ExamTable.edit(examInfo)
#
#
#@router.delete("/courses/{courseId}/exams/{examId}",
#               status_code=HTTP_204_NO_CONTENT)
#async def delete(courseId: int, examId: int,
#                 context: TokenContext=Depends(Token.getContext)):
#    await can(Permission.DELETE, context, courseId, examId)
#    await ExamTable.delete(courseId)
