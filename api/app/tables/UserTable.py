import logging

from fastapi import HTTPException

from starlette.status import HTTP_409_CONFLICT

import sqlalchemy as sa
from sqlalchemy import Boolean, Column, DateTime, Integer, Unicode, Table
from app.tables import dbMetadata

from asyncpg.exceptions import UniqueViolationError

# database connection
from app import db

from app.helpers import Password
from app.helpers import TableOp

from app.models.User import UserIn, UserNewIn

log = logging.getLogger(__name__)

table = Table(
    'user',
    dbMetadata,
    Column('id', Integer, primary_key=True),
    Column('username', Unicode(255), nullable=False),
    Column('password', Unicode(255), nullable=False),
    Column('name', Unicode(255)),
    Column('preferredName', Unicode(255)),
    Column('email', Unicode(255)),
    Column('studentNumber', Unicode(255)),
    Column('isAdmin', Boolean),
    Column('created', DateTime),
    # postgresql doesn't have onupdate without sql triggers, so we'll just
    # let sqlalchemy take care of it instead
    Column('modified', DateTime, onupdate=sa.func.current_timestamp())
)

async def getByUsername(username: str):
    return await TableOp.getByField(table, table.c.username, username)

async def get(userId: int):
    return await TableOp.getById(table, userId)

async def getAll():
    query = table.select().order_by('username')
    return await db.fetch_all(query)

async def add(userInfo: UserNewIn):
    newVals = userInfo.dict(skip_defaults=True)
    newVals['password'] = Password.hash(userInfo.password)
    query = table.insert().values(newVals)
    try:
        userId = await db.execute(query)
    except UniqueViolationError as e:
        raise HTTPException(status_code=HTTP_409_CONFLICT,
                            detail=e.detail)
    return await get(userId)

async def edit(userInfo: UserIn):
    newVals = userInfo.dict(skip_defaults=True)
    # rehash the password if user supplied a new one
    if userInfo.password:
        newVals['password'] = Password.hash(userInfo.password)
    elif 'password' in newVals:
        # user supplied an empty string as a password, ignore it
        del newVals['password']

    query = table.update().where(table.c.id==userInfo.id).values(newVals)
    try:
        await db.execute(query)
    except UniqueViolationError as e:
        raise HTTPException(status_code=HTTP_409_CONFLICT,
                            detail=e.detail)

    return await get(userInfo.id)

async def delete(userId: int):
    query = table.delete().where(table.c.id==userId)
    await db.execute(query)
    return

async def has(username: str=None, userId: int=None):
    userExists = None
    if username:
        userExists = await getByUsername(username)
    elif userId:
        userExists = await get(userId)
    else:
        log.warning("No parameter passed into UserTable.has(), will always return False.")
    if userExists:
        return True
    return False
