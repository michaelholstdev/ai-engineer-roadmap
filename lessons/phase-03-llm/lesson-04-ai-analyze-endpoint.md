# Lesson 3.4 — AI Analyze Endpoint

## Goal

Add a FastAPI endpoint that returns an AI-powered text analysis response.

## Learning Objectives

By the end of this lesson, you should understand:

- how to connect a route handler to an AI client boundary
- how to reuse request validation patterns
- how to return structured AI output as JSON
- how to keep route logic thin

## Estimated Time

3-4 hours

## Tutor Instructions

Codex should guide endpoint design and review learner-written code. Codex should not implement the endpoint unless explicitly asked.

## Target Endpoint

Create:

```http
POST /ai/analyze
```

Example response:

```json
{
  "summary": "...",
  "sentiment": "neutral",
  "topics": ["ai", "engineering"],
  "action_items": []
}
```

## Tasks

- [ ] Add request and response schemas for `/ai/analyze`.
- [ ] Add an AI route or extend the current router intentionally.
- [ ] Call the AI client boundary from the route.
- [ ] Return structured JSON.
- [ ] Add endpoint tests with a fake or mocked client.
- [ ] Run `uv run pytest`.
- [ ] Run `uv run ruff check .`.
- [ ] Run `uv run mypy src`.
- [ ] Ask Codex for review.

## Acceptance Criteria

- `POST /ai/analyze` exists.
- The endpoint uses Pydantic request and response models.
- Route logic stays thin.
- Tests do not call the real provider.
- `pytest`, `ruff`, and `mypy` pass.

## Review Prompt

```txt
Review my Lesson 3.4 AI analyze endpoint.
Do not rewrite the code.
Focus on route structure, schema use, and testability.
Here is my code and tool output:
...
```

## Reflection Questions

1. What should the route handler be responsible for?
2. What should the AI client be responsible for?
3. Why should endpoint tests avoid real provider calls?
4. How does structured output help the frontend later?
5. What failure cases should this endpoint expose clearly?
