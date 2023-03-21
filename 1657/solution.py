class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        freq1 = collections.Counter(word1)
        freq2 = collections.Counter(word2)
        return set(freq1.keys()) == set(freq2.keys()) and sorted(freq1.values()) == sorted(freq2.values())