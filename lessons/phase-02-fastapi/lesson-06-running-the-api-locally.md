# Lesson 2.6 — Running the API Locally

## Goal

Run the FastAPI app locally and test it manually through HTTP.

## Learning Objectives

By the end of this lesson, you should understand:

- how to run a FastAPI app with `uvicorn`
- what Swagger UI is
- how to send manual requests to an endpoint
- how manual testing complements automated tests

## Estimated Time

2 hours

## Tutor Instructions

Codex should explain commands and help interpret server or request errors. Codex should not hide failing commands.

## Tasks

- [ ] Add `uvicorn` as a dependency if needed.
- [ ] Run the FastAPI app locally.
- [ ] Open the generated API docs.
- [ ] Send a valid `/analyze` request manually.
- [ ] Send an invalid `/analyze` request manually.
- [ ] Document the local run command in the README.
- [ ] Run `uv run pytest`.
- [ ] Ask Codex for review.

## Acceptance Criteria

- The app runs locally.
- Swagger UI shows the `/analyze` endpoint.
- Manual valid and invalid requests behave as expected.
- The README includes the local run command.
- `uv run pytest` passes.

## Review Prompt

```txt
Review my Lesson 2.6 local API run.
Do not rewrite the README.
Explain whether the command and manual test results make sense.
Here is what I ran and what happened:
...
```

## Reflection Questions

1. What does `uvicorn` do?
2. Why is Swagger UI useful during development?
3. How is manual testing different from automated testing?
4. Why should the README include run instructions?
5. What would you check first if the server starts but the endpoint fails?
