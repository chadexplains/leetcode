class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            parent[find(x)] = find(y)
        candidates = []
        for u, v in edges:
            if parent[v] != v:
                candidates.append([u, v])
            else:
                parent[v] = u
                if find(u) == find(v):
                    return [u, v]
        if candidates:
            return candidates[-1]
        return [0, 0]