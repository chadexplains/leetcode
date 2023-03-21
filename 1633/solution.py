class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                self.dfs(graph, i, visited)
                count += 1
        return count
    
    def dfs(self, graph, node, visited):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                self.dfs(graph, neighbor, visited)