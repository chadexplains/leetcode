class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-pile for pile in piles]
        heapq.heapify(heap)
        for i in range(k):
            pile = -heapq.heappop(heap)
            new_pile = pile - (pile // 2)
            heapq.heappush(heap, -new_pile)
        return -sum(heap)