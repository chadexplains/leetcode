class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        for c in t:
            freq[ord(c) - ord('a')] -= 1
            if freq[ord(c) - ord('a')] < 0:
                return c
        return ''