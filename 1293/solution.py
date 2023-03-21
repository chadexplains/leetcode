class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0, 0, 0)]) # (row, col, steps, obstacles)
        visited = {(0, 0, 0)} # (row, col, obstacles)
        while queue:
            row, col, steps, obstacles = queue.popleft()
            if row == m - 1 and col == n - 1:
                return steps
            for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r, c = row + d[0], col + d[1]
                if 0 <= r < m and 0 <= c < n:
                    if grid[r][c] == 1 and obstacles < k and (r, c, obstacles + 1) not in visited:
                        visited.add((r, c, obstacles + 1))
                        queue.append((r, c, steps + 1, obstacles + 1))
                    elif grid[r][c] == 0 and (r, c, obstacles) not in visited:
                        visited.add((r, c, obstacles))
                        queue.append((r, c, steps + 1, obstacles))
        return -1