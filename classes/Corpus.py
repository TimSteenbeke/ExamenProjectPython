class Corpus:
    def __init__(self, text):
        self.text = text
        self.dictionary = []

    def addCorpusText(self, text):
        self.text += text

    def setDictionary(self, dictionary):
        self.dictionary = dictionary
