class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        parent = list(range(n))
        rank = [0] * n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] > rank[py]:
                parent[py] = px
            elif rank[px] < rank[py]:
                parent[px] = py
            else:
                parent[py] = px
                rank[px] += 1
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j] == 1:
                    union(i, j)
        return len(set(find(i) for i in range(n)))