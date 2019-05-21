from sqlalchemy import Column, Integer, Unicode, Table
from app.tables import db_metadata

userTable = Table(
    'users',
    db_metadata,
    Column('id', Integer, primary_key=True),
    Column('username', Unicode(255), nullable=False),
    Column('password', Unicode(255), nullable=False),
    Column('name', Unicode(255)),
    Column('preferredName', Unicode(255)),
    Column('email', Unicode(255)),
    Column('studentNumber', Unicode(255))
)
