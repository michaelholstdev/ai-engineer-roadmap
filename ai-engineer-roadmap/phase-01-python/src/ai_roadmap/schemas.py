from datetime import datetime
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, field_validator


class AnalyzeRequest(BaseModel):
    text: str

    @field_validator("text")
    @classmethod
    def validate_text_not_blank(cls, value: str) -> str:
        if value.strip() == "":
            raise ValueError("Invalid text, text must not be empty")
        return value


class AnalyzeResponse(BaseModel):
    word_count: int
    character_count: int
    sentence_count: int


class AIAnalyzeResponse(BaseModel):
    summary: str
    sentiment: Literal["positive", "neutral", "negative"]
    topics: list[str]
    action_items: list[str]


class AnalysisHistoryResponse(BaseModel):
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


class NoteCreateRequest(BaseModel):
    title: str
    content: str

    @field_validator("title", "content")
    @classmethod
    def validate_text_not_blank(cls, value: str) -> str:
        if value.strip() == "":
            raise ValueError("Field must not be empty")
        return value


class NoteResponse(BaseModel):
    id: UUID
    title: str
    content: str
    embedding_model: str
    created_at: datetime
    updated_at: datetime
