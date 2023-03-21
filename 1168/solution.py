def minCostToSupplyWater(n: int, wells: List[int], pipes: List[List[int]]) -> int:
    edges = [(0, i+1, wells[i]) for i in range(n)] + pipes
    edges.sort(key=lambda x: x[2])
    uf = {i: i for i in range(n+1)}
    def find(x):
        if uf[x] != x:
            uf[x] = find(uf[x])
        return uf[x]
    cost = 0
    for u, v, w in edges:
        pu, pv = find(u), find(v)
        if pu == pv:
            continue
        uf[pu] = pv
        cost += w
        if len(uf) == 2:
            break
    return cost