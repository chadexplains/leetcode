class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = right = 0
        max_len = 0
        num_zeros = 0
        while right < len(nums):
            if nums[right] == 0:
                num_zeros += 1
            while num_zeros > 1:
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1
            max_len = max(max_len, right - left)
            right += 1
        return max_len