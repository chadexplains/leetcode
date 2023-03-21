class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target == 0:
            return len(nums)
        if target < 0:
            return -1
        left, right, curr_sum, min_ops = 0, 0, 0, float('inf')
        while right < len(nums):
            curr_sum += nums[right]
            while curr_sum > target and left <= right:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == target:
                min_ops = min(min_ops, len(nums) - (right - left + 1))
            right += 1
        return min_ops if min_ops != float('inf') else -1