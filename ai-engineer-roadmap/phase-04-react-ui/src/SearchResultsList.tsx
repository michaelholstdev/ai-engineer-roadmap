import { type SearchResultResponse } from "./apiClient";

const SearchResultsList = ({
  results,
}: {
  results: SearchResultResponse[];
}) => {
  return (
    <ul>
      {results.map((result) => (
        <li key={result.id}>
          <h3>{result.title}</h3>
          <p>{result.content}</p>
          <p>Relevance score: {result.score}</p>
          <p>Mode: {result.search_mode}</p>
          <p>Model: {result.embedding_model}</p>
        </li>
      ))}
    </ul>
  );
};

export default SearchResultsList;
