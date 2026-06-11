# Full-Stack Persistence Run Design

## Goal

Create a reproducible local workflow for running PostgreSQL, migrations,
optional Ollama, FastAPI, and React together and verifying persistence from
user input through the database and back into the frontend history.

## Documentation Location

Add a central `README.md` in `ai-engineer-roadmap`. The workflow belongs at
the repository level because it coordinates multiple projects and services.

The backend and frontend READMEs remain focused on their own projects and link
to the central full-stack guide.

## Startup Model

Use separate terminals for long-running services:

1. PostgreSQL through Docker Compose
2. Ollama when AI analysis is being verified
3. FastAPI backend
4. React frontend

This keeps service logs visible and makes failures easier to attribute.
Containerizing every service or adding a process-management script is outside
this lesson.

## Central README Structure

The guide documents:

- prerequisites
- one-time backend and frontend installation
- PostgreSQL startup and status checks
- Alembic migration execution and version checks
- optional Ollama startup and model verification
- backend startup with required environment variables
- frontend startup
- application, Swagger, and API URLs
- normal analysis verification
- AI analysis verification
- frontend history verification
- direct PostgreSQL verification
- service-specific troubleshooting
- shutdown commands

## Verification Flow

### Infrastructure

- Start PostgreSQL.
- Confirm the container is healthy enough to accept connections.
- Apply migrations.
- Confirm Alembic is at `head`.

### Application Services

- Start Ollama and confirm `llama3:latest` is available for the AI path.
- Start FastAPI with `DATABASE_URL` and `AI_PROVIDER=ollama`.
- Open Swagger or request an endpoint to confirm the backend responds.
- Start the React development server and open the application.

### Persistence

- Create a normal text analysis in the frontend.
- Confirm it appears at the top of the history.
- Create an AI analysis.
- Confirm summary, sentiment, topics, action items, and provider are rendered
  when present.
- Query PostgreSQL directly and confirm both records exist.

## Failure Diagnosis

The guide distinguishes:

- frontend failures: browser console, failed requests, incorrect API base URL
- backend failures: Uvicorn logs, HTTP status codes, missing environment values
- database failures: Docker status/logs, migration status, connection errors
- provider failures: Ollama process, installed model, provider HTTP errors
- browser CORS failures: failed preflight or missing backend origin allowance

## Acceptance Criteria

- A learner can start the complete stack using the documented commands.
- Migrations are applied before persistence is tested.
- Normal and AI analyses are stored.
- Both records appear in the frontend history.
- PostgreSQL queries confirm the records exist.
- The central README explains startup, verification, diagnosis, and shutdown.
