import logging
from typing import Any, Dict

import sqlalchemy as sa
from sqlalchemy import Column, Table

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
