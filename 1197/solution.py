class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        q = [(0, 0, 0)]
        visited = set()
        while q:
            i, j, steps = q.pop(0)
            if (i, j) == (x, y):
                return steps
            if (i, j) in visited:
                continue
            visited.add((i, j))
            for di, dj in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]:
                q.append((i+di, j+dj, steps+1))
        return -1