"""add enrolment and role table

Revision ID: a54d28f79eb3
Revises: dcf5e4847c19
Create Date: 2019-05-30 15:27:06.627753

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Unicode, UniqueConstraint

import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '../..')))
from helpers import Permission

# revision identifiers, used by Alembic.
revision = 'a54d28f79eb3'
down_revision = '08c4e9538fcb'
branch_labels = None
depends_on = None


def upgrade():
    roleTable = op.create_table(
        'role',
        Column('id', Integer, primary_key=True),
        Column('name', Unicode(255), unique=True),
        Column('modified', DateTime, server_default=sa.func.current_timestamp(),
               server_onupdate=sa.func.current_timestamp()),
        Column('created', DateTime, server_default=sa.func.current_timestamp())
    )
    op.bulk_insert(roleTable, [
        {'name': Permission.STUDENT},
        {'name': Permission.TA},
        {'name': Permission.INSTRUCTOR}
    ])
    op.create_table(
        'enrolment',
        Column('id', Integer, primary_key=True),
        Column('course_id', Integer, ForeignKey('course.id',ondelete="CASCADE")),
        Column('user_id', Integer, ForeignKey('user.id',ondelete="CASCADE")),
        Column('role_id', Integer, ForeignKey('role.id')),
        Column('modified', DateTime, server_default=sa.func.current_timestamp(),
               server_onupdate=sa.func.current_timestamp()),
        Column('created', DateTime, server_default=sa.func.current_timestamp()),
        UniqueConstraint('course_id', 'user_id')
    )


def downgrade():
    op.drop_table('enrolment')
    op.drop_table('role')
