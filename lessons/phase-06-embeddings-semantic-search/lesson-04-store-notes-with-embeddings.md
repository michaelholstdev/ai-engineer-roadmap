# Lesson 6.4 — Store Notes with Embeddings

## Goal

Create notes by generating and transactionally storing their embeddings.

## Learning Objectives

By the end of this lesson, you should understand:

- how a service coordinates provider and repository boundaries
- why embedding and persistence form one logical operation
- how typed request, domain, and response models differ
- why raw vectors should not be returned to clients
- how failures prevent partial records

## Estimated Time

4-5 hours

## Tutor Instructions

Codex should guide with TDD. Keep HTTP, orchestration, and SQL responsibilities separate.

## Scope

Implement note creation and `POST /notes`. Search is introduced in later lessons.

## Tasks

- [ ] Add typed note-create domain and response models.
- [ ] Add repository tests for inserting a note with its vector and model name.
- [ ] Implement the notes repository insert operation.
- [ ] Add service tests that coordinate document embedding and persistence.
- [ ] Ensure embedding failures do not execute an insert.
- [ ] Add request validation for non-blank title and content.
- [ ] Add `POST /notes` without exposing the embedding.
- [ ] Map provider and configuration failures to safe HTTP responses.
- [ ] Run backend checks and ask Codex for review.

## Acceptance Criteria

- One successful request creates one note with one embedding.
- The title and content use a deterministic document-embedding format.
- Failed embedding generation does not persist a note.
- Raw embeddings are absent from API responses.
- Routes contain neither raw SQL nor Ollama response parsing.

## Review Prompt

```txt
Review my Lesson 6.4 note-creation workflow.
Do not rewrite files.
Focus on service and repository boundaries, transaction behavior, validation, error mapping, and vector exposure.
Here are my code and test output:
...
```

## Reflection Questions

1. Which layer coordinates embedding generation and persistence?
2. Why should the embedding not appear in the response?
3. What prevents partially created notes?
4. Why should title and content formatting be deterministic?
5. Which errors should result in no database write?
