class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1
        queue = collections.deque([u for u in range(numCourses) if in_degree[u] == 0])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return all(in_degree[i] == 0 for i in range(numCourses))