class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if (i, j) in visited:
                return True
            visited.add((i, j))
            if grid[i][j] == 1:
                return True
            res = True
            for dx, dy in directions:
                res &= dfs(i+dx, j+dy)
            return res
        m, n = len(grid), len(grid[0])
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i, j) not in visited:
                    if dfs(i, j):
                        count += 1
        return count