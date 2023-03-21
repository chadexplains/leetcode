class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        step_sum = 0
        min_start_value = float('inf')
        for num in nums:
            step_sum += num
            if step_sum < 1:
                min_start_value = min(min_start_value, abs(step_sum) + 1)
        return min_start_value if min_start_value != float('inf') else 1