from unittest.mock import Mock

from sqlalchemy.engine import Connection
from datetime import datetime, timezone
from uuid import UUID


from ai_roadmap.ai_client import EMBEDDING_DIMENSIONS, EMBEDDING_MODEL
from ai_roadmap.notes_repository import (
    Note,
    NoteCreate,
    format_embedding_for_pgvector,
    save_note,
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
