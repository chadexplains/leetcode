class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        pq = []
        max_val = float('-inf')
        for x, y in points:
            while pq and x - pq[0][1] > k:
                heapq.heappop(pq)
            if pq:
                max_val = max(max_val, pq[0][0] + x + y)
            heapq.heappush(pq, (y - x, x))
        return max_val