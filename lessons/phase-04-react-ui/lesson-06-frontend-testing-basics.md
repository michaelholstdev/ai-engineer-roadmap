# Lesson 4.6 — Frontend Testing Basics

## Goal

Add focused frontend tests for rendering, form behavior, and API interaction without requiring the real backend.

## Learning Objectives

By the end of this lesson, you should understand:

- what frontend tests should verify
- how to test user-visible behavior
- why tests should fake backend calls
- how frontend tests differ from backend tests
- how to keep tests useful without overfitting implementation details

## Estimated Time

4-5 hours

## Tutor Instructions

Codex should help the learner choose small, behavior-focused tests. Codex should discourage brittle tests that assert implementation details.

## Tasks

- [ ] Add frontend testing tools if they are not present.
- [ ] Test that the analyzer form renders.
- [ ] Test that submitting text calls the API client.
- [ ] Test that successful statistics render.
- [ ] Test one error state.
- [ ] Fake API calls instead of using the real backend.
- [ ] Run frontend tests.
- [ ] Ask Codex for review.

## Acceptance Criteria

- Frontend tests run locally.
- Tests do not require FastAPI to be running.
- Tests focus on user-visible behavior.
- At least one success and one error path are covered.
- The learner can explain what the tests do and do not prove.

## Review Prompt

```txt
Review my Lesson 4.6 frontend tests.
Do not rewrite them.
Focus on whether the tests verify useful behavior without depending on the real backend.
Here are my tests and command output:
...
```

## Reflection Questions

1. What behavior should frontend tests verify?
2. Why should frontend tests not call the real backend by default?
3. What is the difference between testing a component and testing an API client?
4. What makes a frontend test brittle?
5. Which important behavior is still only manually tested?
