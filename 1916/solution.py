class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        uf = UnionFind(m * n)
        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 1:
                    if i > 0 and grid1[i - 1][j] == 1:
                        uf.union(i * n + j, (i - 1) * n + j)
                    if j > 0 and grid1[i][j - 1] == 1:
                        uf.union(i * n + j, i * n + j - 1)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and not uf.visited(i * n + j):
                    if self.dfs(grid1, grid2, i, j):
                        count += 1
        return count
    def dfs(self, grid1, grid2, i, j):
        if i < 0 or i >= len(grid2) or j < 0 or j >= len(grid2[0]) or grid2[i][j] == 0:
            return True
        if grid1[i][j] == 0:
            return False
        grid2[i][j] = 0
        return self.dfs(grid1, grid2, i - 1, j) and self.dfs(grid1, grid2, i + 1, j) and self.dfs(grid1, grid2, i, j - 1) and self.dfs(grid1, grid2, i, j + 1)
