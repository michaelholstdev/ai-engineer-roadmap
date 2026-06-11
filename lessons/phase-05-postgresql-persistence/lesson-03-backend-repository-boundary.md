# Lesson 5.3 — Backend Repository Boundary

## Goal

Create a backend boundary for database access without mixing persistence code into route handlers.

## Learning Objectives

By the end of this lesson, you should understand:

- what a repository boundary is
- why route handlers should not contain raw database details
- how to pass data between routes, services, and persistence code
- how to test persistence-facing code with fakes or controlled dependencies
- how small backend boundaries prepare the app for future features

## Estimated Time

3-4 hours

## Tutor Instructions

Codex should guide the learner toward a small repository abstraction. Codex should discourage over-engineering and generic database frameworks unless needed.

## Tasks

- [ ] Identify where database access should live.
- [ ] Create a small repository module for analysis history.
- [ ] Define typed input/output shapes for stored analysis records.
- [ ] Add tests for repository-facing behavior using a fake or controlled strategy.
- [ ] Keep routes free of raw SQL or database client details.
- [ ] Run backend checks.
- [ ] Ask Codex for review.

## Acceptance Criteria

- Database access has a clear backend boundary.
- Route handlers do not directly own raw persistence details.
- Tests cover the repository-facing behavior.
- Existing API behavior still works.
- The repository design is small and understandable.

## Review Prompt

```txt
Review my Lesson 5.3 backend repository boundary.
Do not rewrite the code.
Focus on separation of concerns, testability, typing, and keeping routes clean.
Here is my code, tests, and command output:
...
```

## Reflection Questions

1. What responsibility does a repository have?
2. Why should route handlers avoid raw database details?
3. What data shape crosses the route-to-repository boundary?
4. How can repository-facing code be tested safely?
5. What would make this boundary too generic or over-engineered?
