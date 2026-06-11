import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { expect, it, vi } from "vitest";

import HistorySection from "./HistorySection";
import * as apiClient from "./apiClient";

it("shows a loading message while history is loading", () => {
  vi.spyOn(apiClient, "loadAnalysisHistory").mockReturnValue(
    new Promise(() => {}),
  );

  render(<HistorySection refreshKey={0} />);

  expect(screen.getByText("Loading history...")).toBeInTheDocument();
});

it("shows an empty state when no history exists", async () => {
  vi.spyOn(apiClient, "loadAnalysisHistory").mockResolvedValue([]);

  render(<HistorySection refreshKey={0} />);

  expect(await screen.findByText("No analyses yet.")).toBeInTheDocument();
});

it("shows a text history entry", async () => {
  vi.spyOn(apiClient, "loadAnalysisHistory").mockResolvedValue([
    {
      id: "12345678-1234-5678-1234-567812345678",
      analysis_type: "text",
      character_count: 22,
      input_text: "AI Engineering is fun.",
      provider: null,
      sentence_count: 1,
      word_count: 4,
      sentiment: null,
      summary: null,
      topics: [],
      action_items: [],
      created_at: "2026-06-10T08:00:00Z",
    },
  ]);

  render(<HistorySection refreshKey={0} />);

  expect(await screen.findByText("Text")).toBeInTheDocument();
  expect(screen.getByText("AI Engineering is fun.")).toBeInTheDocument();
  expect(screen.getByText("Words: 4")).toBeInTheDocument();
  expect(screen.getByText("Characters: 22")).toBeInTheDocument();
  expect(screen.getByText("Sentences: 1")).toBeInTheDocument();

  const time = document.querySelector("time");
  expect(time).toHaveAttribute("datetime", "2026-06-10T08:00:00Z");
});

it("shows an AI history entry", async () => {
  vi.spyOn(apiClient, "loadAnalysisHistory").mockResolvedValue([
    {
      id: "12345678-1234-5678-1234-567812345678",
      analysis_type: "ai",
      character_count: 22,
      input_text: "AI Engineering is fun.",
      provider: "ollama",
      sentence_count: 1,
      word_count: 4,
      sentiment: "positive",
      summary: "Short summary",
      topics: ["Engineering"],
      action_items: ["Review the roadmap"],
      created_at: "2026-06-10T08:00:00Z",
    },
  ]);

  render(<HistorySection refreshKey={0} />);

  expect(await screen.findByText("AI")).toBeInTheDocument();
  expect(screen.getByText("Short summary")).toBeInTheDocument();
  expect(screen.getByText("Sentiment: positive")).toBeInTheDocument();
  expect(screen.getByText("Provider: ollama")).toBeInTheDocument();
  expect(screen.getByText("Engineering")).toBeInTheDocument();
  expect(screen.getByText("Review the roadmap")).toBeInTheDocument();
});

it("shows an error message when history loading fails", async () => {
  vi.spyOn(apiClient, "loadAnalysisHistory").mockRejectedValue(
    new Error("Network error"),
  );

  render(<HistorySection refreshKey={0} />);

  expect(
    await screen.findByText("Could not load analysis history."),
  ).toBeInTheDocument();

  expect(screen.getByRole("button", { name: "Retry" })).toBeInTheDocument();
});

it("retries loading history after an error", async () => {
  const user = userEvent.setup();

  const loadHistorySpy = vi
    .spyOn(apiClient, "loadAnalysisHistory")
    .mockRejectedValueOnce(new Error("Network error"))
    .mockResolvedValueOnce([]);

  render(<HistorySection refreshKey={0} />);

  await user.click(await screen.findByRole("button", { name: "Retry" }));

  expect(loadHistorySpy).toHaveBeenCalledTimes(2);
  expect(await screen.findByText("No analyses yet.")).toBeInTheDocument();
});

it("shows a loading message while retrying history", async () => {
  const user = userEvent.setup();

  const loadHistorySpy = vi
    .spyOn(apiClient, "loadAnalysisHistory")
    .mockRejectedValueOnce(new Error("Network error"))
    .mockReturnValueOnce(
      new Promise<apiClient.AnalysisHistoryItem[]>(() => {}),
    );

  render(<HistorySection refreshKey={0} />);

  await user.click(await screen.findByRole("button", { name: "Retry" }));

  expect(loadHistorySpy).toHaveBeenCalledTimes(2);
  expect(await screen.findByText("Loading history...")).toBeInTheDocument();
  expect(
    screen.queryByText("Could not load analysis history."),
  ).not.toBeInTheDocument();
});


it("reloads history when the refresh key changes", async () => {
  const loadHistorySpy = vi
    .spyOn(apiClient, "loadAnalysisHistory")
    .mockResolvedValue([]);

  const { rerender } = render(<HistorySection refreshKey={0} />);

  await screen.findByText("No analyses yet.");
  expect(loadHistorySpy).toHaveBeenCalledTimes(1);

  rerender(<HistorySection refreshKey={1} />);

  await vi.waitFor(() => {
    expect(loadHistorySpy).toHaveBeenCalledTimes(2);
  });
});
