def minDifficulty(jobs: List[int], k: int) -> int:
    n = len(jobs)
    if n < k:
        return -1
    dp = [[float('inf')] * (k+1) for _ in range(n+1)]
    dp[0][1] = 0
    for i in range(1, n+1):
        dp[i][1] = max(dp[i-1][1], jobs[i-1])
    for i in range(2, n+1):
        for j in range(2, k+1):
            for x in range(j-2, i):
                dp[i][j] = min(dp[i][j], dp[x][j-1] + max(jobs[x+1:i+1]))
    return dp[n][k]