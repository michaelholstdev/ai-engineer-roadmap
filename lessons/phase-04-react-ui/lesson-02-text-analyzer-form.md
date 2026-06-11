# Lesson 4.2 — Text Analyzer Form

## Goal

Build the first frontend workflow for the existing `POST /analyze` backend endpoint.

## Learning Objectives

By the end of this lesson, you should understand:

- how to capture form input in React
- how to send a JSON request from the browser
- how to render a typed backend response
- how frontend behavior maps to a backend API contract
- why the simple analyzer is useful before adding AI output

## Estimated Time

3-4 hours

## Tutor Instructions

Codex should help the learner build the form incrementally. Codex should review component state, fetch behavior, and response rendering without taking over implementation.

## Target Endpoint

Call the existing backend endpoint:

```http
POST /analyze
```

Example request:

```json
{
  "text": "AI Engineering is fun."
}
```

Example response:

```json
{
  "word_count": 4,
  "character_count": 22,
  "sentence_count": 1
}
```

## Tasks

- [ ] Add a text input or textarea.
- [ ] Add a submit action.
- [ ] Send the text to `POST /analyze`.
- [ ] Display word, character, and sentence counts.
- [ ] Keep the UI simple and focused.
- [ ] Test manually against the local FastAPI backend.
- [ ] Ask Codex for review.

## Acceptance Criteria

- The user can enter text and submit it.
- The frontend calls the backend `/analyze` endpoint.
- The response statistics are displayed clearly.
- The UI does not call the AI endpoint yet.
- Manual testing confirms the workflow works locally.

## Review Prompt

```txt
Review my Lesson 4.2 text analyzer UI.
Do not rewrite the component.
Focus on state handling, API usage, and whether the UI matches the backend contract.
Here is my component code and manual test result:
...
```

## Reflection Questions

1. What data does the frontend send to the backend?
2. What data does the backend return?
3. Why start with `/analyze` before `/ai/analyze`?
4. What can go wrong during a browser-to-API request?
5. What should the user see after a successful request?
