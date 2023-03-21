class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)):
            if nums[i] >= i+1 and (i == 0 or nums[i-1] < i+1):
                return i+1
        return -1