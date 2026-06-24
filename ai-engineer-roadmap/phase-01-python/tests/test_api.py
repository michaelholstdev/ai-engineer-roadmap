from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.engine import Connection
from uuid import UUID
from datetime import datetime, timezone

from ai_roadmap.ai_client import (
    AIClientConfigurationError,
    AIProviderError,
    EMBEDDING_MODEL,
)
from ai_roadmap.api import app
from ai_roadmap.database import get_connection
from ai_roadmap.schemas import AIAnalyzeResponse
from ai_roadmap.analysis_repository import AnalysisRun
from ai_roadmap.notes_repository import Note, SearchResult

client = TestClient(app)


@pytest.fixture(autouse=True)
def override_database_connection():
    connection = Mock(spec=Connection)

    def override_get_connection():
        yield connection

    app.dependency_overrides[get_connection] = override_get_connection

    yield connection

    app.dependency_overrides.pop(get_connection, None)


@pytest.mark.parametrize(
    "text",
    [
        "",
        "    ",
    ],
)
def test_analyze_rejects_blank_text(text: str, override_database_connection):
    response = client.post(
        "/analyze",
        json={
            "text": text,
        },
    )
    assert response.status_code == 422
    override_database_connection.execute.assert_not_called()


def test_analyze_returns_text_statistics():
    response = client.post(
        "/analyze",
        json={
            "text": "AI Engineering is fun.",
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "word_count": 4,
        "character_count": 22,
        "sentence_count": 1,
    }


def test_analyze_rejects_too_large_payloads(override_database_connection):
    response = client.post(
        "/analyze",
        json={
            "text": "a" * 501,
        },
    )
    assert response.status_code == 413
    assert response.json() == {
        "detail": "Text is too long",
    }
    override_database_connection.execute.assert_not_called()


def test_ai_analyze_returns_structured_response(monkeypatch):
    monkeypatch.setattr(
        "ai_roadmap.routes.get_ai_provider",
        lambda: "ollama",
    )

    def fake_analyze_text_with_ai(text: str) -> AIAnalyzeResponse:
        assert text == "AI Engineering is fun."
        return AIAnalyzeResponse(
            summary="Short summary",
            sentiment="neutral",
            topics=["ai", "engineering"],
            action_items=[],
        )

    monkeypatch.setattr(
        "ai_roadmap.routes.analyze_text_with_ai",
        fake_analyze_text_with_ai,
    )

    response = client.post(
        "/ai/analyze",
        json={
            "text": "AI Engineering is fun.",
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "summary": "Short summary",
        "sentiment": "neutral",
        "topics": ["ai", "engineering"],
        "action_items": [],
    }


def test_ai_analyze_returns_503_when_ai_client_is_not_configured(
    monkeypatch, override_database_connection
):
    def fake_analyze_text_with_ai(text: str) -> AIAnalyzeResponse:
        assert text == "some text"
        raise AIClientConfigurationError("OPENAI_API_KEY is not configured")

    monkeypatch.setattr(
        "ai_roadmap.routes.analyze_text_with_ai",
        fake_analyze_text_with_ai,
    )

    response = client.post(
        "/ai/analyze",
        json={
            "text": "some text",
        },
    )

    assert response.status_code == 503
    assert response.json() == {
        "detail": "AI client is not configured",
    }
    override_database_connection.execute.assert_not_called()


def test_ai_analyze_returns_502_when_ai_client_cannot_reach_provider(
    monkeypatch, override_database_connection
):
    def fake_analyze_text_with_ai(text: str) -> AIAnalyzeResponse:
        assert text == "some text"
        raise AIProviderError("AI provider request failed")

    monkeypatch.setattr(
        "ai_roadmap.routes.analyze_text_with_ai",
        fake_analyze_text_with_ai,
    )

    response = client.post(
        "/ai/analyze",
        json={
            "text": "some text",
        },
    )

    assert response.status_code == 502
    assert response.json() == {
        "detail": "AI provider request failed",
    }
    override_database_connection.execute.assert_not_called()


def test_analyze_stores_successful_result(monkeypatch):
    stored_runs = []

    def fake_save_analysis_run(connection, run):
        stored_runs.append(run)

    monkeypatch.setattr(
        "ai_roadmap.routes.save_analysis_run",
        fake_save_analysis_run,
    )

    response = client.post(
        "/analyze",
        json={"text": "AI Engineering is fun."},
    )

    assert response.status_code == 200
    assert len(stored_runs) == 1

    stored_run = stored_runs[0]
    assert stored_run.analysis_type == "text"
    assert stored_run.input_text == "AI Engineering is fun."
    assert stored_run.word_count == 4
    assert stored_run.character_count == 22
    assert stored_run.sentence_count == 1
    assert stored_run.summary is None
    assert stored_run.sentiment is None
    assert stored_run.topics == []
    assert stored_run.action_items == []
    assert stored_run.provider is None


def test_ai_analyze_stores_successful_result(monkeypatch):
    monkeypatch.setattr(
        "ai_roadmap.routes.get_ai_provider",
        lambda: "ollama",
    )

    stored_runs = []

    def fake_save_analysis_run(connection, run):
        stored_runs.append(run)

    monkeypatch.setattr(
        "ai_roadmap.routes.save_analysis_run",
        fake_save_analysis_run,
    )

    def fake_analyze_text_with_ai(text: str) -> AIAnalyzeResponse:
        return AIAnalyzeResponse(
            summary="Short summary",
            sentiment="neutral",
            topics=["AI", "Engineering"],
            action_items=[],
        )

    monkeypatch.setattr(
        "ai_roadmap.routes.analyze_text_with_ai",
        fake_analyze_text_with_ai,
    )

    response = client.post(
        "/ai/analyze",
        json={"text": "AI Engineering is fun."},
    )

    assert response.status_code == 200
    assert len(stored_runs) == 1

    stored_run = stored_runs[0]
    assert stored_run.analysis_type == "ai"
    assert stored_run.input_text == "AI Engineering is fun."
    assert stored_run.word_count == 4
    assert stored_run.character_count == 22
    assert stored_run.sentence_count == 1
    assert stored_run.summary == "Short summary"
    assert stored_run.sentiment == "neutral"
    assert stored_run.topics == ["AI", "Engineering"]
    assert stored_run.action_items == []
    assert stored_run.provider == "ollama"


def test_analyze_fails_when_database_is_unavailable(monkeypatch):
    def fake_save_analysis_run(connection, run):
        raise RuntimeError("database unavailable")

    monkeypatch.setattr(
        "ai_roadmap.routes.save_analysis_run",
        fake_save_analysis_run,
    )

    with pytest.raises(RuntimeError, match="database unavailable"):
        client.post(
            "/analyze",
            json={"text": "AI Engineering is fun"},
        )


def test_list_analyses_returns_empty_history(monkeypatch):
    monkeypatch.setattr(
        "ai_roadmap.routes.list_analysis_runs",
        lambda connection, limit: [],
    )

    response = client.get("/analyses")

    assert response.status_code == 200
    assert response.json() == []


def test_list_analyses_returns_list_when_entries_exist(monkeypatch):
    run_id = UUID("12345678-1234-5678-1234-567812345678")
    created_at = datetime(2026, 6, 9, 12, 0, tzinfo=timezone.utc)

    def fake_list_analysis_runs(connection, limit):
        assert limit == 10
        return [
            AnalysisRun(
                id=run_id,
                created_at=created_at,
                action_items=[],
                analysis_type="ai",
                character_count=22,
                input_text="AI Engineering is fun.",
                provider="ollama",
                sentence_count=1,
                sentiment="positive",
                summary="",
                topics=["AI", "Engineering"],
                word_count=4,
            )
        ]

    monkeypatch.setattr("ai_roadmap.routes.list_analysis_runs", fake_list_analysis_runs)

    response = client.get("/analyses?limit=10")

    assert response.status_code == 200
    assert response.json() == [
        {
            "id": str(run_id),
            "created_at": "2026-06-09T12:00:00Z",
            "action_items": [],
            "analysis_type": "ai",
            "character_count": 22,
            "input_text": "AI Engineering is fun.",
            "provider": "ollama",
            "sentence_count": 1,
            "sentiment": "positive",
            "summary": "",
            "topics": ["AI", "Engineering"],
            "word_count": 4,
        }
    ]


@pytest.mark.parametrize("limit", [0, 101])
def test_list_analyses_rejects_invalid_limit(limit: int, monkeypatch):
    list_runs = Mock()

    monkeypatch.setattr(
        "ai_roadmap.routes.list_analysis_runs",
        list_runs,
    )

    response = client.get(f"/analyses?limit={limit}")

    assert response.status_code == 422
    list_runs.assert_not_called()


def test_create_note_returns_stored_note(monkeypatch):
    note_id = UUID("12345678-1234-5678-1234-567812345678")
    created_at = datetime(2026, 6, 23, 12, 0, tzinfo=timezone.utc)
    updated_at = datetime(2026, 6, 23, 12, 0, tzinfo=timezone.utc)

    def fake_create_note(connection, title: str, content: str) -> Note:
        assert title == "Postgres"
        assert content == "Postgres stores data."
        return Note(
            id=note_id,
            title=title,
            content=content,
            embedding_model=EMBEDDING_MODEL,
            created_at=created_at,
            updated_at=updated_at,
        )

    monkeypatch.setattr(
        "ai_roadmap.routes.create_note",
        fake_create_note,
    )

    response = client.post(
        "/notes",
        json={
            "title": "Postgres",
            "content": "Postgres stores data.",
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "id": str(note_id),
        "title": "Postgres",
        "content": "Postgres stores data.",
        "embedding_model": EMBEDDING_MODEL,
        "created_at": "2026-06-23T12:00:00Z",
        "updated_at": "2026-06-23T12:00:00Z",
    }
    assert "embedding" not in response.json()


def test_create_note_returns_502_when_embedding_provider_fails(
    monkeypatch, override_database_connection
):
    def fake_create_note(connection, title: str, content: str) -> Note:
        raise AIProviderError("AI provider request failed")

    monkeypatch.setattr(
        "ai_roadmap.routes.create_note",
        fake_create_note,
    )

    response = client.post(
        "/notes",
        json={
            "title": "Postgres",
            "content": "Postgres stores data.",
        },
    )

    assert response.status_code == 502
    assert response.json() == {
        "detail": "AI provider request failed",
    }
    override_database_connection.execute.assert_not_called()


def test_create_note_returns_503_when_ai_client_is_not_configured(
    monkeypatch, override_database_connection
):
    def fake_create_note(connection, title: str, content: str) -> Note:
        raise AIClientConfigurationError("AI provider is not configured")

    monkeypatch.setattr(
        "ai_roadmap.routes.create_note",
        fake_create_note,
    )

    response = client.post(
        "/notes",
        json={
            "title": "Postgres",
            "content": "Postgres stores data.",
        },
    )

    assert response.status_code == 503
    assert response.json() == {
        "detail": "AI client is not configured",
    }
    override_database_connection.execute.assert_not_called()


@pytest.mark.parametrize(
    "payload",
    [
        {"title": "", "content": "Postgres stores data."},
        {"title": "   ", "content": "Postgres stores data."},
        {"title": "Postgres", "content": ""},
        {"title": "Postgres", "content": "   "},
    ],
)
def test_create_note_rejects_blank_fields(
    monkeypatch, payload, override_database_connection
):
    create_note_mock = Mock()

    monkeypatch.setattr(
        "ai_roadmap.routes.create_note",
        create_note_mock,
    )

    response = client.post("/notes", json=payload)

    assert response.status_code == 422
    create_note_mock.assert_not_called()
    override_database_connection.execute.assert_not_called()


def test_search_notes_returns_keyword_results(monkeypatch):
    note_id = UUID("12345678-1234-5678-1234-567812345678")
    created_at = datetime(2026, 6, 24, 12, 0, tzinfo=timezone.utc)
    updated_at = datetime(2026, 6, 24, 12, 0, tzinfo=timezone.utc)

    def fake_search_notes(connection, query: str, mode: str, limit: int):
        assert query == "relational data"
        assert mode == "keyword"
        assert limit == 10
        return [
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

    monkeypatch.setattr(
        "ai_roadmap.routes.search_notes",
        fake_search_notes,
    )

    response = client.get("/notes/search?query=relational%20data&mode=keyword&limit=10")

    assert response.status_code == 200
    assert response.json() == [
        {
            "id": str(note_id),
            "title": "Postgres",
            "content": "Postgres stores relational data.",
            "embedding_model": EMBEDDING_MODEL,
            "created_at": "2026-06-24T12:00:00Z",
            "updated_at": "2026-06-24T12:00:00Z",
            "score": 0.75,
            "search_mode": "keyword",
        }
    ]


@pytest.mark.parametrize(
    "url",
    [
        "/notes/search?query=&mode=keyword&limit=10",
        "/notes/search?query=%20%20%20&mode=keyword&limit=10",
        "/notes/search?query=postgres&mode=keyword&limit=0",
        "/notes/search?query=postgres&mode=keyword&limit=101",
        "/notes/search?query=postgres&mode=semantic&limit=10",
    ],
)
def test_search_notes_rejects_invalid_parameters(monkeypatch, url):
    search_notes_mock = Mock()

    monkeypatch.setattr(
        "ai_roadmap.routes.search_notes",
        search_notes_mock,
    )

    response = client.get(url)

    assert response.status_code == 422
    search_notes_mock.assert_not_called()
