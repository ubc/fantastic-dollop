import logging

import sqlalchemy as sa
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Table
from app.tables import dbMetadata

from typing import List

# database connection
from app import db

from app.models.Enrolment import EnrolmentIn, EnrolmentNewIn

from app.tables import CourseTable, RoleTable, UserTable

from app.helpers import TableOp

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

async def getByCourseAndUserId(courseId: int, userId: int):
    return await TableOp.getByFields(table, {table.c.course_id: courseId,
                                                    table.c.user_id: userId})


async def getList(courseId: int, limitUserIds: List[int] = None):
    userIdLimit = sa.sql.expression.true()
    if limitUserIds:
        userIdLimit = UserTable.table.c.id.in_(limitUserIds)

    query = sa.sql \
        .select([
            UserTable.table,
            UserTable.table.c.id.label('user_id'),
            RoleTable.table.c.name.label('role'),
            table]) \
        .where(
            sa.sql.and_(
                table.c.course_id == courseId,
                table.c.user_id == UserTable.table.c.id,
                table.c.role_id == RoleTable.table.c.id,
                userIdLimit
            )) \
        .order_by('username')
    return await db.fetch_all(query)


# get courses that a user is in
async def getEnroledCourses(userId: int):
    query = sa.sql.select([
            RoleTable.table.c.name.label('role'),
            CourseTable.table
        ]) \
        .where(
            sa.sql.and_(
                table.c.user_id == userId,
                table.c.course_id == CourseTable.table.c.id,
                table.c.role_id == RoleTable.table.c.id
            ))
    return await db.fetch_all(query)


async def add(courseId: int, enrolments: List[EnrolmentNewIn]):
    newEnrolments = []
    userIds = []
    for enrolment in enrolments:
        newEnrolment = {
            'course_id': courseId,
            'user_id': enrolment.user_id,
            'role_id': enrolment.role_id
        }
        newEnrolments.append(newEnrolment)
        userIds.append(enrolment.user_id)
    query = table.insert().values(newEnrolments)
    await db.execute(query)
    return await getList(courseId, userIds)


# can only update single user roles
async def edit(courseId: int, enrolment: EnrolmentIn):
    query = table.update().where(table.c.id == enrolment.id)\
        .values({'role_id': enrolment.role_id})
    await db.execute(query)
    ret = await getList(courseId, [enrolment.user_id])
    return ret[0]


async def delete(courseId: int, enrolments: List[EnrolmentIn]):
    ids = [enrolment.id for enrolment in enrolments]
    query = table.delete().where(table.c.id.in_(ids))
    await db.execute(query)
    return
