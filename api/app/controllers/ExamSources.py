import logging

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

# http status codes
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

# data types used for data validation
from typing import List

# database table
from app.tables import ExamSourceTable

# validation models
from app.models.ExamSource import ExamSourceNewIn, ExamSourceOut
from app.models.Token import TokenContext

from app.helpers import Permission, Token

# file management
from depot.manager import DepotManager

log = logging.getLogger(__name__)
router = APIRouter()


async def can(action: str, context: TokenContext, courseId: int,
              examId: int, examSourceId: int=None):
    hasIds = False
    # trying to limit the number of queries to do for this validation
    if examSourceId is None:
        hasIds = await ExamSourceTable.hasParents(courseId, examId)
    else:
        hasIds = await ExamSourceTable.has(courseId, examId, examSourceId)
    if not hasIds:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="Course or exam or exam source not found.")
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
    return await ExamSourceTable.getAll(courseId, examId)


@router.get("/courses/{courseId}/exams/{examId}/sources/{sourceId}",
            response_model=ExamSourceOut)
async def get(courseId: int, examId: int, sourceId: int,
              context: TokenContext=Depends(Token.getContext)):
    await can(Permission.READ, context, courseId, examId)
    return await ExamSourceTable.get(courseId, sourceId)


@router.post("/courses/{courseId}/exams/{examId}/sources",
             response_model=ExamSourceOut, status_code=HTTP_201_CREATED)
async def add(
    courseId: int,
    examId: int,
    context: TokenContext=Depends(Token.getContext),
    file: UploadFile = File(...)
):
    await can(Permission.CREATE, context, courseId, examId)
    depot = DepotManager.get()
    fileId = depot.create(file.file, file.filename)
    # TODO actually fill in page_count
    newSource = ExamSourceNewIn(
        exam_id = examId,
        file=fileId,
        name=file.filename,
        page_count=1
    )
    return await ExamSourceTable.add(courseId, newSource)


@router.delete("/courses/{courseId}/exams/{examId}/sources/{sourceId}",
               status_code=HTTP_204_NO_CONTENT)
async def delete(
    courseId: int,
    examId: int,
    sourceId: int,
    context: TokenContext=Depends(Token.getContext)
):
    await can(Permission.DELETE, context, courseId, examId)
    await ExamSourceTable.delete(courseId, sourceId)
