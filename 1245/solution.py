class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node, parent):
            max_depth = 0
            farthest_node = node
            for neighbor in graph[node]:
                if neighbor != parent:
                    depth, farthest = dfs(neighbor, node)
                    if depth + 1 > max_depth:
                        max_depth = depth + 1
                        farthest_node = farthest
            return max_depth, farthest_node
        _, farthest_node = dfs(0, -1)
        diameter, _ = dfs(farthest_node, -1)
        return diameter