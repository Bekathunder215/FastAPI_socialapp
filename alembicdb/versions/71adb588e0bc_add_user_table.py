"""add user table

Revision ID: 71adb588e0bc
Revises: f6c67090e60a
Create Date: 2025-01-24 15:02:29.874237

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '71adb588e0bc'
down_revision: Union[str, None] = 'f6c67090e60a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id',sa.Integer(),primary_key=True,nullable=False),
                    sa.Column('email',sa.String(),nullable=False),
                    sa.Column('password',sa.String(),nullable=False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False),
                    sa.UniqueConstraint('email'))


def downgrade() -> None:
    op.drop_table('users')
