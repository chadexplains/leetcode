class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        for edge in edges:
            p1 = find(edge[0])
            p2 = find(edge[1])
            if p1 == p2:
                return edge
            parent[p1] = p2
        return []
