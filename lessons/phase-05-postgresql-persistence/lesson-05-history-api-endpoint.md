# Lesson 5.5 — History API Endpoint

## Goal

Add a backend endpoint that returns stored analysis history.

## Learning Objectives

By the end of this lesson, you should understand:

- how to expose persisted records through an API
- why list endpoints need ordering and limits
- how response models protect frontend expectations
- how to avoid leaking internal database details
- how history endpoints prepare the app for richer UI features

## Estimated Time

3-4 hours

## Tutor Instructions

Codex should guide the learner toward a small list endpoint with clear ordering and a simple limit. Codex should avoid complex pagination unless the learner explicitly asks.

## Tasks

- [x] Add a typed response model for history records.
- [x] Add a `GET /analyses` endpoint or similarly named history endpoint.
- [x] Return newest records first.
- [x] Add a small limit strategy.
- [x] Add backend tests for empty and non-empty history.
- [x] Run backend checks.
- [x] Ask Codex for review.

## Acceptance Criteria

- The backend exposes stored analysis history.
- History records are ordered predictably.
- The endpoint response is typed.
- Empty history returns a valid empty list.
- Tests cover the history endpoint without real LLM calls.

## Review Prompt

```txt
Review my Lesson 5.5 history API endpoint.
Do not rewrite the code.
Focus on response shape, ordering, limits, empty history behavior, and test coverage.
Here is my code, tests, and command output:
...
```

## Reflection Questions

1. Why should history records have predictable ordering?
2. Why should list endpoints usually have a limit?
3. What should the endpoint return when no history exists?
4. Why should API response models hide internal database details?
5. What history data will the frontend need?
