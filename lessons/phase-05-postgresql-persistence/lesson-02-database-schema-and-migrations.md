# Lesson 5.2 — Database Schema and Migrations

## Goal

Design the first database schema and create a migration for stored analysis results.

## Learning Objectives

By the end of this lesson, you should understand:

- how to model analysis history as database rows
- why migrations are safer than manual schema changes
- which fields belong in an analysis history table
- how timestamps help debug and sort stored records
- how schema choices affect future features such as embeddings

## Estimated Time

3-4 hours

## Tutor Instructions

Codex should guide schema design carefully and review the migration before the learner applies it. Codex should keep the first schema small.

## Tasks

- [ ] Choose a migration tool or migration workflow.
- [ ] Design an `analysis_runs` table.
- [ ] Include fields for input text, result type, statistics, AI output, provider, and timestamps.
- [ ] Create the first migration.
- [ ] Apply the migration locally.
- [ ] Document how to run migrations.
- [ ] Ask Codex for review.

## Acceptance Criteria

- A migration exists for the first persistence table.
- The schema supports both normal text analysis and AI analysis history.
- The schema avoids storing secrets.
- The migration can be applied locally.
- The learner can explain each table field.

## Review Prompt

```txt
Review my Lesson 5.2 database schema and migration.
Do not rewrite the migration.
Focus on table design, migration safety, stored fields, and readiness for backend integration.
Here is my migration, schema explanation, and command output:
...
```

## Reflection Questions

1. Why use migrations instead of changing the database manually?
2. Which fields are required for normal analysis history?
3. Which fields are required for AI analysis history?
4. Which data should never be stored in this table?
5. How could this schema support embeddings later?
