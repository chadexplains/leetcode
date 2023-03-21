def tallestBillboard(rods):
    n = len(rods)
    s = sum(rods)
    dp = [[-1] * (s + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for j in range(s + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= rods[i - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - rods[i - 1]] + rods[i - 1])
            if j + rods[i - 1] <= s:
                dp[i][j] = max(dp[i][j], dp[i - 1][j + rods[i - 1]])
    return dp[n][0]