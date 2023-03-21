class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(1, 0), (0, -1)],
            4: [(1, 0), (0, 1)],
            5: [(-1, 0), (0, -1)],
            6: [(-1, 0), (0, 1)]
        }
        visited = set()
        m, n = len(grid), len(grid[0])
        def dfs(x, y):
            if x == m - 1 and y == n - 1:
                return True
            visited.add((x, y))
            for dx, dy in directions[grid[x][y]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and (-dx, -dy) in directions[grid[nx][ny]]:
                    if dfs(nx, ny):
                        return True
            return False
        return dfs(0, 0)