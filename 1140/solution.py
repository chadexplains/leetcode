def stoneGameII(piles):
    n = len(piles)
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        for j in range(n, 0, -1):
            if i+j >= n:
                dp[i][j] = sum(piles[i:])
            else:
                for k in range(1, 2*j+1):
                    dp[i][j] = max(dp[i][j], sum(piles[i:i+k]) + dp[i+k][max(j, k)])
    return dp[0][1]