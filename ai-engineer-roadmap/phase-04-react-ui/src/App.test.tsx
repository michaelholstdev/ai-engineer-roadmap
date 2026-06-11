import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { expect, it, vi } from "vitest";

import App from "./App";
import * as apiClient from "./apiClient";

vi.mock("./HistorySection", () => ({
  default: ({ refreshKey }: { refreshKey: number }) => (
    <div data-testid="history-section">{refreshKey}</div>
  ),
}));

it("renders the text analyzer form", () => {
  render(<App />);

  expect(
    screen.getByRole("heading", { name: "Text Analyzer" }),
  ).toBeInTheDocument();
  expect(screen.getByRole("textbox")).toBeInTheDocument();
  expect(screen.getByRole("button", { name: "Analyze" })).toBeInTheDocument();
  expect(
    screen.getByRole("button", { name: "Analyze with AI" }),
  ).toBeInTheDocument();
});

it("shows a validation message when submitting empty text", async () => {
  const user = userEvent.setup();

  render(<App />);

  await user.click(screen.getByRole("button", { name: "Analyze" }));

  expect(screen.getByText("Please enter text to analyze.")).toBeInTheDocument();
});

it("does not call the API when submitting empty text", async () => {
  const user = userEvent.setup();
  const fetchSpy = vi.spyOn(globalThis, "fetch");

  render(<App />);

  await user.click(screen.getByRole("button", { name: "Analyze" }));

  expect(fetchSpy).not.toHaveBeenCalled();
});

it("disables the submit button while analyzing text", async () => {
  const user = userEvent.setup();

  vi.spyOn(globalThis, "fetch").mockReturnValue(
    new Promise(() => {}) as Promise<Response>,
  );

  render(<App />);

  await user.type(screen.getByRole("textbox"), "AI Engineering is fun.");
  await user.click(screen.getByRole("button", { name: "Analyze" }));

  expect(screen.getByRole("button", { name: "Analyzing..." })).toBeDisabled();
});

it("renders text statistics after successful analysis", async () => {
  const user = userEvent.setup();

  vi.spyOn(globalThis, "fetch").mockResolvedValue(
    new Response(
      JSON.stringify({
        word_count: 4,
        character_count: 22,
        sentence_count: 1,
      }),
      {
        status: 200,
        headers: {
          "Content-Type": "application/json",
        },
      },
    ),
  );

  render(<App />);

  await user.type(screen.getByRole("textbox"), "AI Engineering is fun.");
  await user.click(screen.getByRole("button", { name: "Analyze" }));

  expect(await screen.findByText("Words: 4")).toBeInTheDocument();
  expect(screen.getByText("Characters: 22")).toBeInTheDocument();
  expect(screen.getByText("Sentences: 1")).toBeInTheDocument();
});

it("shows an error message when the API request fails", async () => {
  const user = userEvent.setup();

  vi.spyOn(globalThis, "fetch").mockResolvedValue(
    new Response(
      JSON.stringify({
        detail: "Internal server error",
      }),
      {
        status: 500,
        headers: {
          "Content-Type": "application/json",
        },
      },
    ),
  );

  render(<App />);

  await user.type(screen.getByRole("textbox"), "AI Engineering is fun.");
  await user.click(screen.getByRole("button", { name: "Analyze" }));

  expect(
    await screen.findByText("Could not analyze text. Please try again."),
  ).toBeInTheDocument();
});

it("does not show old results after failed api call", async () => {
  const user = userEvent.setup();

  vi.spyOn(globalThis, "fetch")
    .mockResolvedValueOnce(
      new Response(
        JSON.stringify({
          word_count: 4,
          character_count: 22,
          sentence_count: 1,
        }),
        { status: 200, headers: { "Content-Type": "application/json" } },
      ),
    )
    .mockResolvedValueOnce(
      new Response(JSON.stringify({ detail: "Internal server error" }), {
        status: 500,
        headers: { "Content-Type": "application/json" },
      }),
    );

  render(<App />);

  await user.type(screen.getByRole("textbox"), "AI Engineering is fun.");
  await user.click(screen.getByRole("button", { name: "Analyze" }));

  await user.type(
    screen.getByRole("textbox"),
    "AI Engineering is much much more fun.",
  );
  await user.click(screen.getByRole("button", { name: "Analyze" }));

  expect(screen.queryByText("Words: 4")).not.toBeInTheDocument();
});

it("shows an error message when the API request cannot be completed", async () => {
  const user = userEvent.setup();

  vi.spyOn(globalThis, "fetch").mockRejectedValue(new Error("Network error"));

  render(<App />);

  await user.type(screen.getByRole("textbox"), "AI Engineering is fun.");
  await user.click(screen.getByRole("button", { name: "Analyze" }));

  expect(
    await screen.findByText("Could not analyze text. Please try again."),
  ).toBeInTheDocument();
});

it("renders structured AI analysis after successful AI analysis", async () => {
  const user = userEvent.setup();

  vi.spyOn(globalThis, "fetch").mockResolvedValue(
    new Response(
      JSON.stringify({
        summary: "Short summary",
        sentiment: "neutral",
        topics: ["ai", "engineering"],
        action_items: ["Review the roadmap"],
      }),
      {
        status: 200,
        headers: {
          "Content-Type": "application/json",
        },
      },
    ),
  );

  render(<App />);

  await user.type(screen.getByRole("textbox"), "AI Engineering is fun.");
  await user.click(screen.getByRole("button", { name: "Analyze with AI" }));

  expect(await screen.findByText("Short summary")).toBeInTheDocument();
  expect(screen.getByText("Sentiment: neutral")).toBeInTheDocument();
  expect(screen.getByText("ai")).toBeInTheDocument();
  expect(screen.getByText("engineering")).toBeInTheDocument();
  expect(screen.getByText("Review the roadmap")).toBeInTheDocument();
});

it("renders not found topics and action item message when the array is empty", async () => {
  const user = userEvent.setup();

  vi.spyOn(globalThis, "fetch").mockResolvedValue(
    new Response(
      JSON.stringify({
        summary: "Short summary",
        sentiment: "neutral",
        topics: [],
        action_items: [],
      }),
      {
        status: 200,
        headers: {
          "Content-Type": "application/json",
        },
      },
    ),
  );

  render(<App />);

  await user.type(screen.getByRole("textbox"), "AI Engineering is fun.");
  await user.click(screen.getByRole("button", { name: "Analyze with AI" }));

  expect(await screen.findByText("Short summary")).toBeInTheDocument();
  expect(await screen.findByText("No topics found.")).toBeInTheDocument();
  expect(await screen.findByText("No action items found.")).toBeInTheDocument();
});

it("shows an error message when AI analysis fails", async () => {
  const user = userEvent.setup();

  vi.spyOn(globalThis, "fetch")
    .mockResolvedValueOnce(
      new Response(
        JSON.stringify({
          summary: "Short summary",
          sentiment: "neutral",
          topics: [],
          action_items: [],
        }),
        {
          status: 200,
          headers: {
            "Content-Type": "application/json",
          },
        },
      ),
    )
    .mockResolvedValueOnce(
      new Response(JSON.stringify({ detail: "AI provider request failed" }), {
        status: 502,
        headers: { "Content-Type": "application/json" },
      }),
    );

  render(<App />);

  await user.type(screen.getByRole("textbox"), "AI Engineering is fun.");
  await user.click(screen.getByRole("button", { name: "Analyze with AI" }));

  expect(await screen.findByText("No topics found.")).toBeInTheDocument();

  await user.click(screen.getByRole("button", { name: "Analyze with AI" }));

  expect(await screen.queryByText("No topics found.")).not.toBeInTheDocument();
  expect(
    await screen.findByText(
      "Could not analyze text with AI. Please try again.",
    ),
  ).toBeInTheDocument();
});

it("shows an error message when the AI request cannot be completed", async () => {
  const user = userEvent.setup();

  vi.spyOn(globalThis, "fetch").mockRejectedValue(new Error("Network error"));

  render(<App />);

  await user.type(screen.getByRole("textbox"), "AI Engineering is fun.");
  await user.click(screen.getByRole("button", { name: "Analyze with AI" }));

  expect(
    await screen.findByText(
      "Could not analyze text with AI. Please try again.",
    ),
  ).toBeInTheDocument();
});

it("disables the AI analyze button while AI analysis is running", async () => {
  const user = userEvent.setup();

  vi.spyOn(globalThis, "fetch").mockReturnValue(
    new Promise(() => {}) as Promise<Response>,
  );

  render(<App />);

  await user.type(screen.getByRole("textbox"), "AI Engineering is fun.");
  await user.click(screen.getByRole("button", { name: "Analyze with AI" }));

  expect(
    screen.getByRole("button", { name: "Analyzing with AI..." }),
  ).toBeDisabled();
});

it("AI run clears old stats result", async () => {
  const user = userEvent.setup();

  vi.spyOn(apiClient, "analyzeText").mockResolvedValue({
    word_count: 10,
    character_count: 40,
    sentence_count: 1,
  });

  vi.spyOn(apiClient, "analyzeTextWithAI").mockResolvedValue({
    action_items: [],
    sentiment: "positive",
    summary: "AI Engineering is fun.",
    topics: ["AI"],
  });

  render(<App />);

  await user.type(screen.getByRole("textbox"), "Engineering is fun.");
  await user.click(screen.getByRole("button", { name: "Analyze" }));

  expect(screen.getByText("Words: 10")).toBeInTheDocument();

  await user.type(screen.getByRole("textbox"), "AI Engineering is fun.");
  await user.click(screen.getByRole("button", { name: "Analyze with AI" }));

  expect(screen.queryByText("Words: 10")).not.toBeInTheDocument();
  expect(screen.getByText("Sentiment: positive")).toBeInTheDocument();
});

it("Stats run clears old AI result", async () => {
  const user = userEvent.setup();

  vi.spyOn(apiClient, "analyzeText").mockResolvedValue({
    word_count: 10,
    character_count: 40,
    sentence_count: 1,
  });

  vi.spyOn(apiClient, "analyzeTextWithAI").mockResolvedValue({
    action_items: [],
    sentiment: "positive",
    summary: "AI Engineering is fun.",
    topics: ["AI"],
  });

  render(<App />);

  await user.type(screen.getByRole("textbox"), "AI Engineering is fun.");
  await user.click(screen.getByRole("button", { name: "Analyze with AI" }));

  expect(screen.getByText("Sentiment: positive")).toBeInTheDocument();

  await user.type(screen.getByRole("textbox"), "Engineering is fun.");
  await user.click(screen.getByRole("button", { name: "Analyze" }));

  expect(screen.queryByText("Sentiment: positive")).not.toBeInTheDocument();
  expect(screen.queryByText("Words: 10")).toBeInTheDocument();
});

it("refreshes history after successful text analysis", async () => {
  const user = userEvent.setup();

  vi.spyOn(apiClient, "analyzeText").mockResolvedValue({
    word_count: 4,
    character_count: 22,
    sentence_count: 1,
  });

  render(<App />);

  expect(screen.getByTestId("history-section")).toHaveTextContent("0");
  await user.type(screen.getByRole("textbox"), "AI Engineering is fun.");
  await user.click(screen.getByRole("button", { name: "Analyze" }));

  await vi.waitFor(() => {
    expect(screen.getByTestId("history-section")).toHaveTextContent("1");
  });
});

it("refreshes history after successful AI analysis", async () => {
  const user = userEvent.setup();

  vi.spyOn(apiClient, "analyzeTextWithAI").mockResolvedValue({
    summary: "Short summary",
    sentiment: "positive",
    topics: ["Engineering"],
    action_items: [],
  });

  render(<App />);

  expect(screen.getByTestId("history-section")).toHaveTextContent("0");

  await user.type(screen.getByRole("textbox"), "AI Engineering is fun.");
  await user.click(screen.getByRole("button", { name: "Analyze with AI" }));

  await vi.waitFor(() => {
    expect(screen.getByTestId("history-section")).toHaveTextContent("1");
  });
});

it("does not refresh history after failed text analysis", async () => {
  const user = userEvent.setup();

  vi.spyOn(apiClient, "analyzeText").mockRejectedValue(
    new Error("API request failed"),
  );

  render(<App />);

  await user.type(screen.getByRole("textbox"), "AI Engineering is fun.");
  await user.click(screen.getByRole("button", { name: "Analyze" }));

  expect(
    await screen.findByText("Could not analyze text. Please try again."),
  ).toBeInTheDocument();

  expect(screen.getByTestId("history-section")).toHaveTextContent("0");
});

it("does not refresh history after failed AI analysis", async () => {
  const user = userEvent.setup();

  vi.spyOn(apiClient, "analyzeTextWithAI").mockRejectedValue(
    new Error("API request failed"),
  );

  render(<App />);

  await user.type(screen.getByRole("textbox"), "AI Engineering is fun.");
  await user.click(screen.getByRole("button", { name: "Analyze with AI" }));

  expect(
    await screen.findByText(
      "Could not analyze text with AI. Please try again.",
    ),
  ).toBeInTheDocument();

  expect(screen.getByTestId("history-section")).toHaveTextContent("0");
});
