class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        distance = [[float('inf')] * n for _ in range(m)]
        distance[start[0]][start[1]] = 0
        queue = [(start[0], start[1])]
        while queue:
            i, j = queue.pop(0)
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y, dist = i, j, 0
                while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] == 0:
                    x += dx
                    y += dy
                    dist += 1
                if distance[i][j] + dist < distance[x][y]:
                    distance[x][y] = distance[i][j] + dist
                    queue.append((x, y))
        return distance[destination[0]][destination[1]] if distance[destination[0]][destination[1]] != float('inf') else -1