# import is used to make specialty functions available
# These are called modules
import os
import obo
import Frequentie as freq
from classes.Corpus import Corpus
from classes.Question import Question
from classes.Comment import Comment
from classes.Thread import Thread

from bs4 import BeautifulSoup

path = "data/SemEval2016-Task3-CQA-QL-dev-subtaskA.xml"
soup = BeautifulSoup(open(path, 'rt', encoding='utf-8'), 'xml')

threadsOrigin = soup.find_all('Thread')
threads = []
corpus = Corpus("")
for thread in threadsOrigin:
    threadId = thread['THREAD_SEQUENCE']
    t = Thread(threadId)
    qSub = thread.RelQuestion.RelQSubject.string
    qBody = thread.RelQuestion.RelQBody.string
    q = Question(qSub, qBody)
    i = 1
    comments = thread.find_all('RelComment')
    for comment in comments:
        commentId = comment['RELC_ID']
        username = comment['RELC_USERNAME']
        relevance = comment['RELC_RELEVANCE2RELQ']
        body = comment.RelCText.string
        c = Comment(commentId, username, relevance, body, i)
        q.add_comment(c)
        i += 1
        corpus.addCorpusText(body)
    obo.setQuestionDictionaries(q)
    t.set_question(q)
    threads.append(t)
    """
        print("thread id: " + t.id)
        print("question subject: " + t.question.subject)
        print("first comment: " + t.question.comments[0].body)
        print("question dictionary[0]: " + str(t.question.dictionary[0]))
        print("question comment dictionary[0]" + str(t.question.commentDictionary[0]))
        print("comment dictionary[0]: " + str(t.question.comments[0].dictionary[0]))
    """
obo.setCorpusDictionary(corpus)
#print("Corpus dictionary[0]: " + str(corpus.dictionary[0]))
for t in threads:
    q = t.question
    freq.percentageQuestion(corpus, q)
    print("question: " + str(t.id) + ", percentage: " + str(q.percentage))


# file = open("results.txt", "w")
# for thr in threads:
#     file.write(thr.threadString())
# file.close()


