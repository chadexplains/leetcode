class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        rhombus_sums = set()
        for i in range(m):
            for j in range(n):
                rhombus_sums.add(grid[i][j])
                for k in range(1, min(m-i, n-j, i+1, j+1)):
                    rhombus_sum = sum(grid[i-k][j-k+1:j+k]) + sum(grid[i+k][j-k+1:j+k]) + sum(grid[i-k+1:i+k][j-k]) + sum(grid[i-k+1:i+k][j+k]) - 2*grid[i-k][j] - 2*grid[i+k][j] - 2*grid[i][j-k] - 2*grid[i][j+k]
                    rhombus_sums.add(rhombus_sum)
        return sorted(rhombus_sums, reverse=True)[:3]