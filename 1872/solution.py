class Solution:
    def stoneGameVIII(self, stones: List[int]) -> bool:
        n = len(stones)
        prefixSum = [0]*n
        prefixSum[0] = stones[0]
        for i in range(1, n):
            prefixSum[i] = prefixSum[i-1] + stones[i]
        dp = [0]*n
        dp[n-1] = prefixSum[n-1]
        for i in range(n-2, 0, -1):
            dp[i] = max(dp[i+1], prefixSum[i+1] - dp[i+1])
        return dp[1] > 0