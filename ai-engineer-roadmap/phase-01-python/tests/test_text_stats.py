from ai_roadmap.text_stats import count_words, count_characters, count_sentences


def test_count_words():
    assert count_words("AI Engineering is fun") == 4
    assert count_words("hello   world") == 2
    assert count_words("  hello world   ") == 2
    assert count_words("hello     world") == 2
    assert count_words("hello, world!") == 2
    assert count_words("") == 0


def test_count_characters():
    assert count_characters("abc") == 3
    assert count_characters("a b") == 3
    assert count_characters("  abc   ") == 8
    assert count_characters("hello!") == 6
    assert count_characters("") == 0

def test_count_sentences():
    assert count_sentences("Hello.") == 1
    assert count_sentences("Hello! How are you?") == 2
    assert count_sentences("No punctuation") == 0
    assert count_sentences("Wait... what?") == 4
    assert count_sentences("!!!") == 3
    assert count_sentences("") == 0