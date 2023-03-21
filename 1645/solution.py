class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target == 0:
            return len(nums)
        if target < 0:
            return -1
        left, right, curr_sum, max_len = 0, 0, 0, -1
        while right < len(nums):
            curr_sum += nums[right]
            while left <= right and curr_sum > target:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == target:
                max_len = max(max_len, right - left + 1)
            right += 1
        return len(nums) - max_len if max_len != -1 else -1