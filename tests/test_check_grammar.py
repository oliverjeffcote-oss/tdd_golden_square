from lib.check_grammar import check_grammar
import pytest

def test_starts_with_capital_and_ends_with_punctuation():
    result = check_grammar("This is a sentence.")
    assert result == True

def test_starts_with_capital_but_ends_without_punctuation():
    result = check_grammar("This is a poorly written sentence")
    assert result == False

def test_starts_without_capital_but_ends_with_punctuation():
    result = check_grammar("even worse sentence!!!")
    assert result == False

def test_both_false():
    result = check_grammar("the worst sentence possible")
    assert result == False

def test_empty_string():
    result = check_grammar("")
    assert result == "Sentence not long enough to check"

def test_incorrect_data_type():
    with pytest.raises(Exception) as e:
        check_grammar(['list'])
    error = str(e.value)
    assert error == "Incorrect data type provided"