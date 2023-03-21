class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = {}
        for c in s:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1
        first_freq = freq[s[0]]
        for f in freq.values():
            if f != first_freq:
                return False
        return True