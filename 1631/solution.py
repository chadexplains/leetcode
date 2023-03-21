class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        heap = [(0, 0, 0)]
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        efforts = [[float('inf')] * n for _ in range(m)]
        efforts[0][0] = 0
        while heap:
            effort, row, col = heapq.heappop(heap)
            if (row, col) in visited:
                continue
            visited.add((row, col))
            if row == m - 1 and col == n - 1:
                return effort
            for d in directions:
                r, c = row + d[0], col + d[1]
                if 0 <= r < m and 0 <= c < n:
                    new_effort = max(effort, abs(heights[row][col] - heights[r][c]))
                    if new_effort < efforts[r][c]:
                        efforts[r][c] = new_effort
                        heapq.heappush(heap, (new_effort, r, c))
        return -1