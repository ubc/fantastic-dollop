import logging

import sqlalchemy as sa
from sqlalchemy import Column, DateTime, Integer, Table, Unicode
from app.tables import dbMetadata

# database connection
from app import db

from app.helpers import TableOp

log = logging.getLogger(__name__)

table = Table(
    'exam_component_type',
    dbMetadata,
    Column('id', Integer, primary_key=True),
    Column('name', Unicode(255), unique=True, nullable=False),
    Column('modified', DateTime, onupdate=sa.func.current_timestamp()),
    Column('created', DateTime)
)


async def getAll():
    query = table.select().order_by('id')
    return await db.fetch_all(query)


async def has(typeId: int):
    ret = await TableOp.getById(table, typeId)
    if ret:
        return True
    return False
