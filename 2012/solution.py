class Solution:
    def beautySum(self, s: str) -> int:
        result = 0
        for i in range(2, len(s)):
            result += (s[i-2] == s[i-1]) + (s[i-1] == s[i]) + (s[i-2] == s[i])
        return result