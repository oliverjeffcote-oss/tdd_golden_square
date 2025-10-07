# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a writer 
I want my long sentence to be returned truncated with ...
So that I can see there is more text without taking up room on the screen

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def make_snippet(sentence):
    """Extracts the first 5 words from a string and appends "..."

    Parameters: (list all parameters and their types)
        sentence: a string that is a sentence containing multiple words (e.g. "Today I went to work and spoke to my colleague about xyz.")

    Returns: (state the return value and its type)
        a string of no more than 5 words with "..." added if the string contained more than five words initially

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
Given a sentence of 3 words
It returns the full sentence of 3 words
"""
make_snippet("Let's go party") => ["Let's go party"]

"""
Given a sentence of 5 words
It returns the full sentence of 5 words
"""
make_snippet("Today I went to work.") => ["Today I went to work."]

"""
Given a sentence of more than 5 words
The returned sentence contains ... at the end
"""
make_snippet("Today I went to work and handed in a project") => ["Today I went to work..."]

"""
Given a sentence of more than 5 words
It returns only the first five words with ... at the end
"""
make_snippet("Today I went to work and handed in a project") => ["Today I went to work..."]

"""
Given an empty string
It returns an empty string
"""
make_snippet("") => ""

"""
Given an input of None
It throws an error with the message "No sentence provided."
"""
extract_uppercase(None) => "No sentence provided."
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
