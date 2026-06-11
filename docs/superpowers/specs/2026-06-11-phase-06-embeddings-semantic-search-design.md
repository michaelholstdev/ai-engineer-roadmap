# Phase 6 Embeddings and Semantic Search Design

## Goal

Extend the existing full-stack application with persisted notes, local embeddings,
keyword search, and semantic vector search.

Phase 6 should teach the foundations required for RAG without implementing document
upload, extraction, chunking, or answer generation. Those concerns remain in Phase 7.

## Technology Choices

- PostgreSQL remains the primary database.
- The `pgvector` PostgreSQL extension stores and searches embeddings.
- Ollama generates embeddings with `qwen3-embedding:0.6b`.
- FastAPI exposes note creation and search endpoints.
- React provides note creation and search workflows.
- Automated tests replace Ollama and database calls with controlled test doubles.

## Data Model

Semantic-search data is stored separately from `analysis_runs`.

The new `notes` table contains:

- `id`: UUID primary key
- `title`: required text
- `content`: required text
- `embedding`: required pgvector vector with 1024 dimensions
- `embedding_model`: required text
- `created_at`: required timezone-aware timestamp
- `updated_at`: required timezone-aware timestamp

The vector dimension is fixed at 1024 to match `qwen3-embedding:0.6b`. The dimension
and model name are explicitly recorded in the migration and application configuration.
A model change requires a deliberate migration review and re-embedding workflow, even
when the replacement model uses the same vector dimension.

Notes are stored as complete texts during Phase 6. They are not divided into chunks.

## Backend Boundaries

### Embedding Client

The embedding client owns communication with the Ollama embedding endpoint. It accepts
text and returns a validated numeric vector containing exactly 1024 finite numbers.

Stored notes are embedded as documents without a retrieval instruction. Search queries
use a stable English retrieval instruction describing the task of finding relevant
notes. The instruction is application configuration rather than user input.

Provider-specific transport errors and invalid provider responses are converted into
application-specific embedding errors. Routes do not depend directly on `httpx` or
Ollama response formats.

### Notes Repository

The notes repository owns SQL for:

- inserting notes and embeddings
- keyword search
- semantic vector search
- mapping database rows to typed domain objects

Routes do not contain raw SQL or pgvector-specific expressions.

### Notes Service

A small service boundary coordinates note creation:

1. Validate the note input.
2. Combine the title and content into the embedding input.
3. Request an embedding.
4. Persist the note and embedding in one database transaction.
5. Return the typed note response.

Search coordination also lives behind this boundary so routes remain focused on HTTP
input, output, and status-code mapping.

## API Design

### Create Note

```text
POST /notes
```

Request:

```json
{
  "title": "Embedding basics",
  "content": "Embeddings represent semantic meaning as vectors."
}
```

The endpoint returns the stored note without exposing the raw embedding.

### Search Notes

```text
GET /notes/search?q=<query>&mode=keyword|semantic&limit=<number>
```

Rules:

- `q` must contain non-whitespace text.
- `mode` defaults to `semantic`.
- `limit` has a small bounded range.
- Both modes return the same response shape.
- Results are ordered from most relevant to least relevant.

Each result contains:

- note ID
- title
- content
- search mode
- relevance score
- creation timestamp

Keyword and semantic scores have different meanings. The frontend may display them,
but it must not imply that scores from the two modes are directly equivalent.

## Search Behavior

### Keyword Search

Keyword search is implemented with PostgreSQL text-search functionality rather than
ad hoc Python substring matching. It creates a baseline for comparing lexical matching
with semantic similarity.

### Semantic Search

The backend embeds the instructed query using the same model and dimensions used for
stored notes. The repository uses pgvector distance operations to retrieve the nearest
notes.

Cosine distance is the initial similarity strategy. The database index strategy is
introduced only after correctness is verified with a small dataset. Phase 6 should
explain the trade-off between exact search and approximate indexes instead of adding
an index without measurement.

## Frontend Design

The React UI gains two focused workflows:

### Note Creation

- title input
- content textarea
- submit button
- loading, success, validation, and error states

A successfully created note becomes available for search without a page reload.

### Note Search

- query input
- keyword/semantic segmented mode control
- bounded result limit
- search button
- loading, empty, success, and error states
- result list with title, content, score, and timestamp

The same result component renders both search modes so the comparison focuses on result
quality instead of different presentation.

## Error Handling

- Invalid note or query input returns validation errors.
- Missing embedding-provider configuration maps to a service-unavailable response.
- Ollama connection or provider failures map to a bad-gateway response.
- Invalid embedding vectors are rejected before persistence.
- Database failures do not return partially created notes.
- Frontend messages remain user-facing and do not expose internal exception details.

## Testing Strategy

### Backend Unit and API Tests

- validate note request and response schemas
- validate embedding vectors and provider errors
- verify note creation coordinates embedding and persistence
- verify failed embeddings do not persist notes
- verify keyword-search SQL and ordering
- verify semantic-search vector SQL and ordering
- verify API modes, limits, empty results, and error mapping

Tests use mocked connections and fake embedding-client responses. They do not require
PostgreSQL or Ollama by default.

### Migration and Integration Verification

- apply migrations to the local PostgreSQL container
- verify the `vector` extension and `notes` schema
- create notes using a running Ollama instance
- compare keyword and semantic queries manually

These checks are documented and opt-in rather than part of the default unit-test suite.

### Frontend Tests

- note form validation and request behavior
- creation loading, success, and error states
- search mode selection and request construction
- search loading, empty, success, and error states
- rendering consistent results for both modes

Frontend tests mock the API-client boundary and do not require the backend.

## Lesson Structure

### Lesson 6.1 - Embedding and Vector Search Concepts

Define embeddings, dimensions, similarity metrics, and the separation between analysis
history and searchable notes.

### Lesson 6.2 - pgvector Setup and Notes Schema

Add pgvector to local PostgreSQL, design the `notes` table, and create a migration.

### Lesson 6.3 - Embedding Client Boundary

Add a typed Ollama embedding client with validation and controlled error handling.

### Lesson 6.4 - Store Notes with Embeddings

Create the note service, repository insert behavior, and `POST /notes`.

### Lesson 6.5 - Keyword Search

Implement PostgreSQL keyword search and establish a lexical-search baseline.

### Lesson 6.6 - Semantic Search

Embed queries and implement cosine-distance search through pgvector.

### Lesson 6.7 - Notes and Search UI

Build note creation and unified keyword/semantic search workflows in React.

### Lesson 6.8 - Full-Stack Search Comparison

Run PostgreSQL, Ollama, FastAPI, and React; create a controlled note set and compare
keyword with semantic results.

### Lesson 6.9 - Phase Review

Review schema design, embedding boundaries, search correctness, tests, documentation,
and readiness for document chunking and RAG.

## Acceptance Criteria

- Notes are stored separately from analysis history.
- PostgreSQL stores embeddings using pgvector.
- Ollama generates 1024-dimensional `qwen3-embedding:0.6b` vectors through a typed
  backend boundary.
- Note creation is transactional and does not expose raw vectors.
- Keyword and semantic search share one typed API response.
- The React UI creates and searches notes in both modes.
- Default automated tests require neither PostgreSQL nor Ollama.
- Documentation explains local setup and full-stack comparison.
- Phase 7 can build document and chunk ingestion without redesigning analysis history.
