def longestPalindromeSubseq(self, s: str, k: int) -> int:
    n = len(s)
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][i] = 1
    for i in range(n, 0, -1):
        for j in range(i+1, n+1):
            if s[i-1] == s[j-1]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[1][n] + min(k, n - dp[1][n])