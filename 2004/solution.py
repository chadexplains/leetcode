class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited or grid2[i][j] == 0:
                return
            visited.add((i, j))
            for di, dj in dirs:
                dfs(i+di, j+dj)
        
        m, n = len(grid2), len(grid2[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and (i, j) not in visited and grid1[i][j] == 1:
                    dfs(i, j)
                    count += 1
        return count