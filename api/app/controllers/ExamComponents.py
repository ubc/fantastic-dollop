import logging

from fastapi import APIRouter, Depends, HTTPException

# http status codes
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

# data types used for data validation
from typing import List

# database table
from app.tables import ExamComponentTable, ExamComponentTypeTable

# validation models
from app.models.ExamComponent import ExamComponentBase, ExamComponentIn, ExamComponentNewIn, ExamComponentOut
from app.models.Token import TokenContext

from app.helpers import Permission, Token

log = logging.getLogger(__name__)
router = APIRouter()


async def can(action: str, context: TokenContext, courseId: int,
              examId: int, examComponentId: int=None):
    """
    Make sure the user actually has permission to perform actions and that the
    objects they're looking at actually exists.
    """
    hasIds = False
    # trying to limit the number of queries to do for this validation
    if examComponentId is None:
        hasIds = await ExamComponentTable.hasParents(courseId, examId)
    else:
        hasIds = await ExamComponentTable.has(courseId, examId, examComponentId)
    if not hasIds:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="Course or exam or exam component not found.")
    # check if user has permission
    if context.signedInUser.isAdmin:
        return True
    if (
        courseId in context.roles and
        Permission.acl.check(context.roles[courseId], Permission.EXAM, action)
    ):
        return True
    raise Permission.denied


async def checkComponentType(info: ExamComponentBase):
    isValid = await ExamComponentTypeTable.has(info.exam_component_type_id)
    if isValid:
        return True
    raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                        detail="Invalid exam component type.")


@router.get(
    "/courses/{courseId}/exams/{examId}/components",
    response_model=List[ExamComponentOut],
    summary="Get all exam components in an exam.",
    tags=["ExamComponent"]
)
async def getAll(
    courseId: int,
    examId: int,
    context: TokenContext=Depends(Token.getContext)
):
    """
    Exam components specify an element (such as an ID page, a question, etc)
    of a generated exam paper.
    """
    await can(Permission.READ, context, courseId, examId)
    return await ExamComponentTable.getAll(courseId, examId)


@router.get(
    "/courses/{courseId}/exams/{examId}/components/{componentId}",
    response_model=ExamComponentOut,
    summary="Get a specific exam component in an exam.",
    tags=["ExamComponent"]
)
async def get(
    courseId: int,
    examId: int,
    componentId: int,
    context: TokenContext=Depends(Token.getContext)
):
    await can(Permission.READ, context, courseId, examId, componentId)
    return await ExamComponentTable.get(courseId, componentId)


@router.post(
    "/courses/{courseId}/exams/{examId}/components",
    response_model=ExamComponentOut,
    status_code=HTTP_201_CREATED,
    summary="Add a new exam component in an exam.",
    tags=["ExamComponent"]
)
async def add(
    courseId: int,
    examId: int,
    componentInfo: ExamComponentNewIn,
    context: TokenContext=Depends(Token.getContext)
):
    await can(Permission.CREATE, context, courseId, examId)
    componentInfo.exam_id = examId
    await checkComponentType(componentInfo)
    return await ExamComponentTable.add(courseId, componentInfo)


@router.post(
    "/courses/{courseId}/exams/{examId}/components/{componentId}",
    response_model=ExamComponentOut,
    summary="Edit an existing exam component in an exam.",
    tags=["ExamComponent"]
)
async def edit(
    courseId: int,
    examId: int,
    componentId: int,
    componentInfo: ExamComponentIn,
    context: TokenContext=Depends(Token.getContext)
):
    await can(Permission.UPDATE, context, courseId, examId, componentId)
    componentInfo.id = componentId
    componentInfo.exam_id = examId
    await checkComponentType(componentInfo)
    return await ExamComponentTable.edit(courseId, componentInfo)


@router.delete(
    "/courses/{courseId}/exams/{examId}/components/{componentId}",
    status_code=HTTP_204_NO_CONTENT,
    summary="Delete an exam component in an exam.",
    tags=["ExamComponent"]
)
async def delete(
    courseId: int,
    examId: int,
    componentId: int,
    context: TokenContext=Depends(Token.getContext)
):
    await can(Permission.DELETE, context, courseId, examId, componentId)
    await ExamComponentTable.delete(courseId, componentId)
