"""add user table

Revision ID: 3df06695dc0c
Revises: 1d6255581802
Create Date: 2022-03-11 10:45:41.917478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3df06695dc0c'
down_revision = '1d6255581802'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id',sa.Integer(),nullable=False, primary_key=True),
                    sa.Column('email',sa.String(),nullable=False, unique=True),
                    sa.Column('password',sa.String(),nullable=False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
