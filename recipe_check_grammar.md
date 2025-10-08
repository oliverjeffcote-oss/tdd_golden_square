# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user

So that I can improve my grammar

I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def check_grammar(sentence):
    """Validate that a given string begins with a capital letter and ends with a suitable punctuation mark.

    Parameters: (list all parameters and their types)
        sentence: a string that is a sentence containing multiple words (e.g. "Today I went to work and spoke to my colleague about xyz.")

    Returns: (state the return value and its type)
       Boolean - True if the string begins with a capital letter AND ends with punctuation, False otherwise.

    Side effects: (state any side effects)
        no side effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a string of 200 words
It returns 1 
"""
make_snippet("xxx 200 word snippet xxx") => 1

"""
Given a string of 900 words
It returns 5 (ie it rounds up)
"""
make_snippet("xxx 900 word snippet xxx ") => 5

"""
Given a string of 310 words
It returns 2 (ie it rounds up)
"""
make_snippet("xxx 310 word snippet xxx ") => 2

"""
Given a string of 7 words
It returns 1 (ie it rounds up)
"""
make_snippet("This will take less than one minute") => 1

"""
Given an empty string
It returns 0
"""
make_snippet("") => 0

"""
Given an incorrect data type
Throws Exception with error message
"""
make_snippet(99) => Exception("String not provided.")

"""
Given an empty string
It returns an empty string
"""
make_snippet("") => ""

"""
Given an input of None
It throws an error with the message "Error: No input given."
"""
extract_uppercase(None) => "Error: No input given."
```
_Encode each example as a test. You can add to the above list as you go._


## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
