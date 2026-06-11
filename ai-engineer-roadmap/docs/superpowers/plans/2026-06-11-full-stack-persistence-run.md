# Full-Stack Persistence Run Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Verify and document the complete local persistence workflow across PostgreSQL, Alembic, FastAPI, Ollama, and React.

**Architecture:** Long-running services use separate terminals so their logs remain visible. Verification follows the data path from frontend input to backend persistence, direct PostgreSQL inspection, and frontend history rendering. A central repository README owns the multi-service workflow.

**Tech Stack:** Docker Compose, PostgreSQL 17, Alembic, FastAPI/Uvicorn, Ollama, React/Vite, curl, psql

---

### Task 1: Verify Database and Migrations

**Files:**
- Read: `phase-01-python/compose.yaml`
- Read: `phase-01-python/.env.example`

- [ ] **Step 1: Start PostgreSQL**

From `phase-01-python`:

```bash
docker compose up -d postgres
docker compose ps
```

Expected: `phase-01-python-postgres-1` is `Up` and publishes port `5432`.

- [ ] **Step 2: Apply migrations**

```bash
DATABASE_URL=postgresql+psycopg://ai_roadmap:ai_roadmap_dev_password@127.0.0.1:5432/ai_roadmap \
uv run alembic upgrade head
```

Expected: command exits successfully.

- [ ] **Step 3: Verify migration state**

```bash
DATABASE_URL=postgresql+psycopg://ai_roadmap:ai_roadmap_dev_password@127.0.0.1:5432/ai_roadmap \
uv run alembic current
```

Expected: revision `651c16e02b39 (head)`.

### Task 2: Start Provider and Application Services

**Files:**
- Read: `phase-01-python/README.md`
- Read: `phase-04-react-ui/README.md`

- [ ] **Step 1: Verify the Ollama model**

```bash
ollama list
```

Expected: `llama3:latest` is listed.

- [ ] **Step 2: Start Ollama in terminal 1 when it is not already running**

```bash
ollama serve
```

Expected: Ollama listens on `127.0.0.1:11434`. If another Ollama process
already owns the port, use that running process rather than starting a second
one.

- [ ] **Step 3: Start FastAPI in terminal 2**

From `phase-01-python`:

```bash
DATABASE_URL=postgresql+psycopg://ai_roadmap:ai_roadmap_dev_password@127.0.0.1:5432/ai_roadmap \
AI_PROVIDER=ollama \
uv run uvicorn ai_roadmap.api:app --reload
```

Expected: Uvicorn listens on `http://127.0.0.1:8000`.

- [ ] **Step 4: Verify backend endpoints**

```bash
curl -sS http://127.0.0.1:8000/openapi.json
curl -sS "http://127.0.0.1:8000/analyses?limit=1"
```

Expected: OpenAPI JSON and a history JSON array.

- [ ] **Step 5: Start React in terminal 3**

From `phase-04-react-ui`:

```bash
pnpm run dev
```

Expected: Vite prints `http://localhost:5173/`.

### Task 3: Verify Normal Analysis Persistence

**Files:** None

- [ ] **Step 1: Create a unique normal analysis**

In the browser, enter:

```text
Lesson 5.7 normal persistence verification.
```

Click `Analyze`.

- [ ] **Step 2: Verify frontend behavior**

Expected:

- text statistics are rendered
- history refreshes without reloading the page
- the new text record appears first

- [ ] **Step 3: Verify PostgreSQL storage**

From `phase-01-python`:

```bash
docker compose exec postgres psql -U ai_roadmap -d ai_roadmap \
  -c "SELECT analysis_type, input_text, word_count, character_count, sentence_count, created_at FROM analysis_runs WHERE input_text = 'Lesson 5.7 normal persistence verification.' ORDER BY created_at DESC;"
```

Expected: one or more `text` rows matching the unique input.

### Task 4: Verify AI Analysis Persistence

**Files:** None

- [ ] **Step 1: Create a unique AI analysis**

In the browser, replace the input with:

```text
Lesson 5.7 AI persistence verification is useful.
```

Click `Analyze with AI`.

- [ ] **Step 2: Verify frontend behavior**

Expected:

- structured AI output is rendered
- history refreshes without reloading the page
- the new AI record appears first
- summary, sentiment, provider, and non-empty list fields appear

- [ ] **Step 3: Verify PostgreSQL storage**

```bash
docker compose exec postgres psql -U ai_roadmap -d ai_roadmap \
  -c "SELECT analysis_type, input_text, summary, sentiment, topics, action_items, provider, created_at FROM analysis_runs WHERE input_text = 'Lesson 5.7 AI persistence verification is useful.' ORDER BY created_at DESC;"
```

Expected: an `ai` row with provider `ollama` and structured fields.

### Task 5: Write the Central Full-Stack README

**Files:**
- Create: `README.md`
- Modify: `phase-01-python/README.md`
- Modify: `phase-04-react-ui/README.md`

- [ ] **Step 1: Create the central guide**

Write a repository-level README with these exact sections:

```markdown
# AI Engineer Roadmap

## Projects
## Requirements
## First-Time Setup
## Start PostgreSQL
## Run Database Migrations
## Start Ollama
## Start the Backend
## Start the Frontend
## Local URLs
## Verify Persistence
## Troubleshooting
## Stop Local Services
## Run Automated Checks
```

Use only commands that were successfully verified in Tasks 1-4.

- [ ] **Step 2: Document service-specific troubleshooting**

Include these diagnostics:

```bash
docker compose ps
docker compose logs postgres
curl -sS http://127.0.0.1:8000/openapi.json
curl -sS "http://127.0.0.1:8000/analyses?limit=1"
ollama list
```

Explain where to inspect:

- browser console and Network tab for frontend and CORS failures
- Uvicorn output for backend errors
- Docker Compose logs for PostgreSQL failures
- Ollama output for provider failures

- [ ] **Step 3: Add links from project READMEs**

Add a short section to each project README:

```markdown
## Full-stack workflow

See the [repository-level README](../README.md) for the complete PostgreSQL,
backend, Ollama, and frontend startup and persistence verification workflow.
```

- [ ] **Step 4: Review documentation commands**

Check every path, URL, environment variable, model name, and command against
the successful manual run. Remove commands that were not verified.

### Task 6: Final Verification

**Files:** None

- [ ] **Step 1: Run backend checks**

From `phase-01-python`:

```bash
uv run pytest
uv run ruff check .
uv run mypy src
```

Expected: all commands pass.

- [ ] **Step 2: Run frontend checks**

From `phase-04-react-ui`:

```bash
pnpm run test
pnpm run lint
pnpm run build
```

Expected: all commands pass.

- [ ] **Step 3: Verify documentation readability**

Follow the central README from the beginning using fresh terminals. Confirm
that no undocumented environment variable or working-directory assumption is
required.

- [ ] **Step 4: Request final review**

Provide:

- database and migration command output
- normal and AI PostgreSQL query output
- browser verification results
- backend and frontend check output
- the three README files

## Version Control Note

The current project directories are not inside a shared Git repository, so the
plan does not include commit steps.
