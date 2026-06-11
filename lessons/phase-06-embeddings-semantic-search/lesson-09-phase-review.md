# Lesson 6.9 — Phase Review

## Goal

Review the embeddings and semantic-search phase and confirm readiness for document chunking and RAG.

## Learning Objectives

By the end of this lesson, you should understand:

- how schema, model, and vector dimensions form one contract
- how embedding, repository, service, API, and UI boundaries interact
- how lexical and semantic retrieval differ
- how tests isolate provider and database dependencies
- which capabilities belong in the next RAG phase

## Estimated Time

2-3 hours

## Tutor Instructions

Codex should act as reviewer and prioritize correctness, migration safety, model consistency, retrieval behavior, tests, documentation, and Phase 7 readiness.

## Tasks

- [ ] Run all backend checks.
- [ ] Run all frontend checks.
- [ ] Review pgvector migrations and note constraints.
- [ ] Review embedding client and model configuration.
- [ ] Review repository, service, and route boundaries.
- [ ] Review keyword and semantic search behavior.
- [ ] Review frontend note and search workflows.
- [ ] Review local setup and comparison documentation.
- [ ] Summarize learning and remaining risks.
- [ ] Ask Codex for final Phase 6 review.

## Acceptance Criteria

- Backend and frontend checks pass.
- Migrations are documented, reversible, and locally verified.
- Notes use `qwen3-embedding:0.6b` with 1024 dimensions.
- Keyword and semantic modes return one typed response shape.
- Tests do not require real PostgreSQL or Ollama by default.
- The app is ready to add documents, chunks, retrieval context, and grounded generation.

## Review Prompt

```txt
Review my completed Phase 6 embeddings and semantic-search work.
Do not rewrite files.
Focus on schema design, model consistency, migrations, boundaries, retrieval correctness, test safety, documentation, and Phase 7 readiness.
Here is my code, structure, and command output:
...
```

## Reflection Questions

1. What contract connects the model, vector dimension, and database schema?
2. Which layer owns provider calls and which owns vector SQL?
3. When does keyword search outperform semantic search?
4. How do tests avoid uncontrolled provider and database dependencies?
5. What additional data model is required for Phase 7 RAG?
