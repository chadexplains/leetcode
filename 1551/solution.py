class Solution:
    def minOperations(self, n: int) -> int:
        median = (2 * (n // 2)) + 1
        return sum(abs((2 * i) + 1 - median) for i in range(n // 2))