class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        s = ['a'] * n
        k -= n
        i = n - 1
        while k > 0:
            s[i] = chr(ord(s[i]) + min(k, 25))
            k -= min(k, 25)
            i -= 1
        return ''.join(s)