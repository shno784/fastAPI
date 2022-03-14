"""add foreign-key to posts table

Revision ID: b51137c7e546
Revises: 3df06695dc0c
Create Date: 2022-03-11 10:55:19.868087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b51137c7e546'
down_revision = '3df06695dc0c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users',
    local_cols=['owner_id'], remote_cols=['id'],ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('post_users_fk',table_name='posts')
    op.drop_column('posts','owner_id')
    pass
