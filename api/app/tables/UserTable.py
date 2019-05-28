import logging

from sqlalchemy import Boolean, Column, DateTime, Integer, Unicode, Table
from app.tables import dbMetadata

# database connection
from app import db

from app.helpers import Password
from app.helpers import TableRetriever

from app.models.User import UserBase, UserIn, UserNewIn, UserOut

log = logging.getLogger(__name__)

table = Table(
    'users',
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
    Column('modified', DateTime)
)

async def getByUsername(username: str):
    return await TableRetriever.getByField(table, table.c.username, username)

async def get(userId: int):
    return await TableRetriever.getById(table, userId)

async def getAll():
    query = table.select()
    return await db.fetch_all(query)

async def add(userInfo: UserNewIn):
    newVals = userInfo.dict(skip_defaults=True)
    newVals['password'] = Password.hash(userInfo.password)
    query = table.insert().values(newVals)
    userId = await db.execute(query)
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
    await db.execute(query)
    return await get(userInfo.id)

async def has(userInfo: UserBase):
    userExists = await getByUsername(userInfo.username)
    if userExists:
        return True
    return False

