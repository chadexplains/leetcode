class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        curr_len = 1
        max_len = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr_len += 1
            else:
                curr_len = 1
            max_len = max(max_len, curr_len)
        return max_len