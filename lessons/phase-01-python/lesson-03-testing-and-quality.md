# Lesson 1.3 — Testing and Code Quality

## Goal

Learn to use tests, formatting, linting and type checking as feedback tools.

## Learning Objectives

By the end of this lesson, you should understand:

- what a unit test checks
- how to add edge-case tests
- how to run `ruff`
- how to run `mypy`
- how to interpret quality-tool feedback

## Estimated Time

3 hours

## Tutor Instructions

Codex should explain tool output and guide the learner to fix issues themselves.

## Tasks

### Task 1 — Add edge-case tests

Add tests for:

- text with leading and trailing spaces
- text with multiple spaces
- text with punctuation
- empty string

### Task 2 — Run pytest

```bash
uv run pytest
```

### Task 3 — Run ruff

```bash
uv run ruff check .
```

### Task 4 — Run mypy

```bash
uv run mypy src
```

### Task 5 — Review and fix

If a tool reports issues, ask Codex to explain the issue and give hints.

## Acceptance Criteria

- `uv run pytest` passes.
- `uv run ruff check .` passes.
- `uv run mypy src` passes.
- You can explain the difference between tests, linting and type checking.

## Review Prompt

```txt
Review my Lesson 1.3 results.
Do not fix the code for me.
Explain what the tool output means and what I should change.
Here is the output:
...
```

## Reflection Questions

1. What is the difference between a failing test and a linting issue?
2. Why can code pass tests but still fail type checking?
3. What kind of bugs can tests catch that type checking cannot?
4. What kind of bugs can type checking catch before runtime?
5. Why is automated feedback important for AI Engineering projects?
