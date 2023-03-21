class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or grid2[i][j] == 0:
                return
            visited[i][j] = True
            sub_island.append((i, j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        m, n = len(grid2), len(grid2[0])
        visited = [[False]*n for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and not visited[i][j]:
                    sub_island = []
                    dfs(i, j)
                    valid = True
                    for x, y in sub_island:
                        if grid1[x][y] == 0:
                            valid = False
                            break
                    if valid:
                        count += 1
        return count