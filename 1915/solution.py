def maximalNetworkRank(n: int, roads: List[List[int]]) -> int:
    degrees = defaultdict(int)
    edges = set()
    for u, v in roads:
        degrees[u] += 1
        degrees[v] += 1
        edges.add((u, v))
        edges.add((v, u))
    max_rank = 0
    for i in range(n):
        for j in range(i + 1, n):
            rank = degrees[i] + degrees[j]
            if (i, j) in edges:
                rank -= 1
            max_rank = max(max_rank, rank)
    return max_rank