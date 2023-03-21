class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        max_col = min(steps // 2 + 1, arrLen)
        dp = [[0] * (max_col + 2) for _ in range(steps + 1)]
        dp[0][0] = 1
        for i in range(1, steps + 1):
            for j in range(0, max_col):
                dp[i][j] = (dp[i-1][j] + dp[i-1][j-1] + dp[i-1][j+1]) % MOD
            max_col = min(steps - i + 1, arrLen)
        return dp[steps][0]