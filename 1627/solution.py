class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n

    def find(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
        if self.size[root_p] < self.size[root_q]:
            root_p, root_q = root_q, root_p
        self.parent[root_q] = root_p
        self.size[root_p] += self.size[root_q]
        self.count -= 1

def findCriticalEdges(n: int, edges: List[List[int]], threshold: int) -> List[List[int]]:
    uf = UnionFind(n)
    for u, v in edges:
        if abs(u - v) > threshold:
            uf.union(u - 1, v - 1)
    components = defaultdict(list)
    for i in range(n):
        components[uf.find(i)].append(i)
    res = []
    for component in components.values():
        if len(component) > 1:
            for i in range(len(component)):
                for j in range(i + 1, len(component)):
                    res.append([component[i] + 1, component[j] + 1])
    return res
