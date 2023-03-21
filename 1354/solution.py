class Solution:
    def isPossible(self, target: List[int]) -> bool:
        heap = [-x for x in target]
        total = sum(target)
        heapq.heapify(heap)
        while heap[0] != -1:
            largest = -heapq.heappop(heap)
            total -= largest
            if largest <= total or total < 1:
                return False
            largest %= total
            total += largest
            heapq.heappush(heap, -largest)
        return True