"""Create doctors table

Revision ID: 89c15a2c41ce
Revises: 1bd510a54cef
Create Date: 2025-03-31 18:11:59.264788

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import uuid

from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '89c15a2c41ce'
down_revision: Union[str, None] = '1bd510a54cef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """create doctors table."""
    op.create_table(
        "doctors",
        sa.Column("id", sa.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False),
        sa.Column("specialization_id", sa.UUID(as_uuid=True), sa.ForeignKey("doctor_specializations.id", ondelete="CASCADE"), nullable=False),
        sa.Column("first_name", sa.String(100), nullable=True),
        sa.Column("last_name", sa.String(100), nullable=True),
        sa.Column("email", sa.String(100), nullable=True, unique=True),
        sa.Column("username", sa.String(100), nullable=False, unique=True),
        sa.Column("phone_number", sa.String(100), nullable=True, unique=True),
        sa.Column("is_active", sa.Boolean, default=True, nullable=False),
        sa.Column("date_created", sa.DateTime, server_default=sa.func.now(), nullable=False),
        sa.Column("date_modified", sa.DateTime, nullable=True),
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
    # ### end Alembic commands ###
