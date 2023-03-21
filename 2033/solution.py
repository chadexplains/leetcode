class Solution:
    def minOperations(self, grid: List[List[int]], target: int) -> int:
        flat = sorted([x for row in grid for x in row])
        median = flat[len(flat) // 2]
        return sum(abs(x - median) for row in grid for x in row)