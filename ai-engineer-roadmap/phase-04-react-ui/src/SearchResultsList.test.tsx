import { render, screen } from "@testing-library/react";
import { expect, it } from "vitest";

import SearchResultsList from "./SearchResultsList";
import type { SearchResultResponse } from "./apiClient";

it("renders search results without raw embeddings", () => {
  const results: SearchResultResponse[] = [
    {
      id: "12345678-1234-5678-1234-567812345678",
      title: "Postgres",
      content: "Postgres stores relational data.",
      embedding_model: "nomic-embed-text",
      created_at: "2026-06-24T12:00:00Z",
      updated_at: "2026-06-24T12:00:00Z",
      score: 0.75,
      search_mode: "semantic",
    },
  ];

  render(<SearchResultsList results={results} />);

  expect(screen.getByText("Postgres")).toBeInTheDocument();
  expect(
    screen.getByText("Postgres stores relational data."),
  ).toBeInTheDocument();
  expect(screen.getByText("Relevance score: 0.75")).toBeInTheDocument();
  expect(screen.getByText("Mode: semantic")).toBeInTheDocument();
  expect(screen.getByText("Model: nomic-embed-text")).toBeInTheDocument();
});
