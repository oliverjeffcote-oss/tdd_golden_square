def check_grammar(sentence):

    if not isinstance(sentence,str):
        raise Exception("Incorrect data type provided")
    
    if len(sentence) < 2:
        return "Sentence not long enough to check"

    return (sentence[-1] in '.!?' and sentence[0].isupper())

