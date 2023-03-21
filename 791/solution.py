class Solution:
    def customSortString(self, S: str, T: str) -> str:
        freq = {}
        for c in T:
            freq[c] = freq.get(c, 0) + 1
        res = ""
        for c in S:
            if c in freq:
                res += c * freq[c]
                del freq[c]
        for c in freq:
            res += c * freq[c]
        return res