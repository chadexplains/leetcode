class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        logs.sort()
        uf = UnionFind(N)
        for log in logs:
            uf.union(log[1], log[2])
            if uf.count == 1:
                return log[0]
        return -1

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    def find(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p != root_q:
            self.parent[root_p] = root_q
            self.count -= 1
