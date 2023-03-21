class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited = set()
        m, n = len(grid), len(grid[0])
        def dfs(i, j, pi, pj, val):
            if (i, j) in visited:
                return True
            visited.add((i, j))
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == val and (ni, nj) != (pi, pj):
                    if dfs(ni, nj, i, j, val):
                        return True
            return False
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True
        return False