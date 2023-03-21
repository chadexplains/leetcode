class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = {}
        for c in text:
            freq[c] = freq.get(c, 0) + 1
        min_freq = min(freq.get('b', 0), freq.get('a', 0), freq.get('n', 0))
        max_freq = min(freq.get('l', 0) // 2, freq.get('o', 0) // 2)
        return min_freq if min_freq <= max_freq else max_freq