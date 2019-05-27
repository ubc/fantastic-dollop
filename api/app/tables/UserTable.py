from sqlalchemy import Boolean, Column, DateTime, Integer, Unicode, Table
from app.tables import dbMetadata

# database connection
from app import db

from app.helpers import TableRetriever

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
    Column('created', DateTime)
)

async def getByUsername(username: str):
    return await TableRetriever.getByField(table, table.c.username, username)
