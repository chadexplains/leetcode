class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        visited = set()
        stack = [start]
        while stack:
            curr = stack.pop()
            if curr == end:
                return True
            visited.add(curr)
            for neighbor in adj_list[curr]:
                if neighbor not in visited:
                    stack.append(neighbor)
        return False