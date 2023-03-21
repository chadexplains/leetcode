class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        if num < 0:
            num += 2**32
        hex_map = '0123456789abcdef'
        hex_rep = ''
        while num != 0:
            hex_rep += hex_map[num % 16]
            num //= 16
        return hex_rep[::-1]