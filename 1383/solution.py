class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = zip(efficiency, speed)
        engineers = sorted(engineers, reverse=True)
        heap = []
        speed_sum = 0
        max_performance = 0
        for e, s in engineers:
            heapq.heappush(heap, s)
            speed_sum += s
            if len(heap) > k:
                speed_sum -= heapq.heappop(heap)
            max_performance = max(max_performance, speed_sum * e)
        return max_performance % (10**9 + 7)