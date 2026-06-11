# Lesson 6.3 — Embedding Client Boundary

## Goal

Create a typed backend boundary for generating local embeddings with Ollama.

## Learning Objectives

By the end of this lesson, you should understand:

- how an embedding provider differs from a text-generation provider
- how to call Ollama's `/api/embed` endpoint
- how to validate nested provider responses
- how provider errors become application-specific errors
- why provider calls must be replaceable in tests

## Estimated Time

3-4 hours

## Tutor Instructions

Codex should use TDD and progressive hints. Tests must not contact Ollama.

## Scope

Implement and test the embedding client. Do not persist notes or add API routes yet.

## Tasks

- [ ] Add failing tests for valid, missing, malformed, non-finite, and wrong-sized embeddings.
- [ ] Define model, dimension, endpoint, timeout, and retrieval-instruction configuration.
- [ ] Implement a typed `qwen3-embedding:0.6b` Ollama request.
- [ ] Parse exactly one 1024-dimensional vector from the response.
- [ ] Add separate document and query embedding functions.
- [ ] Add the stable English retrieval instruction only to query inputs.
- [ ] Convert request, HTTP-status, and response-validation failures into embedding errors.
- [ ] Run backend checks and ask Codex for review.

## Acceptance Criteria

- Valid responses return `list[float]` with exactly 1024 finite values.
- Query and document inputs are formatted intentionally.
- Provider transport details do not leak into routes.
- Tests mock `httpx` and do not require Ollama.
- Backend checks pass.

## Review Prompt

```txt
Review my Lesson 6.3 Ollama embedding-client boundary.
Do not rewrite the solution.
Focus on request shape, query instructions, vector validation, errors, mocks, and configuration.
Here are my code and test results:
...
```

## Reflection Questions

1. Why is the provider response a nested list of embeddings?
2. Why must vectors contain only finite numbers?
3. Why do queries use an instruction while stored notes do not?
4. Which failures should be retryable?
5. Why should routes not call `httpx` directly?
