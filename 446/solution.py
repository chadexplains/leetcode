class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [{} for i in range(n)]
        ans = 0
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff > 2147483647 or diff < -2147483648:
                    continue
                cnt = dp[j].get(diff, 0)
                ans += cnt
                dp[i][diff] = dp[i].get(diff, 0) + cnt + 1
        return ans