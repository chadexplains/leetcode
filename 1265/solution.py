class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        flat_grid = [grid[i][j] for i in range(m) for j in range(n)]
        k = k % (m * n)
        flat_grid = flat_grid[-k:] + flat_grid[:-k]
        return [flat_grid[i:i+n] for i in range(0, m*n, n)]