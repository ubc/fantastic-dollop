import logging
from typing import List, NamedTuple

import sqlalchemy as sa
from sqlalchemy.sql.expression import and_, exists, select
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Table, Unicode
from app.tables import dbMetadata, ExamTable

# database connection
from app import db

from app.helpers import TableOp
from app.helpers.TableOp import RowSpec

from app.models.ExamSource import ExamSourceIn, ExamSourceNewIn

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


async def getAll(examId: int):
    rowSpecs = []
    rowSpecs.append(
        RowSpec(ExamTable.table, [ExamTable.table.c.id==3])
    )
    rowSpecs.append(
        RowSpec(ExamTable.table, [ExamTable.table.c.id==2,
                                  ExamTable.table.c.course_id==1])
    )
    ret = await TableOp.checkRowsExists(rowSpecs)
    log.debug("**********************************************")
    log.debug(ret)

    return await TableOp.getAllByField(table, table.c.exam_id, examId)


async def get(itemId: int):
    return await TableOp.getById(table, itemId)


async def add(info: ExamSourceNewIn):
    return await TableOp.add(table, info)


async def edit(info: ExamSourceIn):
    return await TableOp.edit(table, info)


async def delete(itemId: int):
    source = await get(itemId)
    depot = DepotManager.get()
    depot.delete(source['file'])
    await TableOp.delete(table, itemId)
    return


async def has(courseId: int, examId: int):
    ret = await get(examId)
    if ret:
        # need to make sure that the exam is actually in the course
        if ret['course_id'] == courseId:
            return True
    return False
