# AI Engineer Roadmap

This repository contains the backend and frontend projects for a text analyzer
with optional local AI analysis and persisted analysis history.

## Projects

- `phase-01-python`: FastAPI backend, PostgreSQL persistence, and Ollama client
- `phase-04-react-ui`: React frontend for text analysis, AI analysis, and history

## Requirements

- Docker with Docker Compose
- Python 3.11+
- `uv`
- Node.js
- `pnpm`
- Optional for AI analysis: Ollama with `llama3:latest`

## First-Time Setup

Install the backend dependencies:

```bash
cd phase-01-python
uv sync
cd ..
```

Install the frontend dependencies:

```bash
cd phase-04-react-ui
pnpm install
cp .env.example .env
cd ..
```

All commands below assume that the current directory is
`ai-engineer-roadmap`.

## Start PostgreSQL

```bash
cd phase-01-python
docker compose up -d postgres
docker compose ps
cd ..
```

PostgreSQL listens on `127.0.0.1:5432`.

## Run Database Migrations

Apply all migrations:

```bash
cd phase-01-python
DATABASE_URL=postgresql+psycopg://ai_roadmap:ai_roadmap_dev_password@127.0.0.1:5432/ai_roadmap \
uv run alembic upgrade head
cd ..
```

Check the current migration version:

```bash
cd phase-01-python
DATABASE_URL=postgresql+psycopg://ai_roadmap:ai_roadmap_dev_password@127.0.0.1:5432/ai_roadmap \
uv run alembic current
cd ..
```

The expected current revision is `db220f8d2751 (head)`.

## Start Ollama

AI analysis is optional. Verify that the model is installed:

```bash
ollama list
```

The output should include `llama3:latest`.

Start Ollama in its own terminal if it is not already running:

```bash
ollama serve
```

Verify that the local Ollama API responds:

```bash
curl -sS http://127.0.0.1:11434/api/tags
```

## Start the Backend

Start FastAPI in its own terminal:

```bash
cd phase-01-python
DATABASE_URL=postgresql+psycopg://ai_roadmap:ai_roadmap_dev_password@127.0.0.1:5432/ai_roadmap \
AI_PROVIDER=ollama \
uv run uvicorn ai_roadmap.api:app --reload
```

Verify the backend from another terminal:

```bash
curl -sS http://127.0.0.1:8000/openapi.json > /dev/null \
  && echo "OpenAPI reachable"
curl -sS "http://127.0.0.1:8000/analyses?limit=1"
```

## Start the Frontend

Start React in its own terminal:

```bash
cd phase-04-react-ui
pnpm run dev
```

## Local URLs

- App: `http://localhost:5173/`
- Swagger UI: `http://127.0.0.1:8000/docs`
- Backend API: `http://127.0.0.1:8000`
- Ollama API: `http://127.0.0.1:11434`

## Verify Persistence

### Normal Analysis

1. Open `http://localhost:5173/`.
2. Enter:

   ```text
   Lesson 5.7 normal persistence verification.
   ```

3. Click `Analyze`.
4. Confirm that the text statistics appear.
5. Confirm that the new text record appears first in `Recent analyses`
   without reloading the page.

Verify the newest text record directly in PostgreSQL:

```bash
cd phase-01-python
docker compose exec postgres psql -U ai_roadmap -d ai_roadmap \
  -c "SELECT analysis_type, input_text, word_count, character_count, sentence_count, created_at FROM analysis_runs WHERE analysis_type = 'text' ORDER BY created_at DESC LIMIT 1;"
```

### AI Analysis

Ollama must be running for this workflow.

1. Enter:

   ```text
   Lesson 5.7 AI persistence verification is useful.
   ```

2. Click `Analyze with AI`.
3. Confirm that the structured AI result appears.
4. Confirm that the new AI record appears first in `Recent analyses`
   without reloading the page.
5. Confirm that summary, sentiment, provider, topics, and action items appear
   when the provider returns values for them.

Verify the newest AI record directly in PostgreSQL:

```bash
cd phase-01-python
docker compose exec postgres psql -U ai_roadmap -d ai_roadmap \
  -c "SELECT analysis_type, input_text, summary, sentiment, topics, action_items, provider, created_at FROM analysis_runs WHERE analysis_type = 'ai' ORDER BY created_at DESC LIMIT 1;"
```

## Troubleshooting

### Frontend

- Inspect the browser console for JavaScript errors.
- Inspect the browser Network tab for failed requests and CORS errors.
- Confirm that `VITE_API_BASE_URL` points to
  `http://127.0.0.1:8000`.
- Confirm that Vite is running on `http://localhost:5173/`.

### Backend

- Inspect the Uvicorn terminal for exceptions and HTTP status codes.
- Confirm that `DATABASE_URL` is set in the terminal that starts Uvicorn.
- Confirm that `AI_PROVIDER=ollama` is set when testing local AI analysis.
- Check backend availability:

  ```bash
  curl -sS http://127.0.0.1:8000/openapi.json > /dev/null \
    && echo "OpenAPI reachable"
  ```

- Check the history endpoint:

  ```bash
  curl -sS "http://127.0.0.1:8000/analyses?limit=1"
  ```

### PostgreSQL

From `phase-01-python`, inspect the container:

```bash
docker compose ps
docker compose logs postgres
```

Check the migration version:

```bash
DATABASE_URL=postgresql+psycopg://ai_roadmap:ai_roadmap_dev_password@127.0.0.1:5432/ai_roadmap \
uv run alembic current
```

### Ollama

Confirm that the process responds and the model exists:

```bash
curl -sS http://127.0.0.1:11434/api/tags
ollama list
```

Provider failures appear as `502` responses in the backend logs. Missing
provider configuration appears as a `503` response.

## Stop Local Services

Stop the frontend, backend, and Ollama processes with `Ctrl+C` in their
respective terminals.

Stop PostgreSQL:

```bash
cd phase-01-python
docker compose down
```

The named PostgreSQL volume remains available for the next run.

## Run Automated Checks

Backend:

```bash
cd phase-01-python
uv run pytest
uv run ruff check .
uv run mypy src
```

Frontend:

```bash
cd phase-04-react-ui
pnpm run test
pnpm run lint
pnpm run build
```
