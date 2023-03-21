class UnionFind:
    def __init__(self):
        self.parent = list(range(26))
        self.rank = [0] * 26
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            self.rank[px] += 1

def smallestEquivalentString(A: str, B: str, S: str) -> str:
    uf = UnionFind()
    for a, b in zip(A, B):
        uf.union(ord(a) - ord('a'), ord(b) - ord('a'))
    res = []
    for c in S:
        res.append(chr(uf.find(ord(c) - ord('a')) + ord('a')))
    return ''.join(res)