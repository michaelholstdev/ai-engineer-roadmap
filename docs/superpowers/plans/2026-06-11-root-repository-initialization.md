# Root Repository Initialization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the unusable root Git metadata and nested backend repository with one repository on `main` containing the complete learning workspace.

**Architecture:** Preserve the old backend Git metadata as a temporary backup outside the workspace, then initialize Git at the workspace root. Root ignore rules exclude dependencies, build output, caches, virtual environments, secrets, and local tool state while retaining example environment files.

**Tech Stack:** Git, Python/uv, React/pnpm

---

### Task 1: Prepare Repository Metadata

**Files:**
- Create: `.gitignore`
- Preserve externally: `ai-engineer-roadmap/phase-01-python/.git`

- [ ] Move the nested backend `.git` directory to a backup under `/tmp`.
- [ ] Remove the empty root `.git` directory.
- [ ] Add root ignore rules for generated and local files.
- [ ] Initialize the root repository with branch `main`.

### Task 2: Verify the Workspace

**Files:**
- Verify: `ai-engineer-roadmap/phase-01-python`
- Verify: `ai-engineer-roadmap/phase-04-react-ui`

- [ ] Run backend tests, Ruff, and mypy.
- [ ] Run frontend tests, ESLint, and the production build.
- [ ] Inspect ignored and staged files to ensure dependencies and secrets are excluded.

### Task 3: Create Initial Commit

**Files:**
- Stage: complete workspace excluding ignored files

- [ ] Stage the complete root repository.
- [ ] Review the staged file list and diff summary.
- [ ] Create the initial commit.
- [ ] Confirm branch `main`, commit ID, and a clean working tree.
