import logging
from fastapi import APIRouter, HTTPException

# http status codes
from starlette.status import HTTP_404_NOT_FOUND

# request body data validation
from pydantic import BaseModel
# data types used for data validation
from typing import List

# database table
from app.models.User import user
# database connection
from app import db

logger = logging.getLogger(__name__)


# For data validation with incoming and outgoing data, this base class contains
# fields that are in both requests and responses.
# unfortunately, this mechanism suffers from code duplication with the database 
# table definition, no clue how to address that
class UserBase(BaseModel):
    username: str
    name: str = None
    preferredName: str = None
    email: str = None
    studentNumber: str = None


# Incoming request data will need to match this spec.
class UserIn(UserBase):
    password: str

# Outgoing response data will be filtered to match this spec.
class UserOut(UserBase):
    id: int

router = APIRouter()

@router.get("/users", response_model=List[UserOut])
async def get():
    query = user.select()
    return await db.fetch_all(query)

@router.get("/users/{userId}", response_model=UserOut)
async def get(userId: int):
    query = user.select().where(user.c.id==userId)
    ret = await db.fetch_one(query)
    if ret:
        return ret
    raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                        detail="User not found")

@router.post("/users", response_model=UserOut)
async def add(userInfo: UserIn):
    query = user.insert().values(
        username=userInfo.username,
        password=userInfo.password,
        name=userInfo.name,
        preferredName=userInfo.preferredName,
        email=userInfo.email,
        studentNumber=userInfo.studentNumber
    )
    last_record_id = await db.execute(query)
    return {**userInfo.dict(), "id": last_record_id}
