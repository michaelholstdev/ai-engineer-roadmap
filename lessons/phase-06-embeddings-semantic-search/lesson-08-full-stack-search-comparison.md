# Lesson 6.8 — Full-Stack Search Comparison

## Goal

Run the complete stack and compare lexical and semantic retrieval with controlled notes.

## Learning Objectives

By the end of this lesson, you should understand:

- how to verify pgvector, Ollama, backend, and frontend together
- how controlled examples reveal differences between search strategies
- how to diagnose failures by system layer
- why manual relevance evaluation complements automated tests
- what must be documented for reproducible local search

## Estimated Time

3-4 hours

## Tutor Instructions

Codex should guide verification and diagnosis. Avoid changing implementation unless a reproducible issue is found.

## Scope

Verify Phase 6 behavior manually. Do not add document upload, chunking, RAG generation, or reranking.

## Tasks

- [ ] Start pgvector-enabled PostgreSQL and apply migrations.
- [ ] Pull and verify `qwen3-embedding:0.6b`.
- [ ] Start Ollama, FastAPI, and React.
- [ ] Create a documented set of notes with lexical and semantic relationships.
- [ ] Compare keyword and semantic searches using the same queries.
- [ ] Inspect API responses, logs, and stored model metadata.
- [ ] Verify no raw embedding is exposed through the API.
- [ ] Update full-stack setup and troubleshooting documentation.
- [ ] Run all backend and frontend checks.
- [ ] Ask Codex for review.

## Acceptance Criteria

- Notes are persisted with 1024-dimensional embeddings.
- Both search modes work through the React UI.
- Controlled examples demonstrate at least one meaningful ranking difference.
- Setup and verification steps are reproducible.
- Automated checks remain independent of PostgreSQL and Ollama.

## Review Prompt

```txt
Review my Lesson 6.8 full-stack search comparison.
Do not add new features.
Focus on reproducibility, stored model metadata, search behavior, diagnostics, documentation, and verification evidence.
Here are my commands, outputs, and observations:
...
```

## Reflection Questions

1. Which services are required for semantic search?
2. Which controlled example best demonstrated semantic retrieval?
3. How did keyword and semantic rankings differ?
4. How can model or dimension mismatches be diagnosed?
5. Why is manual relevance review still necessary?
