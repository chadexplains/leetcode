class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        out_degree = [0] * n
        in_degree = [[] for _ in range(n)]
        q = deque()
        for i in range(n):
            out_degree[i] = len(graph[i])
            if out_degree[i] == 0:
                q.append(i)
            for j in graph[i]:
                in_degree[j].append(i)
        while q:
            node = q.popleft()
            for i in in_degree[node]:
                out_degree[i] -= 1
                if out_degree[i] == 0:
                    q.append(i)
        res = []
        for i in range(n):
            if out_degree[i] == 0:
                res.append(i)
        return res