# Frontend History View Design

## Goal

Add a compact history section below the existing text analyzer. The section
loads persisted analysis records from the backend and handles loading, empty,
success, and error states without requiring a real backend in automated tests.

## Scope

- Load the newest 20 analysis records when the application opens.
- Reload history after a successful text or AI analysis.
- Do not reload history after a failed analysis.
- Display the history below the analyzer in the existing single-column flow.
- Keep HTTP request details inside `apiClient.ts`.
- Do not add navigation, pagination, filtering, or a separate history page.

## Architecture

### API Client

`apiClient.ts` owns the history response type and the HTTP request.

- Add an `AnalysisHistoryItem` type matching `GET /analyses`.
- Add `loadAnalysisHistory(limit = 20)`.
- Add an internal typed GET helper that uses the existing API base URL and
  converts HTTP or network failures into `ApiClientError`.

### Application

`App.tsx` continues to own the analysis workflows. It stores a numeric history
refresh key and increments it after successful text and AI analyses.

Failed analyses do not change the refresh key.

### History Component

Create `HistorySection.tsx` as a focused component.

- It receives the refresh key as a prop.
- It loads history on initial mount.
- It reloads whenever the refresh key changes.
- It owns its loading, result, and error state.
- A retry button starts another history request after a failure.

## UI States

The history section renders one state at a time:

- Loading: `Loading history...`
- Empty: `No analyses yet.`
- Error: a general failure message and a `Retry` button
- Success: a newest-first list of analysis records

Each record displays:

- analysis type (`Text` or `AI`)
- formatted creation date and time
- input text
- word, character, and sentence counts
- summary and sentiment for AI records
- topics and action items only when they contain values

Dates are formatted with `Intl.DateTimeFormat`.

## Data Flow

1. `HistorySection` mounts.
2. It calls `loadAnalysisHistory(20)`.
3. The API client requests `GET /analyses?limit=20`.
4. The component renders loading, empty, success, or error state.
5. A successful analysis increments the refresh key in `App`.
6. `HistorySection` observes the changed key and loads the newest history.

## Error Handling

- Backend error details are not rendered directly.
- History failures do not break the analyzer form or remove current analysis
  results.
- Retry affects only the history request.
- A failed text or AI analysis does not trigger a history reload.

## Testing

### API Client Tests

Verify:

- correct URL and GET method
- default limit of 20
- typed response data is returned
- HTTP failures become `ApiClientError`
- network failures become `ApiClientError`

### History Component Tests

Mock `loadAnalysisHistory` and verify:

- loading state
- empty state
- successful record rendering
- conditional AI fields
- error state
- retry behavior
- reload when the refresh key changes

### Application Tests

Mock API-client functions and verify:

- successful text analysis refreshes history
- successful AI analysis refreshes history
- failed analyses do not refresh history

## Acceptance Criteria

- History loads automatically when the app opens.
- The newest 20 persisted records can be rendered.
- Successful analyses refresh history immediately.
- Empty, loading, success, and error states are visible and tested.
- Automated tests do not call the real backend.
- Request construction remains inside the frontend API client.
