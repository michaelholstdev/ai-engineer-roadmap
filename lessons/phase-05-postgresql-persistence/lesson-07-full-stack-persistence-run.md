# Lesson 5.7 — Full-Stack Persistence Run

## Goal

Run the backend, database, optional Ollama provider, and frontend together and verify persistence manually.

## Learning Objectives

By the end of this lesson, you should understand:

- how multiple local services work together
- how to verify that records are stored after API calls
- how to distinguish frontend, backend, database, and provider failures
- how to document a multi-service local workflow
- why manual full-stack verification complements automated tests

## Estimated Time

3-4 hours

## Tutor Instructions

Codex should help diagnose integration issues carefully. Codex should keep the workflow explicit and update documentation only after the learner has verified the flow.

## Tasks

- [x] Start PostgreSQL locally.
- [x] Run migrations.
- [x] Start the FastAPI backend.
- [x] Start the React frontend.
- [x] Manually create normal and AI analysis records.
- [x] Verify records appear in the history view.
- [x] Update README instructions for the persistence workflow.
- [x] Ask Codex for review.

## Acceptance Criteria

- PostgreSQL, backend, and frontend can run together locally.
- Successful analyses are stored.
- Stored analyses appear in the frontend history view.
- README explains the full persistence workflow.
- Manual verification covers normal analysis and AI analysis.

## Review Prompt

```txt
Review my Lesson 5.7 full-stack persistence run.
Do not rewrite files.
Focus on local workflow, migrations, documentation, and manual verification.
Here are my commands, README changes, and browser test results:
...
```

## Reflection Questions

1. Which services need to run for persistence to work?
2. How can you verify that an analysis was actually stored?
3. How can you tell whether a failure is frontend, backend, database, or provider related?
4. What should README instructions include for a multi-service app?
5. What would make this workflow easier to run in the future?
