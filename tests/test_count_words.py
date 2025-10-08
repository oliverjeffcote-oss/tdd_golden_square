from lib.count_words import *

def test_returns_sentence_of_3_words():
    result = count_words("Let's go party")
    assert result == "Let's go party"