class Solution:
    def minimumSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        in_degree = [0] * (n+1)
        for u, v in dependencies:
            graph[u].append(v)
            in_degree[v] += 1
        queue = deque([i for i in range(1, n+1) if in_degree[i] == 0])
        semester = 0
        while queue:
            for _ in range(min(k, len(queue))):
                node = queue.popleft()
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            semester += 1
        return semester if all(in_degree[1:] == 0) else -1