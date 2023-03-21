class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
        n = len(s)
        uf = list(range(n))
        for i, j in pairs:
            uf[find(i)] = find(j)
        d = collections.defaultdict(list)
        for i in range(n):
            d[find(i)].append(i)
        res = list(s)
        for q in d.values():
            t = sorted(res[i] for i in q)
            for i, c in zip(sorted(q), t):
                res[i] = c
        return ''.join(res)