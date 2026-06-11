# Phase 1 Python / FastAPI Text Analyzer

This project exposes a small FastAPI endpoint for text statistics.

## Full-stack workflow

See the [repository-level README](../README.md) for the complete PostgreSQL,
backend, Ollama, and frontend startup and persistence verification workflow.

## How to run tests

The tests do not call any OpenAI or LLM API.

```bash
uv run pytest
```

## Environment variables

The `.env.example` file can be used as an example environment file.

```bash
OPENAI_API_KEY=replace-with-your-api-key
DATABASE_URL=postgresql+psycopg://ai_roadmap:ai_roadmap_dev_password@127.0.0.1:5432/ai_roadmap
```

## Local PostgreSQL

The local PostgreSQL database can be started with Docker Compose.

The local database URL is:

```text
DATABASE_URL=postgresql+psycopg://ai_roadmap:ai_roadmap_dev_password@127.0.0.1:5432/ai_roadmap
```

To start the local database:

```bash
docker compose up -d postgres
```

To stop the local database:

```bash
docker compose down
```

## Database migrations

Run migrations with:

```bash
DATABASE_URL=postgresql+psycopg://ai_roadmap:ai_roadmap_dev_password@127.0.0.1:5432/ai_roadmap uv run alembic upgrade head
```

Check the current migration version with:

```bash
DATABASE_URL=postgresql+psycopg://ai_roadmap:ai_roadmap_dev_password@127.0.0.1:5432/ai_roadmap uv run alembic current
```

## How to start the local API

```bash
uv run uvicorn ai_roadmap.api:app --reload
```

## Where to open Swagger UI

Swagger UI is reachable after starting the API.

```text
http://127.0.0.1:8000/docs
```

## Implemented endpoints

```text
POST /analyze
POST /ai/analyze
```

## Optional local Ollama provider

The optional local Ollama client uses `llama3:latest` and calls the local Ollama HTTP API at `http://127.0.0.1:11434/api/generate`.

Tests do not require Ollama to be installed or running.

To start Ollama manually:

```bash
ollama serve
```

To test the model manually:

```bash
ollama run llama3:latest
```
