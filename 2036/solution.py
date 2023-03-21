class Solution:
    def minOperations(self, nums: List[int]) -> int:
        prev = nums[0]
        ops = 0
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                ops += prev - nums[i] + 1
                nums[i] = prev + 1
            prev = nums[i]
        return ops