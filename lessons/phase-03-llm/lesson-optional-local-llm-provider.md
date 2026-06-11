# Optional Lesson 3.x — Local LLM Provider with Ollama

## Goal

Compare the external LLM API integration with a local LLM provider.

## Learning Objectives

By the end of this optional lesson, you should understand:

- how a local LLM provider differs from an external API
- what Ollama provides
- how local models affect latency, privacy, cost, and hardware requirements
- how provider boundaries make swapping implementations easier
- why local models still need testing and error handling

## Estimated Time

3-5 hours

## Tutor Instructions

Codex should treat this as optional enrichment after the main Phase 3 path. Codex should not replace the external API integration with a local-only approach unless the learner explicitly chooses that direction.

## Scope

This lesson should happen after the learner understands the external provider integration, AI client boundary, structured output, and mocked tests.

The goal is not to train a model. The goal is to run or call a local model provider and compare tradeoffs.

## Tasks

- [ ] Install or verify a local LLM provider such as Ollama.
- [ ] Choose a small local model appropriate for the machine.
- [ ] Add a local provider client behind the same AI client boundary.
- [ ] Compare output quality and latency with the external provider.
- [ ] Ensure tests still avoid real provider calls by default.
- [ ] Document how to run the local provider.
- [ ] Ask Codex for review.

## Acceptance Criteria

- The local provider is optional and does not break the external provider path.
- Provider-specific code stays behind a clear boundary.
- Tests do not require Ollama or a downloaded model by default.
- The README or notes explain how to run the local provider manually.
- The learner can explain the tradeoffs between local and external LLM providers.

## Review Prompt

```txt
Review my optional local LLM provider work.
Do not rewrite files.
Focus on provider boundaries, test safety, documentation, and tradeoffs.
Here is my code, setup notes, and tool output:
...
```

## Reflection Questions

1. What are the main benefits of a local LLM provider?
2. What are the main drawbacks of a local LLM provider?
3. Why should tests not require a local model to be installed?
4. How did the AI client boundary make provider swapping easier or harder?
5. When would you choose an external provider over a local provider?
