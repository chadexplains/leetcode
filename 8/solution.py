class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        num = 0
        for c in s:
            if not c.isdigit():
                break
            num = num * 10 + int(c)
            if num > 2**31 - 1:
                return 2**31 - 1 if sign == 1 else -2**31
        return sign * num