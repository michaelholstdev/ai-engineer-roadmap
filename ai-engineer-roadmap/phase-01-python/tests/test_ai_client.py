import pytest

import httpx

from ai_roadmap.ai_client import (
    AIClientConfigurationError,
    AIProviderError,
    AI_PROVIDER_ENV,
    OPENAI_API_KEY_ENV,
    EMBEDDING_DIMENSIONS,
    EMBEDDING_MODEL,
    OLLAMA_EMBED_URL,
    analyze_text_with_ai,
    analyze_text_with_ollama,
    embed_note_text,
    embed_search_query,
    get_openai_api_key,
    is_retryable_ai_error,
    parse_ollama_ai_response,
    parse_ollama_embedding_response,
    run_with_ai_retry,
)
from ai_roadmap.schemas import AIAnalyzeResponse


def test_get_openai_api_key_returns_configured_key(monkeypatch):
    api_key = "Here-is-a-key"
    monkeypatch.setenv(OPENAI_API_KEY_ENV, api_key)
    assert get_openai_api_key() == api_key


def test_get_openai_api_key_raises_when_key_is_blank(monkeypatch):
    api_key = ""
    monkeypatch.setenv(OPENAI_API_KEY_ENV, api_key)
    with pytest.raises(AIClientConfigurationError):
        get_openai_api_key()


def test_get_openai_api_key_raises_when_key_is_missing(monkeypatch):
    monkeypatch.delenv(OPENAI_API_KEY_ENV, raising=False)
    with pytest.raises(AIClientConfigurationError):
        get_openai_api_key()


def test_analyze_text_with_ai_uses_ollama_provider(monkeypatch):
    monkeypatch.setenv(AI_PROVIDER_ENV, "ollama")

    def fake_analyze_text_with_ollama(text: str) -> AIAnalyzeResponse:
        assert text == "some text"
        return AIAnalyzeResponse(
            summary="Short summary",
            sentiment="neutral",
            topics=[],
            action_items=[],
        )

    monkeypatch.setattr(
        "ai_roadmap.ai_client.analyze_text_with_ollama",
        fake_analyze_text_with_ollama,
    )

    result = analyze_text_with_ai("some text")

    assert result.summary == "Short summary"


@pytest.mark.parametrize(
    ("error", "expected"),
    [
        (AIProviderError("temporary failure"), True),
        (AIClientConfigurationError("temporary failure"), False),
        (Exception("temporary failure"), False),
    ],
)
def test_is_retryable_ai_error(error: Exception, expected: bool):
    assert is_retryable_ai_error(error) is expected


def test_run_with_ai_retry_succeeded_on_first_try():
    def operation() -> AIAnalyzeResponse:
        return AIAnalyzeResponse(
            summary="Short summary",
            sentiment="neutral",
            topics=["ai", "engineering"],
            action_items=[],
        )

    result = run_with_ai_retry(operation)
    assert result.summary == "Short summary"


def test_run_with_ai_retry_succeeded_on_second_try():
    calls = {"count": 0}

    def operation() -> AIAnalyzeResponse:
        calls["count"] += 1
        if calls["count"] == 1:
            raise AIProviderError("temporary failure")
        return AIAnalyzeResponse(
            summary="Short summary",
            sentiment="neutral",
            topics=["ai", "engineering"],
            action_items=[],
        )

    result = run_with_ai_retry(operation)
    assert result.summary == "Short summary"
    assert calls["count"] == 2


def test_run_with_ai_retry_raise_provider_exception_after_second_try():
    calls = {"count": 0}

    def operation() -> AIAnalyzeResponse:
        calls["count"] += 1
        raise AIProviderError("temporary failure")

    with pytest.raises(AIProviderError):
        run_with_ai_retry(operation)
    assert calls["count"] == 2


def test_run_with_ai_retry_raise_configuration_exception_without_retry():
    calls = {"count": 0}

    def operation() -> AIAnalyzeResponse:
        calls["count"] += 1
        raise AIClientConfigurationError("missing config")

    with pytest.raises(AIClientConfigurationError):
        run_with_ai_retry(operation)
    assert calls["count"] == 1


def test_parse_ollama_ai_response_returned_valid_response():
    data = {
        "response": '{"summary":"ok","sentiment":"neutral","topics":[],"action_items":[]}'
    }
    result = parse_ollama_ai_response(data)
    assert result.summary == "ok"
    assert result.sentiment == "neutral"
    assert result.topics == []
    assert result.action_items == []


def test_parse_ollama_ai_response_exception_on_invalid_response():
    data = {}
    with pytest.raises(AIProviderError):
        parse_ollama_ai_response(data)


def test_parse_ollama_ai_response_exception_on_invalid_json():
    data = {"response": "not json"}
    with pytest.raises(AIProviderError):
        parse_ollama_ai_response(data)


def test_parse_ollama_ai_response_exception_on_invalid_sentiment():
    data = {
        "response": '{"summary":"ok","sentiment":"mixed","topics":[],"action_items":[]}'
    }
    with pytest.raises(AIProviderError):
        parse_ollama_ai_response(data)


def test_parse_ollama_ai_response_raises_when_response_is_not_a_string():
    data = {"response": 123}
    with pytest.raises(AIProviderError):
        parse_ollama_ai_response(data)


def test_analyze_text_with_ollama(monkeypatch):
    class FakeResponse:
        def raise_for_status(self) -> None:
            pass

        def json(self) -> dict[str, object]:
            return {
                "response": '{"summary":"ok","sentiment":"neutral","topics":[],"action_items":[]}'
            }

    def fake_post(url: str, json: dict[str, object], timeout: float):
        assert url == "http://127.0.0.1:11434/api/generate"
        assert json["model"] == "llama3:latest"
        assert json["stream"] is False
        assert json["format"] == "json"
        assert "some text" in str(json["prompt"])
        assert timeout == 30.0
        return FakeResponse()

    monkeypatch.setattr("httpx.post", fake_post)

    result = analyze_text_with_ollama("some text")
    assert result.summary == "ok"
    assert result.sentiment == "neutral"
    assert result.topics == []
    assert result.action_items == []


def test_analyze_text_with_ollama_exception_on_request_error(monkeypatch):
    def fake_post(url: str, json: dict[str, object], timeout: float):
        assert url == "http://127.0.0.1:11434/api/generate"
        assert json["model"] == "llama3:latest"
        assert json["stream"] is False
        assert json["format"] == "json"
        assert "some text" in str(json["prompt"])
        assert timeout == 30.0
        raise httpx.RequestError("connection failed")

    monkeypatch.setattr("httpx.post", fake_post)

    with pytest.raises(AIProviderError):
        analyze_text_with_ollama("some text")


def test_analyze_text_with_ollama_exception_for_raised_response(monkeypatch):
    class FakeResponse:
        def raise_for_status(self) -> None:
            raise httpx.HTTPStatusError(
                "server error",
                request=httpx.Request("POST", "http://127.0.0.1:11434/api/generate"),
                response=httpx.Response(500),
            )

        def json(self) -> dict[str, object]:
            raise AssertionError(
                "json() should not be called when the response has an error status"
            )

    def fake_post(url: str, json: dict[str, object], timeout: float):
        assert url == "http://127.0.0.1:11434/api/generate"
        assert json["model"] == "llama3:latest"
        assert json["stream"] is False
        assert json["format"] == "json"
        assert "some text" in str(json["prompt"])
        assert timeout == 30.0
        return FakeResponse()

    monkeypatch.setattr("httpx.post", fake_post)

    with pytest.raises(AIProviderError):
        analyze_text_with_ollama("some text")


def test_embedding_client_configuration_values():
    assert EMBEDDING_MODEL == "qwen3-embedding:0.6b"
    assert EMBEDDING_DIMENSIONS == 1024
    assert OLLAMA_EMBED_URL == "http://127.0.0.1:11434/api/embed"


def test_parse_ollama_embedding_response_returns_valid_embedding():
    embedding = [0.1] * EMBEDDING_DIMENSIONS
    data = {
        "embeddings": [embedding],
    }

    result = parse_ollama_embedding_response(data)

    assert result == embedding


@pytest.mark.parametrize(
    "data",
    [
        {},
        {"embeddings": "not a list"},
        {"embeddings": []},
        {"embeddings": ["not a vector"]},
    ],
)
def test_parse_ollama_embedding_response_rejects_invalid_shape(data):
    with pytest.raises(AIProviderError):
        parse_ollama_embedding_response(data)


def test_parse_ollama_embedding_response_rejects_wrong_dimension():
    data = {
        "embeddings": [[0.1, 0.2]],
    }

    with pytest.raises(AIProviderError):
        parse_ollama_embedding_response(data)


@pytest.mark.parametrize("value", [float("nan"), float("inf"), float("-inf")])
def test_parse_ollama_embedding_response_rejects_non_finite_values(value: float):
    embedding = [0.1] * EMBEDDING_DIMENSIONS
    embedding[0] = value

    data = {
        "embeddings": [embedding],
    }

    with pytest.raises(AIProviderError):
        parse_ollama_embedding_response(data)


def test_embed_note_text_calls_ollama_embed_api(monkeypatch):
    embedding = [0.1] * EMBEDDING_DIMENSIONS

    class FakeResponse:
        def raise_for_status(self) -> None:
            pass

        def json(self) -> dict[str, object]:
            return {"embeddings": [embedding]}

    def fake_post(url: str, json: dict[str, object], timeout: float):
        assert url == OLLAMA_EMBED_URL
        assert json["model"] == EMBEDDING_MODEL
        assert "Postgres" in str(json["input"])
        assert "stores data" in str(json["input"])
        assert "Represent this query" not in str(json["input"])
        assert timeout == 30.0
        return FakeResponse()

    monkeypatch.setattr("httpx.post", fake_post)

    result = embed_note_text("Postgres", "stores data")

    assert result == embedding


def test_embed_note_text_raises_provider_error_on_request_error(monkeypatch):
    def fake_post(url: str, json: dict[str, object], timeout: float):
        raise httpx.RequestError("connection failed")

    monkeypatch.setattr("httpx.post", fake_post)

    with pytest.raises(AIProviderError):
        embed_note_text("Postgres", "stores data")


def test_embed_search_query_adds_retrieval_instruction(monkeypatch):
    embedding = [0.1] * EMBEDDING_DIMENSIONS

    class FakeResponse:
        def raise_for_status(self) -> None:
            pass

        def json(self) -> dict[str, object]:
            return {"embeddings": [embedding]}

    def fake_post(url: str, json: dict[str, object], timeout: float):
        assert url == OLLAMA_EMBED_URL
        assert json["model"] == EMBEDDING_MODEL
        assert "Represent this query for retrieving relevant notes" in str(
            json["input"]
        )
        assert "database search" in str(json["input"])
        assert timeout == 30.0
        return FakeResponse()

    monkeypatch.setattr("httpx.post", fake_post)

    result = embed_search_query("database search")

    assert result == embedding


def test_embed_note_text_raises_provider_error_for_invalid_embedding_response(
    monkeypatch,
):
    class FakeResponse:
        def raise_for_status(self) -> None:
            pass

        def json(self) -> dict[str, object]:
            return {"embeddings": [[0.1, 0.2]]}

    def fake_post(url: str, json: dict[str, object], timeout: float):
        return FakeResponse()

    monkeypatch.setattr("httpx.post", fake_post)

    with pytest.raises(AIProviderError):
        embed_note_text("Postgres", "stores data")


def test_parse_ollama_embedding_response_rejects_boolean_values():
    embedding = [0.1] * EMBEDDING_DIMENSIONS
    embedding[0] = True

    with pytest.raises(AIProviderError):
        parse_ollama_embedding_response({"embeddings": [embedding]})


def test_parse_ollama_embedding_response_rejects_multiple_embeddings():
    embedding = [0.1] * EMBEDDING_DIMENSIONS

    with pytest.raises(AIProviderError):
        parse_ollama_embedding_response({"embeddings": [embedding, embedding]})
