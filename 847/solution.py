class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = deque([(i, 1 << i, 0) for i in range(n)])
        visited = set([(i, 1 << i) for i in range(n)])
        target = (1 << n) - 1
        while q:
            node, state, dist = q.popleft()
            if state == target:
                return dist
            for neighbor in graph[node]:
                new_state = state | (1 << neighbor)
                if (neighbor, new_state) not in visited:
                    visited.add((neighbor, new_state))
                    q.append((neighbor, new_state, dist + 1))
        return -1