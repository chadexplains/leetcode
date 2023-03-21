class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j, index):
            if 0 <= i < n and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = index
                return 1 + dfs(i+1, j, index) + dfs(i-1, j, index) + dfs(i, j+1, index) + dfs(i, j-1, index)
            return 0
        
        n = len(grid)
        area = {0:0}
        index = 2
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area[index] = dfs(i, j, index)
                    index += 1
        res = max(area.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set(grid[i+dx][j+dy] for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)) if 0 <= i+dx < n and 0 <= j+dy < n and grid[i+dx][j+dy] > 1)
                    res = max(res, 1 + sum(area[index] for index in seen))
        return res