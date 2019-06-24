import logging
from typing import Any, Dict

import sqlalchemy as sa
from sqlalchemy import Column, Table

from pydantic import BaseModel

# database connection
from app import db

log = logging.getLogger(__name__)

# I don't want to write an ORM (yet?), so hoping some helper methods would
# let me avoid that for now

async def getByField(table: Table, field: Column, value):
    query = table.select().where(field==value)
    ret = await db.fetch_one(query)
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

