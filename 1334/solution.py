class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            graph[i][i] = 0
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        min_neighbors = float('inf')
        min_city = -1
        for i in range(n):
            neighbors = sum(1 for j in range(n) if graph[i][j] <= distanceThreshold)
            if neighbors <= min_neighbors:
                min_neighbors = neighbors
                min_city = i
        return min_city