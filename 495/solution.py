class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total_time = 0
        for i in range(1, len(timeSeries)):
            total_time += min(timeSeries[i] - timeSeries[i-1], duration)
        return total_time