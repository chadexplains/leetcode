class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        def dfs(r, c):
            if (r, c) in visited:
                return
            visited.add((r, c))
            if r == 0 or r == m - 1 or c == 0 or c == n - 1 or grid[r - 1][c] != color or grid[r + 1][c] != color or grid[r][c - 1] != color or grid[r][c + 1] != color:
                border.add((r, c))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == color:
                    dfs(nr, nc)
        m, n = len(grid), len(grid[0])
        visited, border = set(), set()
        dfs(r0, c0)
        for r, c in border:
            grid[r][c] = color
        return grid