class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[start[0]][start[1]] = 0
        heap = [(0, start[0], start[1])]
        while heap:
            d, i, j = heappop(heap)
            if [i, j] == destination:
                return d
            for ni, nj in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                nd, steps = d, 0
                while 0 <= ni < m and 0 <= nj < n and not maze[ni][nj]:
                    ni += di
                    nj += dj
                    steps += 1
                ni -= di
                nj -= dj
                nd += steps
                if nd < dist[ni][nj]:
                    dist[ni][nj] = nd
                    heappush(heap, (nd, ni, nj))
        return -1