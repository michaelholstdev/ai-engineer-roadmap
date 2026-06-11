# Lesson 4.4 — AI Analyze UI

## Goal

Add a frontend workflow for structured AI analysis using `POST /ai/analyze`.

## Learning Objectives

By the end of this lesson, you should understand:

- how structured AI output maps to UI elements
- how AI errors differ from simple validation errors
- how to display sentiment, topics, and action items
- why frontend code should not assume AI output is free-form text
- how to keep the AI workflow understandable for users

## Estimated Time

4-5 hours

## Tutor Instructions

Codex should help the learner extend the UI from text statistics to structured AI output. Codex should review data rendering, error behavior, and frontend assumptions.

## Target Endpoint

Call the existing backend endpoint:

```http
POST /ai/analyze
```

Expected response shape:

```json
{
  "summary": "Short summary",
  "sentiment": "neutral",
  "topics": ["ai", "engineering"],
  "action_items": []
}
```

## Tasks

- [ ] Add a UI action for AI analysis.
- [ ] Call `POST /ai/analyze`.
- [ ] Display `summary`.
- [ ] Display `sentiment`.
- [ ] Display `topics` as a list.
- [ ] Display `action_items` as a list.
- [ ] Handle backend AI errors intentionally.
- [ ] Ask Codex for review.

## Acceptance Criteria

- The frontend can call `/ai/analyze`.
- Structured AI response fields are displayed separately.
- Empty lists render cleanly.
- AI provider errors are shown as controlled UI errors.
- The implementation does not require a real LLM call in frontend tests.

## Review Prompt

```txt
Review my Lesson 4.4 AI analyze UI.
Do not rewrite the component.
Focus on structured output rendering, error behavior, and frontend assumptions.
Here is my code and manual test output:
...
```

## Reflection Questions

1. Why is structured AI output easier to render than free-form text?
2. How should empty `topics` or `action_items` be displayed?
3. What should users see when the AI provider fails?
4. What assumptions does the frontend make about sentiment values?
5. How could this UI change when streaming is added later?
