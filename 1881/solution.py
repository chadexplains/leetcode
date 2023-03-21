class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val = 1
        curr_sum = 0
        for num in nums:
            curr_sum += num
            min_val = max(min_val, 1 - curr_sum)
        return min_val