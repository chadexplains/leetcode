class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        def dfs(node, parent, depth):
            max_depth = -1
            for i in range(1, 51):
                if gcd(nums[node], i) == 1:
                    if depths[i]:
                        max_depth = max(max_depth, depths[i][-1][1])
                    if max_depth != -1:
                        res[node] = max(res[node], max_depth - depth)
                if depths[i]:
                    max_depth = max(max_depth, depths[i][-1][1])
                depths[i].append((node, depth))
                for child in graph[node]:
                    if child != parent:
                        dfs(child, node, depth + 1)
                depths[i].pop()
        n = len(nums)
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append(v)
            graph[v].append(u)
        depths = [[] for _ in range(51)]
        res = [-1] * n
        dfs(0, -1, 0)
        return res