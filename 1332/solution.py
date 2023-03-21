class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == s[::-1]:
            return 1
        return 2 if len(set(s)) == 2 else 1