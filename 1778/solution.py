class Solution:
    def findShortestPath(self, master: 'GridMaster') -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = {(0, 0): 0}
        queue = deque([(0, 0)])
        while queue:
            x, y = queue.popleft()
            if master.isTarget(x, y):
                return visited[(x, y)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited and master.canMove(dx, dy):
                    visited[(nx, ny)] = visited[(x, y)] + 1
                    queue.append((nx, ny))
        return -1