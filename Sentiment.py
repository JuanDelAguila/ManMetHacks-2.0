import string
import itertools
class Sentiment ():

    def simple (self, data, dictionary):
        score = 0
        for item in data:
            for entry in dictionary:
                word = entry[0]
                wordScore = entry[1]
                if word == item:
                    score += wordScore
        
        return score

    def rankSentenceScores (self, data, dictionary):
        bySentences = simpleSplitBySentences (data)
        prettyBySentences = prettySplitBySentences (data)
        sentenceScores = []
        for sentence in bySentences:
            score = 0
            for word in sentence:
                for entry in dictionary:
                    term = entry[0]
                    termScore = entry[1]
                    if word == term:
                        score += termScore
            sentenceScores += [score]
        
        numPosScores = len(list(filter (lambda x: x > 0, sentenceScores)))
        numNegScores = len (list (filter (lambda x: x < 0, sentenceScores)))
        print ("\n")
        print ("The total score is: " + str(sum(sentenceScores)), end = '\n\n')
        print ("There are " + str (numPosScores) + " positive sentences")
        print ("The most positive sentence(s) were: ", end = '\n\n')
        greatestScores = list(filter (lambda x: x > 0, sorted(set(sentenceScores))[-3:]))
        positive = [[prettyBySentences[index], score]for (score, index) in zip (sentenceScores, range(0, len(sentenceScores))) if score in greatestScores]
        positive.sort(key = lambda x: (-x[1], -len(x[0])))
        positive = positive[:3]
        for item in positive:
            print(' '.join(item[0]))
            print("--- Score = " + str (item[1]), end = '\n\n')
        
        print ("There are " + str (numNegScores) + " negative sentences")
        print ("The most negative sentence(s) were: ", end = '\n\n')
        lowestScores = list (filter (lambda x: x < 0, sorted(set(sentenceScores))[:3]))
        negative = [[prettyBySentences[index], score]for (score, index) in zip (sentenceScores, range(0, len(sentenceScores))) if score in lowestScores]
        negative.sort(key=lambda x: (x[1], -len(x[0])))
        negative = negative[:3]
        for item in negative:
            print(' '.join(item[0]))
            print("--- Score = " + str (item[1]), end = '\n\n')
        


def simpleSplitBySentences (data):
    sentenceData = []
    while len(data) != 0:
        untilPeriod = myTakeWhileInclusive(data, lambda w: not (w[-1] == '.'))
        if (len(data) > len(untilPeriod)):
            nextWord = data[len(untilPeriod)]
            if nextWord[0].isupper():
                sentenceData += [untilPeriod]
                data = data[len(untilPeriod):]
            else:
                removePeriod = ''.join(list(filter(lambda x: x != '.', data[len(untilPeriod)-1])))
                data[len(untilPeriod)-1] = removePeriod
        else:
            sentenceData += [untilPeriod]
            data = [] 
    return lowerCase (onlyReadableCharacters (sentenceData))
        
def prettySplitBySentences (data):
    sentenceData = []
    while len(data) != 0:
        untilPeriod = myTakeWhileInclusive(data, lambda w: not (w[-1] == '.'))
        if (len(data) > len(untilPeriod)):
            nextWord = data[len(untilPeriod)]
            if nextWord[0].isupper():
                sentenceData += [untilPeriod]
                data = data[len(untilPeriod):]
            else:
                removePeriod = ''.join(list(filter(lambda x: x != '.', data[len(untilPeriod)-1])))
                data[len(untilPeriod)-1] = removePeriod
        else:
            sentenceData += [untilPeriod]
            data = []
    return prettyReadableCharacters (sentenceData)

def myTakeWhileInclusive (text, predicate):
    product = list (itertools.takewhile(predicate, text))
    if (len(text) > len(product)):
        product += [text[len(product)]]
    return product
    
    
def onlyReadableCharacters (sentences):
    permitedCharacters = string.ascii_letters + "-,.;:‘’—" + "1234567890" + "$€" + "“”"
    for sentenceIndex in range (0, len(sentences)):
        sentence = sentences[sentenceIndex]
        for wordIndex in range (0, len(sentence)):
            word = sentence[wordIndex]
            sentences[sentenceIndex][wordIndex] = ''.join(list(filter (lambda x: x in permitedCharacters, word)))
    return (sentences)

def prettyReadableCharacters (sentences):
    permitedCharacters = string.ascii_letters + "-,.;:‘’—" + "1234567890" + "$€" + "“”" + "?!"
    for sentenceIndex in range (0, len(sentences)):
        sentence = sentences[sentenceIndex]
        for wordIndex in range (0, len(sentence)):
            word = sentence[wordIndex]
            sentences[sentenceIndex][wordIndex] = ''.join(list(filter (lambda x: x in permitedCharacters, word)))
    return (sentences)

def lowerCase (sentences):
    for sentenceIndex in range (0, len(sentences)):
        sentence = sentences[sentenceIndex]
        for wordIndex in range (0, len(sentence)):
            sentences[sentenceIndex][wordIndex] = ''.join(list(map (lambda l: l.lower(), sentences[sentenceIndex][wordIndex]))) 
    return (sentences)


