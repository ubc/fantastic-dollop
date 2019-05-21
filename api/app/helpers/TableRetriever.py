from sqlalchemy import Column, Table

# database connection
from app import db

# I don't want to write an ORM (yet?), so hoping some helper methods would
# let me avoid that for now

async def getByField(table: Table, field: Column, value):
    query = table.select().where(field==value)
    ret = await db.fetch_one(query)
    return ret

async def getById(table: Table, value: int):
    return await getByField(table, table.c.id, value)
