# Lesson 5.1 — Persistence Concepts and Setup

## Goal

Prepare the project for storing analysis results with PostgreSQL.

## Learning Objectives

By the end of this lesson, you should understand:

- what persistence means in a full-stack application
- why PostgreSQL is useful for AI application history
- how backend code should receive database configuration
- why automated tests should not depend on an uncontrolled local database
- what local setup documentation needs to include

## Estimated Time

2-3 hours

## Tutor Instructions

Codex should explain database concepts and local setup trade-offs. Codex should not implement persistence yet.

## Scope

This lesson prepares the persistence setup. Do not create tables or store analysis results yet.

## Tasks

- [ ] Review what data should eventually be stored.
- [ ] Decide how PostgreSQL will run locally.
- [ ] Add database environment variable documentation.
- [ ] Decide how tests will avoid depending on an uncontrolled real database.
- [ ] Run existing backend and frontend checks.
- [ ] Ask Codex for review.

## Acceptance Criteria

- The local PostgreSQL setup approach is clear.
- Required database environment variables are documented.
- The learner can explain why persistence belongs behind a backend boundary.
- Existing checks still pass.
- The next migration step is clear.

## Review Prompt

```txt
Review my Lesson 5.1 persistence setup.
Do not implement database code.
Focus on setup clarity, environment variables, test safety, and readiness for migrations.
Here are my notes, docs changes, and command output:
...
```

## Reflection Questions

1. What does persistence add to the current app?
2. Which analysis data should eventually be stored?
3. Where should the database connection string be configured?
4. Why should tests avoid depending on an uncontrolled local database?
5. What needs to be documented so another developer can run PostgreSQL locally?
