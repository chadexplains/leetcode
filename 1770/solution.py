class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[float('-inf')] * (m+1) for _ in range(m+1)]
        dp[0][0] = 0
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] + nums[i-1] * multipliers[m-i]
        for j in range(1, m+1):
            dp[0][j] = dp[0][j-1] + nums[n-j] * multipliers[m-j]
        for i in range(1, m+1):
            for j in range(1, m-i+1):
                dp[i][j] = max(dp[i-1][j] + nums[i-1] * multipliers[m-i+j], dp[i][j-1] + nums[n-j] * multipliers[m-i+j])
        return dp[m][m]