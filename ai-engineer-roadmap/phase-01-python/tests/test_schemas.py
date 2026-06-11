import pytest
from pydantic import ValidationError

from ai_roadmap.schemas import AIAnalyzeResponse


def test_ai_analyze_response_accepts_valid_data():
    result = AIAnalyzeResponse(
        summary="Short summary",
        sentiment="neutral",
        topics=["ai", "engineering"],
        action_items=[],
    )
    assert result.summary == "Short summary"
    assert result.sentiment == "neutral"
    assert result.topics == ["ai", "engineering"]
    assert result.action_items == []


def test_ai_analyze_response_rejects_invalid_sentiment():
    with pytest.raises(ValidationError):
        AIAnalyzeResponse(
            summary="Short summary",
            sentiment="mixed",
            topics=["ai"],
            action_items=[],
        )


def test_ai_analyze_response_rejects_topics_that_are_not_a_list():
    with pytest.raises(ValidationError):
        AIAnalyzeResponse(
            summary="Short summary",
            sentiment="neutral",
            topics="ai",
            action_items=[],
        )