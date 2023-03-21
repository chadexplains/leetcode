class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, float('-inf'), float('-inf')]
        for num in nums:
            dp_new = dp.copy()
            for i in range(3):
                dp_new[(i + num) % 3] = max(dp_new[(i + num) % 3], dp[i] + num)
            dp = dp_new
        return dp[0]