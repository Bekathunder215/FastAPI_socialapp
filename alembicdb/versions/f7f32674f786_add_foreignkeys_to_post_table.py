"""add foreignkeys to post table

Revision ID: f7f32674f786
Revises: 71adb588e0bc
Create Date: 2025-01-24 15:06:58.898905

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f7f32674f786'
down_revision: Union[str, None] = '71adb588e0bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users', local_cols=['user_id'], remote_cols=['id'], ondelete="CASCADE")

def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'user_id')