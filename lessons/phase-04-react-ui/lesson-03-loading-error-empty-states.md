# Lesson 4.3 — Loading, Error, and Empty States

## Goal

Make the text analyzer UI reliable and understandable across common request states.

## Learning Objectives

By the end of this lesson, you should understand:

- why UI state should be explicit
- how loading, success, error, and idle states differ
- how to avoid duplicate submissions
- how to present API errors without leaking internals
- how empty input should behave in the frontend

## Estimated Time

3-4 hours

## Tutor Instructions

Codex should guide the learner toward clear UI state modeling and practical error handling. Codex should keep the scope limited to the non-AI analyzer flow.

## Tasks

- [ ] Define the possible UI states for the analyzer flow.
- [ ] Show a loading state while a request is running.
- [ ] Disable or protect the submit action during loading.
- [ ] Show a clear error state when the request fails.
- [ ] Handle empty or whitespace-only input intentionally.
- [ ] Manually test success, validation failure, and backend-offline behavior.
- [ ] Ask Codex for review.

## Acceptance Criteria

- Loading state is visible and prevents confusing duplicate actions.
- Error messages are useful but do not expose raw backend internals.
- Empty input is handled before or after the backend validation intentionally.
- Success and error states are visually distinct.
- The UI remains understandable when the backend is offline.

## Review Prompt

```txt
Review my Lesson 4.3 UI states.
Do not rewrite the component.
Focus on loading, error, empty, and success behavior.
Here is my code and the cases I tested:
...
```

## Reflection Questions

1. What UI states does this workflow have?
2. Why should loading be represented explicitly?
3. What should happen if the backend is offline?
4. Should empty input be blocked in the frontend, backend, or both?
5. What error details should not be shown to users?
