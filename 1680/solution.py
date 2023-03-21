class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result = 0
        for i in range(1, n+1):
            binary_i = bin(i)[2:]
            result = (result << len(binary_i)) + i
            result %= 10**9 + 7
        return result