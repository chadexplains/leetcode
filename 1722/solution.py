class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            if self.size[pi] < self.size[pj]:
                pi, pj = pj, pi
            self.parent[pj] = pi
            self.size[pi] += self.size[pj]


class Solution:
    def minimumHammingDistance(self, nums1: List[int], nums2: List[int], pairs: List[List[int]]) -> int:
        n = len(nums1)
        uf = UnionFind(n)
        for i, j in pairs:
            uf.union(i, j)
        groups = collections.defaultdict(list)
        for i in range(n):
            groups[uf.find(i)].append(i)
        ans = 0
        for group in groups.values():
            count = collections.Counter(nums1[i] for i in group)
            for i in group:
                if count[nums2[i]] > 0:
                    count[nums2[i]] -= 1
                else:
                    ans += 1
        return ans