import json
import os
from collections.abc import Callable

import httpx
from pydantic import ValidationError

from ai_roadmap.prompts import build_ai_analysis_prompt
from ai_roadmap.schemas import AIAnalyzeResponse

OPENAI_API_KEY_ENV = "OPENAI_API_KEY"
AI_PROVIDER_ENV = "AI_PROVIDER"


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