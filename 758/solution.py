def boldWords(words: List[str], S: str) -> str:
    bold = [False] * len(S)
    for word in words:
        start = S.find(word)
        while start != -1:
            for i in range(start, start+len(word)):
                bold[i] = True
            start = S.find(word, start+1)
    res = []
    i = 0
    while i < len(S):
        if bold[i]:
            res.append("<b>")
            while i < len(S) and bold[i]:
                res.append(S[i])
                i += 1
            res.append("</b>")
        else:
            res.append(S[i])
            i += 1
    return ''.join(res)