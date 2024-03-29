def stoneGame(piles):
    n = len(piles)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = piles[i]
    for d in range(1, n):
        for i in range(n - d):
            j = i + d
            dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
    return dp[0][n-1] > 0