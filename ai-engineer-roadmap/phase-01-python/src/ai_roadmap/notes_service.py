from sqlalchemy.engine import Connection

from ai_roadmap.ai_client import EMBEDDING_MODEL, embed_note_text
from ai_roadmap.notes_repository import Note, NoteCreate, save_note


def create_note(connection: Connection, title: str, content: str) -> Note:
    embedding = embed_note_text(title, content)

    note = NoteCreate(
        title=title,
        content=content,
        embedding=embedding,
        embedding_model=EMBEDDING_MODEL,
    )

    return save_note(connection, note)
