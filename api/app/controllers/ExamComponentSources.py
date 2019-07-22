import logging

from fastapi import APIRouter, Depends, HTTPException

# http status codes
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

# data types used for data validation
from typing import List

# database table
from app.tables import ExamComponentSourceTable

# validation models
from app.models.ExamComponentSource import ExamComponentSourceBase, ExamComponentSourceIn, ExamComponentSourceNewIn, ExamComponentSourceOut
from app.models.Token import TokenContext

from app.helpers import Permission, Token

log = logging.getLogger(__name__)
router = APIRouter()


async def can(action: str, context: TokenContext, courseId: int,
              examId: int, examComponentId: int, examComponentSourceId: int=None):
    """
    Make sure the user actually has permission to perform actions and that the
    objects they're looking at actually exists.
    """
    hasIds = False
    # trying to limit the number of queries to do for this validation
    if examComponentSourceId is None:
        hasIds = await ExamComponentSourceTable.hasParents(courseId, examId,
                                                           examComponentId)
    else:
        hasIds = await ExamComponentSourceTable.has(courseId, examId,
                                                    examComponentId,
                                                    examComponentSourceId)
    if not hasIds:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="Exam component source not found.")
    # check if user has permission
    if context.signedInUser.isAdmin:
        return True
    if (
        courseId in context.roles and
        Permission.acl.check(context.roles[courseId], Permission.EXAM, action)
    ):
        return True
    raise Permission.denied


@router.get(
    "/courses/{courseId}/exams/{examId}/components/{componentId}/sources",
    response_model=List[ExamComponentSourceOut],
    summary="Get an exam component's exam sources.",
    tags=["ExamComponentSource"]
)
async def getAll(
    courseId: int,
    examId: int,
    componentId: int,
    context: TokenContext=Depends(Token.getContext)
):
    """
    Exam components specify an element (such as an ID page, a question, etc)
    of a generated exam paper. The element is copied from one or more exam
    sources.
    """
    await can(Permission.READ, context, courseId, examId, componentId)
    return await ExamComponentSourceTable.getAll(componentId)


@router.get(
    "/courses/{courseId}/exams/{examId}/components/{componentId}/sources/{sourceId}",
    response_model=ExamComponentSourceOut,
    summary="Get a specific exam component's source.",
    tags=["ExamComponentSource"]
)
async def get(
    courseId: int,
    examId: int,
    componentId: int,
    sourceId: int,
    context: TokenContext=Depends(Token.getContext)
):
    await can(Permission.READ, context, courseId, examId, componentId, sourceId)
    return await ExamComponentSourceTable.get(sourceId)


@router.post(
    "/courses/{courseId}/exams/{examId}/components/{componentId}/sources",
    response_model=ExamComponentSourceOut,
    status_code=HTTP_201_CREATED,
    summary="Add an exam source to an exam component.",
    tags=["ExamComponentSource"]
)
async def add(
    courseId: int,
    examId: int,
    componentId: int,
    componentInfo: ExamComponentSourceNewIn,
    context: TokenContext=Depends(Token.getContext)
):
    await can(Permission.CREATE, context, courseId, examId, componentId)
    componentInfo.exam_component_id = componentId
    return await ExamComponentSourceTable.add(componentInfo)


@router.delete(
    "/courses/{courseId}/exams/{examId}/components/{componentId}/sources/{sourceId}",
    status_code=HTTP_204_NO_CONTENT,
    summary="Delete a specific exam component's source in an exam.",
    tags=["ExamSourceComponent"]
)
async def delete(
    courseId: int,
    examId: int,
    componentId: int,
    sourceId: int,
    context: TokenContext=Depends(Token.getContext)
):
    await can(Permission.DELETE, context, courseId, examId, componentId, sourceId)
    await ExamComponentSourceTable.delete(componentId)
