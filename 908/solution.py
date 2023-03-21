class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        max_A = max(A)
        min_A = min(A)
        diff = max_A - min_A
        if diff > 2 * K:
            return diff - 2 * K
        else:
            return 0