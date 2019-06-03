import logging

import sqlalchemy as sa
from sqlalchemy import Column, DateTime, Integer, Unicode, Table
from app.tables import dbMetadata

log = logging.getLogger(__name__)

table = Table(
    'role',
    dbMetadata,
    Column('id', Integer, primary_key=True),
    Column('name', Unicode(255), unique=True),
    Column('created', DateTime),
    Column('modified', DateTime, onupdate=sa.func.current_timestamp())
)
