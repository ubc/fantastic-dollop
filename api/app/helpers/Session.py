import logging

from fastapi import Depends

from fastapi.security import OAuth2PasswordBearer

log = logging.getLogger(__name__)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/signin")

async def getCurrentUser(token: str=Depends(oauth2_scheme)):
    user = {'test': 'blah'}
    return user
