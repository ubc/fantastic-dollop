"""add system admin role for user

Revision ID: 1b43d3d96bf2
Revises: 1628a03786a8
Create Date: 2019-05-26 23:41:29.568690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b43d3d96bf2'
down_revision = '1628a03786a8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('created', sa.DateTime,
                                     server_default=sa.func.current_timestamp()))
    op.add_column('users', sa.Column('isAdmin', sa.Boolean, nullable=False,
                                     server_default=sa.sql.expression.false()))


def downgrade():
    op.drop_column('users', 'created')
    op.drop_column('users', 'isAdmin')
