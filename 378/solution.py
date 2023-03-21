class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        heapq.heapify(heap)
        for i in range(k - 1):
            val, row, col = heapq.heappop(heap)
            if col < len(matrix[0]) - 1:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
        return heapq.heappop(heap)[0]