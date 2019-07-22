"""add exam tables

Revision ID: 9d35bf52e540
Revises: a54d28f79eb3
Create Date: 2019-06-19 14:04:33.539830

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Unicode, \
    UnicodeText, UniqueConstraint


# revision identifiers, used by Alembic.
revision = '9d35bf52e540'
down_revision = 'a54d28f79eb3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'exam',
        Column('id', Integer, primary_key=True),
        Column('course_id', Integer, ForeignKey('course.id',ondelete="CASCADE"),
               nullable=False),
        Column('name', Unicode(255), nullable=False),
        Column('print_id', Unicode(255),
               comment='ID printed on every page of every exam to help humans identify and sort exams. Otherwise, they would need to somehow read the auto-generated QR codes.'),
        Column('modified', DateTime, server_default=sa.func.current_timestamp(),
               server_onupdate=sa.func.current_timestamp()),
        Column('created', DateTime, server_default=sa.func.current_timestamp())
    )

    op.create_table(
        'exam_source',
        Column('id', Integer, primary_key=True),
        Column('exam_id', Integer, ForeignKey('exam.id',ondelete="CASCADE"),
               nullable=False),
        Column('name', Unicode(255), nullable=False),
        Column('file', Unicode(255), nullable=False, unique=True),
        Column('page_count', Integer),
        Column('modified', DateTime, server_default=sa.func.current_timestamp(),
               server_onupdate=sa.func.current_timestamp()),
        Column('created', DateTime, server_default=sa.func.current_timestamp())
    )

    componentTypeTable = op.create_table(
        'exam_component_type',
        Column('id', Integer, primary_key=True),
        Column('name', Unicode(255), unique=True, nullable=False),
        Column('modified', DateTime, server_default=sa.func.current_timestamp(),
               server_onupdate=sa.func.current_timestamp()),
        Column('created', DateTime, server_default=sa.func.current_timestamp())
    )
    op.bulk_insert(componentTypeTable, [
        {'name': 'ID Page'},
        {'name': 'Informational'},
        {'name': 'Question'}
    ])

    op.create_table(
        'exam_component',
        Column('id', Integer, primary_key=True),
        Column('exam_id', Integer, ForeignKey('exam.id', ondelete="CASCADE"),
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
        Column('modified', DateTime, server_default=sa.func.current_timestamp(),
               server_onupdate=sa.func.current_timestamp()),
        Column('created', DateTime, server_default=sa.func.current_timestamp()),
        comment='Defines components used to generate papers for the exam. The order of the questions, ID pages, etc.'
    )

    op.create_table(
        'exam_component_source',
        Column('id', Integer, primary_key=True),
        Column('exam_component_id', Integer,
               ForeignKey('exam_component.id', ondelete="CASCADE"),
               nullable=False),
        Column('exam_source_id', Integer,
               ForeignKey('exam_source.id', ondelete="CASCADE"),
               nullable=False),
        Column('modified', DateTime, server_default=sa.func.current_timestamp(),
               server_onupdate=sa.func.current_timestamp()),
        Column('created', DateTime, server_default=sa.func.current_timestamp()),
        UniqueConstraint('exam_component_id', 'exam_source_id'),
        comment='When generating a paper, defines the sources we should pull from for the given component.'
    )

    op.create_table(
        'exam_paper',
        Column('id', Integer, primary_key=True),
        Column('exam_id', Integer, ForeignKey('exam.id', ondelete="CASCADE"),
               nullable=False),
        Column('name', Unicode(255)),
        Column('file', Unicode(255), nullable=False, unique=True),
        Column('modified', DateTime, server_default=sa.func.current_timestamp(),
               server_onupdate=sa.func.current_timestamp()),
        Column('created', DateTime, server_default=sa.func.current_timestamp()),
        comment='Actual exam paper given to students.'
    )

    op.create_table(
        'exam_paper_component_source',
        Column('id', Integer, primary_key=True),
        Column('exam_paper_id', Integer,
               ForeignKey('exam_paper.id', ondelete="CASCADE"),
               nullable=False),
        Column('exam_component_id', Integer,
               ForeignKey('exam_component.id', ondelete="CASCADE"),
               nullable=False),
        Column('exam_source_id', Integer,
               ForeignKey('exam_source.id', ondelete="CASCADE"),
               nullable=False),
        UniqueConstraint('exam_paper_id', 'exam_component_id'),
        Column('modified', DateTime, server_default=sa.func.current_timestamp(),
               server_onupdate=sa.func.current_timestamp()),
        Column('created', DateTime, server_default=sa.func.current_timestamp())
    )


def downgrade():
    op.drop_table('exam_paper_component_source')
    op.drop_table('exam_paper')
    op.drop_table('exam_component_source')
    op.drop_table('exam_component')
    op.drop_table('exam_component_type')
    op.drop_table('exam_source')
    op.drop_table('exam')
