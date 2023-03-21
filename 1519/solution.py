class Solution:
    def minFlips(self, s: str) -> int:
        current_bit = s[0]
        flips_required = 0
        for i in range(1, len(s)):
            if s[i] != current_bit:
                flips_required += 1
                current_bit = s[i]
        return flips_required