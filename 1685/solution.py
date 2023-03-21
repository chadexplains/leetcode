class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        result = []
        for i in range(n):
            left_sum = prefix_sum[i]
            right_sum = prefix_sum[n-1] - prefix_sum[i]
            left_count = i + 1
            right_count = n - i - 1
            result.append((nums[i] * left_count - left_sum) + (right_sum - nums[i] * right_count))
        return result