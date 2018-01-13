class Comment:
    def __init__(self, commentId, username, relevance, body, rang):
        self.commentId = commentId
        self.username = username
        if relevance == "Good":
            self.relevance = True
        else:
            self.relevance = False
        self.body = body
        self.rang = rang
        self.rangwaarde = 0
        self.dictionary = []

    def setrangwaarde(self, rangwaarde):
        self.rangwaarde = rangwaarde

    def setRang(self,rang):
        self.rang = rang

    def commentString(self):
        return "" + str(self.commentId) + " " + str(self.rang) + " " + str(self.rangwaarde) + " " + str(self.relevance).lower()

    def setDictionary(self, dictionary):
        self.dictionary = dictionary

    def setPercentage(self, percentage):
        self.rangwaarde = percentage
