import logging

import sqlalchemy as sa
from sqlalchemy import Column, DateTime, Integer, Table, Unicode
from app.tables import dbMetadata

# database connection
from app import db

log = logging.getLogger(__name__)

table = Table(
    'role',
    dbMetadata,
    Column('id', Integer, primary_key=True),
    Column('name', Unicode(255), unique=True),
    Column('modified', DateTime, onupdate=sa.func.current_timestamp()),
    Column('created', DateTime)
)


async def getAll():
    query = table.select().order_by('id')
    return await db.fetch_all(query)
