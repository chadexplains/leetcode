class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left, right = 0, 0
        curr_sum = 0
        min_len = float('inf')
        while right < len(nums):
            curr_sum += nums[right]
            while curr_sum >= s:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1
            right += 1
        return min_len if min_len != float('inf') else 0