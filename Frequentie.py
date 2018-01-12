import math

def percentageQuestion(corpus, question):
    l = 0.75
    questionDict = question.dictionary
    corpusDict = corpus.dictionary
    questionPercentage = 0
    for key in questionDict:
        if key in corpusDict.keys():
            questionPercentage += math.log10((l*questionDict[key]) + ((1-l) *corpusDict[key]))
        else:
            questionPercentage += math.log10(questionDict[key])

    question.setPercentage(questionPercentage)
