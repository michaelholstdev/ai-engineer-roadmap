# Lesson 6.6 — Semantic Search

## Goal

Implement semantic note retrieval with query embeddings and pgvector cosine distance.

## Learning Objectives

By the end of this lesson, you should understand:

- how query embeddings are compared with stored vectors
- how pgvector expresses cosine distance
- how distance can be converted into a user-facing relevance score
- why model and dimension consistency are mandatory
- how semantic and keyword scores differ

## Estimated Time

4-5 hours

## Tutor Instructions

Codex should guide with TDD and keep provider orchestration out of repository code.

## Scope

Add semantic mode to the existing search endpoint. Do not add reranking or approximate indexes.

## Tasks

- [ ] Add repository tests for cosine-distance ordering and bounded results.
- [ ] Implement exact semantic search with pgvector.
- [ ] Add service tests that generate one instructed query embedding.
- [ ] Reject invalid query vectors before executing search SQL.
- [ ] Add API tests for `mode=semantic`, defaults, empty results, and provider failures.
- [ ] Convert distance into a documented relevance score.
- [ ] Confirm both modes use the same response model.
- [ ] Run backend checks and ask Codex for review.

## Acceptance Criteria

- Semantic search uses the instructed query embedding.
- Stored notes and queries use the same model and 1024 dimensions.
- Results are ordered from closest to furthest.
- Provider failures do not execute semantic SQL.
- No approximate index or reranker is introduced.

## Review Prompt

```txt
Review my Lesson 6.6 semantic-search implementation.
Do not rewrite files.
Focus on query embeddings, cosine distance, score semantics, repository boundaries, validation, and error handling.
Here are my code and test results:
...
```

## Reflection Questions

1. What is the difference between cosine distance and cosine similarity?
2. Why does semantic search need an embedding-provider call?
3. Why can keyword and semantic scores not be compared directly?
4. What would happen if query vectors used another model?
5. When would an approximate vector index become useful?
