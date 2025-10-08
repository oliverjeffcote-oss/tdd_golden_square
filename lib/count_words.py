def count_words(string):
    if isinstance(string, str) == False:
        raise Exception("String not given.")
    words = [word for word in string.split()]
    return len(words)