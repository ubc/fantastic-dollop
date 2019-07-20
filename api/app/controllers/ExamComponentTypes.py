import logging

from fastapi import APIRouter

# data types used for data validation
from typing import List

# database table
from app.tables import ExamComponentTypeTable

# validation models
from app.models.ExamComponentType import ExamComponentTypeOut

log = logging.getLogger(__name__)
router = APIRouter()


@router.get(
    "/exam_component_types",
    response_model=List[ExamComponentTypeOut],
    summary="Get all exam component types.",
    tags=["ExamComponentType"]
)
async def getAll():
    """
    There are different types of exam components: question, ID page, etc.
    This returns a list of the types that exam components can take.
    """
    return await ExamComponentTypeTable.getAll()
