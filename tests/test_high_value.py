from lib.high_value import HighValue

'''
When calling get_highest and given two numbers, the first lower than the second,
it returns "Second value is higher".
'''

def test_second_value_higher():
    high_value = HighValue(2238457634,687987239492)
    result = high_value.get_highest()
    assert result == "Second value is higher"

'''
When calling get_highest and given two numbers, the first higher than the second,
it returns "First value is higher".
'''

def test_first_value_higher():
    high_value = HighValue(5.6,4.9)
    result = high_value.get_highest()
    assert result == "First value is higher"

'''
When calling get_highest and given two numbers that are the same value,
it returns "Values are equal".
'''

def test_values_are_equal():
    high_value = HighValue(0,0)
    result = high_value.get_highest()
    assert result == "Values are equal"

'''
When given two numbers where the second is higher by 3, 
and we add a value of 4 to the first,
that is reflected in changing the result from get_highest()
'''

def test_adding_makes_first_number_highest():
    high_value = HighValue(2,5)
    high_value.add(4, "first")
    result = high_value.get_highest()
    assert result == "First value is higher"

'''
When given two numbers where the first is higher by 3, 
and we add a value of 4 to the second,
that is reflected in changing the result from get_highest()
'''

def test_adding_makes_second_number_highest():
    high_value = HighValue(5,2)
    high_value.add(4, "second")
    result = high_value.get_highest()
    assert result == "Second value is higher"

'''
When given two numbers where the first is higher by 4, 
and we add a value of 4 to the second,
that is reflected in changing the result from get_highest()
'''

def test_adding_makes_numbers_equal():
    high_value = HighValue(5,1)
    high_value.add(4, "second")
    result = high_value.get_highest()
    assert result == "Values are equal"

'''
When giving a value to value_first show that it has
been stored
'''

def test_value_has_been_stored():
    high_value = HighValue(5,1)
    result = high_value.value_first
    assert result == 5