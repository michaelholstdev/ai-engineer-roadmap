import { useState } from "react";
import type { ChangeEvent, FormEvent } from "react";
import { createNote } from "./apiClient";

const NoteCreateSection = () => {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [successMessage, setSuccessMessage] = useState<string | null>(null);

  const handleTitleChange = (event: ChangeEvent<HTMLInputElement>) => {
    setTitle(event.target.value);
  };

  const handleContentChange = (event: ChangeEvent<HTMLTextAreaElement>) => {
    setContent(event.target.value);
  };

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    try {
      event.preventDefault();
      setIsLoading(true);

      if (title.trim() === "" || content.trim() === "") {
        setSuccessMessage(null);
        setErrorMessage("Please enter a title and content.");
        return;
      }

      await createNote({
        title,
        content,
      });

      setErrorMessage(null);
      setSuccessMessage("Note created.");
      setTitle("");
      setContent("");
    } catch {
      setSuccessMessage(null);
      setErrorMessage("Could not create note. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <section className="notes-section" aria-labelledby="create-note-heading">
      <h2 id="create-note-heading">Create note</h2>
      <form className="note-form" onSubmit={handleSubmit}>
        <label htmlFor="note-title">Title</label>
        <input id="note-title" value={title} onChange={handleTitleChange} />

        <label htmlFor="note-content">Content</label>
        <textarea
          id="note-content"
          value={content}
          onChange={handleContentChange}
        />

        {errorMessage && <p>{errorMessage}</p>}
        {successMessage && <p>{successMessage}</p>}

        <button type="submit" disabled={isLoading}>
          {isLoading ? "Creating note..." : "Create note"}
        </button>
      </form>
    </section>
  );
};

export default NoteCreateSection;
