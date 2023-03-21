class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
        uf = list(range(n + 1))
        cnt = 0
        for t, u, v in edges:
            if t == 3:
                pu, pv = find(u), find(v)
                if pu != pv:
                    uf[pu] = pv
                else:
                    cnt += 1
        tmp = uf.copy()
        for t, u, v in edges:
            if t == 1:
                pu, pv = find(u), find(v)
                if pu != pv:
                    uf[pu] = pv
                else:
                    cnt += 1
        if len(set(find(i) for i in range(1, n + 1))) > 1:
            return -1
        uf = tmp
        for t, u, v in edges:
            if t == 2:
                pu, pv = find(u), find(v)
                if pu != pv:
                    uf[pu] = pv
                else:
                    cnt += 1
        if len(set(find(i) for i in range(1, n + 1))) > 1:
            return -1
        return cnt