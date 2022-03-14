"""add rest of colums to posts

Revision ID: 3d2a6c9f056a
Revises: b51137c7e546
Create Date: 2022-03-11 10:59:53.719358

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d2a6c9f056a'
down_revision = 'b51137c7e546'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column(
        'published',sa.Boolean(),nullable=False, server_default='TRUE'),
    op.add_column('posts',sa.Column(
        'created_at',sa.TIMESTAMP(timezone=True),nullable=False, server_default=sa.text('NOW()')
                                   )
                 )  
                 )
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
