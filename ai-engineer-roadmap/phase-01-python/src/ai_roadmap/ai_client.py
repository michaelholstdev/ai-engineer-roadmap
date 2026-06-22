import json
import math
import os
from collections.abc import Callable, Mapping

import httpx
from pydantic import ValidationError

from ai_roadmap.prompts import build_ai_analysis_prompt
from ai_roadmap.schemas import AIAnalyzeResponse

OPENAI_API_KEY_ENV = "OPENAI_API_KEY"
AI_PROVIDER_ENV = "AI_PROVIDER"

EMBEDDING_MODEL = "qwen3-embedding:0.6b"
EMBEDDING_DIMENSIONS = 1024
OLLAMA_EMBED_URL = "http://127.0.0.1:11434/api/embed"
EMBEDDING_TIMEOUT_SECONDS = 30.0

RETRIEVAL_QUERY_INSTRUCTION = "Represent this query for retrieving relevant notes:"


class AIClientConfigurationError(Exception):
    pass


class AIProviderError(Exception):
    pass


def get_openai_api_key() -> str:
    api_key = os.getenv(OPENAI_API_KEY_ENV)
    if api_key is None or api_key.strip() == "":
        raise AIClientConfigurationError("OPENAI_API_KEY is not configured")
    return api_key


def get_ai_provider() -> str:
    ai_provider = os.getenv(AI_PROVIDER_ENV)
    if ai_provider is None or ai_provider.strip() == "":
        raise AIClientConfigurationError("AI provider is not configured")
    return ai_provider


def parse_ollama_ai_response(data: dict[str, object]) -> AIAnalyzeResponse:
    try:
        raw_response = data["response"]
        if not isinstance(raw_response, str):
            raise AIProviderError("Provider response was invalid")
        response = json.loads(raw_response)
        return AIAnalyzeResponse(
            summary=response["summary"],
            sentiment=response["sentiment"],
            topics=response["topics"],
            action_items=response["action_items"],
        )
    except (KeyError, json.JSONDecodeError, ValidationError) as error:
        raise AIProviderError("Provider response was invalid") from error


def analyze_text_with_ai(text: str) -> AIAnalyzeResponse:
    provider = get_ai_provider()

    if provider == "ollama":
        return analyze_text_with_ollama(text)

    raise AIClientConfigurationError("AI provider is not configured")


def is_retryable_ai_error(error: Exception) -> bool:
    return isinstance(error, AIProviderError)


def run_with_ai_retry(operation: Callable[[], AIAnalyzeResponse]) -> AIAnalyzeResponse:
    try:
        return operation()
    except Exception as error:
        if not is_retryable_ai_error(error):
            raise
        return operation()


def analyze_text_with_ollama(text: str) -> AIAnalyzeResponse:
    prompt = build_ai_analysis_prompt(text)
    try:
        response = httpx.post(
            url="http://127.0.0.1:11434/api/generate",
            json={
                "model": "llama3:latest",
                "prompt": prompt,
                "stream": False,
                "format": "json",
            },
            timeout=30.00,
        )
        response.raise_for_status()
    except (httpx.RequestError, httpx.HTTPStatusError) as error:
        raise AIProviderError("AI provider request failed") from error

    return parse_ollama_ai_response(response.json())


def parse_ollama_embedding_response(data: Mapping[str, object]) -> list[float]:
    try:
        embeddings = data["embeddings"]
        if not isinstance(embeddings, list):
            raise AIProviderError("Provider response was invalid")
        if len(embeddings) != 1:
            raise AIProviderError("Provider response was invalid")

        embedding = embeddings[0]
        if not isinstance(embedding, list):
            raise AIProviderError("Provider response was invalid")

        result: list[float] = []
        for value in embedding:
            if isinstance(value, bool) or not isinstance(value, int | float):
                raise AIProviderError("Provider response was invalid")
            if not math.isfinite(float(value)):
                raise AIProviderError("Provider response was invalid")

            result.append(float(value))

        if len(result) != EMBEDDING_DIMENSIONS:
            raise AIProviderError("Provider response was invalid")

        return result
    except (KeyError, IndexError) as error:
        raise AIProviderError("Provider response was invalid") from error


def embed_text(input_text: str) -> list[float]:
    try:
        response = httpx.post(
            url=OLLAMA_EMBED_URL,
            json={
                "model": EMBEDDING_MODEL,
                "input": input_text,
            },
            timeout=EMBEDDING_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
    except (httpx.RequestError, httpx.HTTPStatusError) as error:
        raise AIProviderError("AI provider request failed") from error

    return parse_ollama_embedding_response(response.json())


def embed_note_text(title: str, content: str) -> list[float]:
    input_text = f"Title: {title}\nContent: {content}"
    return embed_text(input_text)


def embed_search_query(query: str) -> list[float]:
    input_text = f"{RETRIEVAL_QUERY_INSTRUCTION}\n{query}"
    return embed_text(input_text)
