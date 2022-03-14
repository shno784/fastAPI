"""add content column to posts table

Revision ID: 1d6255581802
Revises: 703e86cfaed1
Create Date: 2022-03-11 10:37:39.711372

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d6255581802'
down_revision = '703e86cfaed1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
