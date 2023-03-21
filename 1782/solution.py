class Solution:
    def countPairs(self, n: int, edges: List[List[int]], k: int) -> int:
        adj = [[0] * n for _ in range(n)]
        for u, v in edges:
            adj[u][v] = adj[v][u] = 1
        res = [[0] * n for _ in range(n)]
        for i in range(n):
            res[i][i] = 1
        while k:
            if k % 2:
                res = self.multiply(res, adj)
            adj = self.multiply(adj, adj)
            k //= 2
        return sum(sum(1 for x in row if x == k) for row in res) // 2
    def multiply(self, a, b):
        n = len(a)
        c = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    c[i][j] += a[i][k] * b[k][j]
        return c