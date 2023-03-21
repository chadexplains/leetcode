class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = collections.defaultdict(list)
        for i, m in enumerate(manager):
            if m != -1:
                graph[m].append(i)
        def dfs(node):
            if not graph[node]:
                return 0
            if node not in memo:
                memo[node] = max([dfs(child) for child in graph[node]]) + informTime[node]
            return memo[node]
        memo = {}
        return max([dfs(i) for i in range(n)])