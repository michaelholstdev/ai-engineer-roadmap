from typing import Literal

from sqlalchemy.engine import Connection

from ai_roadmap.ai_client import EMBEDDING_MODEL, embed_note_text
from ai_roadmap.notes_repository import (
    Note,
    NoteCreate,
    SearchResult,
    save_note,
    search_notes_by_keyword,
)


def create_note(connection: Connection, title: str, content: str) -> Note:
    embedding = embed_note_text(title, content)

    note = NoteCreate(
        title=title,
        content=content,
        embedding=embedding,
        embedding_model=EMBEDDING_MODEL,
    )

    return save_note(connection, note)


def search_notes(
    connection: Connection,
    query: str,
    mode: Literal["keyword"] = "keyword",
    limit: int = 20,
) -> list[SearchResult]:
    return search_notes_by_keyword(connection, query, limit)
