"""Create role for user

Revision ID: c6bcf3612324
Revises: 
Create Date: 2024-04-01 18:16:36.567736

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c6bcf3612324'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('role', sa.String(), nullable=True))


def downgrade() -> None:
    pass
