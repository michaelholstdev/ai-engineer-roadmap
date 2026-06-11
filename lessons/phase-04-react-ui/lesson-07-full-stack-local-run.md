# Lesson 4.7 — Full-Stack Local Run

## Goal

Run the React frontend and FastAPI backend together locally and document the workflow.

## Learning Objectives

By the end of this lesson, you should understand:

- how the browser reaches a local backend
- why CORS can appear in full-stack local development
- how to run two development servers together
- how to document local setup clearly
- how to manually verify full-stack behavior

## Estimated Time

3-4 hours

## Tutor Instructions

Codex should help the learner diagnose local integration issues carefully. Codex should only add CORS if the browser requires it.

## Tasks

- [ ] Start the FastAPI backend locally.
- [ ] Start the React frontend locally.
- [ ] Use the browser to call `/analyze` through the UI.
- [ ] Use the browser to call `/ai/analyze` through the UI.
- [ ] Identify whether CORS configuration is needed.
- [ ] Update README instructions for the full-stack local workflow.
- [ ] Ask Codex for review.

## Acceptance Criteria

- Backend and frontend can run at the same time.
- The browser UI can reach the FastAPI backend.
- CORS is handled intentionally if needed.
- README explains how to run the full stack locally.
- Manual verification covers both analyzer workflows.

## Review Prompt

```txt
Review my Lesson 4.7 full-stack local run.
Do not rewrite files.
Focus on local workflow, CORS, documentation, and manual verification.
Here are my commands, README changes, and browser test results:
...
```

## Reflection Questions

1. What servers need to run for the full-stack app?
2. Why does CORS happen in browser-based apps?
3. How can you tell whether a failure is frontend, backend, or network related?
4. What should README instructions include for local development?
5. What would make this workflow easier for future contributors?
