from lib.grammar_stats import GrammarStats
import pytest

'''
Given a text starting with capital letter and ending in punctuation
#check returns True
'''

def test_correct_grammar_returns_true():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("This is valid.") == True

'''
Given a text starting without capital letter and ending in punctuation
#check returns False
'''

def test_no_capital_returns_false():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("not valid.") == False

'''
Given a text starting with capital letter and not ending in punctuation
#check returns False
'''

def test_wrong_punctation_ending_returns_false():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("Not quite&") == False

'''
Given a text starting without capital letter and ending without punctuation
#check returns False
'''

def test_no_capital_no_punctuation_returns_false():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("definitely not") == False

'''
Given an empty string
#check throws error 
'''

def test_empty_string_throws_error():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.check("")
    assert str(e.value) == "Cannot check an empty string"

'''
Given that 2 texts have been checked 
#number_checked returns 2
'''

def test_number_of_texts_checked_is_stored():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello.")
    grammar_stats.check("this is a bad sentence")
    assert grammar_stats.checked_texts == 2

'''
Given that 1 text has been checked and has passed
#percentage_good returns 100
'''

def test_number_of_passed_checks():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello.")
    grammar_stats.check("This is a good sentence!")
    assert grammar_stats.percentage_good() == 100

'''
Given that 2 texts have been checked and 1 of them passed
#percentage_good returns 50
'''

def test_half_texts_passed():
    grammar_stats = GrammarStats()
    grammar_stats.check("hello")
    grammar_stats.check("Okay!")
    assert grammar_stats.percentage_good() == 50
