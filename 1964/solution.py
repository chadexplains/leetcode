class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        dp = []
        res = []
        for obstacle in obstacles:
            idx = bisect.bisect_left(dp, obstacle)
            if idx == len(dp):
                dp.append(obstacle)
            else:
                dp[idx] = obstacle
            res.append(idx + 1)
        return res