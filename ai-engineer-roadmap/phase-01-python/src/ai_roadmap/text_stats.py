def count_words(text: str) -> int:
    return len(text.split())


def count_characters(text: str) -> int:
    return len(text)


def count_sentences(text: str) -> int:
    i = 0
    for character in text:
        if character in (".", "!", "?"):
            i += 1
    return i