from datetime import datetime, timezone
from unittest.mock import Mock
from uuid import UUID

from sqlalchemy.engine import Connection
from sqlalchemy.dialects import postgresql

from ai_roadmap.analysis_repository import (
    AnalysisRun,
    AnalysisRunCreate,
    list_analysis_runs,
    save_analysis_run,
)


def test_create_text_analysis_run_data():
    run = AnalysisRunCreate(
        analysis_type="text",
        input_text="AI Engineering is fun.",
        word_count=4,
        character_count=22,
        sentence_count=1,
        summary=None,
        sentiment=None,
        topics=[],
        action_items=[],
        provider=None,
    )

    assert run.analysis_type == "text"
    assert run.input_text == "AI Engineering is fun."
    assert run.word_count == 4
    assert run.character_count == 22
    assert run.sentence_count == 1
    assert run.summary is None
    assert run.sentiment is None
    assert run.topics == []
    assert run.action_items == []
    assert run.provider is None


def test_create_stored_analysis_run_data():
    run_id = UUID("12345678-1234-5678-1234-567812345678")
    created_at = datetime(2026, 6, 7, 12, 0, tzinfo=timezone.utc)

    run = AnalysisRun(
        id=run_id,
        analysis_type="ai",
        input_text="AI Engineering is fun.",
        word_count=4,
        character_count=22,
        sentence_count=1,
        summary="Short summary",
        sentiment="positive",
        topics=["AI", "Engineering"],
        action_items=["Review the roadmap"],
        provider="ollama",
        created_at=created_at,
    )

    assert run.id == run_id
    assert run.analysis_type == "ai"
    assert run.input_text == "AI Engineering is fun."
    assert run.summary == "Short summary"
    assert run.provider == "ollama"
    assert run.created_at == created_at


def test_save_analysis_run_executes_insert():
    connection = Mock(spec=Connection)
    run = AnalysisRunCreate(
        analysis_type="text",
        input_text="AI Engineering is fun.",
        word_count=4,
        character_count=22,
        sentence_count=1,
        summary=None,
        sentiment=None,
        topics=[],
        action_items=[],
        provider=None,
    )

    save_analysis_run(connection, run)

    connection.execute.assert_called_once()

    statement = connection.execute.call_args.args[0]
    assert statement.compile().params == {
        "analysis_type": "text",
        "input_text": "AI Engineering is fun.",
        "word_count": 4,
        "character_count": 22,
        "sentence_count": 1,
        "summary": None,
        "sentiment": None,
        "topics": [],
        "action_items": [],
        "provider": None,
    }


def test_save_analysis_run_executes_insert_for_ai():
    connection = Mock(spec=Connection)
    run = AnalysisRunCreate(
        analysis_type="ai",
        input_text="AI Engineering is fun.",
        word_count=4,
        character_count=22,
        sentence_count=1,
        summary="Short Summary",
        sentiment="positive",
        topics=["AI", "Engineering"],
        action_items=["Review the roadmap"],
        provider="ollama",
    )

    save_analysis_run(connection, run)

    connection.execute.assert_called_once()

    statement = connection.execute.call_args.args[0]
    assert statement.compile().params == {
        "analysis_type": "ai",
        "input_text": "AI Engineering is fun.",
        "word_count": 4,
        "character_count": 22,
        "sentence_count": 1,
        "summary": "Short Summary",
        "sentiment": "positive",
        "topics": ["AI", "Engineering"],
        "action_items": ["Review the roadmap"],
        "provider": "ollama",
    }


def test_list_analysis_runs_queries_newest_records_with_limit():
    run_id = UUID("12345678-1234-5678-1234-567812345678")
    created_at = datetime(2026, 6, 9, 12, 0, tzinfo=timezone.utc)

    row = {
        "id": run_id,
        "analysis_type": "ai",
        "input_text": "AI Engineering is fun.",
        "word_count": 4,
        "character_count": 22,
        "sentence_count": 1,
        "summary": "Short summary",
        "sentiment": "positive",
        "topics": ["AI"],
        "action_items": [],
        "provider": "ollama",
        "created_at": created_at,
    }

    connection = Mock(spec=Connection)
    connection.execute.return_value.mappings.return_value.all.return_value = [row]

    result = list_analysis_runs(connection, limit=20)

    connection.execute.assert_called_once()

    statement = connection.execute.call_args.args[0]
    compiled_statement = str(
        statement.compile(
            dialect=postgresql.dialect(), compile_kwargs={"literal_binds": True}
        )
    )

    assert (
        "ORDER BY analysis_runs.created_at DESC, analysis_runs.id DESC"
        in compiled_statement
    )
    assert "LIMIT 20" in compiled_statement
    assert result == [
        AnalysisRun(
            id=run_id,
            analysis_type="ai",
            input_text="AI Engineering is fun.",
            word_count=4,
            character_count=22,
            sentence_count=1,
            summary="Short summary",
            sentiment="positive",
            topics=["AI"],
            action_items=[],
            provider="ollama",
            created_at=created_at,
        )
    ]


def test_list_analysis_runs_returns_empty_list_when_no_rows_exist():
    connection = Mock(spec=Connection)
    connection.execute.return_value.mappings.return_value.all.return_value = []

    result = list_analysis_runs(connection)

    assert result == []
