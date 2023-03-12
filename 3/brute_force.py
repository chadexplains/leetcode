class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i+1, n+1):
                if len(set(s[i:j])) == j - i:
                    res = max(res, j - i)
        return res
