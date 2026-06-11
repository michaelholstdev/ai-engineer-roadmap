# Lesson 3.2 — AI Client Boundary

## Goal

Create a clear boundary between FastAPI route handlers and external LLM provider code.

## Learning Objectives

By the end of this lesson, you should understand:

- why external API logic should not live directly in route handlers
- how to read configuration from environment variables
- how to design a small AI client interface
- how to test missing configuration without real API calls

## Estimated Time

2-3 hours

## Tutor Instructions

Codex should guide module design and review learner-written code. Codex should not hardcode secrets or make real provider calls.

## Target Structure

One possible structure:

```txt
src/
  ai_roadmap/
    ai_client.py
    routes.py
    schemas.py
```

The exact structure can change if the learner explains the reason.

## Tasks

- [ ] Create an AI client module.
- [ ] Read the API key from an environment variable.
- [ ] Add a clear error for missing configuration.
- [ ] Keep provider-specific code out of route handlers.
- [ ] Add tests for missing API key behavior.
- [ ] Run `uv run pytest`.
- [ ] Run `uv run ruff check .`.
- [ ] Run `uv run mypy src`.
- [ ] Ask Codex for review.

## Acceptance Criteria

- API keys are not hardcoded.
- AI client logic is separate from route logic.
- Missing configuration is handled intentionally.
- Tests do not call the real provider.
- `pytest`, `ruff`, and `mypy` pass.

## Review Prompt

```txt
Review my Lesson 3.2 AI client boundary.
Do not rewrite the code.
Tell me whether the module boundary is clear and testable.
Here is my code and tool output:
...
```

## Reflection Questions

1. Why should provider calls be isolated from route handlers?
2. What should happen if the API key is missing?
3. Why is a small client interface easier to test?
4. What should the AI client know that the route should not know?
5. What should the route know that the AI client should not know?
