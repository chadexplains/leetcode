class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        count = [0] * 26
        def dfs(node, parent):
            label = ord(labels[node]) - ord('a')
            count[label] += 1
            for child in adj_list[node]:
                if child != parent:
                    dfs(child, node)
                    for i in range(26):
                        count[i] += count[child][i]
            result[node] = count[label]
        result = [0] * n
        dfs(0, -1)
        return result