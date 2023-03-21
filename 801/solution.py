def minSwap(A, B):
    n = len(A)
    dp = [[0, 1] for _ in range(n)]
    for i in range(1, n):
        if A[i] > A[i-1] and B[i] > B[i-1]:
            dp[i][0] = dp[i-1][0]
            dp[i][1] = dp[i-1][1] + 1
        if A[i] > B[i-1] and B[i] > A[i-1]:
            dp[i][0] = dp[i-1][1]
            dp[i][1] = dp[i-1][0] + 1
    return min(dp[n-1][0], dp[n-1][1])