from dataclasses import dataclass
from datetime import datetime
from typing import Literal
from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.engine import Connection
from sqlalchemy.sql.elements import ColumnElement
from ai_roadmap.ai_client import EMBEDDING_MODEL


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


@dataclass(frozen=True)
class SearchResult:
    id: UUID
    title: str
    content: str
    embedding_model: str
    created_at: datetime
    updated_at: datetime
    score: float
    search_mode: Literal["keyword", "semantic"]


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


def search_notes_by_keyword(
    connection: Connection,
    query: str,
    limit: int = 20,
) -> list[SearchResult]:
    english_config: ColumnElement[str] = sa.literal_column("'english'")
    search_vector = sa.func.to_tsvector(
        english_config,
        notes.c.title + sa.literal(" ") + notes.c.content,
    )
    search_query = sa.func.websearch_to_tsquery(english_config, query)
    score = sa.func.ts_rank(search_vector, search_query).label("score")

    statement = (
        sa.select(
            notes.c.id,
            notes.c.title,
            notes.c.content,
            notes.c.embedding_model,
            notes.c.created_at,
            notes.c.updated_at,
            score,
        )
        .where(search_vector.op("@@")(search_query))
        .order_by(
            sa.desc(sa.column("score")),
            notes.c.created_at.desc(),
            notes.c.id.desc(),
        )
        .limit(limit)
    )

    rows = connection.execute(statement).mappings().all()

    return [
        SearchResult(
            id=row["id"],
            title=row["title"],
            content=row["content"],
            embedding_model=row["embedding_model"],
            created_at=row["created_at"],
            updated_at=row["updated_at"],
            score=row["score"],
            search_mode="keyword",
        )
        for row in rows
    ]


def search_notes_by_semantic(
    connection: Connection,
    query_embedding: list[float],
    limit: int = 20,
) -> list[SearchResult]:
    query_vector = format_embedding_for_pgvector(query_embedding)
    distance = notes.c.embedding.op("<=>")(query_vector).label("distance")
    score = (sa.literal(1.0) - distance).label("score")

    statement = (
        sa.select(
            notes.c.id,
            notes.c.title,
            notes.c.content,
            notes.c.embedding_model,
            notes.c.created_at,
            notes.c.updated_at,
            score,
        )
        .where(notes.c.embedding_model == EMBEDDING_MODEL)
        .order_by(
            sa.asc(sa.column("distance")),
            notes.c.created_at.desc(),
            notes.c.id.desc(),
        )
        .limit(limit)
    )

    rows = connection.execute(statement).mappings().all()

    return [
        SearchResult(
            id=row["id"],
            title=row["title"],
            content=row["content"],
            embedding_model=row["embedding_model"],
            created_at=row["created_at"],
            updated_at=row["updated_at"],
            score=row["score"],
            search_mode="semantic",
        )
        for row in rows
    ]
