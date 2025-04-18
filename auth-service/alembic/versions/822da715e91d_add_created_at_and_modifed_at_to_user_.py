"""add created_at and modifed_at to user table

Revision ID: 822da715e91d
Revises: 1d2e8ad3a6d3
Create Date: 2025-04-07 23:49:30.184310

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '822da715e91d'
down_revision: Union[str, None] = '1d2e8ad3a6d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', sa.Column('date_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    op.alter_column('users', sa.Column('date_modified', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###