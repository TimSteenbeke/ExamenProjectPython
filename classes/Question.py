class Question:
    def __init__(self, subject, body):
        self.subject = subject
        self.body = body
        self.comments = []
        self.dictionary = []
        self.commentDictionary = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def setDictionary(self, dictionary):
        self.dictionary = dictionary

    def setAllCommentDictionary(self, dictionary):
        self.commentDictionary = dictionary

