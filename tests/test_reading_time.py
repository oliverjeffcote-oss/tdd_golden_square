from lib.reading_time import *
from tests.sample_texts import *
import pytest

def test_200_word_sample():
    result = reading_time(text_one_200)

    assert result == 1

def test_900_word_sample():
    result = reading_time(text_two_900)

    assert result == 5

def test_310_word_sample():
    result = reading_time(text_three_310)

    assert result == 2

def test_7_word_sample():
    result = reading_time("This will take less than one minute")

    assert result == 1

def test_empty_string():
    result = reading_time("")
    assert result == 0

def test_incorrect_data_type_throws_error():
    with pytest.raises(Exception) as e:
        reading_time(99)
    error_message = str(e.value)
    assert error_message == "String not provided"

