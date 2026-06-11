# Lesson 3.1 — LLM API Concepts and Setup

## Goal

Prepare the project for an external LLM API integration without making real API calls yet.

## Learning Objectives

By the end of this lesson, you should understand:

- why this phase uses an external LLM API first
- what an API key is and why it must not be committed
- how environment variables protect secrets
- why tests should not call real LLM providers
- what configuration is needed before implementing an AI client

## Estimated Time

1-2 hours

## Tutor Instructions

Codex should explain provider setup, secret handling, and testing boundaries. Codex should not create real API keys, call real LLM APIs, or hardcode secrets.

## Scope

This lesson is a setup and design lesson. Do not implement the `/ai/analyze` endpoint yet.

The project should use an external provider first. Local LLM providers such as Ollama can be added later as an optional comparison lesson.

## Tasks

- [ ] Choose the external LLM provider for this phase.
- [ ] Decide the API key environment variable name.
- [ ] Confirm that `.env` or local secret files are ignored by git.
- [ ] Decide whether to add a safe `.env.example`.
- [ ] Write down why tests must use mocks or fakes instead of real provider calls.
- [ ] Ask Codex for review.

## Acceptance Criteria

- The provider choice is explicit.
- The API key environment variable name is explicit.
- Real secrets are not stored in the repository.
- The learner can explain why tests must not call the real LLM API.
- The next implementation step is clear.

## Review Prompt

```txt
Review my Lesson 3.1 LLM setup decisions.
Do not implement the integration.
Tell me whether the provider choice, environment variable name, and testing boundary are clear.
Here is what I decided:
...
```

## Reflection Questions

1. Why should tests not depend on the real LLM API?
2. Why should API keys be stored in environment variables?
3. What could happen if an API key is committed to git?
4. Why start with an external LLM API before a local model?
5. What setup information does an AI client need before it can make a request?
