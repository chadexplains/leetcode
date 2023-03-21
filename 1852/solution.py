class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = -1
        max_index = -1
        for i in range(len(nums)):
            if nums[i] > max_num:
                max_num = nums[i]
                max_index = i
        for i in range(len(nums)):
            if i != max_index and max_num < 2 * nums[i]:
                return -1
        return max_index