class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq = {}
        for i in range(len(s) - minSize + 1):
            substring = s[i:i+minSize]
            if len(set(substring)) <= maxLetters:
                freq[substring] = freq.get(substring, 0) + 1
        return max(freq.values()) if freq else 0