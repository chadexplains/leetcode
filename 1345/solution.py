class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
        queue = deque([(0, 0)])
        visited = set([0])
        while queue:
            curr, steps = queue.popleft()
            if curr == n - 1:
                return steps
            for child in graph[arr[curr]]:
                if child not in visited:
                    visited.add(child)
                    queue.append((child, steps + 1))
            graph[arr[curr]] = []
            for child in [curr - 1, curr + 1]:
                if 0 <= child < n and child not in visited:
                    visited.add(child)
                    queue.append((child, steps + 1))
        return -1