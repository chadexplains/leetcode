class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        mod_count = 0
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                mod_count += 1
                if mod_count > 1:
                    return False
                if i < 2 or nums[i] >= nums[i-2]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
        return True