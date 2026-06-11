# Lesson 5.8 — Phase Review

## Goal

Review the PostgreSQL persistence phase and make sure the app is ready for embeddings and semantic search.

## Learning Objectives

By the end of this lesson, you should understand:

- how to review persistence behavior in a full-stack app
- how database schema choices affect future features
- how to evaluate repository and API boundaries
- how to verify that tests avoid uncontrolled external services
- how persistence prepares the project for semantic search

## Estimated Time

2-3 hours

## Tutor Instructions

Codex should act as reviewer. Codex should prioritize schema clarity, migration safety, API boundaries, test safety, documentation, and readiness for Phase 6.

## Tasks

- [ ] Run backend checks and tests.
- [ ] Run frontend checks and tests.
- [ ] Review migrations and schema design.
- [ ] Review repository boundaries.
- [ ] Review history API and frontend history view.
- [ ] Review README setup instructions.
- [ ] Summarize what you learned.
- [ ] Ask Codex for final Phase 5 review.

## Acceptance Criteria

- Backend checks pass.
- Frontend checks pass.
- Migrations are documented and can be applied locally.
- Analysis history is stored and displayed.
- Tests do not require real LLM calls by default.
- The app is ready for embeddings and semantic search work.

## Review Prompt

```txt
Review my completed Phase 5 PostgreSQL persistence work.
Do not rewrite files.
Focus on schema design, migrations, repository boundaries, API behavior, test safety, documentation, and readiness for Phase 6.
Here is my code, structure, and command output:
...
```

## Reflection Questions

1. What persistence behavior did Phase 5 add?
2. Which backend boundary owns database access?
3. How do migrations make schema changes safer?
4. How do tests avoid uncontrolled database or LLM dependencies?
5. What should be improved before adding embeddings?
