# Lesson 5.6 — Frontend History View

## Goal

Show stored analysis history in the React frontend.

## Learning Objectives

By the end of this lesson, you should understand:

- how the frontend loads persisted backend data
- how to extend the frontend API client safely
- how to render history records with clear empty, loading, success, and error states
- how to test history UI without a real backend
- how persisted history changes the user experience

## Estimated Time

3-4 hours

## Tutor Instructions

Codex should guide the learner through a simple history view. Codex should prioritize clear UI state and API boundary tests over visual polish.

## Tasks

- [x] Add a typed frontend API client function for history.
- [x] Render a history section in the React UI.
- [x] Show empty history clearly.
- [x] Show loading and error states for history loading.
- [x] Add frontend tests for history behavior.
- [x] Run frontend checks.
- [x] Ask Codex for review.

## Acceptance Criteria

- The frontend can request stored analysis history.
- History records render in the UI.
- Empty, loading, success, and error states are handled.
- Frontend tests do not require the real backend.
- API request details stay inside the frontend API client.

## Review Prompt

```txt
Review my Lesson 5.6 frontend history view.
Do not rewrite the code.
Focus on UI behavior, API client boundaries, test safety, and user-visible states.
Here is my code, tests, and command output:
...
```

## Reflection Questions

1. When should the frontend load history?
2. Which history fields are useful to show first?
3. What should users see when history is empty?
4. How do tests avoid calling the real backend?
5. What should stay inside the frontend API client?
