import logging

import sqlalchemy as sa
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Table, Unicode
from app.tables import dbMetadata

# database connection
#from app import db

from app.helpers import TableOp

from app.models.Exam import ExamIn, ExamNewIn

log = logging.getLogger(__name__)

table = Table(
    'exam',
    dbMetadata,
    Column('id', Integer, primary_key=True),
    Column('course_id', Integer, ForeignKey('course.id',ondelete="CASCADE")),
    Column('name', Unicode(255)),
    Column('print_id', Unicode(255)),
    Column('modified', DateTime, onupdate=sa.func.current_timestamp()),
    Column('created', DateTime)
)


async def getAll(courseId: int):
    return await TableOp.getAllByField(table, table.c.course_id, courseId, "name")


async def get(itemId: int):
    return await TableOp.getById(table, itemId)


async def add(info: ExamNewIn):
    return await TableOp.add(table, info)


async def edit(info: ExamIn):
    return await TableOp.edit(table, info)


async def delete(examId: int):
    await TableOp.delete(table, examId)
    return


async def has(courseId: int, examId: int):
    ret = await get(examId)
    if ret:
        # need to make sure that the exam is actually in the course
        if ret['course_id'] == courseId:
            return True
    return False
