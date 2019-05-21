import logging

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# http status codes
from starlette.status import HTTP_400_BAD_REQUEST

# database table
from app.tables.User import userTable
# database connection
from app import db

log = logging.getLogger(__name__)
router = APIRouter()

@router.post("/signin")
async def signin(formData: OAuth2PasswordRequestForm = Depends()):
    log.debug("Starting user sign in")
    query = userTable.select().where(
        userTable.c.username == formData.username)
    ret = await db.fetch_one(query)
    if not ret:
        log.debug("Username not found: " + formData.username)
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail="Incorrect username or password")
    if ret['password'] != formData.password:
        log.debug("Incorrect password.")
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail="Incorrect username or password")
    log.debug("Sign in successful!")
    return {"access_token": "some token", "token_type": "bearer"}
