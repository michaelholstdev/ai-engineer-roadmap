import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { expect, it, vi } from "vitest";

import NoteCreateSection from "./NoteCreateSection";
import * as apiClient from "./apiClient";

it("renders the note creation form", () => {
  render(<NoteCreateSection />);

  expect(
    screen.getByRole("heading", { name: "Create note" }),
  ).toBeInTheDocument();
  expect(screen.getByLabelText("Title")).toBeInTheDocument();
  expect(screen.getByLabelText("Content")).toBeInTheDocument();
  expect(
    screen.getByRole("button", { name: "Create note" }),
  ).toBeInTheDocument();
});

it("shows a validation message when creating a note without title or content", async () => {
  const user = userEvent.setup();
  const createNoteSpy = vi.spyOn(apiClient, "createNote");

  render(<NoteCreateSection />);

  await user.click(screen.getByRole("button", { name: "Create note" }));

  expect(
    screen.getByText("Please enter a title and content."),
  ).toBeInTheDocument();
  expect(createNoteSpy).not.toHaveBeenCalled();
});

it("creates a note and shows a success message", async () => {
  const user = userEvent.setup();

  const createNoteSpy = vi.spyOn(apiClient, "createNote").mockResolvedValue({
    id: "12345678-1234-5678-1234-567812345678",
    title: "Postgres",
    content: "Postgres stores relational data.",
    embedding_model: "nomic-embed-text",
    created_at: "2026-06-24T12:00:00Z",
    updated_at: "2026-06-24T12:00:00Z",
  });

  render(<NoteCreateSection />);

  await user.type(screen.getByLabelText("Title"), "Postgres");
  await user.type(
    screen.getByLabelText("Content"),
    "Postgres stores relational data.",
  );
  await user.click(screen.getByRole("button", { name: "Create note" }));

  expect(createNoteSpy).toHaveBeenCalledWith({
    title: "Postgres",
    content: "Postgres stores relational data.",
  });
  expect(await screen.findByText("Note created.")).toBeInTheDocument();
});

it("disables the create note button while creating a note", async () => {
  const user = userEvent.setup();

  vi.spyOn(apiClient, "createNote").mockReturnValue(new Promise(() => {}));

  render(<NoteCreateSection />);

  await user.type(screen.getByLabelText("Title"), "Postgres");
  await user.type(
    screen.getByLabelText("Content"),
    "Postgres stores relational data.",
  );
  await user.click(screen.getByRole("button", { name: "Create note" }));

  expect(
    screen.getByRole("button", { name: "Creating note..." }),
  ).toBeDisabled();
});

it("shows an error message when creating a note fails", async () => {
  const user = userEvent.setup();

  vi.spyOn(apiClient, "createNote").mockRejectedValue(
    new Error("API request failed"),
  );

  render(<NoteCreateSection />);

  await user.type(screen.getByLabelText("Title"), "Postgres");
  await user.type(
    screen.getByLabelText("Content"),
    "Postgres stores relational data.",
  );
  await user.click(screen.getByRole("button", { name: "Create note" }));

  expect(
    await screen.findByText("Could not create note. Please try again."),
  ).toBeInTheDocument();
});

it("clears the form after creating a note", async () => {
  const user = userEvent.setup();

  vi.spyOn(apiClient, "createNote").mockResolvedValue({
    id: "12345678-1234-5678-1234-567812345678",
    title: "Postgres",
    content: "Postgres stores relational data.",
    embedding_model: "nomic-embed-text",
    created_at: "2026-06-24T12:00:00Z",
    updated_at: "2026-06-24T12:00:00Z",
  });

  render(<NoteCreateSection />);

  const titleInput = screen.getByLabelText("Title");
  const contentInput = screen.getByLabelText("Content");

  await user.type(titleInput, "Postgres");
  await user.type(contentInput, "Postgres stores relational data.");
  await user.click(screen.getByRole("button", { name: "Create note" }));

  expect(await screen.findByText("Note created.")).toBeInTheDocument();
  expect(titleInput).toHaveValue("");
  expect(contentInput).toHaveValue("");
});

it("keeps the form values when creating a note fails", async () => {
  const user = userEvent.setup();

  vi.spyOn(apiClient, "createNote").mockRejectedValue(
    new Error("API request failed"),
  );

  render(<NoteCreateSection />);

  const titleInput = screen.getByLabelText("Title");
  const contentInput = screen.getByLabelText("Content");

  await user.type(titleInput, "Postgres");
  await user.type(contentInput, "Postgres stores relational data.");
  await user.click(screen.getByRole("button", { name: "Create note" }));

  expect(
    await screen.findByText("Could not create note. Please try again."),
  ).toBeInTheDocument();
  expect(titleInput).toHaveValue("Postgres");
  expect(contentInput).toHaveValue("Postgres stores relational data.");
});

it("clears the success message when note validation fails", async () => {
  const user = userEvent.setup();

  vi.spyOn(apiClient, "createNote").mockResolvedValue({
    id: "12345678-1234-5678-1234-567812345678",
    title: "Postgres",
    content: "Postgres stores relational data.",
    embedding_model: "nomic-embed-text",
    created_at: "2026-06-24T12:00:00Z",
    updated_at: "2026-06-24T12:00:00Z",
  });

  render(<NoteCreateSection />);

  await user.type(screen.getByLabelText("Title"), "Postgres");
  await user.type(
    screen.getByLabelText("Content"),
    "Postgres stores relational data.",
  );
  await user.click(screen.getByRole("button", { name: "Create note" }));

  expect(await screen.findByText("Note created.")).toBeInTheDocument();

  await user.click(screen.getByRole("button", { name: "Create note" }));

  expect(
    screen.getByText("Please enter a title and content."),
  ).toBeInTheDocument();
  expect(screen.queryByText("Note created.")).not.toBeInTheDocument();
});
