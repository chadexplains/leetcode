class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        left, right = len(nums), 0
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                left = min(left, i)
                right = max(right, i)
        return right - left + 1 if right > left else 0