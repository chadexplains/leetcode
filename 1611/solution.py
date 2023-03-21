class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        gray = n ^ (n >> 1)
        return bin(gray).count('1')