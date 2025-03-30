"""create patient insurance informations

Revision ID: 243a1b29d430
Revises: e28e3012446e
Create Date: 2025-03-30 01:53:35.114273

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision: str = '243a1b29d430'
down_revision: Union[str, None] = 'e28e3012446e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """create Patient insurance informations table"""
    op.create_table(
        "patient_insurance",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, nullable=False, default=sa.text("uuid_generate_v4()")),
        sa.Column("patient_id", UUID(as_uuid=True), sa.ForeignKey("patients.id", ondelete="CASCADE"), nullable=False, unique=True),
        sa.Column("provider_name", sa.String(100), nullable=False),
        sa.Column("policy_number", sa.String(100), nullable=False, unique=True),
        sa.Column("group_number", sa.String(100), nullable=True),
        sa.Column("plan_type", sa.String(100), nullable=True),
        sa.Column("coverage_start_date", sa.Date(), nullable=True),
        sa.Column("coverage_end_date", sa.Date(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default="true"),
        sa.Column("date_created", sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.Column("date_modified", sa.DateTime(), nullable=True),
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
