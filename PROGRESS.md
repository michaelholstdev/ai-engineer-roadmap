# Progress

Use this file to track completed lessons, test results and learning notes.

## Format

Use the template in `templates/progress-entry-template.md`.

## Entries

## 2026-05-07 — Lesson 1.1 — Project Setup

### Status

Completed

### What I Built

- Created the `ai-engineer-roadmap/phase-01-python` project folder.
- Initialized a Python project with `uv`.
- Added `pytest`, `ruff`, and `mypy` as development dependencies.
- Created a `src/` package layout with `ai_roadmap`.
- Created an initial pytest test file.

### Commands Run

```bash
python --version
git --version
uv --version
uv init
uv add --dev pytest ruff mypy
uv run python --version
uv run pytest
```

### Test Results

- `pytest`: 1 passed
- `ruff`: not run in this lesson
- `mypy`: not run in this lesson

### What I Learned

- `pyproject.toml` stores project metadata and dependencies.
- The `src/` layout separates application code from tests and helps catch import issues.
- `uv run pytest` runs pytest inside the project environment.
- Dev dependencies are tools needed for development and testing, not production runtime code.

### What Was Difficult

- Understanding why `src/` and `tests/` are separated.
- Knowing what to check first when pytest cannot import a package.

### Tutor Review Summary

- The project structure matches the lesson requirements.
- The development dependencies are present.
- The initial pytest test passes.
- Generated cache files should stay ignored by git.

### Next Step

- Start Lesson 1.2 and replace the placeholder test with real tests for text statistics functions.

## 2026-05-07 — Lesson 1.2 — Text Statistics

### Status

Completed

### What I Built

- Implemented `count_words(text: str) -> int`.
- Implemented `count_characters(text: str) -> int`.
- Implemented `count_sentences(text: str) -> int`.
- Added pytest coverage for normal cases and edge cases.

### Commands Run

```bash
uv run python
uv run pytest
```

### Test Results

- `pytest`: 3 passed
- `ruff`: not run in this lesson
- `mypy`: not run in this lesson

### What I Learned

- `str.split()` without arguments treats multiple whitespace characters as separators.
- Empty strings are important test cases because they often reveal incorrect assumptions.
- Edge cases are inputs that sit near the boundary of expected behavior.
- Type hints make Python code easier to read and review.
- Simple sentence counting with punctuation marks is limited for real-world text.

### What Was Difficult

- Understanding how imports work with a `src/` package layout.
- Understanding why regex punctuation characters such as `?` have special meaning.
- Fixing the difference between `=+` assignment and `+=` incrementing.

### Tutor Review Summary

- The text statistics functions match the lesson requirements.
- The tests cover the required examples.
- `uv run pytest` passes with all current tests.
- Real production sentence detection would need more robust parsing than counting punctuation marks.

### Next Step

- Start Lesson 1.3 and run code quality tools with `ruff` and `mypy`.

## 2026-05-10 — Lesson 1.3 — Testing and Code Quality

### Status

Completed

### What I Built

- Added additional edge-case tests for text statistics functions.
- Verified the project with pytest, Ruff, and mypy.

### Commands Run

```bash
uv run pytest
uv run ruff check .
uv run mypy src
```

### Test Results

- `pytest`: 3 passed
- `ruff`: all checks passed
- `mypy`: no issues found in 2 source files

### What I Learned

- Tests check whether code behavior matches expectations.
- Linting checks code style and common quality issues.
- Type checking catches mismatches between expected and actual types before runtime.
- Automated feedback helps catch problems early.

### What Was Difficult

- Distinguishing between behavior checks, linting feedback, and type checking.
- Understanding that code can pass tests but still have type or quality issues.

### Tutor Review Summary

- The added edge-case tests match the current simple text statistics behavior.
- `pytest`, `ruff`, and `mypy` all pass.
- The learner can explain the purpose of each feedback tool.

### Next Step

- Move on to the next phase or add a small review/refactor pass before starting FastAPI.

## 2026-05-10 — Lesson 2.1 — FastAPI Basics

### Status

Completed

### What I Built

- Added FastAPI as a runtime dependency.
- Added `httpx` as a development dependency for API tests.
- Created a FastAPI app module.
- Defined Pydantic request and response models.
- Implemented `POST /analyze` around the existing text statistics functions.
- Added endpoint tests with FastAPI `TestClient`.

### Commands Run

```bash
uv add fastapi
uv add --dev httpx
uv run pytest
uv run ruff check .
uv run mypy src
```

### Test Results

- `pytest`: 5 passed
- `ruff`: all checks passed
- `mypy`: no issues found in 3 source files

### What I Learned

- FastAPI route handlers connect HTTP requests to Python functions.
- Pydantic models define and validate request and response shapes.
- Invalid request bodies should receive validation errors instead of reaching business logic.
- A typed API boundary will make later LLM integration easier to test and reason about.

### What Was Difficult

- Understanding the difference between Python type hints and runtime validation.
- Formatting multi-line JSON-style dictionaries clearly in tests.
- Deciding how empty input should behave.

### Tutor Review Summary

- The `/analyze` endpoint returns the expected JSON response.
- The endpoint uses Pydantic models for request and response data.
- Empty text input is handled intentionally and tested.
- `pytest`, `ruff`, and `mypy` all pass.

### Next Step

- Continue Phase 2 by expanding FastAPI validation and error handling.

## 2026-05-11 — Lesson 2.2 — Request Validation

### Status

Completed

### What I Built

- Added request validation for the `/analyze` endpoint.
- Rejected empty text input.
- Rejected whitespace-only text input.
- Added API tests for valid and invalid request bodies.

### Commands Run

```bash
uv run pytest
uv run ruff check .
uv run mypy src
```

### Test Results

- `pytest`: 6 passed
- `ruff`: all checks passed
- `mypy`: no issues found in 3 source files

### What I Learned

- Pydantic field validators can enforce model-level input rules.
- Empty strings and whitespace-only strings are different values but can both be invalid for an API.
- FastAPI returns HTTP `422` when request validation fails.
- Keeping validation in the request model avoids duplicating the same rule in route handlers.

### What Was Difficult

- Understanding the difference between string type validation and meaningful text validation.
- Moving validation from the route parameter into the request model.
- Understanding how a `ValueError` in Pydantic becomes a FastAPI validation response.

### Tutor Review Summary

- The validation behavior matches the lesson requirements.
- Valid input still returns HTTP `200`.
- Empty and whitespace-only input return HTTP `422`.
- `pytest`, `ruff`, and `mypy` all pass.

### Next Step

- Start Lesson 2.3 and add intentional application-level error handling.

## 2026-05-11 — Lesson 2.3 — Error Handling

### Status

Completed

### What I Built

- Added an application-level maximum text length rule.
- Returned HTTP `413 Payload Too Large` for text longer than 500 characters.
- Added an API test for the application-level error response.
- Verified the error response body.

### Commands Run

```bash
uv run pytest
uv run ruff check .
uv run mypy src
```

### Test Results

- `pytest`: 7 passed
- `ruff`: all checks passed
- `mypy`: no issues found in 3 source files

### What I Learned

- Validation errors happen before business logic runs.
- Application errors happen inside route or business logic after the request is valid.
- `HTTPException` is useful for intentional API errors with clear status codes.
- Error tests should verify both the status code and the response body.

### What Was Difficult

- Choosing the right status code for a too-large request.
- Separating Pydantic validation from application-level rules.
- Thinking about future LLM-specific error cases such as token limits and unsafe input.

### Tutor Review Summary

- Valid requests still return HTTP `200`.
- Pydantic validation errors still return HTTP `422`.
- Too-large text input returns HTTP `413` with a predictable error body.
- `pytest`, `ruff`, and `mypy` all pass.

### Next Step

- Start Lesson 2.4 and improve API test structure.

## 2026-05-11 — Lesson 2.4 — API Testing

### Status

Completed

### What I Built

- Reviewed the existing API endpoint tests.
- Refactored repeated blank-text validation tests with `pytest.mark.parametrize`.
- Kept success, validation failure, and application failure tests focused.

### Commands Run

```bash
uv run pytest
uv run ruff check .
```

### Test Results

- `pytest`: 7 passed
- `ruff`: all checks passed
- `mypy`: not run in this lesson

### What I Learned

- `TestClient` can exercise FastAPI routes and validation without starting a real server.
- Parametrization is useful when tests share the same structure and only inputs change.
- Overly generic parametrization can make tests harder to understand.
- Clear test names make failures easier to diagnose.

### What Was Difficult

- Deciding which tests should be parametrized and which should stay separate.
- Keeping formatting readable in multi-line request and response assertions.

### Tutor Review Summary

- The API tests cover valid input, Pydantic validation failures, and application-level failures.
- The blank-text validation cases are grouped with parametrization.
- The test names describe behavior clearly.
- `pytest` and `ruff` pass.

### Next Step

- Start Lesson 2.5 and refactor the API project structure into clearer modules.

## 2026-05-11 — Lesson 2.5 — API Project Structure

### Status

Completed

### What I Built

- Moved Pydantic request and response models into `schemas.py`.
- Moved the `/analyze` route into `routes.py`.
- Kept FastAPI app creation and router registration in `api.py`.
- Preserved the existing public app import used by tests.

### Commands Run

```bash
uv run pytest
uv run ruff check .
uv run mypy src
```

### Test Results

- `pytest`: 7 passed
- `ruff`: all checks passed
- `mypy`: no issues found in 5 source files

### What I Learned

- App creation, routes, schemas, and business logic should have clear module boundaries.
- Existing tests make refactoring safer by catching broken imports and behavior changes.
- Flatter, descriptive import paths are easier to understand.
- Separating modules prepares the API for future LLM features.

### What Was Difficult

- Moving code without changing behavior.
- Keeping imports clear after splitting modules.
- Deciding which responsibilities belong in each module.

### Tutor Review Summary

- `api.py` now owns app creation and router registration.
- `routes.py` owns the `/analyze` endpoint and application-level error rule.
- `schemas.py` owns request and response models.
- `pytest`, `ruff`, and `mypy` all pass.

### Next Step

- Start Lesson 2.6 and run the API locally with `uvicorn`.

## 2026-05-11 — Lesson 2.6 — Running the API Locally

### Status

Completed

### What I Built

- Added `uvicorn` as a runtime dependency.
- Ran the FastAPI app locally.
- Opened Swagger UI for the API.
- Manually tested valid and invalid `/analyze` requests.
- Documented test, run, and Swagger UI commands in the README.
- Documented the `413` response in the OpenAPI route metadata.

### Commands Run

```bash
uv add uvicorn
uv run uvicorn ai_roadmap.api:app --reload
uv run pytest
uv run ruff check .
uv run mypy src
```

### Test Results

- `pytest`: 7 passed
- `ruff`: all checks passed
- `mypy`: no issues found in 5 source files

### What I Learned

- `uvicorn` starts an ASGI server and loads the FastAPI app.
- Swagger UI makes it easy to inspect and manually test live endpoints.
- Manual testing complements automated tests but does not replace them.
- README run instructions make the project easier to use later.

### What Was Difficult

- Understanding why a runtime `HTTPException` response does not automatically appear in Swagger UI.
- Distinguishing command documentation from test automation.
- Checking the correct app import path for `uvicorn`.

### Tutor Review Summary

- The app runs locally with `uvicorn`.
- Swagger UI is reachable at `/docs`.
- Manual valid and invalid requests behave as expected.
- The README documents the local workflow.
- `pytest`, `ruff`, and `mypy` all pass.

### Next Step

- Start Lesson 2.7 and complete the Phase 2 review.

## 2026-05-11 — Lesson 2.7 — Phase Review

### Status

Completed

### What I Built

- Reviewed the completed FastAPI phase.
- Removed the unused `main.py` placeholder.
- Added cache directories to `.gitignore`.
- Verified the API structure, README, tests, linting, and type checks.

### Commands Run

```bash
uv run pytest
uv run ruff check .
uv run mypy src
```

### Test Results

- `pytest`: 7 passed
- `ruff`: all checks passed
- `mypy`: no issues found in 5 source files

### What I Learned

- A FastAPI request flows through request parsing, Pydantic validation, route logic, response model creation, and JSON serialization.
- Validation belongs at the request boundary when it protects business logic from invalid input.
- Business logic and application-level errors belong in the route or service layer.
- Positive and negative endpoint tests provide confidence in API behavior.

### What Was Difficult

- Distinguishing request validation from application-level checks.
- Reviewing project structure instead of only checking whether tests pass.
- Identifying cleanup work such as unused entry points and cache ignore rules.

### Tutor Review Summary

- Phase 2 has a working FastAPI endpoint for text analysis.
- The API uses Pydantic models, validation, route-level error handling, and endpoint tests.
- The project structure separates app creation, routes, schemas, and text-analysis logic.
- The README documents test and local run commands.
- `pytest`, `ruff`, and `mypy` all pass.

### Next Step

- Start Phase 3 and connect the backend to an LLM API.

## 2026-05-12 — Lesson 3.1 — LLM API Concepts and Setup

### Status

Completed

### What I Built

- Chose OpenAI as the external LLM provider for the main Phase 3 path.
- Chose `OPENAI_API_KEY` as the API key environment variable.
- Added environment file ignore rules.
- Added a safe `.env.example` file without real secrets.
- Confirmed that tests should use mocks or fakes instead of real LLM API calls.

### Commands Run

```bash
uv run pytest
uv run ruff check .
uv run mypy src
```

### Test Results

- `pytest`: 7 passed
- `ruff`: all checks passed
- `mypy`: no issues found in 5 source files

### What I Learned

- Real LLM API calls make tests slow, costly, non-deterministic, and dependent on external availability.
- API keys must stay out of git because they grant access to paid external services.
- `.env` stores local secrets and should be ignored.
- `.env.example` documents required variables with safe placeholder values.

### What Was Difficult

- Placing `.env.example` at the project root instead of inside the Python package.
- Separating real local secrets from safe repository documentation.
- Defining the test boundary before implementing the AI client.

### Tutor Review Summary

- The provider choice is explicit.
- The API key environment variable name is explicit.
- Real secrets are ignored by git.
- `.env.example` is safe to commit.
- `pytest`, `ruff`, and `mypy` all pass.

### Next Step

- Start Lesson 3.2 and create the AI client boundary.

## 2026-05-12 — Lesson 3.2 — AI Client Boundary

### Status

Completed

### What I Built

- Created an `ai_client.py` module.
- Added `OPENAI_API_KEY_ENV` for the provider API key environment variable.
- Added `AIClientConfigurationError` for missing or invalid client configuration.
- Added `get_openai_api_key()` to read the API key from the environment.
- Added tests for configured, missing, and blank API key values.

### Commands Run

```bash
uv run pytest
uv run ruff check .
uv run mypy src
```

### Test Results

- `pytest`: 10 passed
- `ruff`: all checks passed
- `mypy`: no issues found in 6 source files

### What I Learned

- Provider configuration should be isolated from FastAPI route handlers.
- Missing secrets should fail with clear configuration errors.
- Small client boundaries are easier to test because they have fewer responsibilities.
- Tests can control environment variables with `monkeypatch`.

### What Was Difficult

- Keeping tests under `tests/` instead of inside the package.
- Testing exceptions with `pytest.raises`.
- Making the missing-key test independent of local developer environment variables.

### Tutor Review Summary

- The AI client boundary is separate from route logic.
- API keys are not hardcoded.
- Missing and blank API key cases are handled intentionally.
- Tests do not call the real OpenAI API.
- `pytest`, `ruff`, and `mypy` all pass.

### Next Step

- Start Lesson 3.3 and design prompt structure plus typed AI output.

## 2026-05-12 — Lesson 3.3 — Prompt Design and Structured Output

### Status

Completed

### What I Built

- Added `AIAnalyzeResponse` for structured AI analysis output.
- Restricted `sentiment` to `positive`, `neutral`, or `negative`.
- Added tests for valid and invalid structured AI output.
- Added a prompt builder for AI text analysis.
- Added prompt tests for required fields, sentiment values, input text, and additional-field restrictions.

### Commands Run

```bash
uv run pytest
uv run ruff check .
uv run mypy src
```

### Test Results

- `pytest`: 17 passed
- `ruff`: all checks passed
- `mypy`: no issues found in 7 source files

### What I Learned

- Structured output is easier for APIs and frontends to consume than free-form text.
- AI output should be validated because generated data can be malformed or unexpected.
- Prompts need explicit instructions about fields, allowed values, and output format.
- Literal types can constrain values such as sentiment.

### What Was Difficult

- Writing tests for Pydantic validation errors.
- Keeping prompt tests useful without making them too brittle.
- Remembering that a clear prompt does not guarantee valid model output.

### Tutor Review Summary

- The AI output schema is explicit.
- Sentiment values are constrained.
- The prompt asks for JSON using the expected schema.
- Tests validate both schema behavior and important prompt contents.
- `pytest`, `ruff`, and `mypy` all pass.

### Next Step

- Start Lesson 3.4 and add the `/ai/analyze` endpoint behind a testable AI client boundary.

## 2026-05-12 — Lesson 3.4 — AI Analyze Endpoint

### Status

Completed

### What I Built

- Added `analyze_text_with_ai()` as a testable AI client boundary function.
- Added `POST /ai/analyze`.
- Reused `AnalyzeRequest` for validated text input.
- Returned `AIAnalyzeResponse` for structured AI output.
- Added an endpoint test that patches the AI client boundary with a fake response.

### Commands Run

```bash
uv run pytest
uv run ruff check .
uv run mypy src
```

### Test Results

- `pytest`: 19 passed
- `ruff`: all checks passed
- `mypy`: no issues found in 7 source files

### What I Learned

- Route handlers should orchestrate HTTP flow and delegate provider work to a client boundary.
- The AI client should own provider-specific details and external call behavior.
- Endpoint tests should avoid real provider calls by using fakes or mocks.
- Structured output makes frontend rendering and API contracts easier.

### What Was Difficult

- Patching the function in the route module where it is used.
- Keeping the endpoint thin while still returning a typed response.
- Separating validation, route orchestration, and provider-boundary behavior.

### Tutor Review Summary

- `POST /ai/analyze` exists and returns structured JSON through `AIAnalyzeResponse`.
- The route uses a testable AI client boundary.
- Tests do not call a real LLM provider.
- `pytest`, `ruff`, and `mypy` all pass.

### Next Step

- Start Lesson 3.5 and improve mocked external API call tests.

## 2026-05-13 — Lesson 3.5 — Mocking External API Calls

### Status

Completed

### What I Built

- Improved `/ai/analyze` endpoint tests with fake AI client behavior.
- Tested the successful AI response path without real provider calls.
- Tested the AI client configuration failure path without real provider calls.
- Verified that request text is passed to the AI client boundary.

### Commands Run

```bash
uv run pytest
uv run ruff check .
uv run mypy src
```

### Test Results

- `pytest`: 20 passed
- `ruff`: all checks passed
- `mypy`: no issues found in 7 source files

### What I Learned

- Real LLM calls make automated tests slow, costly, non-deterministic, and dependent on external systems.
- Fakes can provide minimal replacement behavior for external services.
- Mocked endpoint tests should still verify request flow, status codes, and response bodies.
- Failure tests can prove that provider errors are translated into controlled API responses.

### What Was Difficult

- Patching the function where the route uses it instead of where it was originally defined.
- Distinguishing direct client tests from endpoint tests.
- Keeping fakes simple while still proving important behavior.

### Tutor Review Summary

- Tests do not require a real API key.
- Tests do not make real network calls.
- Success and failure cases for `/ai/analyze` are covered.
- The test setup is understandable and uses the AI client boundary correctly.
- `pytest`, `ruff`, and `mypy` all pass.

### Next Step

- Start Lesson 3.6 and handle provider errors, retries, rate limits, and cost.

## 2026-05-18 — Lesson 3.6 — Errors, Retries, Rate Limits, and Cost

### Status

Completed

### What I Built

- Added `AIProviderError` for provider-level failures.
- Added `is_retryable_ai_error()` to classify retry-safe AI errors.
- Added `run_with_ai_retry()` with one retry for retryable provider failures.
- Added route-level handling for AI provider failures.
- Added tests for retry success, retry exhaustion, and non-retryable configuration errors.

### Commands Run

```bash
uv run pytest
uv run ruff check .
uv run mypy src
```

### Test Results

- `pytest`: 28 passed
- `ruff`: all checks passed
- `mypy`: no issues found in 7 source files

### What I Learned

- Temporary provider failures can be retryable, but configuration and validation errors should not be retried.
- Retries can increase cost because each retry may be another provider call.
- API responses should avoid exposing raw provider internals.
- Tests can verify retry behavior by counting fake operation calls.

### What Was Difficult

- Understanding why the second provider error is naturally re-raised.
- Avoiding artificial exceptions that replace the original failure context.
- Keeping retry logic limited instead of adding broad retry loops.

### Tutor Review Summary

- Retry behavior is intentionally limited and testable.
- Non-retryable configuration errors are not retried.
- Provider failures are translated into controlled API errors.
- `pytest`, `ruff`, and `mypy` all pass.

### Next Step

- Start Lesson 3.7 and review the completed Phase 3 LLM API work.

## 2026-05-18 — Lesson 3.7 — Phase Review

### Status

Completed

### What I Built

- Reviewed the completed Phase 3 LLM API work.
- Verified secret handling with `.env.example` and `.gitignore`.
- Reviewed AI client boundaries, mocked tests, structured output, and README instructions.
- Confirmed the AI endpoint returns structured JSON through the backend contract.

### Commands Run

```bash
uv run pytest
uv run ruff check .
uv run mypy src
git status --short
```

### Test Results

- `pytest`: 28 passed
- `ruff`: all checks passed
- `mypy`: no issues found in 7 source files

### What I Learned

- Secrets should be documented with examples but never committed as real values.
- Tests should fake LLM provider calls to stay deterministic and cost-free.
- Structured AI responses are easier for frontends to render.
- Provider errors should be translated into stable API errors.

### What Was Difficult

- Distinguishing the intended provider flow from the still-unimplemented external provider call.
- Reviewing the full phase across configuration, routes, schemas, prompts, tests, and documentation.

### Tutor Review Summary

- Phase 3 is reviewed and ready for a frontend phase.
- Tests avoid real LLM calls.
- API keys are not committed.
- README documents setup and endpoints.
- `pytest`, `ruff`, and `mypy` all pass.

### Next Step

- Complete the optional local Ollama provider lesson or move on to Phase 4.

## 2026-05-18 — Optional Lesson 3.x — Local LLM Provider with Ollama

### Status

Completed

### What I Built

- Verified local Ollama installation and available models.
- Manually tested `llama3:latest` through `ollama run` and Ollama's HTTP API.
- Added `parse_ollama_ai_response()` to parse and validate Ollama output.
- Added `analyze_text_with_ollama()` as an optional local provider client.
- Added Ollama JSON-mode payload support with `format: "json"`.
- Added tests for parsing, request errors, HTTP status errors, and successful local-provider behavior without real network calls.
- Updated README with optional Ollama instructions.

### Commands Run

```bash
ollama --version
ollama list
ollama run llama3:latest
curl http://127.0.0.1:11434/api/generate
uv run pytest
uv run ruff check .
uv run mypy src
uv run python
```

### Test Results

- `pytest`: 37 passed
- `ruff`: all checks passed
- `mypy`: no issues found in 7 source files

### What I Learned

- Local LLM providers can avoid external API costs and keep data local.
- Local models can still produce malformed or non-JSON output.
- Ollama's HTTP API returns the model output inside a `response` field.
- Ollama JSON mode improves structured output but does not replace validation.
- Automated tests should not require Ollama, a local model, or network access.

### What Was Difficult

- Understanding why a model can answer with Markdown or explanations even when asked for JSON.
- Debugging the difference between raw Ollama HTTP JSON and the nested model response string.
- Keeping the local provider optional instead of replacing the external-provider boundary.

### Tutor Review Summary

- The optional Ollama provider stays behind the AI client boundary.
- Tests use fakes and do not require Ollama to be running.
- Provider request and response failures are translated into `AIProviderError`.
- Manual integration with `llama3:latest` works.
- `pytest`, `ruff`, and `mypy` all pass.

### Next Step

- Start Phase 4 and build the React AI UI.

## 2026-05-18 — Lesson 4.1 — Frontend Project Setup

### Status

Completed

### What I Built

- Created a React + TypeScript frontend project in `phase-04-react-ui`.
- Verified the Vite development server at `http://localhost:5173/`.
- Added `.env.example` with `VITE_API_BASE_URL`.
- Replaced the template README with project-specific frontend setup instructions.
- Verified frontend linting and production build.

### Commands Run

```bash
node --version
npm --version
pnpm --version
pnpm create vite phase-04-react-ui --template react-ts
pnpm install
pnpm run dev
pnpm run lint
pnpm run build
```

### Test Results

- `pnpm run lint`: passed
- `pnpm run build`: passed

### What I Learned

- Frontend setup should be stable before UI features are built.
- Vite exposes only environment variables prefixed with `VITE_` to browser code.
- Frontend environment variables are public and must not contain secrets.
- `node_modules/`, `dist/`, local `.env` files, logs, and editor files should stay ignored.
- The React app will later communicate with FastAPI through HTTP JSON endpoints.

### What Was Difficult

- Noticing that `phase-04-react-ui` is not currently inside a shared root Git repository.
- Distinguishing public frontend configuration from backend secrets.
- Understanding which generated files should be committed and which should stay ignored.

### Tutor Review Summary

- React + TypeScript setup is complete.
- The Vite dev server starts locally.
- `VITE_API_BASE_URL` is documented in `.env.example`.
- README explains install, dev server, and checks.
- Frontend lint and build checks pass.

### Next Step

- Start Lesson 4.2 and build the first text analyzer form for `POST /analyze`.

## 2026-05-18 — Lesson 4.2 — Text Analyzer Form

### Status

Completed

### What I Built

- Replaced the default Vite UI with a simple text analyzer form.
- Added controlled textarea state.
- Added submit handling with `preventDefault()`.
- Added a typed `AnalyzeResponse` shape in the frontend.
- Called the FastAPI `POST /analyze` endpoint from React.
- Rendered word, character, and sentence counts.
- Added backend CORS configuration for the local Vite dev server.

### Commands Run

```bash
pnpm run lint
pnpm run build
uv run pytest
uv run ruff check .
uv run mypy src
uv run uvicorn ai_roadmap.api:app --reload
```

### Test Results

- Backend `pytest`: 37 passed
- Backend `ruff`: all checks passed
- Backend `mypy`: no issues found in 7 source files
- Frontend `pnpm run lint`: passed
- Frontend `pnpm run build`: passed

### What I Learned

- React controlled inputs keep form state in component state.
- Form submit handlers need `preventDefault()` to avoid a browser page reload.
- The frontend sends JSON with a `text` field to the backend.
- The backend returns `word_count`, `character_count`, and `sentence_count`.
- Browser requests can fail because of CORS when frontend and backend use different origins.

### What Was Difficult

- Choosing the correct React submit event type for the installed React type definitions.
- Understanding why CORS must be configured on the backend.
- Keeping the first API call focused on the deterministic `/analyze` endpoint before using AI endpoints.

### Tutor Review Summary

- The text analyzer form works against the local FastAPI backend.
- The frontend uses the configured API base URL.
- The response is rendered as separate statistics.
- The AI endpoint is not used yet.
- Backend and frontend checks pass.

### Next Step

- Start Lesson 4.3 and add loading, error, and empty states.

## 2026-05-21 — Lesson 4.3 — Loading, Error, and Empty States

### Status

Completed

### What I Built

- Added frontend test tooling with Vitest, jsdom, React Testing Library, user-event, and jest-dom.
- Added a Vitest jsdom setup file with test cleanup and mock restoration.
- Added tests for rendering the form, empty input validation, loading state, success state, API error state, stale result cleanup, and network error behavior.
- Added empty input validation in the React UI.
- Added loading state and disabled the submit button while a request is running.
- Added controlled error messages for failed API responses and network failures.
- Removed stale results when analysis fails.

### Commands Run

```bash
pnpm add -D vitest jsdom @testing-library/react @testing-library/user-event @testing-library/jest-dom
pnpm run test
pnpm run lint
pnpm run build
```

### Test Results

- `pnpm run test`: 8 passed
- `pnpm run lint`: passed
- `pnpm run build`: passed

### What I Learned

- Frontend tests should focus on user-visible behavior.
- React Testing Library needs a DOM-like environment such as jsdom.
- `@testing-library/jest-dom` adds useful matchers such as `toBeInTheDocument`.
- Tests should clean up rendered components and restore mocks between test cases.
- Empty input should be handled in the frontend for UX and in the backend for safety.
- Network failures and HTTP error responses are different failure modes.

### What Was Difficult

- Setting up Vitest with jsdom and jest-dom matchers.
- Understanding why tests initially rendered multiple copies of the app without cleanup.
- Distinguishing API error responses from rejected `fetch` calls.
- Keeping old success results from staying visible after failed requests.

### Tutor Review Summary

- Loading, empty, success, API error, and network error states are covered.
- The submit button is disabled during loading.
- Empty input does not call the backend.
- Error messages are controlled and do not expose raw backend details.
- Frontend tests, lint, and build all pass.

### Next Step

- Start Lesson 4.4 and build the UI for structured AI analysis with `POST /ai/analyze`.

## 2026-05-22 — Lesson 4.4 — AI Analyze UI

### Status

Completed

### What I Built

- Added an `Analyze with AI` UI action.
- Added a typed frontend `AiAnalyzeResponse` shape.
- Called the backend `POST /ai/analyze` endpoint from the React UI.
- Rendered structured AI output: summary, sentiment, topics, and action items.
- Rendered clear empty states for missing topics and action items.
- Added controlled AI error messages for failed API responses and network failures.
- Added AI loading behavior to prevent duplicate submissions.
- Connected the backend AI boundary to the optional Ollama provider through `AI_PROVIDER=ollama`.
- Manually verified the full React + FastAPI + Ollama flow.

### Commands Run

```bash
pnpm run test
pnpm run lint
pnpm run build
uv run pytest
uv run ruff check .
uv run mypy src
AI_PROVIDER=ollama uv run uvicorn ai_roadmap.api:app --reload
pnpm run dev
```

### Test Results

- Frontend `pnpm run test`: passed
- Frontend `pnpm run lint`: passed
- Frontend `pnpm run build`: passed
- Backend `pytest`: passed
- Backend `ruff`: all checks passed
- Backend `mypy`: no issues found

### What I Learned

- Structured AI output is easier to render because each field maps to a clear UI element.
- Empty arrays should render explicit empty states instead of blank UI.
- Frontend tests should fake API responses and should not require Ollama or FastAPI by default.
- AI provider failures should be shown as controlled user-facing errors.
- Frontend sentiment handling assumes the backend returns one of `positive`, `neutral`, or `negative`.
- A local Ollama provider can be used for manual full-stack testing while automated tests stay offline.

### What Was Difficult

- Avoiding accidental form submission from the `Analyze with AI` button.
- Handling AI error responses before treating them as structured AI data.
- Keeping old AI results from staying visible after an AI failure.
- Understanding where to connect the optional Ollama provider without making tests depend on it.

### Tutor Review Summary

- The AI UI calls `/ai/analyze` and renders structured output.
- Topics and action items are displayed as lists, with clear empty states.
- AI loading and error behavior are covered.
- Frontend tests cover success, empty lists, API errors, network errors, and loading behavior without real provider calls.
- Manual full-stack testing with `AI_PROVIDER=ollama` works.

### Next Step

- Start Lesson 4.5 and extract frontend API request logic into a typed React API client boundary.

## 2026-05-26 — Lesson 4.5 — React API Client Boundary

### Status

Completed

### What I Built

- Created a small frontend API client module.
- Added typed `AnalyzeResponse` and `AiAnalyzeResponse` response shapes.
- Added `analyzeText()` for `POST /analyze`.
- Added `analyzeTextWithAI()` for `POST /ai/analyze`.
- Added `ApiClientError` for normalized API client failures.
- Extracted shared JSON POST behavior into a small internal helper.
- Updated `App.tsx` to use the API client instead of calling `fetch` directly.
- Manually verified both analyzer workflows through the browser.

### Commands Run

```bash
pnpm run test
pnpm run lint
pnpm run build
AI_PROVIDER=ollama uv run uvicorn ai_roadmap.api:app --reload
pnpm run dev
```

### Test Results

- `pnpm run test`: 20 passed
- `pnpm run lint`: passed
- `pnpm run build`: passed

### What I Learned

- Fetch logic should move out of UI components to reduce duplication and centralize request behavior.
- A frontend API client can own endpoint URLs, headers, request bodies, and response typing.
- `ApiClientError` gives components a stable error shape without exposing raw backend details.
- Good API boundaries should stay small and understandable.
- The frontend API boundary mirrors the backend AI client boundary: each layer hides technical details from the layer above it.

### What Was Difficult

- Keeping API-client errors distinct between HTTP failures and network failures.
- Avoiding an API client abstraction that is too generic for the current app.
- Understanding which tests belong at the API-client boundary and which should stay focused on UI behavior.

### Tutor Review Summary

- `App.tsx` no longer contains raw endpoint URLs or direct `fetch` calls.
- Request and response shapes are typed in the API client.
- API failures are normalized before they reach the component.
- Both text analysis and AI analysis workflows work manually.
- Frontend tests, lint, and build all pass.

### Next Step

- Start Lesson 4.6 and review/refine frontend tests now that API-client tests exist.

## 2026-06-05 — Lesson 4.6 — Frontend Testing Basics

### Status

Completed

### What I Built

- Reviewed and refined frontend tests after introducing the API client boundary.
- Kept App tests focused on user-visible behavior such as rendering, validation, loading, success, and error states.
- Kept endpoint URL and request body checks in `apiClient.test.ts`.
- Verified that frontend tests fake API behavior instead of requiring the real FastAPI backend.

### Commands Run

```bash
pnpm run test
pnpm run lint
pnpm run build
```

### Test Results

- `pnpm run test`: 19 passed
- `pnpm run lint`: passed
- `pnpm run build`: passed

### What I Learned

- Frontend tests should verify behavior that users can observe.
- Tests should avoid calling the real backend by default because that makes them slower and less deterministic.
- Component tests should focus on UI behavior, while API client tests should verify request details and API boundary behavior.
- A brittle frontend test depends too much on implementation details such as exact markup structure, internal state, or endpoint details in the wrong test layer.
- Full-stack behavior still needs manual or end-to-end verification because mocked frontend tests do not prove that backend, CORS, environment variables, and provider setup all work together.

### What Was Difficult

- Distinguishing useful behavior checks from implementation-detail checks.
- Understanding why endpoint assertions belong in API client tests instead of App component tests.
- Recognizing which behavior is covered by unit/component tests and which behavior still needs full-stack verification.

### Tutor Review Summary

- Frontend tests cover rendering, validation, loading, success, API error, network error, stale result cleanup, and AI analysis behavior.
- API client tests cover `/analyze` and `/ai/analyze` request behavior.
- Tests do not require FastAPI or Ollama to be running.
- Frontend tests, lint, and build all pass.

### Next Step

- Start Lesson 4.7 and manually verify the full React + FastAPI workflow locally.

## 2026-06-05 — Lesson 4.7 — Full-Stack Local Run

### Status

Completed

### What I Built

- Ran the FastAPI backend locally on `http://127.0.0.1:8000`.
- Ran the React frontend locally on `http://localhost:5173/`.
- Manually verified the normal text analyzer workflow through the browser.
- Manually verified the AI analyzer workflow through the browser with the local Ollama provider.
- Confirmed that the browser console did not show CORS or request errors.
- Updated the frontend README with local full-stack setup instructions.

### Commands Run

```bash
AI_PROVIDER=ollama uv run uvicorn ai_roadmap.api:app --reload
pnpm run dev
pnpm run test
pnpm run lint
pnpm run build
```

### Test Results

- `pnpm run test`: 19 passed
- `pnpm run lint`: passed
- `pnpm run build`: passed
- Manual `/analyze` browser test: passed
- Manual `/ai/analyze` browser test with Ollama: passed

### What I Learned

- The full-stack app needs the FastAPI backend, the React frontend, and Ollama for local AI analysis.
- Browser-based apps can hit CORS rules when frontend and backend run on different origins.
- Browser console output, frontend UI state, backend logs, and provider logs help locate whether a failure is frontend, backend, network, or provider related.
- README instructions should include requirements, environment variables, install steps, server startup commands, checks, and manual verification steps.
- Clear local development instructions lower the entry barrier for future contributors.

### What Was Difficult

- Keeping automated frontend tests separate from manual full-stack verification.
- Understanding which server is responsible for which part of the workflow.
- Making the README accurate now that the frontend calls the backend.

### Tutor Review Summary

- Backend and frontend run at the same time.
- The browser UI can reach the FastAPI backend.
- CORS is handled intentionally and no browser CORS errors appeared during verification.
- README documents the local full-stack workflow.
- Manual verification covers both analyzer workflows.

### Next Step

- Start Lesson 4.8 and review the complete React UI phase.

## 2026-06-05 — Lesson 4.8 — Phase Review

### Status

Completed

### What I Built

- Reviewed the completed React UI phase.
- Verified frontend tests, linting, and production build.
- Verified backend tests, linting, and type checking before the phase review.
- Reviewed frontend project structure, API client boundary, UI states, and README setup instructions.
- Added cleanup behavior so a new analysis run clears stale statistics, stale AI results, and stale error messages.
- Added frontend tests for clearing stale results when switching between normal analysis and AI analysis.

### Commands Run

```bash
pnpm run test
pnpm run lint
pnpm run build
uv run pytest
uv run ruff check .
uv run mypy src
```

### Test Results

- `pnpm run test`: 21 passed
- `pnpm run lint`: passed
- `pnpm run build`: passed
- Backend `pytest`: 37 passed
- Backend `ruff`: all checks passed
- Backend `mypy`: no issues found in 7 source files

### What I Learned

- The frontend validates user input, sends valid requests through the API client, and renders success or error states based on the response.
- The frontend API boundary lives in `apiClient.ts`.
- Frontend tests avoid real backend or LLM calls by faking request behavior.
- Clear UI states include idle, validation error, loading, success, API error, network error, and empty AI lists.
- Before adding persistence, stale UI state should be cleaned up so users can trust which result belongs to the current run.

### What Was Difficult

- Deciding whether normal analysis results and AI analysis results should stay visible together.
- Distinguishing component test responsibilities from API client test responsibilities.
- Identifying which behavior is fully covered by tests and which behavior still needs manual full-stack verification.

### Tutor Review Summary

- Frontend and backend verification commands pass.
- The API client boundary is clear and keeps request details out of the React component.
- Tests do not require FastAPI or Ollama by default.
- README explains the full-stack local workflow.
- The UI is ready for the next phase, with the main remaining improvement being stronger runtime validation of API responses before scaling the app further.

### Next Step

- Start Phase 5 and add persistence around analysis results.

## 2026-06-05 — Lesson 5.1 — Persistence Concepts and Setup

### Status

Completed

### What I Built

- Chose Docker Compose as the local PostgreSQL setup strategy.
- Added a local PostgreSQL service with `postgres:17`.
- Added `DATABASE_URL` to `.env.example`.
- Updated the backend README with local PostgreSQL startup and shutdown instructions.
- Verified that PostgreSQL starts locally and exposes port `5432`.

### Commands Run

```bash
docker --version
docker compose version
docker compose config
docker compose up -d postgres
docker compose ps
uv run pytest
uv run ruff check .
uv run mypy src
pnpm run test
pnpm run lint
pnpm run build
```

### Test Results

- PostgreSQL container: running with `postgres:17`
- `docker compose config`: valid
- Backend checks: passed
- Frontend checks: passed

### What I Learned

- Persistence adds durable storage so analysis inputs and outputs can be stored beyond a single request.
- The app should eventually store user input, normal text statistics, AI responses, provider metadata, and timestamps.
- The database connection string should be configured through environment variables such as `DATABASE_URL`.
- Automated tests should avoid depending on an uncontrolled local database because that makes them slower and less deterministic.
- Local database setup should document Docker Compose commands, environment variables, ports, and how to stop the service.

### What Was Difficult

- Understanding the difference between a valid Compose file and a container that actually keeps running.
- Debugging the PostgreSQL 18 Docker image data directory behavior.
- Choosing a conservative PostgreSQL version for a stable learning setup.

### Tutor Review Summary

- Docker Compose is a good fit for the local persistence setup.
- `postgres:17` is running locally and avoids the Postgres 18 data directory surprise.
- `DATABASE_URL` is documented but not used by application code yet.
- No persistence code, migrations, or database tables were added in this lesson.
- Existing backend and frontend checks still pass.

### Next Step

- Start Lesson 5.2 and design the first database schema and migration.

## 2026-06-05 — Lesson 5.2 — Database Schema and Migrations

### Status

Completed

### What I Built

- Added SQLAlchemy, Alembic, and psycopg as backend runtime dependencies.
- Initialized Alembic migrations in the backend project.
- Configured Alembic to read `DATABASE_URL` from the environment.
- Designed the `analysis_runs` table for normal text analysis and AI analysis history.
- Created and applied the first migration.
- Documented migration commands in the backend README.

### Commands Run

```bash
uv add sqlalchemy alembic psycopg[binary]
uv run python -c "import sqlalchemy; import alembic; import psycopg; print('ok')"
uv run alembic init migrations
uv run alembic revision -m "create analysis runs table"
uv run ruff check migrations
DATABASE_URL=postgresql+psycopg://ai_roadmap:ai_roadmap_dev_password@127.0.0.1:5432/ai_roadmap uv run alembic upgrade head
DATABASE_URL=postgresql+psycopg://ai_roadmap:ai_roadmap_dev_password@127.0.0.1:5432/ai_roadmap uv run alembic current
docker compose exec postgres psql -U ai_roadmap -d ai_roadmap -c "\d analysis_runs"
docker compose exec postgres psql -U ai_roadmap -d ai_roadmap -c "select * from alembic_version;"
uv run pytest
uv run ruff check .
uv run mypy src
```

### Test Results

- Backend `pytest`: 37 passed
- Backend `ruff`: all checks passed
- Backend `mypy`: no issues found in 7 source files
- Alembic current version: `651c16e02b39 (head)`
- Database schema verification: `analysis_runs` table exists

### What I Learned

- Migrations make schema changes reproducible and reviewable.
- `analysis_runs` stores the stable history fields: `id`, `analysis_type`, `input_text`, counts, and `created_at`.
- AI analysis history also stores `summary`, `sentiment`, `topics`, `action_items`, and `provider`.
- Secrets, API keys, provider debug payloads, stack traces, and unnecessary personal data should not be stored in history.
- The schema can support embeddings later because each stored analysis has a stable UUID that future embedding records can reference.

### What Was Difficult

- Translating table design into Alembic and SQLAlchemy column definitions.
- Understanding the difference between SQL-like pseudocode and Python migration code.
- Keeping database URLs consistent between `.env.example`, README, and Alembic commands.
- Understanding why SQLAlchemy uses `postgresql+psycopg://` to identify the PostgreSQL driver explicitly.

### Tutor Review Summary

- Alembic is initialized and reads `DATABASE_URL` from the environment.
- The first migration creates `analysis_runs` with UUID primary keys, JSONB list fields, timestamps, and check constraints.
- The migration was applied successfully to local PostgreSQL.
- README documents how to run migrations and check the current migration version.
- Existing backend checks still pass.

### Next Step

- Start Lesson 5.3 and create a backend repository boundary for analysis history.

## 2026-06-07 — Lesson 5.3 — Backend Repository Boundary

### Status

Completed

### What I Built

- Added a SQLAlchemy Core table definition for `analysis_runs`.
- Added `AnalysisRunCreate` as the typed input contract for new records.
- Added `AnalysisRun` as the typed output contract for stored records.
- Added `save_analysis_run()` to translate repository input into a SQLAlchemy insert.
- Added repository unit tests for normal text analysis and structured AI analysis.

### Commands Run

```bash
uv run pytest tests/test_analysis_repository.py
uv run pytest
uv run ruff check .
uv run mypy src
```

### Test Results

- Repository tests: 4 passed
- Full backend test suite: 41 passed
- `ruff`: all checks passed
- `mypy`: no issues found in 8 source files

### What I Learned

- A repository owns persistence operations such as storing and later loading analysis records.
- Routes should not contain raw table, SQL statement, or database connection details.
- `AnalysisRunCreate` crosses the business-to-repository boundary when a new record is stored.
- `AnalysisRun` represents a record returned from persistence with its database-generated ID and timestamp.
- Repository mapping can be unit tested by mocking the SQLAlchemy connection and inspecting the executed statement.
- A controlled integration test will still be useful later to prove the statement works against PostgreSQL.

### What Was Difficult

- Distinguishing Python type annotations from SQLAlchemy column definitions.
- Understanding the expected arguments for `sa.Table`.
- Understanding why a SQLAlchemy connection uses `connection.execute(statement)`.
- Deciding which apparent duplication represents separate contracts rather than unnecessary repetition.

### Tutor Review Summary

- Database access now has a small, explicit repository boundary.
- Routes remain free of database and SQLAlchemy details.
- Create and stored-record contracts are intentionally separate.
- Tests cover insert mapping for both normal and AI analysis records without using a real database.
- The design avoids premature generic repository abstractions.

### Next Step

- Start Lesson 5.4 and persist successful `/analyze` and `/ai/analyze` results.

## 2026-06-08 — Lesson 5.4 — Store Analysis Results

### Status

Completed

### What I Built

- Added database configuration helpers for reading `DATABASE_URL`, creating a cached SQLAlchemy engine, and yielding transactional connections.
- Added FastAPI database dependency wiring through `get_connection`.
- Updated `/analyze` to store successful text analysis results.
- Updated `/ai/analyze` to store successful AI analysis results, including provider, summary, sentiment, topics, and action items.
- Kept existing endpoint response shapes stable while adding persistence.
- Added API tests that verify successful storage and that failed requests do not create history rows.
- Manually verified that both `/analyze` and `/ai/analyze` create records in local PostgreSQL.

### Commands Run

```bash
uv run pytest tests/test_database.py
uv run pytest tests/test_api.py
uv run pytest
uv run ruff check .
uv run mypy src
DATABASE_URL=postgresql+psycopg://ai_roadmap:ai_roadmap_dev_password@127.0.0.1:5432/ai_roadmap AI_PROVIDER=ollama uv run uvicorn ai_roadmap.api:app --reload
curl -X POST http://127.0.0.1:8000/analyze -H "Content-Type: application/json" -d '{"text":"Persistence works."}'
curl -X POST http://127.0.0.1:8000/ai/analyze -H "Content-Type: application/json" -d '{"text":"AI Engineering is fun."}'
docker compose exec postgres psql -U ai_roadmap -d ai_roadmap -c "SELECT analysis_type, input_text, word_count, character_count, sentence_count FROM analysis_runs ORDER BY created_at DESC LIMIT 1;"
docker compose exec postgres psql -U ai_roadmap -d ai_roadmap -c "SELECT analysis_type, input_text, word_count, summary, sentiment, topics, action_items, provider FROM analysis_runs ORDER BY created_at DESC LIMIT 1;"
```

### Test Results

- Backend `pytest`: 47 passed
- Backend `ruff`: all checks passed
- Backend `mypy`: no issues found in 9 source files
- Manual `/analyze` persistence test: passed
- Manual `/ai/analyze` persistence test with Ollama: passed

### What I Learned

- Storage happens after successful analysis and before the response is returned.
- Persistence can be added without changing the public API response shape.
- Validation failures, oversized payloads, AI configuration failures, and provider failures should not create successful history rows.
- API tests can fake the database dependency and AI provider call so automated tests do not require PostgreSQL or Ollama.
- Stored fields such as input text, analysis type, provider, timestamps, counts, and structured AI output are useful for later debugging and history features.

### What Was Difficult

- Understanding that FastAPI dependencies must be overridden separately from monkeypatched functions.
- Patching functions where they are used, such as `ai_roadmap.routes.analyze_text_with_ai`.
- Deciding how to handle database failures as part of the successful request contract.
- Avoiding accidental real database access in automated API tests.

### Tutor Review Summary

- Successful `/analyze` requests are persisted.
- Successful `/ai/analyze` requests are persisted.
- Existing endpoint responses remain stable.
- Failed requests do not create successful history rows.
- Automated tests avoid real database and LLM calls by using dependency overrides and fakes.
- Manual verification confirms records are written to PostgreSQL.

### Next Step

- Start Lesson 5.5 and expose stored analysis history through a backend API endpoint.

## 2026-06-09 — Lesson 5.5 — History API Endpoint

### Status

Completed

### What I Built

- Added `AnalysisHistoryResponse` as the typed API contract for stored history records.
- Added repository support for loading analysis records newest first with a configurable limit.
- Added `GET /analyses` with a default limit of 20 and an allowed range from 1 to 100.
- Added API tests for empty history, populated history, response serialization, and invalid limits.
- Manually verified the endpoint against local PostgreSQL.

### Commands Run

```bash
uv run pytest tests/test_api.py -k list_analyses -vv
uv run pytest tests/test_api.py -k invalid_limit -vv
uv run pytest
uv run ruff check .
uv run mypy src
curl "http://127.0.0.1:8000/analyses?limit=2"
```

### Test Results

- Backend `pytest`: 53 passed
- Backend `ruff`: all checks passed
- Backend `mypy`: no issues found in 9 source files
- Manual PostgreSQL history request: passed
- History limit and newest-first ordering: verified

### What I Learned

- History endpoints need deterministic ordering so clients receive stable, predictable results.
- A limit keeps response size, database work, and request duration bounded.
- Empty history is represented by an empty JSON array.
- A dedicated response model separates the public API contract from internal database records.
- The frontend will need identity, timestamp, analysis type, input text, count fields, and optional AI result fields to render useful history entries.

### What Was Difficult

- Mapping repository dataclasses into an explicit API response model.
- Remembering that UUID and datetime values are serialized to JSON strings.
- Testing request validation without accidentally calling the repository.
- Deciding which persisted fields belong in the public history response.

### Tutor Review Summary

- `GET /analyses` returns typed stored history records.
- Records are ordered newest first and bounded by a validated limit.
- Empty and populated responses are covered without real database or LLM calls.
- Invalid limits return `422` before repository access.
- Manual verification confirms the endpoint returns persisted PostgreSQL records.

### Next Step

- Start Lesson 5.6 and add a frontend history view.

## 2026-06-10 — Lesson 5.6 — Frontend History View

### Status

Completed

### What I Built

- Added a typed frontend API-client function for `GET /analyses`.
- Added a focused `HistorySection` component below the analyzer.
- Added automatic history loading when the application opens.
- Added automatic refresh after successful text and AI analyses.
- Added loading, empty, success, error, and retry behavior.
- Rendered text and AI history fields conditionally.
- Added responsive single-column styling and removed unused template CSS.

### Commands Run

```bash
pnpm exec vitest run src/apiClient.test.ts
pnpm exec vitest run src/HistorySection.test.tsx
pnpm exec vitest run src/App.test.tsx
pnpm run test
pnpm run lint
pnpm run build
```

### Test Results

- Frontend `vitest`: 36 passed
- Frontend `eslint`: no errors
- Frontend production build: passed
- Manual PostgreSQL, backend, and frontend history flow: passed
- Browser console and responsive layout verification: passed

### What I Learned

- History loads on application startup and refreshes only after successful analyses.
- HTTP request construction belongs in the frontend API-client boundary.
- Component tests can mock API-client functions without using a real backend.
- App tests mock `HistorySection` so they test refresh-key integration without duplicating component behavior.
- History needs explicit loading, empty, success, and error states.
- Failed analyses do not refresh history because they do not create persisted records.

### What Was Difficult

- Avoiding synchronous state updates directly inside an effect.
- Preventing stale asynchronous requests from updating an unmounted component.
- Separating `App` integration tests from `HistorySection` request tests.
- Updating older fetch-based tests after adding an automatic request on mount.
- Keeping list markup semantic while conditionally rendering AI fields.

### Tutor Review Summary

- The API client owns the typed history request and error conversion.
- `HistorySection` has a focused responsibility and independently tested UI states.
- Successful text and AI analyses trigger history refreshes.
- Failed analyses leave the refresh key unchanged.
- Automated tests do not require PostgreSQL or the backend.
- Manual verification confirms persisted records appear newest first in the frontend.

### Next Step

- Start Lesson 5.7 and verify the complete persistence workflow from PostgreSQL through the backend to the frontend.

## 2026-06-11 — Lesson 5.7 — Full-Stack Persistence Run

### Status

Completed

### What I Built

- Added a repository-level README for the complete local full-stack workflow.
- Documented setup and startup for PostgreSQL, migrations, Ollama, FastAPI, and React.
- Added persistence verification instructions for normal and AI analyses.
- Added direct PostgreSQL queries for inspecting the newest stored records.
- Added service-specific troubleshooting and shutdown instructions.
- Linked both project READMEs to the central full-stack guide.

### Commands Run

```bash
docker compose up -d postgres
docker ps
DATABASE_URL=postgresql+psycopg://ai_roadmap:ai_roadmap_dev_password@127.0.0.1:5432/ai_roadmap uv run alembic upgrade head
DATABASE_URL=postgresql+psycopg://ai_roadmap:ai_roadmap_dev_password@127.0.0.1:5432/ai_roadmap uv run alembic current
ollama list
curl -sS http://127.0.0.1:11434/api/tags
curl -sS http://127.0.0.1:8000/openapi.json
curl -sS "http://127.0.0.1:8000/analyses?limit=1"
docker compose exec postgres psql -U ai_roadmap -d ai_roadmap -c "SELECT analysis_type, input_text, word_count, character_count, sentence_count, created_at FROM analysis_runs WHERE analysis_type = 'text' ORDER BY created_at DESC LIMIT 1;"
docker compose exec postgres psql -U ai_roadmap -d ai_roadmap -c "SELECT analysis_type, input_text, summary, sentiment, topics, action_items, provider, created_at FROM analysis_runs WHERE analysis_type = 'ai' ORDER BY created_at DESC LIMIT 1;"
uv run pytest
uv run ruff check .
uv run mypy src
pnpm run test
pnpm run lint
pnpm run build
```

### Test Results

- Backend `pytest`: 53 passed
- Backend `ruff`: all checks passed
- Backend `mypy`: no issues found in 9 source files
- Frontend `vitest`: 36 passed
- Frontend `eslint`: no errors
- Frontend production build: passed
- PostgreSQL and Alembic startup: passed
- Normal analysis persistence: verified in the UI and PostgreSQL
- AI analysis persistence with Ollama: verified in the UI and PostgreSQL
- Browser console and Network tab: no errors

### What I Learned

- PostgreSQL, FastAPI, React, and Ollama must run for the complete AI persistence workflow.
- Direct SQL queries provide independent proof that API results were persisted.
- Browser tools, Uvicorn logs, Docker logs, SQL queries, and Ollama diagnostics isolate failures by layer.
- Manual full-stack verification catches integration and configuration problems that isolated tests cannot reproduce.
- Containerizing the frontend and backend could later allow the complete stack to start through Docker Compose.

### What Was Difficult

- Coordinating several long-running services and their environment variables.
- Distinguishing a failed exact SQL text match from a failed persistence operation.
- Discovering that textarea input contained additional newline characters.
- Keeping startup instructions explicit about working directories and terminal ownership.
- Writing database verification queries that remain robust despite small input differences.

### Tutor Review Summary

- The complete local stack runs with PostgreSQL, Ollama, FastAPI, and React.
- Alembic migrations are applied before persistence verification.
- Normal and AI analyses are stored and immediately appear in frontend history.
- Direct PostgreSQL queries confirm both record types.
- The central README documents setup, startup, verification, troubleshooting, automated checks, and shutdown.
- Backend and frontend checks pass after the full-stack run.

### Next Step

- Start Lesson 5.8 and complete the Phase 5 review.

## 2026-06-11 — Lesson 5.8 — Phase Review

### Status

Completed

### What I Built

- Reviewed the complete PostgreSQL persistence flow across backend and frontend.
- Added deterministic history ordering by `created_at DESC` and `id DESC`.
- Added the `ix_analysis_runs_created_at_id` database index in a new Alembic migration.
- Applied and verified migration revision `db220f8d2751`.
- Updated the full-stack README with the current migration revision.

### Commands Run

```bash
uv run pytest
uv run ruff check .
uv run mypy src
pnpm run test
pnpm run lint
pnpm run build
DATABASE_URL=postgresql+psycopg://ai_roadmap:ai_roadmap_dev_password@127.0.0.1:5432/ai_roadmap uv run alembic upgrade head
DATABASE_URL=postgresql+psycopg://ai_roadmap:ai_roadmap_dev_password@127.0.0.1:5432/ai_roadmap uv run alembic current
docker compose exec postgres psql -U ai_roadmap -d ai_roadmap -c "\d analysis_runs"
```

### Test Results

- Backend `pytest`: 53 passed
- Backend `ruff`: all checks passed
- Backend `mypy`: no issues found in 9 source files
- Frontend `vitest`: 36 passed
- Frontend `eslint`: no errors
- Frontend production build: passed
- Alembic revision: `db220f8d2751 (head)`
- PostgreSQL index: `ix_analysis_runs_created_at_id` verified

### What I Learned

- Phase 5 persists normal and AI analyses in PostgreSQL and exposes them through the history API and frontend.
- The repository layer owns database access and keeps persistence details out of route handlers.
- Alembic migrations provide an ordered and reversible history of schema changes.
- Tests replace database and LLM dependencies with controlled fakes or mocks.
- Deterministic ordering needs a secondary key when timestamps can be equal.
- Query indexes should match frequently used filtering and ordering patterns.
- Analysis history and semantic-search data have different responsibilities.

### What Was Difficult

- Distinguishing the complete persistence behavior from the final ordering optimization.
- Understanding why ordering only by a timestamp is not fully deterministic.
- Deciding whether embeddings belong directly in the existing history table.
- Evaluating migration metadata without introducing incomplete autogeneration support.

### Tutor Review Summary

- Persistence works across PostgreSQL, FastAPI, React, and the optional Ollama provider.
- Repository, API, and frontend boundaries are clearly separated and covered by tests.
- History queries are limited, deterministic, and supported by a composite index.
- Migrations are documented, applied locally, and reversible.
- Automated tests do not require a real PostgreSQL or LLM service.
- `analysis_runs` should remain the analysis history; Phase 6 should use a separate document or chunk model for embeddings.

### Next Step

- Start Phase 6 by designing the document, chunk, embedding-model, vector-dimension, and similarity-search boundaries.

## 2026-06-11 — Phase 6 Preparation — Embeddings and Semantic Search

### Status

Ready to start

### What I Prepared

- Designed a separate `notes` domain for semantic search.
- Selected PostgreSQL with pgvector instead of an additional vector database.
- Selected local Ollama embeddings with `qwen3-embedding:0.6b`.
- Fixed the vector dimension at 1024.
- Defined a shared API shape for keyword and semantic search.
- Planned React workflows for creating and searching notes.
- Added nine Phase 6 lesson files.
- Updated the roadmap and task tracker for Phase 6.

### Architecture Decisions

- `analysis_runs` remains the analysis-history model.
- Notes are stored as complete texts in Phase 6.
- Document upload and chunking remain in Phase 7.
- Stored notes use document embeddings without a retrieval instruction.
- Search queries use a stable English retrieval instruction.
- Keyword search uses PostgreSQL full-text search.
- Semantic search uses exact pgvector cosine distance before considering approximate indexes.
- Automated tests mock database and Ollama boundaries by default.

### Lesson Plan

- Lesson 6.1 — Embedding and Vector Search Concepts
- Lesson 6.2 — pgvector Setup and Notes Schema
- Lesson 6.3 — Embedding Client Boundary
- Lesson 6.4 — Store Notes with Embeddings
- Lesson 6.5 — Keyword Search
- Lesson 6.6 — Semantic Search
- Lesson 6.7 — Notes and Search UI
- Lesson 6.8 — Full-Stack Search Comparison
- Lesson 6.9 — Phase Review

### Next Step

- Start Lesson 6.1 and review the embedding, vector-dimension, similarity, and domain-boundary concepts.

## 2026-06-15 — Lesson 6.1 — Embedding and Vector Search Concepts

### Status

Completed

### What I Designed

- Separated searchable notes from the existing `analysis_runs` history.
- Defined notes as human-readable `title` and `content`.
- Defined embeddings as derived numerical representations rather than domain content.
- Defined search results as notes combined with search mode and relevance metadata.
- Fixed the embedding model at `qwen3-embedding:0.6b` with 1024 dimensions.
- Defined separate document and instructed query embedding inputs.
- Kept document chunking outside Phase 6.

### Commands Run

```bash
uv run pytest
uv run ruff check .
uv run mypy src
pnpm run test
pnpm run lint
pnpm run build
```

### Test Results

- Backend `pytest`: 53 passed
- Backend `ruff`: all checks passed
- Backend `mypy`: no issues found in 9 source files
- Frontend `vitest`: 36 passed
- Frontend `eslint`: no errors
- Frontend production build: passed

### What I Learned

- Keyword search depends on lexical overlap, while semantic search can retrieve related meanings expressed with different words.
- An embedding does not contain priority or accuracy; similarity appears only when vectors are compared.
- Vectors with different dimensions cannot be compared.
- Vectors from different models occupy incompatible semantic spaces even when their dimensions match.
- Smaller cosine distance means greater semantic similarity.
- Note creation and semantic search are separate workflows.
- Short notes can use one embedding, while long Phase 7 documents need chunks for focused retrieval and citations.

### What Was Difficult

- Separating keyword matches from semantic matches in examples without shared words.
- Distinguishing the responsibilities of notes, embeddings, and search results.
- Understanding the difference between a technically impossible dimension mismatch and a semantically invalid model mismatch.
- Keeping note creation separate from the search workflow.

### Tutor Review Summary

- The note, embedding, and search-result boundaries are now clear.
- `analysis_runs` remains independent from semantic-search data.
- The model and 1024-dimensional vector contract are explicit.
- Document and query embedding inputs have separate purposes.
- Cosine distance ordering and the need for consistent embedding spaces are understood.
- Phase 6 remains focused on complete notes; document chunking remains in Phase 7.

### Next Step

- Start Lesson 6.2 and add pgvector plus the initial `notes` schema through Alembic.

## 2026-06-19 — Lesson 6.2 — pgvector Setup and Notes Schema

### Status

Completed

### What I Built

- Switched the local PostgreSQL container image to `pgvector/pgvector:pg17`.
- Created Alembic revision `6ee40cc8e639_create_notes_table.py`.
- Enabled the PostgreSQL `vector` extension through the migration.
- Created the `notes` table with `title`, `content`, `embedding`, `embedding_model`, `created_at`, and `updated_at`.
- Set `notes.embedding` to `vector(1024)` for `qwen3-embedding:0.6b`.
- Added non-blank database constraints for `title`, `content`, and `embedding_model`.
- Documented pgvector and the notes embedding schema in the backend README.

### Commands Run

```bash
docker compose down -v
docker compose up -d postgres
docker compose exec postgres psql -U ai_roadmap -d ai_roadmap -c "CREATE EXTENSION IF NOT EXISTS vector;"
docker compose exec postgres psql -U ai_roadmap -d ai_roadmap -c "SELECT extname FROM pg_extension WHERE extname = 'vector';"
uv run alembic revision -m "create notes table"
uv run ruff check migrations
DATABASE_URL=postgresql+psycopg://ai_roadmap:ai_roadmap_dev_password@127.0.0.1:5432/ai_roadmap uv run alembic upgrade head
DATABASE_URL=postgresql+psycopg://ai_roadmap:ai_roadmap_dev_password@127.0.0.1:5432/ai_roadmap uv run alembic current
docker compose exec postgres psql -U ai_roadmap -d ai_roadmap -c "\d notes"
docker compose exec postgres psql -U ai_roadmap -d ai_roadmap -c "SELECT extname FROM pg_extension WHERE extname IN ('pgcrypto', 'vector');"
uv run pytest
uv run ruff check .
uv run mypy src
```

### Test Results

- Backend `pytest`: 53 passed
- Backend `ruff`: all checks passed
- Backend `mypy`: no issues found in 9 source files
- Alembic revision: `6ee40cc8e639 (head)`
- PostgreSQL extensions: `pgcrypto` and `vector` verified
- `notes.embedding`: verified as `vector(1024)`
- Notes constraints: title, content, and embedding model non-blank checks verified

### What I Learned

- `vector(1024)` is part of the schema because the database must reject vectors with the wrong dimension.
- A 768-dimensional embedding cannot be stored in a `vector(1024)` column and should also be rejected by application validation later.
- Enabling `vector` in a migration makes the extension part of the reproducible schema history.
- HNSW and IVFFlat are approximate nearest-neighbor indexes that trade recall and configuration complexity for speed.
- Exact vector search is the right starting point until data volume and query latency justify an approximate index.
- Changing the embedding model requires regenerating stored embeddings.

### What Was Difficult

- Distinguishing storing vectors from enforcing their dimensional contract.
- Understanding why a wrong-dimension vector should not enter the database.
- Understanding why approximate vector indexes are deferred until after correctness and measurement.
- Handling the local PostgreSQL volume reset after switching to a pgvector-enabled image.

### Tutor Review Summary

- The local PostgreSQL service now uses a pgvector-enabled image.
- The migration follows the existing Alembic chain after `db220f8d2751`.
- The `notes` table uses `vector(1024)` and required text constraints.
- The `vector` extension is enabled through migration, not only manually.
- No premature approximate vector index was added.
- Backend checks and schema verification pass.

### Next Step

- Start Lesson 6.3 and implement a typed Ollama embedding-client boundary with validation and mocked provider tests.

## 2026-06-22 — Lesson 6.3 — Embedding Client Boundary

### Status

Completed

### What I Built

- Added embedding-client configuration for `qwen3-embedding:0.6b`.
- Fixed the embedding contract at 1024 dimensions.
- Added the local Ollama `/api/embed` endpoint and timeout configuration.
- Implemented parsing for Ollama embedding responses.
- Validated that provider responses contain exactly one finite 1024-dimensional vector.
- Rejected missing, malformed, wrong-sized, non-finite, boolean, and multi-embedding responses.
- Added separate document and query embedding functions.
- Added a stable retrieval instruction only for search-query embeddings.
- Converted Ollama request and HTTP-status failures into `AIProviderError`.
- Added tests that mock `httpx` and do not require Ollama to run.

### Commands Run

```bash
uv run pytest tests/test_ai_client.py
uv run pytest
uv run ruff check .
uv run mypy src
```

### Test Results

- Backend `test_ai_client.py`: 35 passed
- Backend `pytest`: 69 passed
- Backend `ruff`: all checks passed
- Backend `mypy`: no issues found in 9 source files

### What I Learned

- Ollama's embedding response is nested because one request can return embeddings for one or more input texts.
- Embedding vectors must contain only finite numeric values because `NaN` and infinity cannot produce meaningful similarity scores.
- Stored notes use plain document embeddings, while search queries use an instruction to shape them for retrieval.
- Transport errors and HTTP-status errors belong behind the AI client boundary.
- Routes should not call `httpx` directly because provider details, retries, validation, and error mapping should stay centralized.

### What Was Difficult

- Understanding why `dict[str, object]` is too strict for typed test dictionaries and why `Mapping[str, object]` works better.
- Remembering that Python treats `bool` as a subclass of `int`.
- Distinguishing wrong response shape from wrong vector dimension.
- Keeping document embedding inputs and query embedding inputs intentionally different.

### Tutor Review Summary

- The embedding client boundary is isolated from routes and persistence.
- The request shape matches the local Ollama embed API.
- Provider responses are validated before a vector leaves the client boundary.
- Query and document embedding functions are separated clearly.
- Tests mock the provider boundary and keep automated checks deterministic.
- Backend checks pass.

### Next Step

- Start Lesson 6.4 and persist notes with generated embeddings through a repository and service boundary.

## 2026-06-23 — Lesson 6.4 — Store Notes with Embeddings

### Status

Completed

### What I Built

- Added typed note domain objects for creating and returning stored notes.
- Added `NoteCreateRequest` with non-blank `title` and `content` validation.
- Added `NoteResponse` without exposing raw embeddings.
- Implemented a notes repository that inserts notes with embeddings and returns stored note metadata.
- Converted Python embedding lists into pgvector-compatible string values at the database boundary.
- Implemented a notes service that coordinates document embedding generation and persistence.
- Ensured embedding failures prevent note inserts.
- Added `POST /notes` with safe provider and configuration error mapping.
- Added repository, service, schema, and API tests for note creation.

### Commands Run

```bash
uv run pytest
uv run ruff check .
uv run mypy src
git diff --check
```

### Test Results

- Backend `pytest`: 88 passed
- Backend `ruff`: all checks passed
- Backend `mypy`: no issues found in 11 source files
- `git diff --check`: no whitespace issues

### What I Learned

- The service layer coordinates embedding generation and persistence.
- The repository layer should only know how to store and return data.
- Raw embeddings are internal retrieval data and should not be returned to API clients.
- Partial note creation is prevented by generating the embedding before calling the repository insert.
- Deterministic title/content formatting matters because embeddings depend on the exact input text.
- Provider and configuration failures before persistence must not create database records.

### What Was Difficult

- Distinguishing service orchestration from repository persistence.
- Understanding why `RETURNING` is needed to get generated `id`, `created_at`, and `updated_at` values.
- Mocking chained database result calls in repository tests.
- Ensuring tests actually prove that `save_note` is not called when embedding generation fails.
- Keeping API responses useful without leaking raw vectors.

### Tutor Review Summary

- Note creation now has clear request, service, repository, and response boundaries.
- The route contains no raw SQL and no Ollama response parsing.
- The service builds one document embedding before persistence.
- Provider and configuration errors are mapped to safe HTTP responses.
- Validation prevents blank note fields before the service runs.
- Backend checks pass.

### Next Step

- Start Lesson 6.5 and add keyword search over stored notes.

## 2026-06-24 — Lesson 6.5 — Keyword Search

### Status

Completed

### What I Built

- Added a shared `SearchResult` domain model for keyword and future semantic search.
- Added `SearchResultResponse` without exposing raw embeddings.
- Implemented PostgreSQL full-text keyword search across note titles and content.
- Used `to_tsvector`, `websearch_to_tsquery`, the `@@` match operator, and `ts_rank`.
- Added deterministic ordering by score, `created_at`, and `id`.
- Added bounded `limit` handling for keyword search.
- Added `search_notes` in the service layer for `mode=keyword`.
- Added `GET /notes/search` with query, mode, and limit validation.
- Verified keyword mode does not call the embedding provider.

### Commands Run

```bash
uv run pytest
uv run ruff check .
uv run mypy src
```

### Test Results

- Backend `pytest`: 100 passed
- Backend `ruff`: all checks passed
- Backend `mypy`: no issues found in 11 source files

### What I Learned

- PostgreSQL full-text search tokenizes and normalizes text, while `LIKE` only performs substring matching.
- The `@@` operator checks whether a `tsvector` matches a `tsquery`.
- `ts_rank` provides a relevance score for matched results.
- Secondary ordering is needed because equal scores should still produce stable API results.
- Keyword mode must avoid the embedding provider so it remains a fast, deterministic lexical baseline.
- Keyword search can miss relevant notes that use different words, synonyms, or misspelled terms.

### What Was Difficult

- Understanding the relationship between `to_tsvector`, `websearch_to_tsquery`, `@@`, and `ts_rank`.
- Handling SQLAlchemy's PostgreSQL `REGCONFIG` literal for the `english` search configuration.
- Testing SQL behavior without relying too much on brittle full SQL-string matching.
- Keeping keyword search separate from the embedding client before semantic search is added.

### Tutor Review Summary

- Keyword search is implemented at the repository boundary with PostgreSQL full-text search.
- Results use the shared search-result shape and do not expose embeddings.
- The API validates query text, search mode, and result limits.
- Ordering is ranked and deterministic.
- Keyword mode is isolated from embedding-provider calls.
- Backend checks pass.

### Next Step

- Start Lesson 6.6 and add semantic search with query embeddings and pgvector ordering.
