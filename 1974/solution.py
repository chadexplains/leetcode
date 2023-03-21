class Solution:
    def minTimeToType(self, word: str) -> int:
        prev = 'a'
        count = 0
        for c in word:
            distance = abs(ord(c) - ord(prev))
            count += min(distance, 26 - distance)
            prev = c
        return count