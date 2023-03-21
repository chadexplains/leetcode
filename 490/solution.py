class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        visited = set()
        queue = deque([tuple(start)])
        visited.add(tuple(start))
        while queue:
            x, y = queue.popleft()
            if [x, y] == destination:
                return True
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                while 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == 0:
                    nx += dx
                    ny += dy
                nx -= dx
                ny -= dy
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        return False