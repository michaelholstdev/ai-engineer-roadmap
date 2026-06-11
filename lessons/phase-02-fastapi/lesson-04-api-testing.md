# Lesson 2.4 — API Testing

## Goal

Improve API tests so they are readable, focused, and cover both success and failure cases.

## Learning Objectives

By the end of this lesson, you should understand:

- how `TestClient` simulates HTTP requests
- how to write focused endpoint tests
- how to reduce repeated test code with parametrization
- how to test status codes and JSON response bodies

## Estimated Time

2-3 hours

## Tutor Instructions

Codex should review test design, naming, and coverage. Codex should guide the learner toward readable tests instead of generating the full test file.

## Tasks

- [ ] Review the current API tests.
- [ ] Identify repeated patterns.
- [ ] Add or refactor tests with `pytest.mark.parametrize` where useful.
- [ ] Keep one test focused on one behavior.
- [ ] Run `uv run pytest`.
- [ ] Run `uv run ruff check .`.
- [ ] Ask Codex for review.

## Acceptance Criteria

- API tests cover valid input.
- API tests cover invalid input.
- Test names describe behavior clearly.
- Repetition is reduced where it improves readability.
- `uv run pytest` passes.
- `uv run ruff check .` passes.

## Review Prompt

```txt
Review my Lesson 2.4 API tests.
Do not rewrite the full test file.
Tell me where the tests are clear and where they could be simpler.
Here is my test code and output:
...
```

## Reflection Questions

1. What does `TestClient` let you test without running a real server?
2. When is parametrization useful?
3. When can parametrization make tests harder to read?
4. Why should test names describe behavior?
5. What makes an API test trustworthy?
