import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { expect, it, vi } from "vitest";
import * as apiClient from "./apiClient";
import NoteSearchSection from "./NoteSearchSection";

it("renders the note search form", () => {
  render(<NoteSearchSection />);

  expect(
    screen.getByRole("heading", { name: "Search notes" }),
  ).toBeInTheDocument();
  expect(screen.getByLabelText("Search query")).toBeInTheDocument();
  expect(screen.getByLabelText("Result limit")).toBeInTheDocument();
  expect(screen.getByRole("button", { name: "Keyword" })).toBeInTheDocument();
  expect(screen.getByRole("button", { name: "Semantic" })).toBeInTheDocument();
  expect(
    screen.getByRole("button", { name: "Search notes" }),
  ).toBeInTheDocument();
});

it("shows a validation message when searching without a query", async () => {
  const user = userEvent.setup();
  const searchNotesSpy = vi.spyOn(apiClient, "searchNotes");

  render(<NoteSearchSection />);

  await user.click(screen.getByRole("button", { name: "Search notes" }));

  expect(screen.getByText("Please enter a search query.")).toBeInTheDocument();
  expect(searchNotesSpy).not.toHaveBeenCalled();
});

it("searches notes with the selected mode and limit", async () => {
  const user = userEvent.setup();

  const searchNotesSpy = vi
    .spyOn(apiClient, "searchNotes")
    .mockResolvedValue([]);

  render(<NoteSearchSection />);

  await user.type(screen.getByLabelText("Search query"), "relational data");
  await user.clear(screen.getByLabelText("Result limit"));
  await user.type(screen.getByLabelText("Result limit"), "5");
  await user.click(screen.getByRole("button", { name: "Semantic" }));
  await user.click(screen.getByRole("button", { name: "Search notes" }));

  expect(searchNotesSpy).toHaveBeenCalledWith({
    query: "relational data",
    mode: "semantic",
    limit: 5,
  });
});

it("disables the search button while searching notes", async () => {
  const user = userEvent.setup();

  vi.spyOn(apiClient, "searchNotes").mockReturnValue(new Promise(() => {}));

  render(<NoteSearchSection />);

  await user.type(screen.getByLabelText("Search query"), "relational data");
  await user.click(screen.getByRole("button", { name: "Search notes" }));

  expect(
    screen.getByRole("button", { name: "Searching notes..." }),
  ).toBeDisabled();
});

it("renders search results after a successful search", async () => {
  const user = userEvent.setup();

  vi.spyOn(apiClient, "searchNotes").mockResolvedValue([
    {
      id: "12345678-1234-5678-1234-567812345678",
      title: "Postgres",
      content: "Postgres stores relational data.",
      embedding_model: "nomic-embed-text",
      created_at: "2026-06-24T12:00:00Z",
      updated_at: "2026-06-24T12:00:00Z",
      score: 0.75,
      search_mode: "keyword",
    },
  ]);

  render(<NoteSearchSection />);

  await user.type(screen.getByLabelText("Search query"), "relational data");
  await user.click(screen.getByRole("button", { name: "Search notes" }));

  expect(await screen.findByText("Postgres")).toBeInTheDocument();
  expect(
    screen.getByText("Postgres stores relational data."),
  ).toBeInTheDocument();
  expect(screen.getByText("Relevance score: 0.75")).toBeInTheDocument();
  expect(screen.getByText("Mode: keyword")).toBeInTheDocument();
});

it("shows an empty state when search returns no results", async () => {
  const user = userEvent.setup();

  vi.spyOn(apiClient, "searchNotes").mockResolvedValue([]);

  render(<NoteSearchSection />);

  await user.type(screen.getByLabelText("Search query"), "nothing here");
  await user.click(screen.getByRole("button", { name: "Search notes" }));

  expect(await screen.findByText("No notes found.")).toBeInTheDocument();
});

it("shows an error message when searching notes fails", async () => {
  const user = userEvent.setup();

  vi.spyOn(apiClient, "searchNotes").mockRejectedValue(
    new Error("API request failed"),
  );

  render(<NoteSearchSection />);

  await user.type(screen.getByLabelText("Search query"), "relational data");
  await user.click(screen.getByRole("button", { name: "Search notes" }));

  expect(
    await screen.findByText("Could not search notes. Please try again."),
  ).toBeInTheDocument();
});

it("does not show old search results after a failed search", async () => {
  const user = userEvent.setup();

  vi.spyOn(apiClient, "searchNotes")
    .mockResolvedValueOnce([
      {
        id: "12345678-1234-5678-1234-567812345678",
        title: "Postgres",
        content: "Postgres stores relational data.",
        embedding_model: "nomic-embed-text",
        created_at: "2026-06-24T12:00:00Z",
        updated_at: "2026-06-24T12:00:00Z",
        score: 0.75,
        search_mode: "keyword",
      },
    ])
    .mockRejectedValueOnce(new Error("API request failed"));

  render(<NoteSearchSection />);

  await user.type(screen.getByLabelText("Search query"), "relational data");
  await user.click(screen.getByRole("button", { name: "Search notes" }));

  expect(await screen.findByText("Postgres")).toBeInTheDocument();

  await user.clear(screen.getByLabelText("Search query"));
  await user.type(screen.getByLabelText("Search query"), "broken search");
  await user.click(screen.getByRole("button", { name: "Search notes" }));

  expect(
    await screen.findByText("Could not search notes. Please try again."),
  ).toBeInTheDocument();
  expect(screen.queryByText("Postgres")).not.toBeInTheDocument();
});

it("marks the selected search mode", async () => {
  const user = userEvent.setup();

  render(<NoteSearchSection />);

  expect(screen.getByRole("button", { name: "Keyword" })).toHaveAttribute(
    "aria-pressed",
    "true",
  );
  expect(screen.getByRole("button", { name: "Semantic" })).toHaveAttribute(
    "aria-pressed",
    "false",
  );

  await user.click(screen.getByRole("button", { name: "Semantic" }));

  expect(screen.getByRole("button", { name: "Keyword" })).toHaveAttribute(
    "aria-pressed",
    "false",
  );
  expect(screen.getByRole("button", { name: "Semantic" })).toHaveAttribute(
    "aria-pressed",
    "true",
  );
});

it("explains that scores are only comparable within the selected search mode", () => {
  render(<NoteSearchSection />);

  expect(
    screen.getByText(
      "Scores are only comparable within the selected search mode.",
    ),
  ).toBeInTheDocument();
});
