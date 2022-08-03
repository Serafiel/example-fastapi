"""add content column to posts table

Revision ID: 6240e7dfdf39
Revises: 5dda3511a932
Create Date: 2022-08-02 17:38:21.244809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6240e7dfdf39'
down_revision = '5dda3511a932'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False ))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
