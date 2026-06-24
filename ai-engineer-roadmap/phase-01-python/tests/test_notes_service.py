from datetime import datetime, timezone
from unittest.mock import Mock
from uuid import UUID

import pytest
from sqlalchemy.engine import Connection

from ai_roadmap.ai_client import AIProviderError, EMBEDDING_DIMENSIONS, EMBEDDING_MODEL
from ai_roadmap.notes_repository import Note, SearchResult
from ai_roadmap.notes_service import create_note, save_note, search_notes


def test_create_note_embeds_and_stores_note(monkeypatch):
    embedding = [0.1] * EMBEDDING_DIMENSIONS
    stored_note = Note(
        id=UUID("12345678-1234-5678-1234-567812345678"),
        title="Postgres",
        content="Postgres stores data.",
        embedding_model=EMBEDDING_MODEL,
        created_at=datetime(2026, 6, 23, 12, 0, tzinfo=timezone.utc),
        updated_at=datetime(2026, 6, 23, 12, 0, tzinfo=timezone.utc),
    )

    def fake_embed_note_text(title: str, content: str) -> list[float]:
        assert title == "Postgres"
        assert content == "Postgres stores data."
        return embedding

    saved_notes = []

    def fake_save_note(connection: Connection, note):
        saved_notes.append(note)
        return stored_note

    monkeypatch.setattr(
        "ai_roadmap.notes_service.embed_note_text",
        fake_embed_note_text,
    )
    monkeypatch.setattr(
        "ai_roadmap.notes_service.save_note",
        fake_save_note,
    )

    connection = Mock(spec=Connection)

    result = create_note(
        connection=connection,
        title="Postgres",
        content="Postgres stores data.",
    )

    assert result == stored_note
    assert len(saved_notes) == 1
    assert saved_notes[0].title == "Postgres"
    assert saved_notes[0].content == "Postgres stores data."
    assert saved_notes[0].embedding == embedding
    assert saved_notes[0].embedding_model == EMBEDDING_MODEL


def test_create_note_does_not_save_when_embedding_fails(monkeypatch):
    save_note_mock = Mock(spec=save_note)

    def fake_embed_note_text(title, content):
        raise AIProviderError("Provider call failed")

    monkeypatch.setattr(
        "ai_roadmap.notes_service.embed_note_text", fake_embed_note_text
    )

    monkeypatch.setattr("ai_roadmap.notes_service.save_note", save_note_mock)

    connection = Mock(spec=Connection)

    with pytest.raises(AIProviderError):
        create_note(
            connection=connection,
            title="Postgres",
            content="Postgres stores data",
        )

    save_note_mock.assert_not_called()


def test_search_notes_uses_keyword_repository(monkeypatch):
    note_id = UUID("12345678-1234-5678-1234-567812345678")
    created_at = datetime(2026, 6, 24, 12, 0, tzinfo=timezone.utc)
    updated_at = datetime(2026, 6, 24, 12, 0, tzinfo=timezone.utc)

    expected_results = [
        SearchResult(
            id=note_id,
            title="Postgres",
            content="Postgres stores relational data.",
            embedding_model=EMBEDDING_MODEL,
            created_at=created_at,
            updated_at=updated_at,
            score=0.75,
            search_mode="keyword",
        )
    ]

    def fake_search_notes_by_keyword(connection, query: str, limit: int):
        assert query == "relational data"
        assert limit == 10
        return expected_results

    monkeypatch.setattr(
        "ai_roadmap.notes_service.search_notes_by_keyword",
        fake_search_notes_by_keyword,
    )

    connection = Mock(spec=Connection)

    result = search_notes(
        connection=connection,
        query="relational data",
        mode="keyword",
        limit=10,
    )

    assert result == expected_results


def test_search_notes_keyword_mode_does_not_call_embedding_provider(monkeypatch):
    search_results: list[SearchResult] = []

    def fake_search_notes_by_keyword(connection, query: str, limit: int):
        return search_results

    embed_search_query_mock = Mock()

    monkeypatch.setattr(
        "ai_roadmap.notes_service.search_notes_by_keyword",
        fake_search_notes_by_keyword,
    )
    monkeypatch.setattr(
        "ai_roadmap.ai_client.embed_search_query",
        embed_search_query_mock,
    )

    connection = Mock(spec=Connection)

    result = search_notes(
        connection=connection,
        query="relational data",
        mode="keyword",
        limit=10,
    )

    assert result == []
    embed_search_query_mock.assert_not_called()
