import { expect, it, vi } from "vitest";

import {
  analyzeText,
  analyzeTextWithAI,
  createNote,
  loadAnalysisHistory,
  searchNotes,
} from "./apiClient";

it("sends text to the analyze endpoint and returns text statistics", async () => {
  const fetchSpy = vi.spyOn(globalThis, "fetch").mockResolvedValue(
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

  const result = await analyzeText("AI Engineering is fun.");

  expect(fetchSpy).toHaveBeenCalledWith(
    `${import.meta.env.VITE_API_BASE_URL}/analyze`,
    expect.objectContaining({
      method: "POST",
      body: JSON.stringify({ text: "AI Engineering is fun." }),
    }),
  );

  expect(result).toEqual({
    word_count: 4,
    character_count: 22,
    sentence_count: 1,
  });
});

it("throws an API client error when text analysis fails", async () => {
  vi.spyOn(globalThis, "fetch").mockResolvedValue(
    new Response(JSON.stringify({ detail: "Internal server error" }), {
      status: 500,
      headers: {
        "Content-Type": "application/json",
      },
    }),
  );

  await expect(analyzeText("AI Engineering is fun.")).rejects.toThrow(
    "API request failed",
  );
});

it("throws an API client error when text analysis cannot reach the API", async () => {
  vi.spyOn(globalThis, "fetch").mockRejectedValue(new Error("Network error"));

  await expect(analyzeText("AI Engineering is fun.")).rejects.toThrow(
    "Network error",
  );
});

it("sends text to the AI analyze endpoint and returns structured AI analysis", async () => {
  const fetchSpy = vi.spyOn(globalThis, "fetch").mockResolvedValue(
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

  const result = await analyzeTextWithAI("Ai Engineering is fun.");

  expect(fetchSpy).toHaveBeenCalledWith(
    `${import.meta.env.VITE_API_BASE_URL}/ai/analyze`,
    expect.objectContaining({
      method: "POST",
      body: JSON.stringify({ text: "Ai Engineering is fun." }),
    }),
  );

  expect(result).toEqual({
    summary: "Short summary",
    sentiment: "neutral",
    topics: ["ai", "engineering"],
    action_items: ["Review the roadmap"],
  });
});

it("throws an API client error when AI analysis fails", async () => {
  vi.spyOn(globalThis, "fetch").mockResolvedValue(
    new Response(JSON.stringify({ detail: "AI provider request failed" }), {
      status: 502,
      headers: {
        "Content-Type": "application/json",
      },
    }),
  );

  await expect(analyzeTextWithAI("AI Engineering is fun.")).rejects.toThrow(
    "API request failed",
  );
});

it("throws an API client error when AI analysis cannot reach the API", async () => {
  vi.spyOn(globalThis, "fetch").mockRejectedValue(new Error("Network error"));

  await expect(analyzeTextWithAI("AI Engineering is fun.")).rejects.toThrow(
    "Network error",
  );
});

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

  const fetchSpy = vi
    .spyOn(globalThis, "fetch")
    .mockResolvedValue(
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

it("throws an API client error when get analyses cannot reach the API", async () => {
  vi.spyOn(globalThis, "fetch").mockRejectedValue(new Error("Network error"));

  await expect(loadAnalysisHistory()).rejects.toThrow("Network error");
});

it("throws an API client error when get analyses fails", async () => {
  vi.spyOn(globalThis, "fetch").mockResolvedValue(
    new Response(JSON.stringify({}), {
      status: 502,
      headers: {
        "Content-Type": "application/json",
      },
    }),
  );

  await expect(loadAnalysisHistory()).rejects.toThrow("API request failed");
});

it("sends note data to the notes endpoint and returns the created note", async () => {
  const note = {
    id: "12345678-1234-5678-1234-567812345678",
    title: "Postgres",
    content: "Postgres stores relational data.",
    embedding_model: "nomic-embed-text",
    created_at: "2026-06-24T12:00:00Z",
    updated_at: "2026-06-24T12:00:00Z",
  };

  const fetchSpy = vi.spyOn(globalThis, "fetch").mockResolvedValue(
    new Response(JSON.stringify(note), {
      status: 200,
      headers: {
        "Content-Type": "application/json",
      },
    }),
  );

  const result = await createNote({
    title: "Postgres",
    content: "Postgres stores relational data.",
  });

  expect(fetchSpy).toHaveBeenCalledWith(
    `${import.meta.env.VITE_API_BASE_URL}/notes`,
    expect.objectContaining({
      method: "POST",
      body: JSON.stringify({
        title: "Postgres",
        content: "Postgres stores relational data.",
      }),
    }),
  );

  expect(result).toEqual(note);
});

it("searches notes with query mode and limit", async () => {
  const results = [
    {
      id: "12345678-1234-5678-1234-567812345678",
      title: "Postgres",
      content: "Postgres stores relational data.",
      embedding_model: "nomic-embed-text",
      created_at: "2026-06-24T12:00:00Z",
      updated_at: "2026-06-24T12:00:00Z",
      score: 0.75,
      search_mode: "keyword" as const,
    },
  ];

  const fetchSpy = vi
    .spyOn(globalThis, "fetch")
    .mockResolvedValue(
      new Response(JSON.stringify(results), {
        status: 200,
        headers: { "Content-Type": "application/json" },
      }),
    );

  const result = await searchNotes({
    query: "relational data",
    mode: "keyword",
    limit: 10,
  });

  expect(fetchSpy).toHaveBeenCalledWith(
    `${import.meta.env.VITE_API_BASE_URL}/notes/search?query=relational+data&mode=keyword&limit=10`,
    expect.objectContaining({ method: "GET" }),
  );
  expect(result).toEqual(results);
});
