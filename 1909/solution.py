class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        removed = False
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                if removed:
                    return False
                if i == 1 or nums[i-2] < nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
                removed = True
        return True