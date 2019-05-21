"""add user session storage

Revision ID: 1628a03786a8
Revises: 08c4e9538fcb
Create Date: 2019-05-20 21:52:58.867266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1628a03786a8'
down_revision = '08c4e9538fcb'
branch_labels = None
depends_on = None


def upgrade():
    # make usernames unique, they have to be, since we're using them for sign in
    op.create_unique_constraint('unique_username', 'users', ['username'])

def downgrade():
    op.drop_constraint('unique_username', 'users')
