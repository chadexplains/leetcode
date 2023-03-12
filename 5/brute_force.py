class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        for i in range(n):
            for j in range(i, n):
                if s[i:j+1] == s[i:j+1][::-1]:
                    if len(s[i:j+1]) > len(res):
                        res = s[i:j+1]
        return res
