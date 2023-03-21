def largeGroupPositions(s):
    result = []
    start = 0
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            if i - start >= 3:
                result.append([start, i-1])
            start = i
    if len(s) - start >= 3:
        result.append([start, len(s)-1])
    return result