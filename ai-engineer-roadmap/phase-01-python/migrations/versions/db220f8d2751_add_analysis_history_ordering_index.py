"""add analysis history ordering index

Revision ID: db220f8d2751
Revises: 651c16e02b39
Create Date: 2026-06-11 09:28:03.045617

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "db220f8d2751"
down_revision: Union[str, Sequence[str], None] = "651c16e02b39"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_index(
        "ix_analysis_runs_created_at_id",
        "analysis_runs",
        ["created_at", "id"],
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(
        "ix_analysis_runs_created_at_id",
        table_name="analysis_runs",
    )
