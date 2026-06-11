# Lesson 6.2 — pgvector Setup and Notes Schema

## Goal

Add pgvector to local PostgreSQL and create the schema for embedded notes.

## Learning Objectives

By the end of this lesson, you should understand:

- how PostgreSQL extensions add database capabilities
- how pgvector stores fixed-dimension vectors
- how schema decisions constrain embedding-model changes
- how Alembic applies reversible schema changes
- why vector indexes should follow correctness and measurement

## Estimated Time

3-4 hours

## Tutor Instructions

Codex should guide migration design and local pgvector setup. The learner should write and apply the migration.

## Scope

Create the database foundation only. Do not call Ollama or expose note routes yet.

## Tasks

- [ ] Choose a PostgreSQL Docker image that includes pgvector.
- [ ] Add the `vector` extension through a new Alembic migration.
- [ ] Create a `notes` table with UUID, title, content, `vector(1024)`, model, and timestamps.
- [ ] Add database constraints for required non-empty note fields where appropriate.
- [ ] Add a reversible downgrade.
- [ ] Apply the migration locally and inspect the resulting schema.
- [ ] Document pgvector startup and migration commands.
- [ ] Run backend checks and ask Codex for review.

## Acceptance Criteria

- Local PostgreSQL exposes the `vector` extension.
- `notes.embedding` uses exactly 1024 dimensions.
- The migration follows the existing revision chain and supports downgrade.
- No approximate vector index is added without a demonstrated need.
- Setup and migration commands are documented.

## Review Prompt

```txt
Review my Lesson 6.2 pgvector setup and notes migration.
Do not rewrite the migration.
Focus on schema constraints, vector dimensions, migration safety, downgrade behavior, and documentation.
Here are my files and command output:
...
```

## Reflection Questions

1. Why is the vector dimension part of the database schema?
2. What happens if a provider returns a vector with the wrong dimension?
3. Why should the extension be enabled through a migration?
4. Why are approximate vector indexes deferred?
5. What must happen to stored notes when the embedding model changes?
