def splitArraySameAverage(A):
    n = len(A)
    s = sum(A)
    if s % n == 0:
        dp = [[False] * (s + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            for j in range(s + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= A[i - 1]:
                    dp[i][j] |= dp[i - 1][j - A[i - 1]]
        for i in range(1, n // 2 + 1):
            if s * i % n == 0 and dp[i][s * i // n]:
                return True
    return False