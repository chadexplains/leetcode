class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev = 0
        result = 0
        for num in target:
            diff = num - prev
            if diff > 0:
                result += diff
            prev = num
        return result