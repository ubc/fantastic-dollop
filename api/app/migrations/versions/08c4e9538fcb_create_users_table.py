"""create users table

Revision ID: 08c4e9538fcb
Revises: 
Create Date: 2019-05-03 13:54:37.306918

"""
from alembic import op
from sqlalchemy import Column, Integer, Unicode


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
    op.create_table(
        'users',
        Column('id', Integer, primary_key=True),
        Column('username', Unicode(255), nullable=False),
        Column('password', Unicode(255), nullable=False),
        Column('name', Unicode(255)),
        Column('preferredName', Unicode(255)),
        Column('email', Unicode(255)),
        Column('studentNumber', Unicode(255))
    )


def downgrade():
    op.drop_table('users')
