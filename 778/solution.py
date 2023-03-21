class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        res = 0
        while heap:
            t, i, j = heapq.heappop(heap)
            res = max(res, t)
            if i == j == n - 1:
                return res
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < n and 0 <= y < n and (x, y) not in visited:
                    visited.add((x, y))
                    heapq.heappush(heap, (grid[x][y], x, y))
        return -1
