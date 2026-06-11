# React AI UI

Frontend for the FastAPI text and AI analyzer.

## Full-stack workflow

See the [repository-level README](../README.md) for the complete PostgreSQL,
backend, Ollama, and frontend startup and persistence verification workflow.

## Requirements

- NodeJS
- pnpm
- FastAPI backend from `../phase-01-python`
- Optional: Ollama with `llama3:latest` for AI analysis

## Environment variables

```text
VITE_API_BASE_URL=http://127.0.0.1:8000
```

## Install

```bash
pnpm install
```

## Start the backend

```bash
cd ../phase-01-python
AI_PROVIDER=ollama uv run uvicorn ai_roadmap.api:app --reload
```

## Start the frontend

```bash
pnpm run dev
```

## Open the app

```text
http://localhost:5173/
```

## Run checks

```bash
pnpm run test
pnpm run lint
pnpm run build
```

## Manual verification

- Enter text and click `Analyze`.
- Enter text and click `Analyze with AI`.
- Check the browser console for errors.
