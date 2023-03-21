class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        ones = binary.count('1')
        zeros = binary.count('0')
        if zeros == 0:
            return binary
        first_zero = binary.index('0')
        consecutive_ones = binary[first_zero:].count('1')
        return '1' * (ones + consecutive_ones - 1) + '0' + '0' * (zeros - 1 - consecutive_ones)