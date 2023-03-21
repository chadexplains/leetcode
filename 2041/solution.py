class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        dp = [0] * (max_or + 1)
        dp[0] = 1
        for num in nums:
            for i in range(max_or, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[max_or]