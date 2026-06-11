# Tasks

This file tracks the current learning tasks. You, the learner, implement the code. Codex reviews and guides.

## Current Phase

Phase 5 — PostgreSQL and Persistence

## Current Lesson

Lesson 5.1 — Persistence Concepts and Setup

## Active Tasks

### Lesson 5.1 — Persistence Concepts and Setup

- [ ] Review what data should eventually be stored.
- [ ] Decide how PostgreSQL will run locally.
- [ ] Add database environment variable documentation.
- [ ] Decide how tests will avoid depending on an uncontrolled real database.
- [ ] Run existing backend and frontend checks.
- [ ] Ask Codex for review.

## Upcoming Tasks

### Lesson 5.2 — Database Schema and Migrations

- [ ] Choose a migration tool or migration workflow.
- [ ] Design an `analysis_runs` table.
- [ ] Create and apply the first migration.
- [ ] Document how to run migrations.
- [ ] Ask Codex for review.

### Lesson 5.3 — Backend Repository Boundary

- [ ] Create a small repository module for analysis history.
- [ ] Define typed input/output shapes for stored records.
- [ ] Keep routes free of raw database details.
- [ ] Add tests for repository-facing behavior.
- [ ] Ask Codex for review.

### Lesson 5.4 — Store Analysis Results

- [ ] Store successful `/analyze` results.
- [ ] Store successful `/ai/analyze` results.
- [ ] Avoid storing validation or provider failures as successful records.
- [ ] Add backend tests for storage behavior.
- [ ] Ask Codex for review.

### Lesson 5.5 — History API Endpoint

- [ ] Add a typed response model for history records.
- [ ] Add a history list endpoint.
- [ ] Return newest records first with a small limit strategy.
- [ ] Add backend tests for empty and non-empty history.
- [ ] Ask Codex for review.

### Lesson 5.6 — Frontend History View

- [ ] Add a typed frontend API client function for history.
- [ ] Render a history section in the React UI.
- [ ] Handle empty, loading, success, and error states.
- [ ] Add frontend tests for history behavior.
- [ ] Ask Codex for review.

### Lesson 5.7 — Full-Stack Persistence Run

- [ ] Start PostgreSQL locally.
- [ ] Run migrations.
- [ ] Start backend and frontend.
- [ ] Verify stored records appear in the history view.
- [ ] Update README instructions for the persistence workflow.
- [ ] Ask Codex for review.

### Lesson 5.8 — Phase Review

- [ ] Run backend checks.
- [ ] Run frontend checks.
- [ ] Review schema, migrations, repository boundaries, API behavior, tests, and docs.
- [ ] Summarize what you learned.

## Rules

- Do not ask Codex to implement the whole lesson.
- Ask for hints first.
- Ask for full solutions only after you have tried seriously.
- Keep code and documentation in English.


## Global Tutor Rule

- Codex should guide, review and explain in German.
- The learner writes the implementation code.
- Repository artifacts stay in English.
