class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + stoneValue[i - 1]
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for k in range(i, j):
                    left_sum = prefix_sum[k + 1] - prefix_sum[i]
                    right_sum = prefix_sum[j + 1] - prefix_sum[k + 1]
                    if left_sum <= right_sum:
                        dp[i][j] = max(dp[i][j], left_sum + dp[i][k])
                    if left_sum >= right_sum:
                        dp[i][j] = max(dp[i][j], right_sum + dp[k + 1][j])
        return dp[0][n - 1]