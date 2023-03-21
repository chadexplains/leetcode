class Solution:
    def minOperations(self, n: int) -> int:
        target = n
        result = 0
        for i in range(n):
            result += abs((2 * i + 1) - target)
        return result // 2