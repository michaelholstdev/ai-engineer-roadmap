# Lesson 2.5 — API Project Structure

## Goal

Refactor the FastAPI code into small modules with clear responsibilities.

## Learning Objectives

By the end of this lesson, you should understand:

- why API projects separate app creation, routes, schemas, and business logic
- how imports work across package modules
- how to refactor while keeping tests green
- how structure prepares the backend for later LLM integration

## Estimated Time

3-4 hours

## Tutor Instructions

Codex should help the learner plan a safe refactor and review each step. Codex should not move code automatically unless explicitly asked.

## Target Structure

One possible structure:

```txt
src/
  ai_roadmap/
    __init__.py
    api.py
    routes.py
    schemas.py
    text_stats.py
```

The exact names can be adjusted if the learner explains the reason.

## Tasks

- [ ] Identify the responsibilities currently inside `api.py`.
- [ ] Move Pydantic models to a schema module.
- [ ] Move route handlers to a route module.
- [ ] Keep `app` creation easy to import in tests.
- [ ] Run tests after each small refactor.
- [ ] Run `uv run pytest`.
- [ ] Run `uv run ruff check .`.
- [ ] Run `uv run mypy src`.
- [ ] Ask Codex for review.

## Acceptance Criteria

- The API still exposes `POST /analyze`.
- Tests still import the FastAPI app successfully.
- Schemas and route logic are separated.
- `pytest`, `ruff`, and `mypy` pass.

## Review Prompt

```txt
Review my Lesson 2.5 project structure refactor.
Do not rewrite the files.
Tell me whether the module boundaries are clear.
Here is my structure, code, and tool output:
...
```

## Reflection Questions

1. What responsibility should each module have?
2. Why is refactoring safer when tests already exist?
3. What makes an import path clear or confusing?
4. How does this structure help future LLM features?
5. What would be a sign that a module is doing too much?
