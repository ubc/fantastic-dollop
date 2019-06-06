import logging

from datetime import datetime, timedelta

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from starlette.status import HTTP_401_UNAUTHORIZED

import jwt
from jwt import PyJWTError

from app.config import EnvConfig

from app.models.Token import TokenContext
from app.models.Course import CourseOut
from app.models.User import UserOut

from app.tables import EnrolmentTable
from app.tables import UserTable

log = logging.getLogger(__name__)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/signin")

TOKEN_SECRET = EnvConfig.getTokenSecret()
TOKEN_ALGORITHM = EnvConfig.getTokenAlgorithm()
TOKEN_EXPIRE = EnvConfig.getTokenExpire()


async def getCurrentUser(token: str=Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, TOKEN_SECRET, algorithms=[TOKEN_ALGORITHM])
        userId: int = payload.get("sub")
        if userId is None:
            raise credentials_exception
    except PyJWTError:
        raise credentials_exception
    user = await UserTable.get(userId)
    if not user:
        raise credentials_exception
    return UserOut(**user)


# one stop shop for everything you need to know about the signed in user
async def getContext(signedInUser: UserOut=Depends(getCurrentUser)):
    # get courses that the user is enroled in
    courses = await EnrolmentTable.getEnroledCourses(signedInUser.id)
    roles = {course['id'] : course['role'] for course in courses}
    courses = [CourseOut(**course) for course in courses]
    return TokenContext(signedInUser=signedInUser, enroledCourses=courses,
                        roles=roles)


def create(*, data: dict,
           expires_delta: timedelta = timedelta(minutes=TOKEN_EXPIRE)):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, TOKEN_SECRET, algorithm=TOKEN_ALGORITHM)
    return encoded_jwt
