from lib.diary_entry import DiaryEntry
from tests.sample_texts import *
import pytest

'''
When initiating a new instance of DiaryEntry with a title and contents
Title is stored and can be returned
'''

def test_diary_entry_stores_title():
    diary_entry = DiaryEntry("Monday 1st September", "Today I went to the park with my dog.")
    result = diary_entry.title

    assert result == "Monday 1st September"

'''
If title or contents is empty
Throws an error
'''

def test_for_empty_title_or_contents():
    with pytest.raises(Exception) as e:
        diary_entry = DiaryEntry("", "")
    assert str(e.value) == "Diary entries must have title and contents"

'''
When initiating a new instance of DiaryEntry with a title and contents
Contents is stored and can be returned
'''

def test_diary_entry_stores_contents():
    diary_entry = DiaryEntry("Monday 1st September", "Today I went to the park with my dog.")
    result = diary_entry.contents

    assert result == "Today I went to the park with my dog."

'''
When calling diary_entry.format() on the stored title and contents
It returns a formatted diary entry as "My Title: These are the contents:
'''

def test_diary_entries_are_formatted_tuesday():
    diary_entry = DiaryEntry("Tuesday 2nd September", "I went to work at the cafe.")
    assert diary_entry.format() == "Tuesday 2nd September: I went to work at the cafe."

def test_diary_entries_are_formatted_wednesday():
    diary_entry = DiaryEntry("Wednesday 3rd September", "Today I went to the shopping centre and bought a present for my best friend's birthday.")
    assert diary_entry.format() == "Wednesday 3rd September: Today I went to the shopping centre and bought a present for my best friend's birthday."

'''
When requesting a word count on the diary entry
Returns an integer of the number of words in the diary entry.
'''

def test_returns_word_count_for_entry_contents_short():
    diary_entry = DiaryEntry("Wednesday 3rd September", "Today I went to the shopping centre and bought a present for my best friend's birthday.")
    assert diary_entry.count_words() == 16

def test_returns_word_count_for_entry_contents_long():
    diary_entry = DiaryEntry("Monday", text_three_310)
    assert diary_entry.count_words() == 310

'''
When given a wpm reading rate
Returns the correct estimate of the reading time in minutes
'''

def test_returns_correct_reading_time_200wpm():
    diary_entry = DiaryEntry("Thursday 4th September", text_two_900)
    assert diary_entry.reading_time(200) == 5

def test_returns_correct_reading_time_100wpm():
    diary_entry = DiaryEntry("Thursday 4th September", text_one_200)
    assert diary_entry.reading_time(100) == 2

'''
Given a wpm of 0
#reading-time throws an error
'''

def test_throws_error_if_wpm_is_0():
    diary_entry = DiaryEntry("Weds 3rd Sept", text_one_200)
    with pytest.raises(Exception) as e:
        assert diary_entry.reading_time(0)
    error_message = str(e.value)
    assert error_message == "Cannot have a wpm value of 0 or less"

'''
Given a wpm of less than 0
#reading-time throws an error
'''

def test_throws_error_if_wpm_is_0():
    diary_entry = DiaryEntry("Weds 3rd Sept", text_one_200)
    with pytest.raises(Exception) as e:
        assert diary_entry.reading_time(-4)
    error_message = str(e.value)
    assert error_message == "Cannot have a wpm value of 0 or less"

'''
When given words per minute and an integer with number of minutes a user has got to read
will return a string with the contents that the user can read in the given number of minutes
'''
def test_returns_number_of_words_user_can_read_simple():
    diary_entry = DiaryEntry("Weds 3rd Sept", "one two three four")
    assert diary_entry.reading_chunk(1, 2) == "one two"

def test_returns_number_of_words_user_can_read_full_text():
    diary_entry = DiaryEntry("Weds 3rd Sept", text_one_200)
    assert diary_entry.reading_chunk(100, 2) == text_one_200

def test_returns_number_of_words_user_can_read_long_text():
    diary_entry = DiaryEntry("Weds 3rd Sept", text_two_900)
    assert diary_entry.reading_chunk(100, 2) == ' '.join(text_two_900.split()[:200])

'''
When some of the content has already been read, the next chunk is provided for the user to read in the specified number of minutes
'''
def test_returns_next_chunk_of_words_simple():
    diary_entry = DiaryEntry("Weds 3rd Sept", "one two three four five")
    diary_entry.reading_chunk(1, 2)
    assert diary_entry.reading_chunk(1, 2) == "three four"

def test_returns_next_chunk_of_words_complex():
    diary_entry = DiaryEntry("Weds 3rd Sept", text_two_900)
    diary_entry.reading_chunk(100, 2)
    assert diary_entry.reading_chunk(100, 2) == ' '.join(text_two_900.split()[200:400])

'''
When there is some content left but less words than the available words that can be read, 
It only returns the remaining words and doesn't wrap back to the start
'''

def test_returns_remaining_chunk_of_words_simple():
    diary_entry = DiaryEntry("Weds 3rd Sept", "one two three four five")
    diary_entry.reading_chunk(1, 2)
    diary_entry.reading_chunk(1, 2)
    assert diary_entry.reading_chunk(1, 2) == "five"

def test_returns_remaining_chunk_of_words():
    diary_entry = DiaryEntry("Weds 3rd Sept", text_two_900)
    diary_entry.reading_chunk(100, 2)
    diary_entry.reading_chunk(100, 2)
    diary_entry.reading_chunk(100, 2)
    diary_entry.reading_chunk(100, 2)
    assert diary_entry.reading_chunk(100, 3) == ' '.join(text_two_900.split()[800:])

'''
When there is no diary content left and the user asks for the next reading chunk
It returns the chunk that starts from the beginning 
'''

def test_starts_from_beginning_when_all_text_is_read():
    diary_entry = DiaryEntry("Weds 3rd Sept", text_one_200)
    diary_entry.reading_chunk(100, 2)
    assert diary_entry.reading_chunk(100, 1) == ' '.join(text_two_900.split()[:100])
