import math

def reading_time(text):
    if isinstance(text, str) == False:
        raise Exception("String not provided")
    return math.ceil(len(text.split())/200)