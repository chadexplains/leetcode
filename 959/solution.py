class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        uf = UnionFind(n*n*4)
        for i in range(n):
            for j in range(n):
                idx = i*n+j
                if i > 0:
                    uf.union(idx*4, (idx-n)*4+2)
                if i < n-1:
                    uf.union(idx*4+2, (idx+n)*4)
                if j > 0:
                    uf.union(idx*4+3, (idx-1)*4+1)
                if j < n-1:
                    uf.union(idx*4+1, (idx+1)*4+3)
                if grid[i][j] == '/':
                    uf.union(idx*4, idx*4+1)
                    uf.union(idx*4+2, idx*4+3)
                elif grid[i][j] == '\':
                    uf.union(idx*4, idx*4+3)
                    uf.union(idx*4+1, idx*4+2)
                else:
                    uf.union(idx*4, idx*4+1)
                    uf.union(idx*4+1, idx*4+2)
                    uf.union(idx*4+2, idx*4+3)
        return uf.count