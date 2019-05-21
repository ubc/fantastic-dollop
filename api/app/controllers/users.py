import logging

from fastapi import APIRouter, Depends, HTTPException

# http status codes
from starlette.status import HTTP_404_NOT_FOUND

# request body data validation
from pydantic import BaseModel
# data types used for data validation
from typing import List

# database table
from app.tables import UserTable
# database connection
from app import db

# validation models
from app.models.User import UserIn, UserOut

# session data
from app.helpers import Token
# password security
from app.helpers import Password
# database retrival
from app.helpers import TableRetriever

log = logging.getLogger(__name__)
router = APIRouter()

@router.get("/users", response_model=List[UserOut])
async def get(currentUser: UserOut=Depends(Token.getCurrentUser)):
    query = UserTable.table.select()
    return await db.fetch_all(query)

@router.get("/users/{userId}", response_model=UserOut)
async def get(userId: int):
    ret = await TableRetriever.getById(UserTable.table, userId)
    if ret:
        return ret
    raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                        detail="User not found")

@router.post("/users", response_model=UserOut)
async def add(userInfo: UserIn):
    hashedPassword = Password.hash(userInfo.password)
    query = UserTable.table.insert().values(
        username=userInfo.username,
        password=hashedPassword,
        name=userInfo.name,
        preferredName=userInfo.preferredName,
        email=userInfo.email,
        studentNumber=userInfo.studentNumber
    )
    last_record_id = await db.execute(query)
    return {**userInfo.dict(), "id": last_record_id}
