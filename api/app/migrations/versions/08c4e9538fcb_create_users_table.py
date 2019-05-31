"""create users table

Revision ID: 08c4e9538fcb
Revises:
Create Date: 2019-05-03 13:54:37.306918

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Boolean, Column, DateTime, Integer, Unicode, UnicodeText

# revision identifiers, used by Alembic.
revision = '08c4e9538fcb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # length on fields is specified for compatibility with mysql,
    # postgres doesn't care if no length is entered. A length of 255
    # used to be max in mysql 4, but is no longer the case in mysql 5.
    # It's used here cause it's familiar, but can be upped if needed.
    userTable = op.create_table(
        'user',
        Column('id', Integer, primary_key=True),
        Column('username', Unicode(255), nullable=False, unique=True),
        Column('password', Unicode(255), nullable=False),
        Column('name', Unicode(255)),
        Column('preferredName', Unicode(255)),
        Column('email', Unicode(255)),
        Column('studentNumber', Unicode(255)),
        Column('isAdmin', Boolean, nullable=False,
               server_default=sa.sql.expression.false()),
        Column('modified', DateTime, server_default=sa.func.current_timestamp(),
               server_onupdate=sa.func.current_timestamp()),
        Column('created', DateTime, server_default=sa.func.current_timestamp())

    )
    op.bulk_insert(userTable, [
        {'username': 'admin', 'password': '$2b$12$kD4DGvXC3GWOQkc0mBO4xejJM3pupLif49.sFeCTkeesGR1wEdw4S', 'isAdmin': True}
    ])
    op.create_table(
        'course',
        Column('id', Integer, primary_key=True),
        Column('name', Unicode(255), nullable=False, unique=True),
        Column('description', UnicodeText),
        Column('isActive', Boolean, server_default=sa.sql.expression.true()),
        Column('modified', DateTime, server_default=sa.func.current_timestamp(),
               server_onupdate=sa.func.current_timestamp()),
        Column('created', DateTime, server_default=sa.func.current_timestamp()),
    )

def downgrade():
    op.drop_table('course')
    op.drop_table('user')
