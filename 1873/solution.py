class Solution:
    def stoneGameVIII(self, stones: List[int]) -> bool:
        n = len(stones)
        prefix_sum = [0] * n
        prefix_sum[0] = stones[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + stones[i]
        dp = [0] * n
        dp[n-1] = prefix_sum[n-1]
        for i in range(n-2, 0, -1):
            dp[i] = max(dp[i+1], prefix_sum[i] - dp[i+1])
        return dp[1] > 0