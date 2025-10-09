class GrammarStats:
    def __init__(self):
        self.checked_texts = 0
        self.passed_texts = 0

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if text == '':
            raise Exception("Cannot check an empty string")
        
        self.checked_texts += 1
        if text[0].isupper() and text[-1] in '.!?':
            self.passed_texts += 1
            return True
        else:
            return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        return int((self.passed_texts / self.checked_texts) * 100)
