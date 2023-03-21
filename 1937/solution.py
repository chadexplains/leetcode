def maxPoints(self, points: List[List[int]], k: int) -> int:
    m, n = len(points), len(points[0])
    dp = [[0] * n for _ in range(m)]
    for j in range(n):
        dp[0][j] = points[0][j]
    for i in range(1, m):
        left = [0] * n
        right = [0] * n
        left[0] = dp[i-1][0]
        for j in range(1, n):
            left[j] = max(left[j-1] - 1, dp[i-1][j])
        right[n-1] = dp[i-1][n-1]
        for j in range(n-2, -1, -1):
            right[j] = max(right[j+1] - 1, dp[i-1][j])
        for j in range(n):
            dp[i][j] = max(left[j], right[j], dp[i-1][j]) + points[i][j]
    return max(dp[-1])