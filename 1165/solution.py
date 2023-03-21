class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        index = {c: i for i, c in enumerate(keyboard)}
        prev = 0
        time = 0
        for c in word:
            time += abs(index[c] - prev)
            prev = index[c]
        return time