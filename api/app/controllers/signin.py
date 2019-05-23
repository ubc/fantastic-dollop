import logging

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from pydantic import BaseModel

# http status codes
from starlette.status import HTTP_400_BAD_REQUEST

# database table
from app.tables import UserTable
# database connection
from app import db

# session & password security
from app.helpers import Token, Password

log = logging.getLogger(__name__)
router = APIRouter()

class TokenOut(BaseModel):
    access_token: str
    token_type: str

@router.post("/signin", response_model=TokenOut)
async def signin(formData: OAuth2PasswordRequestForm = Depends()):
    log.info("Starting user sign in for '" + formData.username + "'")
    ret = await UserTable.getByUsername(formData.username)
    if not ret:
        log.info("Sign in failed.")
        log.debug("Username not found: " + formData.username)
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail="Incorrect username or password")

    if not Password.verify(formData.password, ret['password']):
        log.info("Sign in failed.")
        log.debug("Incorrect password.")
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail="Incorrect username or password")
    log.info("Sign in successful, generating token.")
    token = Token.create(data={"sub": ret['username']})
    return {"access_token": token, "token_type": "bearer"}
