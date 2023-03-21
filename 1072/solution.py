class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        counts = {}
        for row in matrix:
            pattern = tuple([1-x for x in row]) if row[0] == 0 else tuple(row)
            counts[pattern] = counts.get(pattern, 0) + 1
        return max(counts.values())