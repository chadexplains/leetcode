def splitLoopedString(strs):
    s = ''.join([max(s, s[::-1]) for s in strs])
    res = ''
    for i in range(len(s)):
        for j in range(2):
            tmp = s[i:] + s[:i][::-1] if j == 0 else s[i:][::-1] + s[:i]
            for k in range(len(strs)):
                if tmp.startswith(strs[k]) or tmp.endswith(strs[k]):
                    if tmp[::-1].startswith(strs[k]) or tmp[::-1].endswith(strs[k]):
                        res = max(res, tmp)
    return res