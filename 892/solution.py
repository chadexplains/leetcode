class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    area += 2 + 4 * grid[i][j]
                if i:
                    area -= min(grid[i][j], grid[i-1][j])
                if j:
                    area -= min(grid[i][j], grid[i][j-1])
                if i < n - 1:
                    area -= min(grid[i][j], grid[i+1][j])
                if j < n - 1:
                    area -= min(grid[i][j], grid[i][j+1])
        return area