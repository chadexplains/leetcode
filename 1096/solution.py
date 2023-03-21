def largestSumOfAverages(A: List[int], K: int) -> float:
    n = len(A)
    prefix_sums = [0] * (n+1)
    for i in range(1, n+1):
        prefix_sums[i] = prefix_sums[i-1] + A[i-1]
    dp = [[0] * (n+1) for _ in range(K+1)]
    for j in range(1, n+1):
        dp[1][j] = prefix_sums[j] / j
    for i in range(2, K+1):
        for j in range(i, n+1):
            for k in range(i-1, j):
                dp[i][j] = max(dp[i][j], dp[i-1][k] + (prefix_sums[j] - prefix_sums[k]) / (j-k))
    return dp[K][n]