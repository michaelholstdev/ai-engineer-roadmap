import { useEffect, useState } from "react";
import { type AnalysisHistoryItem, loadAnalysisHistory } from "./apiClient";

type HistorySectionProps = {
  refreshKey: number;
};

const dateFormatter = new Intl.DateTimeFormat(undefined, {
  dateStyle: "medium",
  timeStyle: "short",
});

const HistorySection = ({ refreshKey }: HistorySectionProps) => {
  const [history, setHistory] = useState<AnalysisHistoryItem[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;

    loadAnalysisHistory()
      .then((loadedHistory) => {
        if (!cancelled) {
          setHistory(loadedHistory);
          setErrorMessage(null);
          setIsLoading(false);
        }
      })
      .catch(() => {
        if (!cancelled) {
          setErrorMessage("Could not load analysis history.");
          setIsLoading(false);
        }
      });

    return () => {
      cancelled = true;
    };
  }, [refreshKey]);

  const requestHistory = async () => {
    try {
      setIsLoading(true);
      setErrorMessage(null);
      const loadedHistory = await loadAnalysisHistory();

      setHistory(loadedHistory);
    } catch {
      setHistory([]);
      setErrorMessage("Could not load analysis history.");
    } finally {
      setIsLoading(false);
    }
  };

  const renderHistory = () => (
    <ul className="history-list">
      {history.map((item) => (
        <li key={item.id} className="history-item">
          <p>{item.analysis_type === "ai" ? "AI" : "Text"}</p>
          <time dateTime={item.created_at}>
            {dateFormatter.format(new Date(item.created_at))}
          </time>
          <p>{item.input_text}</p>
          <ul className="history-counts">
            <li>Words: {item.word_count}</li>
            <li>Characters: {item.character_count}</li>
            <li>Sentences: {item.sentence_count}</li>
          </ul>
          {item.summary && <p>{item.summary}</p>}

          {item.sentiment && <p>Sentiment: {item.sentiment}</p>}

          {item.provider && <p>Provider: {item.provider}</p>}

          {item.topics.length > 0 && (
            <>
              <p>Topics:</p>
              <ul>
                {item.topics.map((topic) => (
                  <li key={topic}>{topic}</li>
                ))}
              </ul>
            </>
          )}

          {item.action_items.length > 0 && (
            <>
              <p>Action Items:</p>
              <ul>
                {item.action_items.map((actionItem) => (
                  <li key={actionItem}>{actionItem}</li>
                ))}
              </ul>
            </>
          )}
        </li>
      ))}
    </ul>
  );

  return (
    <section aria-labelledby="history-heading" className="history">
      <h2 id="history-heading">Recent analyses</h2>
      {isLoading && <p>Loading history...</p>}
      {!isLoading && !errorMessage && history.length === 0 && (
        <p>No analyses yet.</p>
      )}
      {errorMessage && (
        <>
          <p>{errorMessage}</p>
          <button type="button" onClick={requestHistory}>
            Retry
          </button>
        </>
      )}
      {history.length > 0 && renderHistory()}
    </section>
  );
};

export default HistorySection;
