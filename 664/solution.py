def strangePrinter(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n): dp[i][i] = 1
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = dp[i + 1][j] + 1
            for k in range(i + 1, j):
                if s[k] == s[i]:
                    dp[i][j] = min(dp[i][j], dp[i][k - 1] + dp[k + 1][j])
            if s[i] == s[j]:
                dp[i][j] = min(dp[i][j], dp[i + 1][j])
    return dp[0][n - 1]