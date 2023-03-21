class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(N+1)]
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        color = [0] * (N+1)
        def dfs(node, c):
            color[node] = c
            for nei in graph[node]:
                if color[nei] == c:
                    return False
                if color[nei] == 0 and not dfs(nei, -c):
                    return False
            return True
        for i in range(1, N+1):
            if color[i] == 0 and not dfs(i, 1):
                return False
        return True