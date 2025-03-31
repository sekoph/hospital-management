"""Added DoctorSpecialization model

Revision ID: 1bd510a54cef
Revises: 0cbd879644c9
Create Date: 2025-03-31 15:29:30.740419

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import uuid


# revision identifiers, used by Alembic.
revision: str = '1bd510a54cef'
down_revision: Union[str, None] = '0cbd879644c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """create doctor specializations table"""
    op.create_table(
        "doctor_specializations",
        sa.Column("id", sa.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False),
        sa.Column("specialization", sa.String(length=100), nullable=False),
        sa.Column("title", sa.String(length=100), nullable=True),
        sa.Column("description", sa.String(length=100), nullable=True),
        sa.Column("date_created", sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.Column("date_modified", sa.DateTime(), nullable=True),
    )


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
