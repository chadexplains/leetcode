class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi == pj:
            return
        if self.size[pi] > self.size[pj]:
            pi, pj = pj, pi
        self.parent[pi] = pj
        self.size[pj] += self.size[pi]
        self.count -= 1

def minMalwareSpread(graph: List[List[int]], initial: List[int]) -> int:
    n = len(graph)
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] == 1:
                uf.union(i, j)
    infected = collections.Counter(uf.find(i) for i in initial)
    candidates = [(i, uf.find(i), infected[uf.find(i)] == 1) for i in initial]
    candidates.sort(key=lambda x: (-x[2], x[1]))
    for i, _, _ in candidates:
        for j in range(n):
            if graph[i][j] == 1 and uf.find(i) != uf.find(j):
                infected[uf.find(j)] += 1
        uf.parent[i] = i
    return min(initial, key=lambda x: (infected[uf.find(x)], x))