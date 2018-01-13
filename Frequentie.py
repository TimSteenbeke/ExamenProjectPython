import math

def percentageQuestion(corpus, question):
    l = 0.75
    questionDict = question.dictionary
    corpusDict = corpus.dictionary
    questionPercentage = 0
    for key in questionDict:
        if key in corpusDict.keys():
            questionPercentage += math.log10((l*questionDict[key]) + ((1-l) *corpusDict[key]))
            # questionPercentage += ((l*questionDict[key]) + ((1-l) *corpusDict[key]))
        else:
            questionPercentage += math.log10(questionDict[key])
            # questionPercentage += (questionDict[key])

    question.setPercentage(questionPercentage)

    for comment in question.comments:
        commentdict = comment.dictionary
        commentPercentage = 0
        for key in questionDict.keys():
            if key in commentdict.keys():
                if key in corpusDict.keys():
                    commentPercentage += math.log10((l*commentdict[key]) + ((1-l) *corpusDict[key]))
                    # commentPercentage += ((l * commentdict[key]) + ((1 - l) * corpusDict[key]))
                else:
                    commentPercentage += math.log10(commentdict[key])
                    # commentPercentage += (commentdict[key])
            comment.setPercentage(commentPercentage)

