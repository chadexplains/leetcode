def findSubstringInWraproundString(p):
    dp = [0] * 26
    max_len = 0
    for i in range(len(p)):
        if i > 0 and (ord(p[i]) - ord(p[i-1]) == 1 or ord(p[i-1]) - ord(p[i]) == 25):
            max_len += 1
        else:
            max_len = 1
        dp[ord(p[i]) - ord('a')] = max(dp[ord(p[i]) - ord('a')], max_len)
    return sum(dp)