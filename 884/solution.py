class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        words = A.split() + B.split()
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        return [word for word in freq if freq[word] == 1]