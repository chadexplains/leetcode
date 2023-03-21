class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        indices = defaultdict(list)
        for i, c in enumerate(s):
            indices[c].append(i)
        count = 0
        for word in words:
            i = 0
            for c in word:
                if c not in indices:
                    break
                j = bisect_left(indices[c], i)
                if j == len(indices[c]):
                    break
                i = indices[c][j] + 1
            else:
                count += 1
        return count