# Full-Stack AI Engineer Learning Repository

This repository is designed as a guided learning path for becoming a Full-Stack AI Engineer.

The goal is not to let an AI assistant write the code for you. The goal is to help you learn by writing the code yourself, running tests, receiving feedback, and iterating.

## Learning Mode

Use Codex or another AI coding assistant as a tutor and reviewer.

The assistant should:

- explain the current lesson
- break tasks into small steps
- review your code
- explain test failures
- give progressive hints
- ask understanding questions
- update progress after you complete work

The assistant should not:

- implement lesson code for you by default
- generate full solution files unless explicitly asked
- silently fix bugs
- skip learning checkpoints

## Recommended Workflow

1. Read `CODEX.md`.
2. Start with `ROADMAP.md`.
3. Open the current lesson file.
4. Ask Codex to guide you through the lesson as a tutor.
5. Write the code yourself.
6. Run tests locally.
7. Ask Codex to review your implementation.
8. Update `PROGRESS.md` after the lesson is complete.

## Suggested Codex Start Prompt

```txt
Read CODEX.md, ROADMAP.md, TASKS.md and lessons/phase-01-python/lesson-01-project-setup.md.

Act as my tutor and code reviewer, not as the implementer.

Communicate with me in German for explanations, reviews, debugging and learning questions.
Keep code, comments, commit messages and repository documentation in English.

Guide me through Lesson 1.1 step by step.
Do not write the solution code unless I explicitly ask.
Explain the goal, then give me the first small task.
After I write code, review it and give hints.
```

## Repository Structure

```txt
ai-engineer-roadmap/
  README.md
  ROADMAP.md
  TASKS.md
  CODEX.md
  PROGRESS.md
  DECISIONS.md
  docs/
    weekly-review.md
    portfolio-criteria.md
  lessons/
    phase-01-python/
    phase-02-fastapi/
    phase-03-llm/
    phase-04-react-ui/
    phase-05-postgresql-persistence/
    phase-06-embeddings-semantic-search/
  ai-engineer-roadmap/
    phase-01-python/
    phase-04-react-ui/
  templates/
    lesson-template.md
    progress-entry-template.md
    decision-template.md
  .github/
    copilot-instructions.md
```

## Language Rules

- Codex should communicate with you in German during tutoring, reviews, debugging and learning discussions.
- Repository documentation, code comments, commit messages, branch names and README content should stay in English.
- Code, terminal commands and error messages can stay in their original language, with German explanations.
