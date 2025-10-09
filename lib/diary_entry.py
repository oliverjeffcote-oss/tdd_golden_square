import math

class DiaryEntry:
    def __init__(self, title, contents):
        if title == '' or contents == '':
            raise Exception("Diary entries must have title and contents")

        self.title = title
        self.contents = contents
        self.words = contents.split()
        self.words_read = 0

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        return f"{self.title}: {self.contents}"

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        return len(self.contents.split())

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        if wpm <= 0:
            raise Exception("Cannot have a wpm value of 0 or less")
        
        reading_time_estimate = math.ceil(self.count_words() / wpm)
        return reading_time_estimate

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        
        number_of_words_user_can_read = wpm * minutes

        if self.words_read >= len(self.words):
            self.words_read = 0

        if self.words_read == 0:
            chunk = ' '.join(self.words[:number_of_words_user_can_read])
            self.words_read = number_of_words_user_can_read
            return chunk
        else:
            chunk = ' '.join(self.words[self.words_read:self.words_read + number_of_words_user_can_read])
            print(chunk)
            self.words_read += number_of_words_user_can_read
            return chunk

        
# diary_entry = DiaryEntry("xxx", text_two_900)
# print(diary_entry.reading_chunk(200, 3))
# print(diary_entry.reading_chunk(200, 3))
# print(diary_entry.reading_chunk(200, 3))
