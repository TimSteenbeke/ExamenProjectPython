import nltk
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer, PorterStemmer

lmtzr = WordNetLemmatizer()
stm = PorterStemmer()

def lemetizeWordList(wordlist):
    for i in range(len(wordlist)):
        lemWord = lmtzr.lemmatize(wordlist[i])
        wordlist[i] = lemWord
        return wordlist

def stemetizWordList(wordlist):
    for i in range(len(wordlist)):
        stemWord = stm.stem(wordlist[i])
        wordlist[i] = stemWord
        return wordlist


def commentRang(question):
    comments = question.comments
    commentsSorted = sorted(comments, key=lambda comment: comment.rangwaarde, reverse=True)
    for i in range(len(commentsSorted)):
        commentsSorted[i].setRang(i+1)
    question.comments = commentsSorted


def regexText(text):
    regText = nltk.re.sub('[^A-Za-z]+', ' ', text)
    return regText