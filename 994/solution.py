class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        time_elapsed = 0
        while queue:
            i, j, time = queue.pop(0)
            time_elapsed = max(time_elapsed, time)
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = 2
                    queue.append((x, y, time+1))
        if any(1 in row for row in grid):
            return -1
        return time_elapsed