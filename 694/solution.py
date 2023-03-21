class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(i, j, path):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return
            grid[i][j] = 0
            path.append((i - r, j - c))
            dfs(i + 1, j, path)
            dfs(i - 1, j, path)
            dfs(i, j + 1, path)
            dfs(i, j - 1, path)
        shapes = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    path = []
                    dfs(r, c, path)
                    shapes.add(tuple(path))
        return len(shapes)