from dataclasses import dataclass
from datetime import datetime
from typing import Literal
from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.engine import Connection

metadata = sa.MetaData()

analysis_runs = sa.Table(
    "analysis_runs",
    metadata,
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


@dataclass(frozen=True)
class AnalysisRunCreate:
    analysis_type: Literal["text", "ai"]
    input_text: str
    word_count: int
    character_count: int
    sentence_count: int
    summary: str | None
    sentiment: Literal["positive", "neutral", "negative"] | None
    topics: list[str]
    action_items: list[str]
    provider: str | None


@dataclass(frozen=True)
class AnalysisRun:
    id: UUID
    analysis_type: Literal["text", "ai"]
    input_text: str
    word_count: int
    character_count: int
    sentence_count: int
    summary: str | None
    sentiment: Literal["positive", "neutral", "negative"] | None
    topics: list[str]
    action_items: list[str]
    provider: str | None
    created_at: datetime


def save_analysis_run(connection: Connection, run: AnalysisRunCreate) -> None:
    statement = sa.insert(analysis_runs).values(
        analysis_type=run.analysis_type,
        input_text=run.input_text,
        word_count=run.word_count,
        character_count=run.character_count,
        sentence_count=run.sentence_count,
        summary=run.summary,
        sentiment=run.sentiment,
        topics=run.topics,
        action_items=run.action_items,
        provider=run.provider,
    )
    connection.execute(statement)


def list_analysis_runs(connection: Connection, limit: int = 20) -> list[AnalysisRun]:
    statement = (
        sa.select(analysis_runs)
        .order_by(
            analysis_runs.c.created_at.desc(),
            analysis_runs.c.id.desc(),
        )
        .limit(limit)
    )

    rows = connection.execute(statement).mappings().all()

    return [
        AnalysisRun(
            id=row["id"],
            analysis_type=row["analysis_type"],
            input_text=row["input_text"],
            word_count=row["word_count"],
            character_count=row["character_count"],
            sentence_count=row["sentence_count"],
            summary=row["summary"],
            sentiment=row["sentiment"],
            topics=row["topics"],
            action_items=row["action_items"],
            provider=row["provider"],
            created_at=row["created_at"],
        )
        for row in rows
    ]
