class Solution:
    def getMinimumDifference(self, nums: List[int]) -> int:
        nums.sort()
        min_diff = float('inf')
        for i in range(1, len(nums)):
            diff = abs(nums[i] - nums[i-1])
            if diff < min_diff:
                min_diff = diff
        return min_diff