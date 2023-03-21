class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            if not graph[node]:
                return node == destination
            for child in graph[node]:
                if not dfs(child):
                    return False
            visited.remove(node)
            return True
        return dfs(source)