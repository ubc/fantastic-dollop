import logging
from typing import Any, Dict, List, NamedTuple

from sqlalchemy.sql.expression import and_, exists, select
from sqlalchemy.sql.operators import Operators
from sqlalchemy import Column, Table

from pydantic import BaseModel

# database connection
from app import db

log = logging.getLogger(__name__)

# Helpers to compensate for not being able to use SQLAlchemy's ORM


class RowSpec(NamedTuple):
    table: Table
    conditions: List[Operators]


# We need to validate ids used in the API path, such as course, exams, etc.
# Instead of doing multiple queries to check if each individual item exists,
# this function attempts to shorten it to just 1 query to check if everything
# we need exists.
#
# The end goal is to build an SQL query that looks something like this:
#   SELECT EXISTS( SELECT 1 FROM course WHERE id=1 ) AND EXISTS( SELECT 1 FROM exam WHERE id=2 AND course_id=1 ) as "exists";
# which returns true if everything exists, false otherwise.
#
# An individual RowSpec would be specified like this:
#    RowSpec(ExamTable.table, [ExamTable.table.c.id==2,
#                              ExamTable.table.c.course_id==1])
# where we specify the table and the fields/values that we need to check. Note
# the multiple conditions, we sometimes might want to make sure that the given
# exam actually belongs to the course given in the path.
async def checkRowsExists(rowSpecs: List[RowSpec]):
    conditions = []
    for tableCondition in rowSpecs:
        # build a EXISTS() query
        query = tableCondition.table.select()
        for condition in tableCondition.conditions:
            # combine conditions into the WHERE clause
            query = query.where(condition)
        conditions.append(exists(query))
    # combine the exists queries together
    query = select([and_(*conditions)])
    return await db.execute(query)


async def getByField(table: Table, field: Column, value):
    query = table.select().where(field==value)
    ret = await db.fetch_one(query)
    return ret


async def getAllByField(table: Table, field: Column, value):
    query = table.select().where(field==value)
    ret = await db.fetch_all(query)
    return ret


async def getByFields(table: Table, fields: Dict[Column, Any]):
    wheres = [col == val for col, val in fields.items()]
    query = table.select()
    for where in wheres:
        query = query.where(where)
    return await db.fetch_one(query)


async def getById(table: Table, value: int):
    return await getByField(table, table.c.id, value)


async def add(table: Table, info: BaseModel):
    newVals = info.dict(skip_defaults=True)
    query = table.insert().values(newVals)
    newId = await db.execute(query)
    return await getById(table, newId)


async def edit(table: Table, info: BaseModel):
    newVals = info.dict(skip_defaults=True)
    query = table.update().where(table.c.id==info.id).values(newVals)
    await db.execute(query)
    return await getById(table, info.id)


async def delete(table: Table, itemId: int):
    query = table.delete().where(table.c.id==itemId)
    await db.execute(query)
    return
