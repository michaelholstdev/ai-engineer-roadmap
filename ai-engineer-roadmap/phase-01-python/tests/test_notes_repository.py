from unittest.mock import Mock

from sqlalchemy.engine import Connection
from sqlalchemy.dialects import postgresql
from datetime import datetime, timezone
from uuid import UUID


from ai_roadmap.ai_client import EMBEDDING_DIMENSIONS, EMBEDDING_MODEL
from ai_roadmap.notes_repository import (
    Note,
    NoteCreate,
    SearchResult,
    format_embedding_for_pgvector,
    save_note,
    search_notes_by_keyword,
    search_notes_by_semantic,
)

def test_create_note_data():
    embedding = [0.1] * EMBEDDING_DIMENSIONS

    note = NoteCreate(
        title="Postgres",
        content="Postgres stores data.",
        embedding=embedding,
        embedding_model=EMBEDDING_MODEL,
    )

    assert note.title == "Postgres"
    assert note.content == "Postgres stores data."
    assert note.embedding == embedding
    assert note.embedding_model == EMBEDDING_MODEL


def test_save_note_executes_insert():
    connection = Mock(spec=Connection)
    embedding = [0.1] * EMBEDDING_DIMENSIONS
    note = NoteCreate(
        title="Postgres",
        content="Postgres stores data.",
        embedding=embedding,
        embedding_model=EMBEDDING_MODEL,
    )

    connection.execute.return_value.mappings.return_value.one.return_value = {
        "id": UUID("12345678-1234-5678-1234-567812345678"),
        "title": "Postgres",
        "content": "Postgres stores data.",
        "embedding_model": EMBEDDING_MODEL,
        "created_at": datetime(2026, 6, 22, 12, 0, tzinfo=timezone.utc),
        "updated_at": datetime(2026, 6, 22, 12, 0, tzinfo=timezone.utc),
    }

    save_note(connection, note)

    connection.execute.assert_called_once()

    statement = connection.execute.call_args.args[0]
    assert statement.compile().params == {
        "title": "Postgres",
        "content": "Postgres stores data.",
        "embedding": format_embedding_for_pgvector(embedding),
        "embedding_model": EMBEDDING_MODEL,
    }


def test_format_embedding_for_pgvector():
    assert format_embedding_for_pgvector([0.1, 0.2, 0.3]) == "[0.1,0.2,0.3]"


def test_save_note_returns_stored_note():
    note_id = UUID("12345678-1234-5678-1234-567812345678")
    created_at = datetime(2026, 6, 22, 12, 0, tzinfo=timezone.utc)
    updated_at = datetime(2026, 6, 22, 12, 0, tzinfo=timezone.utc)

    row = {
        "id": note_id,
        "title": "Postgres",
        "content": "Postgres stores data.",
        "embedding_model": EMBEDDING_MODEL,
        "created_at": created_at,
        "updated_at": updated_at,
    }

    connection = Mock(spec=Connection)
    connection.execute.return_value.mappings.return_value.one.return_value = row

    note = NoteCreate(
        title="Postgres",
        content="Postgres stores data.",
        embedding=[0.1] * EMBEDDING_DIMENSIONS,
        embedding_model=EMBEDDING_MODEL,
    )

    result = save_note(connection, note)

    assert result == Note(
        id=note_id,
        title="Postgres",
        content="Postgres stores data.",
        embedding_model=EMBEDDING_MODEL,
        created_at=created_at,
        updated_at=updated_at,
    )


def test_create_search_result_data():
    note_id = UUID("12345678-1234-5678-1234-567812345678")
    created_at = datetime(2026, 6, 24, 12, 0, tzinfo=timezone.utc)
    updated_at = datetime(2026, 6, 24, 12, 0, tzinfo=timezone.utc)

    result = SearchResult(
        id=note_id,
        title="Postgres",
        content="Postgres stores relational data.",
        embedding_model=EMBEDDING_MODEL,
        created_at=created_at,
        updated_at=updated_at,
        score=0.75,
        search_mode="keyword",
    )

    assert result.id == note_id
    assert result.title == "Postgres"
    assert result.content == "Postgres stores relational data."
    assert result.embedding_model == EMBEDDING_MODEL
    assert result.created_at == created_at
    assert result.updated_at == updated_at
    assert result.score == 0.75
    assert result.search_mode == "keyword"


def test_search_notes_by_keyword_queries_ranked_matches_with_limit():
    note_id = UUID("12345678-1234-5678-1234-567812345678")
    created_at = datetime(2026, 6, 24, 12, 0, tzinfo=timezone.utc)
    updated_at = datetime(2026, 6, 24, 12, 0, tzinfo=timezone.utc)

    row = {
        "id": note_id,
        "title": "Postgres",
        "content": "Postgres stores relational data.",
        "embedding_model": EMBEDDING_MODEL,
        "created_at": created_at,
        "updated_at": updated_at,
        "score": 0.75,
    }

    connection = Mock(spec=Connection)
    connection.execute.return_value.mappings.return_value.all.return_value = [row]

    results = search_notes_by_keyword(
        connection=connection,
        query="relational data",
        limit=10,
    )

    connection.execute.assert_called_once()

    statement = connection.execute.call_args.args[0]
    compiled_statement = str(
        statement.compile(
            dialect=postgresql.dialect(),
            compile_kwargs={"literal_binds": True},
        )
    )

    assert "to_tsvector" in compiled_statement
    assert "websearch_to_tsquery" in compiled_statement
    assert "ts_rank" in compiled_statement
    assert "ORDER BY score DESC" in compiled_statement
    assert "notes.created_at DESC" in compiled_statement
    assert "notes.id DESC" in compiled_statement
    assert "LIMIT 10" in compiled_statement

    assert results == [
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


def test_search_notes_by_keyword_returns_empty_list_when_no_matches_exist():
    connection = Mock(spec=Connection)
    connection.execute.return_value.mappings.return_value.all.return_value = []

    result = search_notes_by_keyword(
        connection=connection,
        query="missing topic",
        limit=10,
    )

    assert result == []


def test_search_notes_by_semantic_queries_closest_vectors_with_limit():
    note_id = UUID("12345678-1234-5678-1234-567812345678")
    created_at = datetime(2026, 6, 25, 12, 0, tzinfo=timezone.utc)
    updated_at = datetime(2026, 6, 25, 12, 0, tzinfo=timezone.utc)
    query_embedding = [0.1] * EMBEDDING_DIMENSIONS

    row = {
        "id": note_id,
        "title": "Postgres",
        "content": "Postgres supports reliable storage.",
        "embedding_model": EMBEDDING_MODEL,
        "created_at": created_at,
        "updated_at": updated_at,
        "score": 0.91,
    }

    connection = Mock(spec=Connection)
    connection.execute.return_value.mappings.return_value.all.return_value = [row]

    results = search_notes_by_semantic(
        connection=connection,
        query_embedding=query_embedding,
        limit=10,
    )

    connection.execute.assert_called_once()

    statement = connection.execute.call_args.args[0]
    compiled_statement = str(
        statement.compile(
            dialect=postgresql.dialect(),
            compile_kwargs={"literal_binds": True},
        )
    )

    assert "<=>" in compiled_statement
    assert "ORDER BY distance ASC" in compiled_statement
    assert "notes.created_at DESC" in compiled_statement
    assert "notes.id DESC" in compiled_statement
    assert "LIMIT 10" in compiled_statement

    assert results == [
        SearchResult(
            id=note_id,
            title="Postgres",
            content="Postgres supports reliable storage.",
            embedding_model=EMBEDDING_MODEL,
            created_at=created_at,
            updated_at=updated_at,
            score=0.91,
            search_mode="semantic",
        )
    ]


def test_search_notes_by_semantic_filters_by_embedding_model():
    connection = Mock(spec=Connection)
    connection.execute.return_value.mappings.return_value.all.return_value = []

    search_notes_by_semantic(
        connection=connection,
        query_embedding=[0.1] * EMBEDDING_DIMENSIONS,
        limit=10,
    )

    statement = connection.execute.call_args.args[0]
    compiled_statement = str(
        statement.compile(
            dialect=postgresql.dialect(),
            compile_kwargs={"literal_binds": True},
        )
    )

    assert "notes.embedding_model = 'qwen3-embedding:0.6b'" in compiled_statement
