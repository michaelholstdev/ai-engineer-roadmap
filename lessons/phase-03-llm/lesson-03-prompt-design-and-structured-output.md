# Lesson 3.3 — Prompt Design and Structured Output

## Goal

Design the prompt and response shape for an AI-powered text analysis result.

## Learning Objectives

By the end of this lesson, you should understand:

- how prompts define task instructions
- why structured output is easier to consume than free text
- how Pydantic models can validate AI output
- why LLM responses should be treated as untrusted data

## Estimated Time

3-4 hours

## Tutor Instructions

Codex should explain prompt design and structured output tradeoffs. Codex should review the learner's schema and prompt design without calling a real LLM.

## Target Output

Design a structured response similar to:

```json
{
  "summary": "...",
  "sentiment": "neutral",
  "topics": ["ai", "engineering"],
  "action_items": []
}
```

## Tasks

- [ ] Define the AI response fields.
- [ ] Add Pydantic models for structured AI output.
- [ ] Draft a prompt that asks for those fields.
- [ ] Decide allowed sentiment values.
- [ ] Add tests for validating structured output.
- [ ] Run `uv run pytest`.
- [ ] Run `uv run ruff check .`.
- [ ] Run `uv run mypy src`.
- [ ] Ask Codex for review.

## Acceptance Criteria

- The output schema is explicit.
- The prompt asks for structured data.
- Invalid AI output can be detected.
- Tests do not call the real provider.
- `pytest`, `ruff`, and `mypy` pass.

## Review Prompt

```txt
Review my Lesson 3.3 prompt and structured output design.
Do not rewrite the full prompt.
Tell me whether the schema is clear and whether the prompt supports it.
Here is my code, prompt draft, and tool output:
...
```

## Reflection Questions

1. Why is structured output easier for an API than free-form text?
2. Why should AI output be validated?
3. What makes a prompt too vague?
4. Why should allowed values such as sentiment be constrained?
5. What could still go wrong even with a clear prompt?
