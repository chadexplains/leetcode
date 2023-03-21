class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        shifts = [0] * 26
        for i in range(len(s)):
            shift = (ord(t[i]) - ord(s[i])) % 26
            if shift != 0:
                if shifts[shift] == 0:
                    shifts[shift] = shift
                elif k < shifts[shift] + 26:
                    return False
                else:
                    shifts[shift] += 26
        return True