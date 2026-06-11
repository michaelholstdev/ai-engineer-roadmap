# Lesson 3.6 — Errors, Retries, Rate Limits, and Cost

## Goal

Handle realistic LLM provider failure modes intentionally.

## Learning Objectives

By the end of this lesson, you should understand:

- common LLM API failures
- when retries help and when they do not
- why timeouts matter
- how rate limits and token usage affect cost
- how to expose provider errors safely through your API

## Estimated Time

3-4 hours

## Tutor Instructions

Codex should help the learner reason about reliability and cost. Codex should keep the implementation simple and testable.

## Tasks

- [ ] List expected provider failure modes.
- [ ] Add simple timeout handling if supported by the client.
- [ ] Add retry behavior for one retry-safe failure case.
- [ ] Return clear API errors for provider failures.
- [ ] Add tests for timeout, retry, and provider error behavior.
- [ ] Run `uv run pytest`.
- [ ] Run `uv run ruff check .`.
- [ ] Run `uv run mypy src`.
- [ ] Ask Codex for review.

## Acceptance Criteria

- Provider failures are handled intentionally.
- Retry behavior is limited and testable.
- The API does not leak secrets or raw provider internals.
- Tests cover at least one provider failure.
- `pytest`, `ruff`, and `mypy` pass.

## Review Prompt

```txt
Review my Lesson 3.6 LLM error handling.
Do not rewrite the code.
Tell me whether the retry and error behavior is clear and safe.
Here is my code and tool output:
...
```

## Reflection Questions

1. Which LLM errors are safe to retry?
2. Which errors should not be retried?
3. Why can retries increase cost?
4. Why should API responses avoid exposing raw provider errors?
5. What should be logged for debugging without leaking secrets?
