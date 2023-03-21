def orderOfLargestPlusSign(n: int, mines: List[List[int]]) -> int:
    dp = [[n] * n for _ in range(n)]
    for x, y in mines:
        dp[x][y] = 0
    for i in range(n):
        l, r, u, d = 0, 0, 0, 0
        for j, k in zip(range(n), reversed(range(n))):
            l = l + 1 if dp[i][j] != 0 else 0
            dp[i][j] = min(dp[i][j], l)
            r = r + 1 if dp[i][k] != 0 else 0
            dp[i][k] = min(dp[i][k], r)
            u = u + 1 if dp[j][i] != 0 else 0
            dp[j][i] = min(dp[j][i], u)
            d = d + 1 if dp[k][i] != 0 else 0
            dp[k][i] = min(dp[k][i], d)
    return max(max(row) for row in dp)