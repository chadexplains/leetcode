class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        unique = set()
        left = right = 0
        max_sum = curr_sum = 0
        while right < len(nums):
            if nums[right] not in unique:
                unique.add(nums[right])
                curr_sum += nums[right]
                max_sum = max(max_sum, curr_sum)
                right += 1
            else:
                unique.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
        return max_sum