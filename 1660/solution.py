class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        max_count = 0
        for i in range(len(sequence)):
            count = 0
            while sequence[i:i+len(word)] == word:
                count += 1
                i += len(word)
            max_count = max(max_count, count)
        return max_count