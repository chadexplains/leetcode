class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_val = max(nums)
        dp = [0] * (max_val + 1)
        for num in nums:
            dp[num] += num
        prev = 0
        curr = 0
        for i in range(max_val + 1):
            temp = max(curr, prev + dp[i])
            prev = curr
            curr = temp
        return curr