# Lesson 2.1 — FastAPI Basics

## Goal

Build a small HTTP API around your text statistics functions.

## Learning Objectives

By the end of this lesson, you should understand:

- FastAPI route handlers
- request and response models
- Pydantic validation
- JSON APIs
- basic error handling

## Estimated Time

4-5 hours

## Tutor Instructions

Codex should explain the API design and review the learner's implementation. Codex should not generate the complete FastAPI app unless explicitly asked.

## Target Endpoint

Create an endpoint:

```http
POST /analyze
```

Example request:

```json
{
  "text": "AI Engineering is fun."
}
```

Example response:

```json
{
  "word_count": 4,
  "character_count": 22,
  "sentence_count": 1
}
```

## Tasks

- [ ] Add FastAPI as a dependency.
- [ ] Create an app module.
- [ ] Define request and response models.
- [ ] Implement `POST /analyze` yourself.
- [ ] Add tests for the endpoint.
- [ ] Run tests.
- [ ] Ask Codex for review.

## Acceptance Criteria

- The endpoint returns valid JSON.
- The endpoint uses Pydantic models.
- Empty input is handled intentionally.
- Tests cover the endpoint.
- `uv run pytest` passes.

## Reflection Questions

1. Why do APIs need explicit request and response schemas?
2. What does Pydantic validate?
3. What should happen if the request body is invalid?
4. Why is this backend structure useful for later LLM integration?
