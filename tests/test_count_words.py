from lib.count_words import *

def test_returns_3_for_sentence_of_3_words():
    result = count_words("Let's go party")
    assert result == 3
