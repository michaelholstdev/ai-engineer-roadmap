import { useState, useCallback } from "react";
import type { ChangeEvent, SubmitEvent } from "react";
import "./App.css";
import {
  type AnalyzeResponse,
  type AiAnalyzeResponse,
  analyzeText,
  analyzeTextWithAI,
} from "./apiClient";
import HistorySection from "./HistorySection";

function App() {
  const [text, setText] = useState<string>("");
  const [result, setResult] = useState<AnalyzeResponse | null>(null);
  const [aiResult, setAiResult] = useState<AiAnalyzeResponse | null>(null);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [refreshKey, setRefreshKey] = useState(0);

  const handleOnChangeTextarea = (event: ChangeEvent<HTMLTextAreaElement>) => {
    setText(event.target.value);
  };

  const validateIfTextIsEmpty = (text: string) => text.trim() === "";

  const resetResults = () => {
    setAiResult(null);
    setResult(null);
    setErrorMessage(null);
  };

  const handleSubmit = async (event: SubmitEvent) => {
    event.preventDefault();

    if (validateIfTextIsEmpty(text)) {
      setErrorMessage("Please enter text to analyze.");
      return;
    }

    try {
      setIsLoading(true);
      resetResults();

      const data = await analyzeText(text);

      setResult(data);
      setRefreshKey((current) => current + 1);
      setErrorMessage(null);
    } catch {
      setResult(null);
      setErrorMessage("Could not analyze text. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  const handleAiSubmit = useCallback(async () => {
    if (validateIfTextIsEmpty(text)) {
      setErrorMessage("Please enter text to analyze.");
      return;
    }

    try {
      setIsLoading(true);
      resetResults();

      const data = await analyzeTextWithAI(text);

      setAiResult(data);
      setRefreshKey((current) => current + 1);
      setErrorMessage(null);
    } catch {
      setAiResult(null);
      setErrorMessage("Could not analyze text with AI. Please try again.");
    } finally {
      setIsLoading(false);
    }
  }, [text]);

  const renderResult = () =>
    result && (
      <ul>
        <li>Words: {result.word_count}</li>
        <li>Characters: {result.character_count}</li>
        <li>Sentences: {result.sentence_count}</li>
      </ul>
    );

  function renderList(items: string[]) {
    if (items.length === 0) {
      return null;
    }
    return (
      <ul>
        {items.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    );
  }

  const renderTopicList = () =>
    aiResult && (renderList(aiResult.topics) ?? <p>No topics found.</p>);

  const renderActionItemList = () =>
    aiResult &&
    (renderList(aiResult.action_items) ?? <p>No action items found.</p>);

  const renderAiResult = () =>
    aiResult && (
      <section>
        <h2>AI Analysis</h2>
        <p>{aiResult.summary}</p>
        <p>Sentiment: {aiResult.sentiment}</p>
        <p>Topics:</p>
        {renderTopicList()}
        <p>Action Items:</p>
        {renderActionItemList()}
      </section>
    );

  return (
    <main className="app">
      <h1>Text Analyzer</h1>
      <form className="analyze-form" onSubmit={handleSubmit}>
        <textarea onChange={handleOnChangeTextarea} value={text} />
        {errorMessage && <p>{errorMessage}</p>}
        <button type="submit" disabled={isLoading}>
          {isLoading ? "Analyzing..." : "Analyze"}
        </button>
        <button type="button" onClick={handleAiSubmit} disabled={isLoading}>
          {isLoading ? "Analyzing with AI..." : "Analyze with AI"}
        </button>
      </form>
      {renderResult()}
      {renderAiResult()}
      <HistorySection refreshKey={refreshKey} />
    </main>
  );
}

export default App;
