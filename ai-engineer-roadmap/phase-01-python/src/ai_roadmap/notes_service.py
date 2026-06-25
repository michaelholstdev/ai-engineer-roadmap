from typing import Literal

from sqlalchemy.engine import Connection

from ai_roadmap.ai_client import (
    AIProviderError,
    EMBEDDING_DIMENSIONS,
    EMBEDDING_MODEL,
    embed_note_text,
    embed_search_query,
)
from ai_roadmap.notes_repository import (
    Note,
    NoteCreate,
    SearchResult,
    save_note,
    search_notes_by_keyword,
    search_notes_by_semantic,
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
    mode: Literal["keyword", "semantic"] = "keyword",
    limit: int = 20,
) -> list[SearchResult]:
    if mode == "semantic":
        query_embedding = embed_search_query(query)
        if len(query_embedding) != EMBEDDING_DIMENSIONS:
            raise AIProviderError("Provider response was invalid")
        return search_notes_by_semantic(connection, query_embedding, limit)

    return search_notes_by_keyword(connection, query, limit)
