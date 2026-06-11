# Lesson 1.1 — Project Setup

## Goal

Create a clean Python project structure for future AI Engineering lessons.

In this lesson, the learner creates the files manually. Codex acts only as tutor and reviewer.

## Learning Objectives

By the end of this lesson, you should understand:

- why Python projects often use a `src/` layout
- what `pyproject.toml` is used for
- how to add development dependencies
- how to run tests with `pytest`
- how to ask for code review without asking for implementation

## Estimated Time

2-3 hours

## Tutor Instructions

Codex should:

- explain each step before the learner performs it
- ask the learner to run commands
- wait for output
- review the created structure
- not create files automatically unless explicitly requested

## Tasks

### Task 1 — Check local tools

Run these commands:

```bash
python --version
git --version
uv --version
```

If `uv` is not installed, install it with the method appropriate for your system.

### Task 2 — Create the project folder

Create this structure manually:

```txt
ai-engineer-roadmap/
  phase-01-python/
```

### Task 3 — Initialize the Python project

Inside `phase-01-python`, initialize the project.

Recommended:

```bash
uv init
```

Then add development tools:

```bash
uv add --dev pytest ruff mypy
```

### Task 4 — Create the source and test structure

Create:

```txt
phase-01-python/
  src/
    ai_roadmap/
      __init__.py
      text_stats.py
  tests/
    test_text_stats.py
```

### Task 5 — Add a minimal test

Write a tiny test yourself. It can be a placeholder test for now.

Do not ask Codex to write it. If stuck, ask for a Level 1 or Level 2 hint.

### Task 6 — Run tests

Run:

```bash
uv run pytest
```

Paste the output to Codex for review.

## Acceptance Criteria

- The project has a `src/` layout.
- `pytest`, `ruff`, and `mypy` are installed as dev dependencies.
- `uv run pytest` runs successfully.
- You can explain what `src/`, `tests/`, and `pyproject.toml` are for.

## Review Prompt

Use this prompt after you finish:

```txt
Review my setup for Lesson 1.1.
Do not rewrite files.
Tell me what looks correct, what is missing and what I should fix myself.
Here is my folder structure and test output:
...
```

## Reflection Questions

Answer these before moving on:

1. What is the purpose of `pyproject.toml`?
2. Why do we separate `src/` and `tests/`?
3. What does `uv run pytest` do?
4. What are dev dependencies?
5. What would you check first if pytest cannot import your package?

## Hint Bank

### Hint 1

The project should be importable as a package, not only as loose scripts.

### Hint 2

The `src/` layout helps avoid accidentally importing from the current working directory instead of the installed package.

### Hint 3

If imports fail, check package name, folder structure, and whether the project is installed correctly in the environment.
