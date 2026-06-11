# Lesson 4.5 — React API Client Boundary

## Goal

Move backend request logic out of UI components and into a small typed frontend API client.

## Learning Objectives

By the end of this lesson, you should understand:

- why frontend API boundaries are useful
- how typed request and response shapes improve React code
- how to normalize fetch errors
- how to keep components focused on UI behavior
- how frontend and backend contracts should stay aligned

## Estimated Time

3-4 hours

## Tutor Instructions

Codex should guide the learner through extracting fetch logic incrementally. Codex should prioritize clarity over abstraction.

## Tasks

- [ ] Identify duplicated or component-level fetch logic.
- [ ] Create a small frontend API client module.
- [ ] Add typed functions for `analyzeText` and `analyzeTextWithAI`.
- [ ] Normalize failed responses into a predictable frontend error shape.
- [ ] Update components to use the API client.
- [ ] Manually retest both analyzer workflows.
- [ ] Ask Codex for review.

## Acceptance Criteria

- UI components no longer contain raw endpoint URLs.
- Request and response shapes are typed in frontend code.
- API failures are handled consistently.
- The API client remains small and understandable.
- Both existing workflows still work manually.

## Review Prompt

```txt
Review my Lesson 4.5 React API client boundary.
Do not rewrite the code.
Focus on boundaries, typing, error normalization, and component clarity.
Here is my code and manual test result:
...
```

## Reflection Questions

1. Why should fetch logic move out of UI components?
2. What types should the frontend define for backend responses?
3. What makes an API error shape useful for components?
4. When does an API client abstraction become too complex?
5. How does this boundary compare to the backend AI client boundary?
