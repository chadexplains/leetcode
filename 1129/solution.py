class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red_adj = defaultdict(list)
        blue_adj = defaultdict(list)
        for u, v in red_edges:
            red_adj[u].append(v)
        for u, v in blue_edges:
            blue_adj[u].append(v)
        res = [-1] * n
        queue = deque([(0, 0), (0, 1)])
        visited = set([(0, 0), (0, 1)])
        level = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node, color = queue.popleft()
                if res[node] == -1:
                    res[node] = level
                adj = red_adj if color == 0 else blue_adj
                for nei in adj[node]:
                    if (nei, 1 - color) not in visited:
                        visited.add((nei, 1 - color))
                        queue.append((nei, 1 - color))
            level += 1
        return res