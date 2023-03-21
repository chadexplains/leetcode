class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def backtrack(i, j, curr):
            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or grid[i][j] == 0:
                return
            visited[i][j] = True
            curr += grid[i][j]
            nonlocal max_gold
            max_gold = max(max_gold, curr)
            backtrack(i+1, j, curr)
            backtrack(i-1, j, curr)
            backtrack(i, j+1, curr)
            backtrack(i, j-1, curr)
            visited[i][j] = False
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        max_gold = 0
        for i in range(m):
            for j in range(n):
                backtrack(i, j, 0)
        return max_gold