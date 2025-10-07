def make_snippet(sentence):
    # word_list = []

    if len(sentence.split()) > 5:
        return sentence + "..."
    else:
        return sentence