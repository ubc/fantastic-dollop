import logging

import sqlalchemy as sa
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Table, Unicode
from app.tables import dbMetadata, ExamTable

# database connection
from app import db

from app.helpers import TableOp
from app.helpers.TableOp import RowSpec

from app.models.ExamSource import ExamSourceNewIn

# file management
from depot.manager import DepotManager

log = logging.getLogger(__name__)

table = Table(
    'exam_source',
    dbMetadata,
    Column('id', Integer, primary_key=True),
    Column('exam_id', Integer, ForeignKey('exam.id',ondelete="CASCADE"),
           nullable=False),
    Column('name', Unicode(255)),
    Column('file', Unicode(255), nullable=False, unique=True),
    Column('page_count', Integer),
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


async def add(courseId: int, info: ExamSourceNewIn):
    source = await TableOp.add(table, info)
    return await get(courseId, source['id'])


async def delete(courseId: int, itemId: int):
    source = await get(courseId, itemId)
    sourceFileId = source['file']
    await TableOp.delete(table, itemId)
    depot = DepotManager.get()
    depot.delete(sourceFileId)
    return


async def hasParents(courseId: int, examId: int):
    rowSpecs = []
    rowSpecs.append(
        RowSpec(ExamTable.table, [ExamTable.table.c.id == examId,
                                  ExamTable.table.c.course_id == courseId])
    )
    return await TableOp.checkRowsExists(rowSpecs)


async def has(courseId: int, examId: int, sourceId: int):
    rowSpecs = []
    rowSpecs.append(
        RowSpec(ExamTable.table, [ExamTable.table.c.id == examId,
                                  ExamTable.table.c.course_id == courseId])
    )
    rowSpecs.append(RowSpec(table, [table.c.id == sourceId,
                                    table.c.examId == examId]))
    return await TableOp.checkRowsExists(rowSpecs)

