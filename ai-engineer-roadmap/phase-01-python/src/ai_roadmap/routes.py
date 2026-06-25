from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.engine import Connection

from ai_roadmap.ai_client import (
    AIClientConfigurationError,
    AIProviderError,
    analyze_text_with_ai,
    get_ai_provider,
)
from ai_roadmap.analysis_repository import (
    AnalysisRunCreate,
    save_analysis_run,
    list_analysis_runs,
)
from ai_roadmap.database import get_connection
from ai_roadmap.schemas import (
    AIAnalyzeResponse,
    AnalyzeRequest,
    AnalyzeResponse,
    AnalysisHistoryResponse,
    NoteCreateRequest,
    NoteResponse,
    SearchResultResponse,
)
from ai_roadmap.text_stats import count_characters, count_sentences, count_words
from ai_roadmap.notes_service import create_note, search_notes

MAX_TEXT_LENGTH = 500


router = APIRouter()


@router.post(
    "/analyze",
    responses={
        413: {
            "description": "Text is too long",
        },
    },
)
def analyze(
    request: AnalyzeRequest, connection: Connection = Depends(get_connection)
) -> AnalyzeResponse:
    if len(request.text) > MAX_TEXT_LENGTH:
        raise HTTPException(
            status_code=413,
            detail="Text is too long",
        )

    analyzed_response = AnalyzeResponse(
        word_count=count_words(request.text),
        character_count=count_characters(request.text),
        sentence_count=count_sentences(request.text),
    )

    run = AnalysisRunCreate(
        analysis_type="text",
        word_count=analyzed_response.word_count,
        character_count=analyzed_response.character_count,
        sentence_count=analyzed_response.sentence_count,
        topics=[],
        action_items=[],
        input_text=request.text,
        provider=None,
        sentiment=None,
        summary=None,
    )
    save_analysis_run(connection, run)

    return analyzed_response


@router.post("/ai/analyze")
def ai_analyze(
    request: AnalyzeRequest, connection: Connection = Depends(get_connection)
) -> AIAnalyzeResponse:
    try:
        analyzed_response = analyze_text_with_ai(request.text)

        run = AnalysisRunCreate(
            analysis_type="ai",
            word_count=count_words(request.text),
            character_count=count_characters(request.text),
            sentence_count=count_sentences(request.text),
            topics=analyzed_response.topics,
            action_items=analyzed_response.action_items,
            input_text=request.text,
            provider=get_ai_provider(),
            sentiment=analyzed_response.sentiment,
            summary=analyzed_response.summary,
        )

        save_analysis_run(connection, run)

        return analyzed_response
    except AIClientConfigurationError:
        raise HTTPException(
            status_code=503,
            detail="AI client is not configured",
        )
    except AIProviderError:
        raise HTTPException(
            status_code=502,
            detail="AI provider request failed",
        )


@router.get("/analyses")
def list_analysis(
    connection: Connection = Depends(get_connection),
    limit: int = Query(default=20, ge=1, le=100),
) -> list[AnalysisHistoryResponse]:
    runs = list_analysis_runs(connection, limit)

    return [
        AnalysisHistoryResponse(
            id=run.id,
            input_text=run.input_text,
            action_items=run.action_items,
            analysis_type=run.analysis_type,
            character_count=run.character_count,
            provider=run.provider,
            sentence_count=run.sentence_count,
            sentiment=run.sentiment,
            summary=run.summary,
            topics=run.topics,
            word_count=run.word_count,
            created_at=run.created_at,
        )
        for run in runs
    ]


@router.post("/notes")
def create_note_route(
    request: NoteCreateRequest,
    connection: Connection = Depends(get_connection),
) -> NoteResponse:
    try:
        note = create_note(connection, request.title, request.content)
        return NoteResponse(
            id=note.id,
            title=note.title,
            content=note.content,
            embedding_model=note.embedding_model,
            updated_at=note.updated_at,
            created_at=note.created_at,
        )
    except AIClientConfigurationError:
        raise HTTPException(
            status_code=503,
            detail="AI client is not configured",
        )
    except AIProviderError:
        raise HTTPException(
            status_code=502,
            detail="AI provider request failed",
        )


@router.get("/notes/search")
def search_notes_route(
    connection: Connection = Depends(get_connection),
    query: str = Query(min_length=1, pattern=r"\S"),
    mode: Literal["keyword", "semantic"] = "keyword",
    limit: int = Query(default=20, ge=1, le=100),
) -> list[SearchResultResponse]:
    try:
        results = search_notes(
            connection=connection,
            query=query,
            mode=mode,
            limit=limit,
        )
        return [
            SearchResultResponse(
                id=result.id,
                title=result.title,
                content=result.content,
                embedding_model=result.embedding_model,
                created_at=result.created_at,
                updated_at=result.updated_at,
                score=result.score,
                search_mode=result.search_mode,
            )
            for result in results
        ]
    except AIClientConfigurationError:
        raise HTTPException(status_code=503, detail="AI client is not configured")
    except AIProviderError:
        raise HTTPException(status_code=502, detail="AI provider request failed")
