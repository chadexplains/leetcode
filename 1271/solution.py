class Solution:
    def toHexspeak(self, num: str) -> str:
        hex_num = hex(int(num))[2:].upper()
        hex_set = set(['A', 'B', 'C', 'D', 'E', 'F', 'I'])
        for c in hex_num:
            if c not in hex_set:
                return "ERROR"
        return hex_num.replace('0', 'O')