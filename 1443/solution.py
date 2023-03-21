class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        def dfs(node):
            visited.add(node)
            time = 0
            for child in graph[node]:
                if child not in visited:
                    child_time = dfs(child)
                    if child_time > 0 or hasApple[child]:
                        time += child_time + 2
            return time
        return max(0, dfs(0) - 2)