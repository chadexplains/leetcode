class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0, 0, 0)]) # (i, j, steps, obstacles)
        visited = {(0, 0, 0)}
        while queue:
            i, j, steps, obstacles = queue.popleft()
            if i == m-1 and j == n-1:
                return steps
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] == 0 and (x, y, obstacles) not in visited:
                        visited.add((x, y, obstacles))
                        queue.append((x, y, steps+1, obstacles))
                    elif grid[x][y] == 1 and obstacles < k and (x, y, obstacles+1) not in visited:
                        visited.add((x, y, obstacles+1))
                        queue.append((x, y, steps+1, obstacles+1))
        return -1