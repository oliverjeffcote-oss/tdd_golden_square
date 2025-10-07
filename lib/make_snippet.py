def make_snippet(sentence):
    
    if sentence == None:
        raise Exception("Error: No input given.")
    
    if len(sentence.split()) > 5:
        return " ".join(sentence.split()[:5]) + "..."
    else:
        return sentence