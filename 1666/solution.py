class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        max_count = 0
        for i in range(len(sequence)):
            for j in range(i+1, len(sequence)):
                if sequence[i:j] == word:
                    count = 1
                    k = j
                    while k + len(word) <= len(sequence) and sequence[k:k+len(word)] == word:
                        count += 1
                        k += len(word)
                    max_count = max(max_count, count)
        return max_count