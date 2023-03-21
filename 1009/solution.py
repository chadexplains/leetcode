class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        num_bits = int(math.log2(N)) + 1
        mask = (1 << num_bits) - 1
        return N ^ mask