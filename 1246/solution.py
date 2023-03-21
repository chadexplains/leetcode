def minimumMoves(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            dp[i][j] = float('inf')
            if arr[i] == arr[j]:
                dp[i][j] = dp[i+1][j-1]
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])
    return dp[0][n-1]