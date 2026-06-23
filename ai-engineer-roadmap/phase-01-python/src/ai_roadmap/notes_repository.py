from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.engine import Connection


@dataclass(frozen=True)
class NoteCreate:
    title: str
    content: str
    embedding: list[float]
    embedding_model: str


@dataclass(frozen=True)
class Note:
    id: UUID
    title: str
    content: str
    embedding_model: str
    created_at: datetime
    updated_at: datetime


metadata = sa.MetaData()

notes = sa.Table(
    "notes",
    metadata,
    sa.Column(
        "id",
        sa.UUID(),
        primary_key=True,
        server_default=sa.text("gen_random_uuid()"),
    ),
    sa.Column("title", sa.Text(), nullable=False),
    sa.Column("content", sa.Text(), nullable=False),
    sa.Column("embedding", sa.Text(), nullable=False),
    sa.Column("embedding_model", sa.Text(), nullable=False),
    sa.Column(
        "created_at",
        sa.DateTime(timezone=True),
        nullable=False,
        server_default=sa.text("now()"),
    ),
    sa.Column(
        "updated_at",
        sa.DateTime(timezone=True),
        nullable=False,
        server_default=sa.text("now()"),
    ),
)


def format_embedding_for_pgvector(embedding: list[float]) -> str:
    return "[" + ",".join(str(value) for value in embedding) + "]"


def save_note(connection: Connection, note: NoteCreate) -> Note:
    statement = (
        sa.insert(notes)
        .values(
            title=note.title,
            content=note.content,
            embedding=format_embedding_for_pgvector(note.embedding),
            embedding_model=note.embedding_model,
        )
        .returning(
            notes.c.id,
            notes.c.title,
            notes.c.content,
            notes.c.embedding_model,
            notes.c.created_at,
            notes.c.updated_at,
        )
    )

    row = connection.execute(statement).mappings().one()

    return Note(
        id=row["id"],
        content=row["content"],
        title=row["title"],
        embedding_model=row["embedding_model"],
        created_at=row["created_at"],
        updated_at=row["updated_at"],
    )
