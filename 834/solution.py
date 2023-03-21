class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        count = [1] * N
        ans = [0] * N
        def dfs1(node, parent):
            for nei in graph[node]:
                if nei != parent:
                    dfs1(nei, node)
                    count[node] += count[nei]
                    ans[node] += ans[nei] + count[nei]
        def dfs2(node, parent):
            for nei in graph[node]:
                if nei != parent:
                    ans[nei] = ans[node] - count[nei] + N - count[nei]
                    dfs2(nei, node)
        dfs1(0, -1)
        dfs2(0, -1)
        return ans