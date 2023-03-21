class Solution:
    def encode(self, num: int) -> str:
        if num == 0:
            return ""
        binary = bin(num)[2:]
        binary = binary.lstrip('0')
        length = bin(len(binary))[2:]
        return '0' * (len(length) - 1) + length + binary