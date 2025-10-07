def make_snippet(sentence):

    if len(sentence.split()) > 5:
        return " ".join(sentence.split()[:5]) + "..."
    else:
        return sentence