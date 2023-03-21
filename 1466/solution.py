class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))
        queue = deque([0])
        visited = set([0])
        count = 0
        while queue:
            node = queue.popleft()
            for neighbor, direction in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    if direction == 1:
                        count += 1
                    queue.append(neighbor)
        return count