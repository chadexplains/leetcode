class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 1 or (i, j) in visited:
                return
            visited.add((i, j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        m, n = len(grid), len(grid[0])
        visited = set()
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i, j) not in visited:
                    is_closed = True
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        if x == 0 or x == m-1 or y == 0 or y == n-1:
                            is_closed = False
                        dfs(x, y)
                        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nx, ny = x+dx, y+dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                                stack.append((nx, ny))
                    if is_closed:
                        count += 1
        return count