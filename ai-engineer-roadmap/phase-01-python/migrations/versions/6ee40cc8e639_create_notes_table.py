"""create notes table

Revision ID: 6ee40cc8e639
Revises: db220f8d2751
Create Date: 2026-06-19 13:40:42.076565

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "6ee40cc8e639"
down_revision: Union[str, Sequence[str], None] = "db220f8d2751"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("CREATE EXTENSION IF NOT EXISTS vector")
    op.execute("""
      CREATE TABLE notes (
          id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
          title text NOT NULL,
          content text NOT NULL,
          embedding vector(1024) NOT NULL,
          embedding_model text NOT NULL,
          created_at timestamp with time zone NOT NULL DEFAULT now(),
          updated_at timestamp with time zone NOT NULL DEFAULT now(),
          CONSTRAINT notes_title_not_blank CHECK (btrim(title) <> ''),
          CONSTRAINT notes_content_not_blank CHECK (btrim(content) <> ''),
          CONSTRAINT notes_embedding_model_not_blank CHECK (btrim(embedding_model) <> '')
      )
      """)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("notes")
