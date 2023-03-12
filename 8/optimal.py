class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        sign = 1
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        if i < len(s) and (s[i] == "+" or s[i] == "-"):
            sign = 1 if s[i] == "+" else -1
            i += 1
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
        res *= sign
        if res < -2**31:
            return -2**31
        elif res > 2**31 - 1:
            return 2**31 - 1
        else:
            return res
