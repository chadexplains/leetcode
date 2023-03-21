class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        nums.sort()
        max_diff = 0
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff > max_diff:
                max_diff = diff
        return max_diff