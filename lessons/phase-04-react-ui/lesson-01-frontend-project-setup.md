# Lesson 4.1 — Frontend Project Setup

## Goal

Create a React and TypeScript frontend that can later call the FastAPI backend.

## Learning Objectives

By the end of this lesson, you should understand:

- where the frontend belongs in the repository
- how a React development server works
- how frontend code will find the backend API URL
- how to keep frontend setup separate from backend implementation
- what basic project files should be committed

## Estimated Time

2-3 hours

## Tutor Instructions

Codex should guide the learner through frontend setup decisions and review the generated project structure. Codex should not build the UI features yet.

## Scope

This lesson only sets up the frontend project. Do not implement calls to `/analyze` or `/ai/analyze` yet.

## Tasks

- [ ] Choose the frontend project location.
- [ ] Create a React + TypeScript frontend project.
- [ ] Start the frontend development server.
- [ ] Decide how the frontend will configure the backend API base URL.
- [ ] Add or update README instructions for running the frontend.
- [ ] Run the frontend's default checks if available.
- [ ] Ask Codex for review.

## Acceptance Criteria

- A React + TypeScript frontend project exists.
- The frontend development server starts locally.
- The backend API base URL strategy is explicit.
- Generated dependencies and lockfiles are understood.
- The next UI implementation step is clear.

## Review Prompt

```txt
Review my Lesson 4.1 frontend setup.
Do not implement the UI.
Tell me whether the project structure, scripts, and API base URL plan are clear.
Here is my file structure and command output:
...
```

## Reflection Questions

1. Why should frontend setup be completed before building UI features?
2. Where should API base URLs be configured in a frontend app?
3. Which generated files should be committed?
4. Which generated files should stay ignored?
5. How will the React app eventually communicate with FastAPI?
