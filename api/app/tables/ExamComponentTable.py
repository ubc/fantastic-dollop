import logging

import sqlalchemy as sa
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Table, UnicodeText
from app.tables import dbMetadata, ExamTable

# database connection
from app import db

from app.helpers import TableOp
from app.helpers.TableOp import RowSpec

from app.models.ExamComponent import ExamComponentIn, ExamComponentNewIn

log = logging.getLogger(__name__)

table = Table(
    'exam_component',
    dbMetadata,
    Column('id', Integer, primary_key=True),
    Column('exam_id', Integer, ForeignKey('exam.id',ondelete="CASCADE"),
           nullable=False),
    Column('exam_component_type_id', Integer,
           ForeignKey('exam_component_type.id', ondelete="CASCADE"),
           nullable=False),
    Column('sequence', Integer,
           comment='Determines order, eg: question 1, question 2...'),
    Column('page_start', Integer,
           comment='The pages from the exam source to take.'),
    Column('page_end', Integer),
    Column('mark', Integer, server_default='0'),
    Column('comment', UnicodeText,
           comment='Visible only to instructors, as a note-to-self type of comment.'),
    Column('modified', DateTime, onupdate=sa.func.current_timestamp()),
    Column('created', DateTime)
)


async def getAll(courseId: int, examId: int):
    query = sa.sql.select([ExamTable.table.c.course_id, table]) \
        .where(table.c.exam_id == examId)
    return await db.fetch_all(query)


async def get(courseId: int, itemId: int):
    query = sa.sql.select([ExamTable.table.c.course_id, table]) \
        .where(table.c.id == itemId)
    return await db.fetch_one(query)


async def add(courseId: int, info: ExamComponentNewIn):
    component = await TableOp.add(table, info)
    return await get(courseId, component['id'])


async def edit(courseId: int, info: ExamComponentIn):
    component = await TableOp.edit(table, info)
    return await get(courseId, component['id'])


async def delete(courseId: int, itemId: int):
    return await TableOp.delete(table, itemId)


async def hasParents(courseId: int, examId: int):
    rowSpecs = []
    rowSpecs.append(
        RowSpec(ExamTable.table, [ExamTable.table.c.id == examId,
                                  ExamTable.table.c.course_id == courseId])
    )
    return await TableOp.checkRowsExists(rowSpecs)


async def has(courseId: int, examId: int, componentId: int):
    rowSpecs = []
    rowSpecs.append(
        RowSpec(ExamTable.table, [ExamTable.table.c.id == examId,
                                  ExamTable.table.c.course_id == courseId])
    )
    rowSpecs.append(RowSpec(table, [table.c.id == componentId,
                                    table.c.exam_id == examId]))
    return await TableOp.checkRowsExists(rowSpecs)
