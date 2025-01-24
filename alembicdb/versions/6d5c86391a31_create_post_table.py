"""create post table

Revision ID: 6d5c86391a31
Revises: 
Create Date: 2025-01-24 14:50:48.634497

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6d5c86391a31'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id',sa.Integer(),primary_key=True,nullable=False), sa.Column('title',sa.String,nullable=False))

def downgrade() -> None:
    op.drop_table('posts')
