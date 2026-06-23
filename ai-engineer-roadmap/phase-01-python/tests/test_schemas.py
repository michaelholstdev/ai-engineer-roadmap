from datetime import datetime, timezone
from uuid import UUID

import pytest
from pydantic import ValidationError

from ai_roadmap.schemas import AIAnalyzeResponse, NoteCreateRequest, NoteResponse


def test_ai_analyze_response_accepts_valid_data():
    result = AIAnalyzeResponse(
        summary="Short summary",
        sentiment="neutral",
        topics=["ai", "engineering"],
        action_items=[],
    )
    assert result.summary == "Short summary"
    assert result.sentiment == "neutral"
    assert result.topics == ["ai", "engineering"]
    assert result.action_items == []


def test_ai_analyze_response_rejects_invalid_sentiment():
    with pytest.raises(ValidationError):
        AIAnalyzeResponse(
            summary="Short summary",
            sentiment="mixed",
            topics=["ai"],
            action_items=[],
        )


def test_ai_analyze_response_rejects_topics_that_are_not_a_list():
    with pytest.raises(ValidationError):
        AIAnalyzeResponse(
            summary="Short summary",
            sentiment="neutral",
            topics="ai",
            action_items=[],
        )


def test_note_create_request_accepts_valid_data():
    request = NoteCreateRequest(
        title="Postgres",
        content="Postgres stores data.",
    )

    assert request.title == "Postgres"
    assert request.content == "Postgres stores data."


@pytest.mark.parametrize(
    ("title", "content"),
    [
        ("", "Postgres stores data."),
        ("   ", "Postgres stores data."),
        ("Postgres", ""),
        ("Postgres", "   "),
    ],
)
def test_note_create_request_rejects_blank_fields(title: str, content: str):
    with pytest.raises(ValidationError):
        NoteCreateRequest(title=title, content=content)


def test_note_response_accepts_stored_note_data_without_embedding():
    note_id = UUID("12345678-1234-5678-1234-567812345678")
    created_at = datetime(2026, 6, 23, 12, 0, tzinfo=timezone.utc)
    updated_at = datetime(2026, 6, 23, 12, 0, tzinfo=timezone.utc)

    response = NoteResponse(
        id=note_id,
        title="Postgres",
        content="Postgres stores data.",
        embedding_model="qwen3-embedding:0.6b",
        created_at=created_at,
        updated_at=updated_at,
    )

    assert response.id == note_id
    assert response.title == "Postgres"
    assert response.content == "Postgres stores data."
    assert response.embedding_model == "qwen3-embedding:0.6b"
    assert response.created_at == created_at
    assert response.updated_at == updated_at
