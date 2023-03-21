def generateAbbreviations(word):
    def backtrack(index, abbr, count):
        if index == len(word):
            res.append(abbr)
            return
        backtrack(index+1, abbr+word[index], 0)
        if count == 0:
            for i in range(index, len(word)):
                backtrack(i+1, abbr+str(i-index+1), 1)
    res = []
    backtrack(0, '', 0)
    return res