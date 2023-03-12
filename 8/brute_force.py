class Solution:
    def myAtoi(self, s: str) -> int:
        res = ""
        sign = 1
        for i, c in enumerate(s):
            if c == " ":
                continue
            elif c == "+" or c == "-":
                if i < len(s) - 1 and s[i + 1].isdigit():
                    sign = 1 if c == "+" else -1
                else:
                    return 0
            elif c.isdigit():
                res += c
            else:
                break
        if res == "":
            return 0
        res = sign * int(res)
        if res < -2**31:
            return -2**31
        elif res > 2**31 - 1:
            return 2**31 - 1
        else:
            return res
