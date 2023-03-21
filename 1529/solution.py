class Solution:
    def minFlips(self, s: str) -> int:
        transitions = 0
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                transitions += 1
        return transitions