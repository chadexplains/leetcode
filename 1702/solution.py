class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        count_zeros = binary.count('0')
        if count_zeros == 0:
            return binary
        first_zero = binary.index('0')
        result = '1' * (len(binary) - count_zeros - 1) + '0' + '1' * count_zeros
        return result