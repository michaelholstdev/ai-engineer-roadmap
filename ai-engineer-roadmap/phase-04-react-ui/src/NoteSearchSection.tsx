import { useState } from "react";
import type { ChangeEvent, SubmitEvent } from "react";
import {
  searchNotes,
  type SearchMode,
  type SearchResultResponse,
} from "./apiClient";
import SearchResultsList from "./SearchResultsList";

const NoteSearchSection = () => {
  const [query, setQuery] = useState("");
  const [limit, setLimit] = useState(10);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [mode, setMode] = useState<SearchMode>("keyword");
  const [results, setResults] = useState<SearchResultResponse[]>([]);
  const [hasSearched, setHasSearched] = useState(false);

  const handleQueryChange = (event: ChangeEvent<HTMLInputElement>) => {
    setQuery(event.target.value);
  };

  const handleLimitChange = (event: ChangeEvent<HTMLInputElement>) => {
    setLimit(Number(event.target.value));
  };

  const handleSubmit = async (event: SubmitEvent) => {
    try {
      event.preventDefault();
      setIsLoading(true);
      setErrorMessage(null);

      if (query.trim() === "") {
        setErrorMessage("Please enter a search query.");
        return;
      }

      setErrorMessage(null);
      const data = await searchNotes({
        query,
        mode,
        limit,
      });

      setResults(data);
      setHasSearched(true);
    } catch {
      setResults([]);
      setHasSearched(false);
      setErrorMessage("Could not search notes. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <section className="notes-section" aria-labelledby="search-notes-heading">
      <h2 id="search-notes-heading">Search notes</h2>

      <form className="note-form" onSubmit={handleSubmit}>
        <label htmlFor="note-search-query">Search query</label>
        <input
          id="note-search-query"
          value={query}
          onChange={handleQueryChange}
        />

        <label htmlFor="note-search-limit">Result limit</label>
        <input
          id="note-search-limit"
          type="number"
          min="1"
          max="50"
          value={limit}
          onChange={handleLimitChange}
        />

        <div>
          <button
            type="button"
            aria-pressed={mode === "keyword"}
            onClick={() => setMode("keyword")}
          >
            Keyword
          </button>
          <button
            type="button"
            aria-pressed={mode === "semantic"}
            onClick={() => setMode("semantic")}
          >
            Semantic
          </button>
        </div>

        <p>Scores are only comparable within the selected search mode.</p>

        {errorMessage && <p>{errorMessage}</p>}

        <button type="submit" disabled={isLoading}>
          {isLoading ? "Searching notes..." : "Search notes"}
        </button>
      </form>
      {hasSearched && results.length === 0 && <p>No notes found.</p>}
      {results.length > 0 && <SearchResultsList results={results} />}
    </section>
  );
};

export default NoteSearchSection;
