class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = reduce(lambda x, y: x | y, nums)
        dp = {0: 1}
        for num in nums:
            for k, v in list(dp.items()):
                dp[k | num] = dp.get(k | num, 0) + v
        return dp[max_or]