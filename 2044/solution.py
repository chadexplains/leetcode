class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = reduce(lambda x, y: x | y, nums)
        n = len(nums)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                if reduce(lambda x, y: x | y, nums[i:j]) == max_or:
                    dp[i] += dp[j] + 1
        return dp[0]