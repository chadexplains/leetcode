class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lp = {}
        for c in licensePlate:
            if c.isalpha():
                lp[c.lower()] = lp.get(c.lower(), 0) + 1
        shortest = None
        for word in words:
            freq = lp.copy()
            for c in word:
                if c.lower() in freq:
                    freq[c.lower()] -= 1
            if all(val <= 0 for val in freq.values()):
                if shortest is None or len(word) < len(shortest):
                    shortest = word
        return shortest