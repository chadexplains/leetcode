class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        max_sum = nums[0]
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]
        for i in range(1, n):
            prefix[i] = max(nums[i], prefix[i-1] + nums[i])
            max_sum = max(max_sum, prefix[i])
        for i in range(n-2, -1, -1):
            suffix[i] = max(nums[i], suffix[i+1] + nums[i])
        for i in range(n):
            max_sum = max(max_sum, max(prefix[i-1] if i > 0 else 0, suffix[i+1] if i < n-1 else 0) + nums[i])
        return max_sum