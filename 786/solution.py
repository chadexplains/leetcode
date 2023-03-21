class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        heap = [(A[0] / A[i], 0, i) for i in range(len(A) - 1, 0, -1)]
        for _ in range(K - 1):
            frac, i, j = heapq.heappop(heap)
            if i + 1 < j:
                heapq.heappush(heap, ((A[i + 1] / A[j]), i + 1, j))
        return [A[heap[0][2]], A[len(A) - heap[0][1] - 1]]