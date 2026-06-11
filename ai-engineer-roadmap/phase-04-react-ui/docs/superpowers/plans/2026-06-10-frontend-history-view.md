# Frontend History View Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Load and display the newest persisted analysis records below the analyzer, including loading, empty, success, error, retry, and automatic refresh behavior.

**Architecture:** `apiClient.ts` owns the typed `GET /analyses` request. A focused `HistorySection` component owns history request state and rendering. `App` increments a refresh key after successful analyses so the component reloads persisted data without coupling it to the analysis workflows.

**Tech Stack:** React 19, TypeScript, Vite, Vitest, Testing Library

---

## File Structure

- Modify `src/apiClient.ts`: add the history response type and GET request function.
- Modify `src/apiClient.test.ts`: cover history request construction and failures.
- Create `src/HistorySection.tsx`: own history loading and rendering.
- Create `src/HistorySection.test.tsx`: cover component states and refresh behavior.
- Modify `src/App.tsx`: render the component and trigger refreshes after successful analyses.
- Modify `src/App.test.tsx`: cover integration between analysis success and history refresh.
- Modify `src/App.css`: add restrained layout styles for the history section.

### Task 1: Typed History API Client

**Files:**
- Modify: `src/apiClient.ts`
- Test: `src/apiClient.test.ts`

- [ ] **Step 1: Write a failing success-path test**

Add a test that imports `loadAnalysisHistory`, mocks `fetch`, and returns one complete history record:

```ts
it("loads analysis history with the default limit", async () => {
  const history = [
    {
      id: "12345678-1234-5678-1234-567812345678",
      analysis_type: "ai" as const,
      input_text: "AI Engineering is fun.",
      word_count: 4,
      character_count: 22,
      sentence_count: 1,
      summary: "Short summary",
      sentiment: "positive" as const,
      topics: ["AI"],
      action_items: [],
      provider: "ollama",
      created_at: "2026-06-10T08:00:00Z",
    },
  ];

  const fetchSpy = vi.spyOn(globalThis, "fetch").mockResolvedValue(
    new Response(JSON.stringify(history), {
      status: 200,
      headers: { "Content-Type": "application/json" },
    }),
  );

  const result = await loadAnalysisHistory();

  expect(fetchSpy).toHaveBeenCalledWith(
    `${import.meta.env.VITE_API_BASE_URL}/analyses?limit=20`,
    expect.objectContaining({ method: "GET" }),
  );
  expect(result).toEqual(history);
});
```

- [ ] **Step 2: Run the focused test and verify RED**

Run:

```bash
pnpm run test -- src/apiClient.test.ts
```

Expected: compilation or import failure because `loadAnalysisHistory` does not exist.

- [ ] **Step 3: Add the response type and minimal GET helper**

Add:

```ts
export type AnalysisHistoryItem = {
  id: string;
  analysis_type: "text" | "ai";
  input_text: string;
  word_count: number;
  character_count: number;
  sentence_count: number;
  summary: string | null;
  sentiment: "positive" | "neutral" | "negative" | null;
  topics: string[];
  action_items: string[];
  provider: string | null;
  created_at: string;
};
```

Add a typed GET helper that mirrors the existing POST error handling:

```ts
async function getJson<TResponse>(path: string): Promise<TResponse> {
  try {
    const response = await fetch(
      `${import.meta.env.VITE_API_BASE_URL}${path}`,
      { method: "GET" },
    );

    if (!response.ok) {
      throw new ApiClientError("API request failed");
    }

    return (await response.json()) as TResponse;
  } catch (error) {
    if (error instanceof ApiClientError) {
      throw error;
    }

    throw new ApiClientError("Network error");
  }
}

export async function loadAnalysisHistory(
  limit = 20,
): Promise<AnalysisHistoryItem[]> {
  return getJson<AnalysisHistoryItem[]>(`/analyses?limit=${limit}`);
}
```

- [ ] **Step 4: Run the focused test and verify GREEN**

Run:

```bash
pnpm run test -- src/apiClient.test.ts
```

Expected: all API-client tests pass.

- [ ] **Step 5: Add HTTP and network failure tests**

Add separate tests asserting that a non-OK response and a rejected `fetch`
cause `loadAnalysisHistory()` to reject with the existing public messages:

```ts
await expect(loadAnalysisHistory()).rejects.toThrow("API request failed");
```

```ts
await expect(loadAnalysisHistory()).rejects.toThrow("Network error");
```

- [ ] **Step 6: Verify the complete API-client test file**

Run:

```bash
pnpm run test -- src/apiClient.test.ts
```

Expected: all API-client tests pass without warnings.

### Task 2: History Loading and Empty States

**Files:**
- Create: `src/HistorySection.tsx`
- Create: `src/HistorySection.test.tsx`

- [ ] **Step 1: Write a failing loading-state test**

Mock `loadAnalysisHistory` with a promise that does not resolve, render
`<HistorySection refreshKey={0} />`, and assert:

```ts
expect(screen.getByText("Loading history...")).toBeInTheDocument();
```

- [ ] **Step 2: Run the focused test and verify RED**

Run:

```bash
pnpm run test -- src/HistorySection.test.tsx
```

Expected: import failure because `HistorySection` does not exist.

- [ ] **Step 3: Create the component with request state**

Create a component with this public contract:

```ts
type HistorySectionProps = {
  refreshKey: number;
};
```

Use `useEffect` to call `loadAnalysisHistory()` on mount and whenever
`refreshKey` changes. Store:

```ts
const [history, setHistory] = useState<AnalysisHistoryItem[]>([]);
const [isLoading, setIsLoading] = useState(true);
const [errorMessage, setErrorMessage] = useState<string | null>(null);
```

Render a `<section aria-labelledby="history-heading">` with the heading
`Recent analyses` and the loading text while the request is pending.

- [ ] **Step 4: Verify the loading test passes**

Run:

```bash
pnpm run test -- src/HistorySection.test.tsx
```

Expected: loading test passes.

- [ ] **Step 5: Write a failing empty-state test**

Resolve `loadAnalysisHistory` with `[]` and assert:

```ts
expect(await screen.findByText("No analyses yet.")).toBeInTheDocument();
```

- [ ] **Step 6: Add the minimal empty-state rendering**

After loading succeeds, render `No analyses yet.` when `history.length === 0`.

- [ ] **Step 7: Verify loading and empty states**

Run:

```bash
pnpm run test -- src/HistorySection.test.tsx
```

Expected: both tests pass.

### Task 3: History Success Rendering

**Files:**
- Modify: `src/HistorySection.tsx`
- Modify: `src/HistorySection.test.tsx`

- [ ] **Step 1: Write a failing text-record rendering test**

Resolve the API call with a text record and assert that the UI displays:

```txt
Text
AI Engineering is fun.
Words: 4
Characters: 22
Sentences: 1
```

Also assert a date is rendered using the record's `created_at` value. Avoid
asserting a locale-specific full string; locate the `<time>` element and assert
its `dateTime` attribute equals the original ISO value.

- [ ] **Step 2: Implement the common record fields**

Render records in a semantic list. Each item contains:

- a visible `Text` or `AI` label
- `<time dateTime={item.created_at}>`
- input text
- word, character, and sentence counts

Format visible date text with:

```ts
const dateFormatter = new Intl.DateTimeFormat(undefined, {
  dateStyle: "medium",
  timeStyle: "short",
});
```

- [ ] **Step 3: Verify text-record rendering**

Run:

```bash
pnpm run test -- src/HistorySection.test.tsx
```

Expected: text history record test passes.

- [ ] **Step 4: Write a failing AI-record rendering test**

Resolve with an AI record and assert summary, sentiment, topic, action item,
and provider are displayed.

- [ ] **Step 5: Implement conditional AI fields**

Only render:

- summary when non-null
- sentiment when non-null
- provider when non-null
- topics when `topics.length > 0`
- action items when `action_items.length > 0`

- [ ] **Step 6: Verify success rendering**

Run:

```bash
pnpm run test -- src/HistorySection.test.tsx
```

Expected: text and AI record tests pass.

### Task 4: History Error and Retry

**Files:**
- Modify: `src/HistorySection.tsx`
- Modify: `src/HistorySection.test.tsx`

- [ ] **Step 1: Write a failing error-state test**

Reject `loadAnalysisHistory` and assert:

```ts
expect(
  await screen.findByText("Could not load analysis history."),
).toBeInTheDocument();
expect(screen.getByRole("button", { name: "Retry" })).toBeInTheDocument();
```

- [ ] **Step 2: Implement the error state**

Catch request failures, clear stale history, and set the general message:

```ts
"Could not load analysis history."
```

Render a `Retry` button only in the error state.

- [ ] **Step 3: Write a failing retry test**

Make the first call reject and the second resolve with `[]`. Click `Retry` and
assert:

```ts
expect(loadAnalysisHistory).toHaveBeenCalledTimes(2);
expect(await screen.findByText("No analyses yet.")).toBeInTheDocument();
```

- [ ] **Step 4: Implement retry without changing the public props**

Extract the request into a component-local async function. Call it from both
the effect and the retry button.

- [ ] **Step 5: Verify error and retry behavior**

Run:

```bash
pnpm run test -- src/HistorySection.test.tsx
```

Expected: all history component tests pass.

### Task 5: Refresh After Successful Analyses

**Files:**
- Modify: `src/App.tsx`
- Modify: `src/App.test.tsx`
- Modify: `src/HistorySection.test.tsx`

- [ ] **Step 1: Write a failing refresh-key component test**

Render `HistorySection` with `refreshKey={0}`, wait for the first request,
rerender with `refreshKey={1}`, and assert:

```ts
expect(loadAnalysisHistory).toHaveBeenCalledTimes(2);
```

- [ ] **Step 2: Verify the existing effect satisfies the refresh contract**

Run:

```bash
pnpm run test -- src/HistorySection.test.tsx
```

Expected: test passes if `refreshKey` is correctly included in the effect
dependency list; otherwise update only that dependency.

- [ ] **Step 3: Write a failing App integration test**

Mock `HistorySection` as a test component that renders its `refreshKey`. Mock a
successful `analyzeText`, submit the form, and assert the displayed key changes
from `0` to `1`.

- [ ] **Step 4: Render HistorySection and increment after success**

In `App`:

```ts
const [historyRefreshKey, setHistoryRefreshKey] = useState(0);
```

Render:

```tsx
<HistorySection refreshKey={historyRefreshKey} />
```

After each successful analysis result:

```ts
setHistoryRefreshKey((current) => current + 1);
```

Do not increment it in `catch` or `finally`.

- [ ] **Step 5: Add successful AI and failed-analysis coverage**

Verify:

- successful AI analysis increments the key
- failed text analysis does not increment it
- failed AI analysis does not increment it

- [ ] **Step 6: Verify App integration tests**

Run:

```bash
pnpm run test -- src/App.test.tsx
```

Expected: all App tests pass.

### Task 6: Layout and Final Verification

**Files:**
- Modify: `src/App.css`
- Modify: `src/App.tsx`
- Modify: `src/HistorySection.tsx`

- [ ] **Step 1: Replace inline layout styles with focused classes**

Add stable single-column layout classes for:

- app content
- analyzer form
- history section
- history list
- history item
- compact metadata and count rows

Keep the history below the analyzer and ensure the layout works at narrow
viewport widths. Do not add navigation, nested cards, or a two-column desktop
layout.

- [ ] **Step 2: Run all frontend checks**

Run:

```bash
pnpm run test
pnpm run lint
pnpm run build
```

Expected:

- all Vitest tests pass
- ESLint reports no errors
- TypeScript and Vite production build succeeds

- [ ] **Step 3: Manually verify against the backend**

Start PostgreSQL, backend, and frontend. Verify:

- history loads when the app opens
- newest records appear first
- successful text analysis adds a new history entry
- successful AI analysis adds a structured history entry
- the browser console contains no errors

- [ ] **Step 4: Request final review**

Provide the modified files and command output for review against the Lesson 5.6
acceptance criteria.

## Version Control Note

No commit steps are included because `phase-04-react-ui` is not currently
inside a Git repository. If the project is later placed under Git, commit after
each completed task rather than combining the entire lesson into one commit.
