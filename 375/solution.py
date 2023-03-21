def getMoneyAmount(n):
    dp = [[0] * (n+1) for _ in range(n+1)]
    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            dp[i][j] = min(k + max(dp[i][k-1], dp[k+1][j]) for k in range(i, j))
    return dp[1][n]