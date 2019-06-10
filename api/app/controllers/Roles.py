import logging

from fastapi import APIRouter

# data types used for data validation
from typing import List

# database table
from app.tables import RoleTable

# validation models
from app.models.Role import RoleOut

log = logging.getLogger(__name__)
router = APIRouter()


@router.get("/roles", response_model=List[RoleOut])
async def getAll():
    return await RoleTable.getAll()
