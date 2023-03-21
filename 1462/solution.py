class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        order = self.topologicalSort(graph, n)
        res = []
        for u, v in queries:
            res.append(self.isReachable(graph, order, u, v))
        return res
    
    def topologicalSort(self, graph, n):
        indegree = [0] * n
        for u in graph:
            for v in graph[u]:
                indegree[v] += 1
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        order = []
        while queue:
            u = queue.popleft()
            order.append(u)
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        return order
    
    def isReachable(self, graph, order, u, v):
        return u in order[:order.index(v)+1]