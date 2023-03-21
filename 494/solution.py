class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        sum_nums = sum(nums)
        if sum_nums < S or (sum_nums + S) % 2 == 1:
            return 0
        target = (sum_nums + S) // 2
        dp = [[0] * (2 * target + 1) for _ in range(n + 1)]
        dp[0][target] = 1
        for i in range(1, n + 1):
            for j in range(2 * target + 1):
                if j - nums[i - 1] >= 0:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]
                if j + nums[i - 1] <= 2 * target:
                    dp[i][j] += dp[i - 1][j + nums[i - 1]]
        return dp[n][target + S]