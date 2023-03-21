class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        buildings = sum(grid[i][j] == 1 for i in range(m) for j in range(n))
        distances = [[0] * n for _ in range(m)]
        reach = [[0] * n for _ in range(m)]
        def bfs(start_i, start_j):
            visited = [[False] * n for _ in range(m)]
            visited[start_i][start_j] = True
            queue = collections.deque([(start_i, start_j, 0)])
            while queue:
                i, j, dist = queue.popleft()
                for x, y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                        visited[x][y] = True
                        if not grid[x][y]:
                            distances[x][y] += dist + 1
                            reach[x][y] += 1
                            queue.append((x, y, dist+1))
                        elif grid[x][y] == 1:
                            reach[x][y] += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j)
        return min([distances[i][j] for i in range(m) for j in range(n) if not grid[i][j] and reach[i][j] == buildings] or [-1])