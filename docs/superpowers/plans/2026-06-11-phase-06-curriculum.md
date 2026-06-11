# Phase 6 Curriculum Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a complete nine-lesson Phase 6 curriculum for pgvector-backed note embeddings, keyword search, semantic search, and a React search workflow.

**Architecture:** The curriculum follows the approved Phase 6 design and the established lesson format. Concepts and schema decisions come first, backend boundaries and search behavior follow, and frontend/full-stack verification complete the phase without introducing Phase 7 document chunking.

**Tech Stack:** Markdown, PostgreSQL, pgvector, Alembic, FastAPI, SQLAlchemy, Ollama, `qwen3-embedding:0.6b`, React, Vitest

---

### Task 1: Add Phase 6 Lesson Files

**Files:**
- Create: `lessons/phase-06-embeddings-semantic-search/lesson-01-embedding-and-vector-search-concepts.md`
- Create: `lessons/phase-06-embeddings-semantic-search/lesson-02-pgvector-setup-and-notes-schema.md`
- Create: `lessons/phase-06-embeddings-semantic-search/lesson-03-embedding-client-boundary.md`
- Create: `lessons/phase-06-embeddings-semantic-search/lesson-04-store-notes-with-embeddings.md`
- Create: `lessons/phase-06-embeddings-semantic-search/lesson-05-keyword-search.md`
- Create: `lessons/phase-06-embeddings-semantic-search/lesson-06-semantic-search.md`
- Create: `lessons/phase-06-embeddings-semantic-search/lesson-07-notes-and-search-ui.md`
- Create: `lessons/phase-06-embeddings-semantic-search/lesson-08-full-stack-search-comparison.md`
- Create: `lessons/phase-06-embeddings-semantic-search/lesson-09-phase-review.md`

- [ ] Give every lesson a concrete goal, learning objectives, scope, TDD-oriented tasks, acceptance criteria, review prompt, and reflection questions.
- [ ] Keep `analysis_runs` separate from the new `notes` model.
- [ ] Fix the embedding model at `qwen3-embedding:0.6b` and the vector dimension at 1024.
- [ ] Keep document upload and chunking outside Phase 6.

### Task 2: Update Curriculum Trackers

**Files:**
- Modify: `ROADMAP.md`
- Modify: `TASKS.md`
- Modify: `PROGRESS.md`

- [ ] Add the nine Phase 6 lessons to the roadmap.
- [ ] Set Phase 6 and Lesson 6.1 as the current work in `TASKS.md`.
- [ ] Add upcoming task checklists for Lessons 6.2 through 6.9.
- [ ] Add a Phase 6 preparation entry to `PROGRESS.md` referencing the approved architecture.

### Task 3: Verify and Commit

**Files:**
- Verify: all files from Tasks 1 and 2

- [ ] Check that all nine lesson files exist and are referenced by `ROADMAP.md` and `TASKS.md`.
- [ ] Search for stale embedding-model references in Phase 6 artifacts.
- [ ] Check Markdown changes for whitespace errors and unresolved placeholders.
- [ ] Review the complete diff for Phase 7 scope leakage.
- [ ] Commit the curriculum package with a focused commit message.
