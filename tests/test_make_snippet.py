from lib.make_snippet import *

def test_returns_full_sentence_given_less_than_5_words():
    result = make_snippet("Let's go party")
    assert result == "Let's go party"

def test_returns_full_sentence_of_5_words():
    result = make_snippet("Today I went to work.")
    assert result == "Today I went to work."

def test_long_sentence_ends_with_dots():
    result = make_snippet("Today I went to work and spoke to my friend")
    assert result[-3:] == "..."

def test_long_sentences_are_truncated_to_5_words():
    result = make_snippet("Today I went to work and spoke to my friend")
    assert result == "Today I went to work..."