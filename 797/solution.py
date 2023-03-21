class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, target, path):
            if node == target:
                res.append(path)
                return
            for nei in graph[node]:
                dfs(nei, target, path + [nei])
        res = []
        dfs(0, len(graph) - 1, [0])
        return res