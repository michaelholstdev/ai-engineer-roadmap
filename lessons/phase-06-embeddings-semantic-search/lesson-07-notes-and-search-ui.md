# Lesson 6.7 — Notes and Search UI

## Goal

Build React workflows for creating notes and comparing keyword with semantic search.

## Learning Objectives

By the end of this lesson, you should understand:

- how frontend API types model note and search responses
- how separate forms manage independent asynchronous state
- how a segmented control communicates search mode
- how shared result components keep comparisons consistent
- how frontend tests isolate the API-client boundary

## Estimated Time

5-6 hours

## Tutor Instructions

Codex should guide frontend work with component-first TDD and preserve existing UI conventions.

## Scope

Add note creation and search to the existing app. Do not redesign unrelated analysis-history features.

## Tasks

- [ ] Add typed API-client functions for note creation and search.
- [ ] Test request paths, bodies, query parameters, and error conversion.
- [ ] Build a note form with title and content validation.
- [ ] Add note creation loading, success, and error states.
- [ ] Build a search form with query, keyword/semantic mode, and bounded limit.
- [ ] Use a segmented control for search mode.
- [ ] Render both modes with one result-list component.
- [ ] Add loading, empty, success, and error tests for search.
- [ ] Run frontend checks and ask Codex for review.

## Acceptance Criteria

- Notes can be created without a page reload.
- Search requests send the selected mode and limit.
- Keyword and semantic results share the same presentation.
- The UI does not imply that mode scores are directly comparable.
- Frontend tests require neither backend nor Ollama.

## Review Prompt

```txt
Review my Lesson 6.7 React notes and search UI.
Do not redesign the complete application.
Focus on component boundaries, accessible controls, async states, API-client types, result consistency, and tests.
Here are my files and command output:
...
```

## Reflection Questions

1. Why should note creation and search have separate loading states?
2. Why is a segmented control appropriate for the search mode?
3. Which logic belongs in the API client rather than components?
4. Why should both modes use the same result component?
5. How do tests avoid contacting the real backend?
