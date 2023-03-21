class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        freq = collections.Counter(s)
        odd_count = sum(1 for f in freq.values() if f % 2 == 1)
        return odd_count <= k