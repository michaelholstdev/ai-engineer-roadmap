# Lesson 4.8 — Phase Review

## Goal

Review the React AI UI phase and make sure the full-stack app is understandable, testable, and ready for persistence work.

## Learning Objectives

By the end of this lesson, you should understand:

- how to review a frontend connected to an API
- how to evaluate UI states and error behavior
- how to verify that frontend tests avoid real backends
- how to keep frontend API boundaries maintainable
- how to prepare for adding persistence later

## Estimated Time

2-3 hours

## Tutor Instructions

Codex should act as reviewer. Codex should prioritize user-visible behavior, API boundary clarity, tests, documentation, and readiness for Phase 5.

## Tasks

- [ ] Run frontend checks and tests.
- [ ] Run backend checks and tests.
- [ ] Review frontend project structure.
- [ ] Review API client boundary.
- [ ] Review UI loading, error, empty, and success states.
- [ ] Review README setup instructions.
- [ ] Summarize what you learned.
- [ ] Ask Codex for final Phase 4 review.

## Acceptance Criteria

- Frontend checks pass.
- Backend checks pass.
- The UI can call the backend locally.
- Tests do not require real backend or LLM calls by default.
- README explains the full-stack local workflow.
- The app is ready for a persistence phase.

## Review Prompt

```txt
Review my completed Phase 4 React AI UI work.
Do not rewrite files.
Focus on UI behavior, API boundaries, test safety, documentation, and readiness for Phase 5.
Here is my code, structure, and command output:
...
```

## Reflection Questions

1. What does the frontend do from user input to rendered result?
2. Where does the frontend API boundary live?
3. How do tests avoid real backend or LLM calls?
4. Which UI states are handled clearly?
5. What should be improved before adding persistence?
