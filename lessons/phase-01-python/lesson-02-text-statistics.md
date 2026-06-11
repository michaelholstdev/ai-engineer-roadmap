# Lesson 1.2 — Text Statistics

## Goal

Implement basic text statistics functions yourself and test them.

## Learning Objectives

By the end of this lesson, you should understand:

- simple Python functions
- type hints
- string methods
- edge cases
- test-driven thinking

## Estimated Time

3-4 hours

## Tutor Instructions

Codex should review learner-written code and provide hints. Codex should not implement the functions unless explicitly asked.

## Functions to Implement

In `src/ai_roadmap/text_stats.py`, implement these functions yourself:

```python
def count_words(text: str) -> int:
    ...


def count_characters(text: str) -> int:
    ...


def count_sentences(text: str) -> int:
    ...
```

## Expected Behavior

### `count_words`

Counts words separated by whitespace.

Examples:

| Input | Expected |
|---|---:|
| `"AI Engineering is fun"` | `4` |
| `""` | `0` |
| `"hello   world"` | `2` |

### `count_characters`

Counts all characters including spaces.

Examples:

| Input | Expected |
|---|---:|
| `"abc"` | `3` |
| `"a b"` | `3` |
| `""` | `0` |

### `count_sentences`

Counts simple sentence endings: `.`, `!`, and `?`.

Examples:

| Input | Expected |
|---|---:|
| `"Hello."` | `1` |
| `"Hello! How are you?"` | `2` |
| `"No punctuation"` | `0` |

## Tasks

- [ ] Write tests for `count_words`.
- [ ] Implement `count_words`.
- [ ] Run tests.
- [ ] Write tests for `count_characters`.
- [ ] Implement `count_characters`.
- [ ] Run tests.
- [ ] Write tests for `count_sentences`.
- [ ] Implement `count_sentences`.
- [ ] Run tests.
- [ ] Ask Codex for review.

## Acceptance Criteria

- All functions have type hints.
- Empty strings are handled correctly.
- Multiple spaces are handled correctly for word counting.
- Tests cover normal cases and edge cases.
- `uv run pytest` passes.

## Review Prompt

```txt
Review my Lesson 1.2 implementation.
Do not rewrite the full solution.
Give me feedback and hints only.
Here is my code and test output:
...
```

## Reflection Questions

1. How does `str.split()` behave with multiple spaces?
2. Why should tests include empty strings?
3. What is an edge case?
4. Why are type hints useful even if Python is dynamically typed?
5. What would make `count_sentences` more difficult in real production text?

## Hint Bank

### Hint 1

Start by writing one test for the simplest normal case.

### Hint 2

For word counting, check what `"hello   world".split()` returns.

### Hint 3

For sentence counting, you can inspect each character and count punctuation marks.

### Hint 4

A production-grade sentence counter is harder because abbreviations like `Dr.` and decimals like `3.14` exist. For this lesson, keep it simple.
