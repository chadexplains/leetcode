class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        queue = [(0, 0, 1)]
        visited = set()
        while queue:
            x, y, steps = queue.pop(0)
            if x == n-1 and y == n-1:
                return steps
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < n and not grid[nx][ny] and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps+1))
        return -1