import logging

import sqlalchemy as sa
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Unicode, Table
from app.tables import dbMetadata

# database connection
from app import db

from app.helpers import TableRetriever

from app.models.Course import CourseIn, CourseNewIn, CourseOut

from app.tables import RoleTable, UserTable

log = logging.getLogger(__name__)

table = Table(
    'enrolment',
    dbMetadata,
    Column('id', Integer, primary_key=True),
    Column('course_id', Integer, ForeignKey('course.id',ondelete="CASCADE")),
    Column('user_id', Integer, ForeignKey('user.id',ondelete="CASCADE")),
    Column('role_id', Integer, ForeignKey('role.id')),
    Column('created', DateTime),
    Column('modified', DateTime, onupdate=sa.func.current_timestamp())
)

async def getEnroled(courseId: int):
    query = sa.sql \
        .select([
            UserTable.table,
            RoleTable.table.c.id.label('role_id'),
            RoleTable.table.c.name.label('role')]) \
        .where(
            sa.sql.and_(
                table.c.course_id == courseId,
                table.c.user_id == UserTable.table.c.id,
                table.c.role_id == RoleTable.table.c.id
            ))
    return await db.fetch_all(query)
