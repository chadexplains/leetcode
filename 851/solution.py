class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        for u, v in richer:
            graph[v].append(u)
        n = len(quiet)
        res = [-1] * n
        def dfs(node):
            if res[node] >= 0:
                return res[node]
            res[node] = node
            for nei in graph[node]:
                candidate = dfs(nei)
                if quiet[candidate] < quiet[res[node]]:
                    res[node] = candidate
            return res[node]
        for i in range(n):
            dfs(i)
        return res