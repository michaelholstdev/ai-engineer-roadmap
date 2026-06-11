# Lesson 3.5 — Mocking External API Calls

## Goal

Test AI-powered behavior without calling the real LLM provider.

## Learning Objectives

By the end of this lesson, you should understand:

- why tests should be deterministic
- how fakes and mocks replace external services
- how to test success and failure cases
- how to avoid accidental network calls in tests

## Estimated Time

3 hours

## Tutor Instructions

Codex should explain test doubles and review the learner's test design. Codex should not use the real provider in tests.

## Tasks

- [ ] Identify where the real provider call is made.
- [ ] Replace it in tests with a fake or mock.
- [ ] Test a successful AI response.
- [ ] Test a provider failure.
- [ ] Test invalid provider output if applicable.
- [ ] Run `uv run pytest`.
- [ ] Run `uv run ruff check .`.
- [ ] Ask Codex for review.

## Acceptance Criteria

- Tests never require a real API key.
- Tests never make real network calls.
- Success and failure cases are covered.
- Test setup is understandable.
- `pytest` and `ruff` pass.

## Review Prompt

```txt
Review my Lesson 3.5 mocked AI tests.
Do not rewrite the tests.
Tell me whether the mocks are clear and whether any real network call could still happen.
Here is my test code and output:
...
```

## Reflection Questions

1. Why are real LLM calls bad for automated tests?
2. What is the difference between a fake and a mock?
3. What makes a mocked test trustworthy?
4. What are the risks of over-mocking?
5. How can tests prove that failure cases are handled?
