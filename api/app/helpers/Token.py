import logging

from datetime import datetime, timedelta

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from starlette.status import HTTP_401_UNAUTHORIZED

import jwt
from jwt import PyJWTError

from app.config import EnvConfig
from app.models.User import UserOut
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
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except PyJWTError:
        raise credentials_exception
    user = await UserTable.getByUsername(username)
    if not user:
        raise credentials_exception
    return UserOut(**user)

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
