"""create analysis runs table

Revision ID: 651c16e02b39
Revises:
Create Date: 2026-06-05 22:30:25.210601

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy.dialects import postgresql
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '651c16e02b39'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute('CREATE EXTENSION IF NOT EXISTS "pgcrypto"')
    op.create_table(
        "analysis_runs",
        sa.Column(
            "id",
            sa.UUID(),
            primary_key=True,
            server_default=sa.text("gen_random_uuid()"),
        ),
        sa.Column(
            "analysis_type",
            sa.Text(),
            nullable=False,
        ),
        sa.CheckConstraint(
            "analysis_type IN ('text', 'ai')",
            name="analysis_runs_analysis_type_check",
        ),
        sa.Column(
            "input_text",
            sa.Text(),
            nullable=False,
        ),
        sa.Column(
            "word_count",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "character_count",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "sentence_count",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "summary",
            sa.Text(),
        ),
        sa.Column(
            "sentiment",
            sa.Text(),
        ),
        sa.CheckConstraint(
            "sentiment IS NULL OR sentiment IN ('positive', 'neutral', 'negative')",
            name="analysis_runs_sentiment_check",
        ),
        sa.Column(
            "topics",
            postgresql.JSONB(),
            nullable=False,
            server_default=sa.text("'[]'::jsonb"),
        ),
        sa.Column(
            "action_items",
            postgresql.JSONB(),
            nullable=False,
            server_default=sa.text("'[]'::jsonb"),
        ),
        sa.Column(
            "provider",
            sa.Text(),
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("analysis_runs")
