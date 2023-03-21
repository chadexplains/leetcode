class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = zip(efficiency, speed)
        engineers = sorted(engineers, reverse=True)
        heap = []
        total_speed = 0
        max_performance = 0
        for e, s in engineers:
            total_speed += s
            heappush(heap, s)
            if len(heap) > k:
                total_speed -= heappop(heap)
            max_performance = max(max_performance, total_speed * e)
        return max_performance % (10**9 + 7)