"""create posts table

Revision ID: 703e86cfaed1
Revises: 
Create Date: 2022-03-11 10:25:50.064734

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '703e86cfaed1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key= True),
    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
