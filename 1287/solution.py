class Solution:
    def findSpecialInteger(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0, n, n//4):
            if nums.count(nums[i]) > n//4:
                return nums[i]
        return -1