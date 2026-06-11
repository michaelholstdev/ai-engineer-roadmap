# Lesson 2.3 — Error Handling

## Goal

Learn how to return intentional API errors with clear status codes and response bodies.

## Learning Objectives

By the end of this lesson, you should understand:

- when to use validation errors and when to use explicit route errors
- how to raise `HTTPException`
- how status codes communicate failure type
- how to test error responses

## Estimated Time

2-3 hours

## Tutor Instructions

Codex should help the learner distinguish validation errors from application errors. Codex should review tests and error behavior without implementing the solution unless explicitly asked.

## Target Behavior

Add one intentional application-level error case for `/analyze`.

Example option:

- reject text longer than a chosen maximum length
- return HTTP `413 Payload Too Large` or HTTP `400 Bad Request`
- include a clear JSON error response

The learner should decide the exact limit before implementing it.

## Tasks

- [ ] Choose one application-level error condition.
- [ ] Write a failing API test for that error.
- [ ] Raise `HTTPException` in the route handler.
- [ ] Verify the response status code and error body.
- [ ] Run `uv run pytest`.
- [ ] Run `uv run ruff check .`.
- [ ] Run `uv run mypy src`.
- [ ] Ask Codex for review.

## Acceptance Criteria

- Existing valid requests still return HTTP `200`.
- Pydantic validation errors still return HTTP `422`.
- The new application-level error returns the chosen status code.
- Tests cover success, validation failure, and application failure.
- `pytest`, `ruff`, and `mypy` pass.

## Review Prompt

```txt
Review my Lesson 2.3 error handling.
Do not rewrite the code.
Explain whether my status code and error response make sense.
Here is my code and tool output:
...
```

## Reflection Questions

1. What is the difference between a validation error and an application error?
2. When would you use `HTTPException`?
3. Why should error responses be predictable?
4. How should tests verify error behavior?
5. What errors might an LLM-backed endpoint need to handle later?
