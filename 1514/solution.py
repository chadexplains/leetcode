class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, -log(succProb[i])))
            graph[v].append((u, -log(succProb[i])))
        pq = [(0, start)]
        visited = set()
        while pq:
            prob, node = heappop(pq)
            if node == end:
                return exp(-prob)
            if node in visited:
                continue
            visited.add(node)
            for neighbor, edge_prob in graph[node]:
                heappush(pq, (prob + edge_prob, neighbor))
        return 0.0