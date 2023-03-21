def maxSumAfterPartitioning(A, K):
    n = len(A)
    dp = [0] * (n+1)
    for i in range(1, n+1):
        max_val = 0
        for j in range(1, min(i, K)+1):
            max_val = max(max_val, A[i-j])
            dp[i] = max(dp[i], dp[i-j] + j * max_val)
    return dp[n]