class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        dp = {0: 1}
        max_or = 0
        for num in nums:
            for key in list(dp.keys()):
                new_or = key | num
                if new_or not in dp:
                    dp[new_or] = 0
                dp[new_or] += dp[key]
                max_or = max(max_or, new_or)
        return dp[max_or]