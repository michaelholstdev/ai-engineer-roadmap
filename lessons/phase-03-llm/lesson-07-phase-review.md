# Lesson 3.7 — Phase Review

## Goal

Review the LLM API phase and make sure the integration is safe, testable, and understandable.

## Learning Objectives

By the end of this lesson, you should understand:

- how to evaluate an LLM-backed backend feature
- how to verify that secrets are not committed
- how to check that tests avoid real provider calls
- how to summarize structured AI behavior
- how to prepare for a React UI integration

## Estimated Time

2-3 hours

## Tutor Instructions

Codex should act as reviewer. Codex should prioritize security, testability, error handling, and maintainability.

## Tasks

- [ ] Run `uv run pytest`.
- [ ] Run `uv run ruff check .`.
- [ ] Run `uv run mypy src`.
- [ ] Review secret handling.
- [ ] Review AI client boundaries.
- [ ] Review mocked tests.
- [ ] Review README setup instructions.
- [ ] Summarize what you learned.
- [ ] Ask Codex for final Phase 3 review.

## Acceptance Criteria

- `pytest`, `ruff`, and `mypy` pass.
- API keys are not committed.
- Tests do not call the real LLM API.
- The AI endpoint returns structured JSON.
- Provider failure cases are handled intentionally.

## Review Prompt

```txt
Review my completed Phase 3 LLM API work.
Do not rewrite files.
Focus on security, testability, error handling, and readiness for Phase 4.
Here is my code, structure, and tool output:
...
```

## Reflection Questions

1. How does the AI request flow from FastAPI to the provider and back?
2. Where are secrets read and validated?
3. How do tests avoid real LLM calls?
4. What makes the AI response usable by a frontend?
5. What should be improved before this is production-ready?
