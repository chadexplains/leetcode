class Solution:
    def triangleJudgement(self, nums: List[int]) -> bool:
        nums.sort()
        return nums[0] + nums[1] > nums[2]