def addBoldTag(s: str, dict: List[str]) -> str:
    n = len(s)
    bold = [False] * n
    for word in dict:
        start = s.find(word)
        while start != -1:
            for i in range(start, start+len(word)):
                bold[i] = True
            start = s.find(word, start+1)
    ans = []
    i = 0
    while i < n:
        if bold[i]:
            ans.append("<b>")
            while i < n and bold[i]:
                ans.append(s[i])
                i += 1
            ans.append("</b>")
        else:
            ans.append(s[i])
            i += 1
    return ''.join(ans)