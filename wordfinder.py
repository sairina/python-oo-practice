from random import choice


class WordFinder:
    """Finds random words from text.
    
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, file_name):
        """Read contents of file and reports number of items read"""

        file = open(file_name)
        self.words = self.read(file)
        print(f"{len(self.words)} words read")

    def random(self):
        """Return random word"""

        return choice(self.words)

    def read(self, file):
        """Read file and create a list of words"""
        
        return [word.strip() for word in file]


class SpecialWordFinder(WordFinder):
    def read(self, file):
        """Read file and return random words that 
        are not blank lines or contain #"""

        return [word.strip() for word in file if word.strip() and not word.startswith("#")]