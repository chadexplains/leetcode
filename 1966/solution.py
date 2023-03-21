class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        max_val = -1
        count = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > max_val:
                count += 1
                max_val = nums[i]
        return count