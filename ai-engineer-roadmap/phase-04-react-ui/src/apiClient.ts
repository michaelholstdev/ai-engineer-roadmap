export type AnalyzeResponse = {
  word_count: number;
  character_count: number;
  sentence_count: number;
};

export type AiAnalyzeResponse = {
  summary: string;
  sentiment: "positive" | "neutral" | "negative";
  topics: string[];
  action_items: string[];
};

export type AnalysisHistoryItem = {
  id: string;
  analysis_type: "ai" | "text";
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

class ApiClientError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "ApiClientError";
  }
}

async function getJson<TResponse>(path: string): Promise<TResponse> {
  try {
    const response = await fetch(
      `${import.meta.env.VITE_API_BASE_URL}${path}`,
      {
        method: "GET",
      },
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

async function postJson<TResponse>(
  path: string,
  body: unknown,
): Promise<TResponse> {
  try {
    const response = await fetch(
      `${import.meta.env.VITE_API_BASE_URL}${path}`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(body),
      },
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

export async function analyzeText(text: string): Promise<AnalyzeResponse> {
  return postJson<AnalyzeResponse>("/analyze", { text });
}

export async function analyzeTextWithAI(
  text: string,
): Promise<AiAnalyzeResponse> {
  return postJson<AiAnalyzeResponse>("/ai/analyze", { text });
}

export async function loadAnalysisHistory(
  limit: number = 20,
): Promise<AnalysisHistoryItem[]> {
  return getJson<AnalysisHistoryItem[]>(`/analyses?limit=${limit}`);
}
