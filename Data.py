import itertools

class Data ():
    def getBasicDictionary (self):
        fileName = "dictionary.txt"
        data = open (fileName, "r")
        self.text = data.read().split('\n')
        dictionary = []
        for word in self.text:
            newEntry = [word.split('\t')]
            newEntry[0][1] = int(newEntry[0][1])
            dictionary += newEntry
        return dictionary

    def getComplexDictionary(self):
        fileName = 'goodDictionary.txt'
        data = open (fileName, "r")
        crudeText = data.read()
        byLines = crudeText.split("\n")
        for lineIndex in range (0, len(byLines)):
            line = byLines[lineIndex]
            while line.count('\t') > 1:
                ls = list (line)
                ls.remove('\t')
                line = ''.join(ls)
            line = line.split('\t')
            line[1] = float(line[1])
            byLines[lineIndex] = line
        return byLines

    def getCompanies (self):
        fileName = "Fortune500companies.txt"
        data = open (fileName, "r")
        text = data.read().split('\n')
        return text