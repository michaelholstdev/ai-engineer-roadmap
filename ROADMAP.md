# Full-Stack AI Engineer Roadmap

## Learner Profile

- Current Python level: basics
- Weekly time budget: about 10 hours
- Existing strength: React and TypeScript
- Target role: Full-Stack AI Engineer

## Learning Philosophy

You learn by building. The AI assistant acts as a tutor and reviewer, not as the implementer.

Each phase includes:

- learning goals
- implementation tasks
- tests
- acceptance criteria
- review checkpoints
- reflection questions

## Estimated Timeline

| Milestone | Estimated Time |
|---|---:|
| First useful AI app | 4-6 weeks |
| Solid RAG portfolio project | 3-4 months |
| Job-ready full-stack AI portfolio | 6-9 months |

## Weekly Structure

| Activity | Time |
|---|---:|
| Learning and reading | 2h |
| Guided coding | 5h |
| Practice and refactoring | 2h |
| Notes, README, review | 1h |

## Phase 1 — Python for AI Backends

**Duration:** 3-4 weeks

### Goals

- Build confidence with Python project structure.
- Use type hints and tests.
- Write small, reliable utility functions.
- Understand how Python differs from TypeScript.

### Lessons

- Lesson 1.1 — Project Setup
- Lesson 1.2 — Text Statistics
- Lesson 1.3 — Testing and Code Quality

### Output

A tested Python package with basic text-analysis utilities.

## Phase 2 — FastAPI

**Duration:** 3-4 weeks

### Goals

- Build API endpoints.
- Validate input and output with Pydantic.
- Return structured JSON.
- Handle errors cleanly.

### Lessons

- Lesson 2.1 — FastAPI Basics
- Lesson 2.2 — Request Validation
- Lesson 2.3 — Error Handling
- Lesson 2.4 — API Testing
- Lesson 2.5 — API Project Structure
- Lesson 2.6 — Running the API Locally
- Lesson 2.7 — Phase Review

### Output

A small text-analysis API.

## Phase 3 — LLM APIs

**Duration:** 4-5 weeks

### Goals

- Connect a backend to an LLM API.
- Use environment variables safely.
- Design prompts.
- Return structured outputs.
- Understand retries, rate limits, and cost.

### Lessons

- Lesson 3.1 — LLM API Concepts and Setup
- Lesson 3.2 — AI Client Boundary
- Lesson 3.3 — Prompt Design and Structured Output
- Lesson 3.4 — AI Analyze Endpoint
- Lesson 3.5 — Mocking External API Calls
- Lesson 3.6 — Errors, Retries, Rate Limits, and Cost
- Lesson 3.7 — Phase Review
- Optional Lesson 3.x — Local LLM Provider with Ollama

### Output

An AI-powered analyzer endpoint.

## Phase 4 — React AI UI

**Duration:** 3-4 weeks

### Goals

- Connect React to the FastAPI backend.
- Handle loading, error and success states.
- Display structured AI output.
- Add streaming later.

### Lessons

- Lesson 4.1 — Frontend Project Setup
- Lesson 4.2 — Text Analyzer Form
- Lesson 4.3 — Loading, Error, and Empty States
- Lesson 4.4 — AI Analyze UI
- Lesson 4.5 — React API Client Boundary
- Lesson 4.6 — Frontend Testing Basics
- Lesson 4.7 — Full-Stack Local Run
- Lesson 4.8 — Phase Review

### Output

A small full-stack AI application.

## Phase 5 — PostgreSQL and Persistence

**Duration:** 3-4 weeks

### Goals

- Store prompts and outputs.
- Build a history view.
- Understand migrations.
- Learn basic database design for AI apps.

### Lessons

- Lesson 5.1 — Persistence Concepts and Setup
- Lesson 5.2 — Database Schema and Migrations
- Lesson 5.3 — Backend Repository Boundary
- Lesson 5.4 — Store Analysis Results
- Lesson 5.5 — History API Endpoint
- Lesson 5.6 — Frontend History View
- Lesson 5.7 — Full-Stack Persistence Run
- Lesson 5.8 — Phase Review

### Output

AI analysis history stored in PostgreSQL.

## Phase 6 — Embeddings and Semantic Search

**Duration:** 3-4 weeks

### Goals

- Understand embeddings.
- Implement semantic search.
- Compare keyword search and vector search.
- Use pgvector with PostgreSQL.

### Lessons

- Lesson 6.1 — Embedding and Vector Search Concepts
- Lesson 6.2 — pgvector Setup and Notes Schema
- Lesson 6.3 — Embedding Client Boundary
- Lesson 6.4 — Store Notes with Embeddings
- Lesson 6.5 — Keyword Search
- Lesson 6.6 — Semantic Search
- Lesson 6.7 — Notes and Search UI
- Lesson 6.8 — Full-Stack Search Comparison
- Lesson 6.9 — Phase Review

### Output

Keyword and semantic search over embedded notes using PostgreSQL, pgvector, Ollama,
FastAPI, and React.

## Phase 7 — RAG

**Duration:** 6-8 weeks

### Goals

- Upload documents.
- Extract text.
- Chunk documents.
- Embed chunks.
- Retrieve relevant context.
- Generate grounded answers with citations.
- Evaluate answer quality.

### Output

Main portfolio project: Chat with Documents.

## Phase 8 — Tool Calling and Agents

**Duration:** 4-6 weeks

### Goals

- Understand when an agent is useful.
- Implement tool calling.
- Build deterministic workflows before agentic workflows.
- Add logging and safety limits.

### Output

AI Research Assistant with controlled tool usage.

## Phase 9 — Classical ML for Product Engineers

**Duration:** 4-6 weeks

### Goals

- Understand regression and classification.
- Train and evaluate models with scikit-learn.
- Deploy a model behind an API.

### Output

Prediction API portfolio project.

## Phase 10 — Production AI and LLMOps

**Duration:** 5-7 weeks

### Goals

- Dockerize services.
- Add logging and monitoring.
- Track cost and latency.
- Version prompts.
- Create evaluation sets.

### Output

Production-ready RAG app with monitoring and evaluation.
