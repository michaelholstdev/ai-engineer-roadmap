# Lesson 2.2 — Request Validation

## Goal

Make the `/analyze` endpoint reject invalid text input intentionally.

## Learning Objectives

By the end of this lesson, you should understand:

- how FastAPI uses Pydantic models for request validation
- how to validate empty strings and whitespace-only strings
- what HTTP `422 Unprocessable Entity` means
- how validation affects endpoint tests

## Estimated Time

2-3 hours

## Tutor Instructions

Codex should explain validation behavior and review the learner's tests and model changes. Codex should not implement the validation unless explicitly asked.

## Target Behavior

The `/analyze` endpoint should accept meaningful text and reject empty or whitespace-only input.

Valid request:

```json
{
  "text": "AI Engineering is fun."
}
```

Invalid requests:

```json
{
  "text": ""
}
```

```json
{
  "text": "   "
}
```

## Tasks

- [ ] Decide whether empty text should be allowed or rejected.
- [ ] Add API tests for empty text and whitespace-only text.
- [ ] Make the tests fail first.
- [ ] Add Pydantic validation to `AnalyzeRequest`.
- [ ] Run `uv run pytest`.
- [ ] Run `uv run ruff check .`.
- [ ] Run `uv run mypy src`.
- [ ] Ask Codex for review.

## Acceptance Criteria

- Meaningful text still returns HTTP `200`.
- Empty text returns HTTP `422`.
- Whitespace-only text returns HTTP `422`.
- Tests cover valid and invalid request bodies.
- `uv run pytest` passes.
- `uv run ruff check .` passes.
- `uv run mypy src` passes.

## Review Prompt

```txt
Review my Lesson 2.2 validation changes.
Do not rewrite the code.
Explain what looks correct, what is missing, and what I should fix myself.
Here is my code and tool output:
...
```

## Reflection Questions

1. Why should APIs validate input before running business logic?
2. What is the difference between `""` and `"   "` for validation?
3. Why does FastAPI return `422` for validation errors?
4. Where should validation live: in tests, route handlers, or request models?
5. What validation might be useful before sending text to an LLM?
