from lib.count_words import *
import pytest

def test_returns_3_for_sentence_of_3_words():
    result = count_words("Let's go party")
    assert result == 3

def test_long_sentence_with_punctuation():
    result = count_words("Today I went to the shop and bought 5 things: a bunch of grapes, some greek yoghurt, blueberries, a jar of honey, and some granola.")
    assert result == 25

def test_empty_string():
    result = count_words("")
    assert result == 0

def test_string_of_numbers_returns_0():
    with pytest.raises(Exception) as e:
        count_words(3468908777)

    assert str(e.value) == "String not given."

