def numWays(n: int, k: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return k
    dp = [[0, 0] for _ in range(n)]
    dp[0][0], dp[0][1], dp[1][0], dp[1][1] = k, k, k * (k - 1), k
    for i in range(2, n):
        dp[i][0] = dp[i-1][1]
        dp[i][1] = (dp[i-1][0] + dp[i-1][1]) * (k - 1)
    return dp[n-1][0] + dp[n-1][1]