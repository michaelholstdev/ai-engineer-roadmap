# Lesson 6.1 — Embedding and Vector Search Concepts

## Goal

Design the semantic-search domain before adding pgvector or embedding code.

## Learning Objectives

By the end of this lesson, you should understand:

- how embeddings represent text as numeric vectors
- why vector dimensions must remain consistent
- how cosine distance differs from keyword matching
- why analysis history and searchable notes need separate models
- why changing an embedding model requires re-embedding stored content

## Estimated Time

2-3 hours

## Tutor Instructions

Codex should explain embedding and retrieval concepts and review architecture decisions. Codex should not implement pgvector or provider calls yet.

## Scope

Define the Phase 6 data flow and boundaries. Do not create migrations, API routes, or frontend components yet.

## Tasks

- [ ] Compare keyword matching with semantic similarity using concrete examples.
- [ ] Define the responsibilities of notes, embeddings, and search results.
- [ ] Record `qwen3-embedding:0.6b` as the embedding model.
- [ ] Record 1024 as the required vector dimension.
- [ ] Decide how document text and instructed search queries differ.
- [ ] Run the existing backend and frontend checks.
- [ ] Ask Codex for review.

## Acceptance Criteria

- `analysis_runs` remains separate from searchable notes.
- The embedding model and vector dimension are explicit.
- The learner can explain cosine distance and model consistency.
- Document chunking remains outside Phase 6.
- Existing checks pass.

## Review Prompt

```txt
Review my Lesson 6.1 embedding and vector-search design.
Do not implement code.
Focus on domain boundaries, model consistency, dimensions, similarity, and Phase 7 scope.
Here are my decisions and command output:
...
```

## Reflection Questions

1. What information does an embedding preserve that keyword matching may miss?
2. Why must stored and query embeddings use the same model and dimensions?
3. Why should notes not be stored in `analysis_runs`?
4. What does a smaller cosine distance mean?
5. Why is chunking deferred until Phase 7?
