"""add courses table

Revision ID: dcf5e4847c19
Revises: 1b43d3d96bf2
Create Date: 2019-05-27 14:18:25.999916

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, DateTime, Integer, Unicode


# revision identifiers, used by Alembic.
revision = 'dcf5e4847c19'
down_revision = '1b43d3d96bf2'
branch_labels = None
depends_on = None


def upgrade():
    # automatically updated 'modified' timestamp specified by 'server_onupdate'
    # isn't supported on sqlite
    op.create_table(
        'courses',
        Column('id', Integer, primary_key=True),
        Column('name', Unicode(255), nullable=False, unique=True),
        Column('modified', DateTime, server_default=sa.func.current_timestamp(),
               server_onupdate=sa.func.current_timestamp()),
        Column('created', DateTime, server_default=sa.func.current_timestamp()),
    )
    op.add_column(
        'users',
        Column('modified', sa.DateTime,
               server_default=sa.func.current_timestamp(),
               server_onupdate=sa.func.current_timestamp())
    )

def downgrade():
    op.drop_table('courses')
    op.drop_column('users', 'modified')
