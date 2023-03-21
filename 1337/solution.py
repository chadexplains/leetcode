class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row_counts = [(i, sum(row)) for i, row in enumerate(mat)]
        row_counts.sort(key=lambda x: x[1])
        return [row[0] for row in row_counts[:k]]