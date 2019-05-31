import logging

import sqlalchemy as sa
from sqlalchemy import Column, DateTime, Integer, Unicode, Table
from app.tables import dbMetadata

# database connection
from app import db

from app.helpers import TableRetriever

from app.models.Course import CourseIn, CourseNewIn, CourseOut 

log = logging.getLogger(__name__)

table = Table(
    'course',
    dbMetadata,
    Column('id', Integer, primary_key=True),
    Column('name', Unicode(255), unique=True),
    Column('created', DateTime),
    Column('modified', DateTime, onupdate=sa.func.current_timestamp())
)

async def getByName(name: str):
    return await TableRetriever.getByField(table, table.c.name, name)

async def get(courseId: int):
    return await TableRetriever.getById(table, courseId)

async def getAll():
    query = table.select()
    return await db.fetch_all(query)

async def add(info: CourseNewIn):
    newVals = info.dict(skip_defaults=True)
    query = table.insert().values(newVals)
    newId = await db.execute(query)
    return await get(newId)

async def edit(info: CourseIn):
    newVals = info.dict(skip_defaults=True)
    query = table.update().where(table.c.id==info.id).values(newVals)
    await db.execute(query)
    return await get(info.id)

async def delete(courseId: int):
    query = table.delete().where(table.c.id==courseId)
    await db.execute(query)
    return

async def has(name: str=None, courseId: int=None):
    courseExists = False
    if name:
        courseExists = await getByName(name)
    elif courseId:
        courseExists = await get(courseId)
    else:
        log.warning("No parameter passed into CourseTable.has(), will always return False.")
    if courseExists:
        return True
    return False
