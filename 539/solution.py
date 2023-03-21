class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [int(time[:2]) * 60 + int(time[3:]) for time in timePoints]
        minutes.sort()
        min_diff = float('inf')
        for i in range(len(minutes) - 1):
            diff = minutes[i+1] - minutes[i]
            min_diff = min(min_diff, diff)
        diff = minutes[0] + 1440 - minutes[-1]
        min_diff = min(min_diff, diff)
        return min_diff