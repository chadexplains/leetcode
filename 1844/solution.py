class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(c, x):
            return chr(ord(c) + x)
        res = ''
        for i in range(len(s)):
            if i % 2 == 0:
                res += s[i]
            else:
                res += shift(s[i-1], int(s[i]))
        return res