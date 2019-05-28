import logging

from fastapi import APIRouter, Depends, HTTPException

# http status codes
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT

# request body data validation
from pydantic import BaseModel
# data types used for data validation
from typing import List

# database table
from app.tables import UserTable

# validation models
from app.models.User import UserIn, UserNewIn, UserOut

# session data
from app.helpers import Token

log = logging.getLogger(__name__)
router = APIRouter()

@router.get("/users", response_model=List[UserOut])
async def getAll(currentUser: UserOut=Depends(Token.getCurrentUser)):
    return await UserTable.getAll()

@router.get("/users/{userId}", response_model=UserOut)
async def get(userId: int):
    ret = await UserTable.get(userId)
    if ret:
        return ret
    raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                        detail="User not found.")

@router.post("/users", response_model=UserOut)
async def post(userInfo: UserNewIn):
    userExists = await UserTable.has(userInfo)
    if userExists:
        raise HTTPException(status_code=HTTP_409_CONFLICT,
                            detail="Username is taken.")
    return await UserTable.add(userInfo)

@router.post("/users/{userId}", response_model=UserOut)
async def post(userId: int, userInfo: UserIn):
    # TODO: if user changes username, need to make sure new username is unique
    if userId != userInfo.id:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail="User ID in route does not match user ID in request data.")
    return await UserTable.edit(userInfo)
