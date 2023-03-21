class Solution:
    def checkWays(self, pairs: List[List[int]]) -> Optional[List[List[int]]]:
        n = len(pairs)
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)
        for u, v in pairs:
            graph[u].append(v)
            graph[v].append(u)
            in_degree[u] += 1
            in_degree[v] += 1
        root = [i for i in range(1, n + 1) if in_degree[i] == n - 2]
        if not root:
            return None
        root = root[0]
        q = deque([root])
        visited = set()
        while q:
            node = q.popleft()
            visited.add(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == n - 3:
                    q.append(neighbor)
        if len(visited) != n:
            return None
        edges = []
        for u, v in pairs:
            if in_degree[u] > in_degree[v]:
                u, v = v, u
            if in_degree[u] == n - 2 and in_degree[v] == 1:
                edges.append([u, v])
        return edges if edges else None