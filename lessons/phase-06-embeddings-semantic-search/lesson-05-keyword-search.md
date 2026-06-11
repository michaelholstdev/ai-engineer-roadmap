# Lesson 6.5 — Keyword Search

## Goal

Implement PostgreSQL keyword search as a lexical retrieval baseline.

## Learning Objectives

By the end of this lesson, you should understand:

- how lexical search differs from substring matching
- how PostgreSQL tokenizes and ranks searchable text
- how repository code contains search-specific SQL
- how limits and deterministic ordering protect APIs
- why a baseline is needed before evaluating vector search

## Estimated Time

3-4 hours

## Tutor Instructions

Codex should explain PostgreSQL full-text search and guide repository-first TDD.

## Scope

Implement keyword mode only. Do not generate query embeddings in this lesson.

## Tasks

- [ ] Define one typed search-result domain model shared by both future modes.
- [ ] Add failing repository tests for keyword matching, ranking, limit, and empty results.
- [ ] Implement PostgreSQL full-text search across title and content.
- [ ] Return a relevance score and deterministic secondary ordering.
- [ ] Add service and API tests for `mode=keyword`.
- [ ] Validate query text and bounded limits.
- [ ] Return the unified search response shape.
- [ ] Run backend checks and ask Codex for review.

## Acceptance Criteria

- Keyword search executes in PostgreSQL.
- Results are ranked and deterministically ordered.
- Empty matches return an empty list.
- The API uses the shared search-result shape.
- Keyword mode does not call the embedding provider.

## Review Prompt

```txt
Review my Lesson 6.5 keyword-search implementation.
Do not rewrite the query.
Focus on PostgreSQL search behavior, ranking, deterministic ordering, limits, API shape, and tests.
Here are my code and outputs:
...
```

## Reflection Questions

1. How does full-text search differ from `LIKE '%query%'`?
2. What does the keyword relevance score represent?
3. Why does the query need a secondary ordering key?
4. Why must keyword mode avoid the embedding client?
5. What kinds of relevant notes can keyword search miss?
