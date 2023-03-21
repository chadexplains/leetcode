class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        mask = (1 << len(binary)) - 1
        complement = num ^ mask
        return int(str(complement), 2)