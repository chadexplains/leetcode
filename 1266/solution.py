class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time_taken = 0
        for i in range(1, len(points)):
            x_diff = abs(points[i][0] - points[i-1][0])
            y_diff = abs(points[i][1] - points[i-1][1])
            time_taken += max(x_diff, y_diff)
        return time_taken