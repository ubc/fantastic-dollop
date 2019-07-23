import logging

import sqlalchemy as sa
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Table, UnicodeText
from app.tables import dbMetadata, ExamComponentTable, ExamSourceTable, ExamTable

# database connection
from app import db

from app.helpers import TableOp
from app.helpers.TableOp import RowSpec

from app.models.ExamComponentSource import ExamComponentSourceIn, ExamComponentSourceNewIn

log = logging.getLogger(__name__)

table = Table(
    'exam_component_source',
    dbMetadata,
    Column('id', Integer, primary_key=True),
    Column('exam_component_id', Integer,
           ForeignKey('exam_component.id', ondelete="CASCADE"),
           nullable=False),
    Column('exam_source_id', Integer,
           ForeignKey('exam_source.id', ondelete="CASCADE"),
           nullable=False),
    Column('modified', DateTime, onupdate=sa.func.current_timestamp()),
    Column('created', DateTime)
)


async def getAll(examComponentId: int):
    query = sa.sql.select([
            ExamComponentTable.table.c.exam_id,
            ExamTable.table.c.id,
            ExamTable.table.c.course_id,
            ExamSourceTable.table.c.name.label('exam_source_name'),
            table
        ]) \
        .where(sa.sql.and_(
            table.c.exam_component_id == examComponentId,
            ExamComponentTable.table.c.id == examComponentId,
            ExamTable.table.c.id == ExamComponentTable.table.c.exam_id,
            ExamSourceTable.table.c.id == table.c.exam_source_id
        ))
    return await db.fetch_all(query)


async def get(examComponentSourceId: int):
    query = sa.sql.select([
            ExamComponentTable.table.c.exam_id,
            ExamTable.table.c.id,
            ExamTable.table.c.course_id,
            ExamSourceTable.table.c.name.label('exam_source_name'),
            table
        ]) \
        .where(sa.sql.and_(
            table.c.id == examComponentSourceId,
            ExamComponentTable.table.c.id == table.c.exam_component_id,
            ExamTable.table.c.id == ExamComponentTable.table.c.exam_id,
            ExamSourceTable.table.c.id == table.c.exam_source_id
        ))
    return await db.fetch_one(query)


async def add(info: ExamComponentSourceNewIn):
    componentSource = await TableOp.add(table, info)
    return await get(componentSource['id'])


async def delete(itemId: int):
    return await TableOp.delete(table, itemId)


async def hasParents(courseId: int, examId: int, componentId: int):
    rowSpecs = []
    rowSpecs.append(
        RowSpec(ExamTable.table, [ExamTable.table.c.id == examId,
                                  ExamTable.table.c.course_id == courseId])
    )
    rowSpecs.append(
        RowSpec(ExamComponentTable.table,
                [ExamComponentTable.table.c.id == componentId,
                 ExamComponentTable.table.c.exam_id == examId])
    )
    return await TableOp.checkRowsExists(rowSpecs)


async def has(courseId: int, examId: int, componentId: int, sourceId: int):
    rowSpecs = []
    rowSpecs.append(
        RowSpec(ExamTable.table, [ExamTable.table.c.id == examId,
                                  ExamTable.table.c.course_id == courseId])
    )
    rowSpecs.append(
        RowSpec(ExamComponentTable.table,
                [ExamComponentTable.table.c.id == componentId,
                 ExamComponentTable.table.c.exam_id == examId])
    )
    rowSpecs.append(RowSpec(table, [table.c.id == sourceId,
                                    table.c.exam_component_id == componentId]))
    return await TableOp.checkRowsExists(rowSpecs)
