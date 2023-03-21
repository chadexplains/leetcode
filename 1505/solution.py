class Solution:
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        pos = [[] for _ in range(10)]
        for i in range(n):
            pos[int(num[i])].append(i)
        res = []
        bit = BinaryIndexedTree(n)
        for i in range(n):
            for j in range(10):
                if not pos[j]:
                    continue
                cost = pos[j][0] + bit.query(pos[j][0])
                if cost <= k:
                    k -= cost
                    res.append(str(j))
                    bit.update(pos[j][0] + 1, 1)
                    pos[j].pop(0)
                    break
        return ''.join(res)

class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res