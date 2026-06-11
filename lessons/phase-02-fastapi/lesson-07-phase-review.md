# Lesson 2.7 — Phase Review

## Goal

Review the FastAPI phase and make sure the API is tested, typed, documented, and understandable.

## Learning Objectives

By the end of this lesson, you should understand:

- how to evaluate a small backend project
- how to use test, lint, and type-check output as release criteria
- how to summarize API behavior
- how to prepare for LLM API integration

## Estimated Time

2-3 hours

## Tutor Instructions

Codex should act as reviewer. Codex should prioritize correctness, clarity, missing tests, and maintainability.

## Tasks

- [ ] Run `uv run pytest`.
- [ ] Run `uv run ruff check .`.
- [ ] Run `uv run mypy src`.
- [ ] Review the API structure.
- [ ] Review the endpoint tests.
- [ ] Update the README if needed.
- [ ] Summarize what you learned.
- [ ] Ask Codex for final Phase 2 review.

## Acceptance Criteria

- `pytest`, `ruff`, and `mypy` pass.
- The README explains how to run and test the API.
- The learner can explain the request and response flow.
- The API is ready to be used by a later LLM-powered endpoint.

## Review Prompt

```txt
Review my completed Phase 2 FastAPI work.
Do not rewrite files.
Focus on bugs, missing tests, unclear structure, and readiness for Phase 3.
Here is my code, structure, and tool output:
...
```

## Reflection Questions

1. What happens from HTTP request to JSON response?
2. Where does validation happen?
3. Where does business logic happen?
4. What tests give you confidence in the API?
5. What should be added before connecting to an LLM API?
