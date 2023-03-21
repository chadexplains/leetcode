class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        dp = {0: 1}
        for num in nums:
            for key in list(dp.keys()):
                new_key = key | num
                if new_key not in dp:
                    dp[new_key] = 0
                dp[new_key] += dp[key]
        return dp[max_or]