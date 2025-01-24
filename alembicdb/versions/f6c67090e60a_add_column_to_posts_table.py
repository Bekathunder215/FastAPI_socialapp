"""add column to posts table

Revision ID: f6c67090e60a
Revises: 6d5c86391a31
Create Date: 2025-01-24 14:59:53.901586

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6c67090e60a'
down_revision: Union[str, None] = '6d5c86391a31'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
