from classes.Question import Question


class Thread:
    def __init__(self, id):
        self.id = id
        self.question = Question("", "")

    def set_question(self, question):
        self.question = question

    def threadString(self):
        returnValue = ""
        for comment in self.question.comments:
            returnValue += self.id + "  " + comment.commentString() + "\n"

        return returnValue
