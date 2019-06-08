import logging

from fastapi import APIRouter, Depends, HTTPException

# http status codes
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT

# data types used for data validation
from typing import List

# database table
from app.tables import UserTable

# validation models
from app.models.User import UserIn, UserNewIn, UserOut

# session data
from app.helpers import ModelChecker
from app.helpers import Token
from app.helpers import Permission

log = logging.getLogger(__name__)
router = APIRouter()


# check permissions, only users fiddling with their own accounts or admins
# can use these functions
async def can(signedInUser: UserOut, targetUserId: int = -1):
    # check if target user exists
    if targetUserId > 0:
        hasUser = UserTable.has(userId=targetUserId)
        if not hasUser:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                                detail="User not found.")
    # check if user has permission
    if targetUserId > 0 and signedInUser.id == targetUserId:
        return True
    if signedInUser.isAdmin:
        return True
    raise Permission.denied


@router.get("/users", response_model=List[UserOut])
async def getAll(signedInUser: UserOut=Depends(Token.getCurrentUser)):
    await can(signedInUser)
    return await UserTable.getAll()


@router.get("/users/{userId}", response_model=UserOut)
async def get(userId: int, signedInUser: UserOut=Depends(Token.getCurrentUser)):
    await can(signedInUser, userId)
    return await UserTable.get(userId)


@router.post("/users", response_model=UserOut, status_code=HTTP_201_CREATED)
async def create(userInfo: UserNewIn,
                 signedInUser: UserOut=Depends(Token.getCurrentUser)):
    await can(signedInUser)
    userExists = await UserTable.has(username=userInfo.username)
    if userExists:
        raise HTTPException(status_code=HTTP_409_CONFLICT,
                            detail="Username is taken.")
    return await UserTable.add(userInfo)


@router.post("/users/{userId}", response_model=UserOut)
async def edit(userId: int, userInfo: UserIn,
               signedInUser: UserOut=Depends(Token.getCurrentUser)):
    await can(signedInUser, userId)
    userInfo = await ModelChecker.checkId(userId, userInfo)
    return await UserTable.edit(userInfo)


@router.delete("/users/{userId}", status_code=HTTP_204_NO_CONTENT)
async def delete(userId: int,
                 signedInUser: UserOut=Depends(Token.getCurrentUser)):
    await can(signedInUser, userId)
    await UserTable.delete(userId)
