class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        max_val = 0
        for num in arr:
            max_val = min(num, max_val + 1)
        return max_val