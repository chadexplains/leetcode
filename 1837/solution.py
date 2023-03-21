class Solution:
    def difference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] - nums[0]