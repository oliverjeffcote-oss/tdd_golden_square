from lib.diary_entry import DiaryEntry

'''
When initiating a new instance of DiaryEntry with a title and contents
Title is stored and can be returned
'''

def test_diary_entry_stores_title():
    diary_entry = DiaryEntry("Monday 1st September", "Today I went to the park with my dog.")
    result = diary_entry.title

    assert result == "Monday 1st September"

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

'''
When requesting a word count on the diary entry
Returns an integer of the number of words in the diary entry.
'''

'''
When given an integer that represents the number of words per minute a user can read
Returns an integer with an estimate of the reading time in minutes for the diary entry at that given words per minute
'''

'''
When given words per minute and an integer with number of minutes a user has got to read
will return a string with the contents that the user can read in the given number of minutes
'''

'''
When some of the content has already been read, the next chunk is provided for the user to read in the specified number of minutes
'''

'''
When there is some content left and the remaining content is requested
It is returned
'''

'''
When there is no diary content left and the user asks for the next reading chunk
It returns the chunk that starts from the beginning 
'''