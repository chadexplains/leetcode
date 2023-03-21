class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_pair_sum = float('-inf')
        left, right = 0, len(nums) - 1
        while left < right:
            pair_sum = nums[left] + nums[right]
            max_pair_sum = max(max_pair_sum, pair_sum)
            left += 1
            right -= 1
        return max_pair_sum