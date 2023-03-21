class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.count -= 1

def makeConnected(n: int, connections: List[List[int]]) -> int:
    uf = UnionFind(n)
    for a, b in connections:
        uf.union(a, b)
    sets = set(uf.find(i) for i in range(n))
    return uf.count - 1 if len(sets) - 1 <= uf.count - 1 else -1