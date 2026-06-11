# Lesson 5.4 — Store Analysis Results

## Goal

Store successful analysis results when users call the existing backend endpoints.

## Learning Objectives

By the end of this lesson, you should understand:

- where persistence fits into the existing request flow
- why failed requests should usually not be stored as successful history
- how to store normal analysis and AI analysis results consistently
- how to keep endpoint responses stable while adding persistence
- how to test storage behavior without making tests brittle

## Estimated Time

3-4 hours

## Tutor Instructions

Codex should guide the learner through adding storage behavior without changing the public response shape unless intentionally required.

## Tasks

- [ ] Store successful `/analyze` results.
- [ ] Store successful `/ai/analyze` results.
- [ ] Do not store validation failures.
- [ ] Do not store provider failures as successful history records.
- [ ] Add backend tests for storage behavior.
- [ ] Run backend checks.
- [ ] Ask Codex for review.

## Acceptance Criteria

- Successful normal analysis requests are persisted.
- Successful AI analysis requests are persisted.
- Existing endpoint response shapes remain stable.
- Failed requests are handled intentionally.
- Tests verify persistence behavior without requiring real provider calls.

## Review Prompt

```txt
Review my Lesson 5.4 result storage.
Do not rewrite the code.
Focus on request flow, stored data, failure behavior, response stability, and test safety.
Here is my code, tests, and command output:
...
```

## Reflection Questions

1. Where does storage happen in the request flow?
2. Why should successful response shape stay stable?
3. Which failures should not create successful history rows?
4. How do tests verify storage without calling the real LLM provider?
5. What information is useful to store for future debugging?
