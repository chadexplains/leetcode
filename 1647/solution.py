class Solution:
    def minDeletions(self, s: str) -> int:
        freq = collections.Counter(s)
        freq_set = set()
        deletions = 0
        for char in freq:
            while freq[char] in freq_set:
                freq[char] -= 1
                deletions += 1
            freq_set.add(freq[char])
        return deletions